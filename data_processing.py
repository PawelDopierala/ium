from sklearn.model_selection import train_test_split
import pandas as pd
import subprocess

subprocess.run(["kaggle", "datasets", "download", "muhammadbinimran/housing-price-prediction-data", "--unzip"])
housing_price_dataset = pd.read_csv('housing_price_dataset.csv')

housing_price_dataset = pd.get_dummies(housing_price_dataset, columns=['Neighborhood'])

hp_train_test, hp_dev = train_test_split(housing_price_dataset, test_size=0.1)
hp_train, hp_test = train_test_split(hp_train_test, test_size=1000)

hp_train.to_csv('hp_train.csv', index=False)
hp_dev.to_csv('hp_dev.csv', index=False)
hp_test.to_csv('hp_test.csv', index=False)
