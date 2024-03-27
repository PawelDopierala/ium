#!/bin/bash
kaggle datasets download muhammadbinimran/housing-price-prediction-data --unzip
head -n $1 housing_price_dataset.csv > processed_data.txt