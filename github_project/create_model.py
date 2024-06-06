import pandas as pd
import sys
from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam
from keras import regularizers
import mlflow

from helper import prepare_tensors

epochs = int(sys.argv[1])
learning_rate = float(sys.argv[2])
batch_size = int(sys.argv[3])

hp_train = pd.read_csv('./github_project/hp_train.csv')
hp_dev = pd.read_csv('./github_project/hp_dev.csv')

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

model.save('./github_project/hp_model.h5')

with mlflow.start_run() as run:
    mlflow.log_param("epochs", epochs)
    mlflow.log_param("learning_rate", learning_rate)
    mlflow.log_param("batch_size", batch_size)
