import numpy as np
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import regularizers
from sacred import Experiment
from sacred.observers import MongoObserver, FileStorageObserver
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

from helper import prepare_tensors

ex = Experiment('495719', save_git_info=False)

ex.observers.append(MongoObserver(url='mongodb://admin:IUM_2021@tzietkiewicz.vm.wmi.amu.edu.pl:27017'))
ex.observers.append(FileStorageObserver('my_runs'))

@ex.config
def config():
    epochs = 10
    learning_rate = 0.001
    batch_size = 32

@ex.main
def main(epochs, learning_rate, batch_size, _run):
    with _run.open_resource("hp_train.csv") as f:
        hp_train = pd.read_csv(f)
    with _run.open_resource("hp_dev.csv") as f:
        hp_dev = pd.read_csv(f)

    X_train, Y_train = prepare_tensors(hp_train)
    X_dev, Y_dev = prepare_tensors(hp_dev)

    model = Sequential()
    model.add(Dense(64, input_dim=7, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(32, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(16, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(8, activation='relu', kernel_regularizer=regularizers.l2(0.01)))
    model.add(Dense(1, activation='linear'))

    adam = Adam(learning_rate=learning_rate, beta_1=0.9, beta_2=0.999, epsilon=1e-7)
    model.compile(optimizer=adam, loss='mean_squared_error')

    model.fit(X_train, Y_train, epochs=epochs, batch_size=batch_size, validation_data=(X_dev, Y_dev))

    model.save('hp_model.h5')
    ex.add_artifact("hp_model.h5")

    with _run.open_resource("hp_test.csv") as f:
        hp_test = pd.read_csv(f)

    X_test, Y_test = prepare_tensors(hp_test)

    test_predictions = model.predict(X_test)

    rmse = np.sqrt(mean_squared_error(Y_test, test_predictions))
    mae = mean_absolute_error(Y_test, test_predictions)

    _run.log_scalar("rmse", rmse)
    _run.log_scalar("mae", mae)


if __name__ == '__main__':
    ex.run()
