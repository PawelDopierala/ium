import pandas as pd
from keras.models import load_model
from helper import prepare_tensors

hp_test = pd.read_csv('hp_test.csv')
X_test, Y_test = prepare_tensors(hp_test)

model = load_model('hp_model.h5')

test_predictions = model.predict(X_test)

predictions_df = pd.DataFrame(test_predictions, columns=["Predicted_Price"])
predictions_df.to_csv('hp_test_predictions.csv', index=False)
