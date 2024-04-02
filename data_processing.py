import sklearn
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder
import pandas as pd

housing_price_dataset = pd.read_csv('housing_price_dataset.csv')

hp_train_test, hp_dev = train_test_split(housing_price_dataset, test_size=0.1)
hp_train, hp_test = train_test_split(hp_train_test, test_size=1000)

hp_train = pd.get_dummies(hp_train, columns=['Neighborhood'])
hp_dev = pd.get_dummies(hp_dev, columns=['Neighborhood'])
hp_test = pd.get_dummies(hp_test, columns=['Neighborhood'])

hp_train.to_csv('hp_train.csv', index=False)
hp_dev.to_csv('hp_dev.csv', index=False)
hp_test.to_csv('hp_test.csv', index=False)
