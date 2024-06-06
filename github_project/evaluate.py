import pandas as pd
import numpy as np
import sys
import os

import mlflow
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from keras.models import load_model
from helper import prepare_tensors
import matplotlib.pyplot as plt

if len(sys.argv) > 1:
    build_number = int(sys.argv[1])
else:
    build_number = 0

hp_test = pd.read_csv('./github_project/hp_test.csv')
X_test, Y_test = prepare_tensors(hp_test)

model = load_model('./github_project/hp_model.h5')

test_predictions = model.predict(X_test)

predictions_df = pd.DataFrame(test_predictions, columns=["Predicted_Price"])
predictions_df.to_csv('./github_project/hp_test_predictions.csv', index=False)

rmse = np.sqrt(mean_squared_error(Y_test, test_predictions))
mae = mean_absolute_error(Y_test, test_predictions)
r2 = r2_score(Y_test, test_predictions)

metrics_df = pd.DataFrame({
    'Build_Number': [build_number],
    'RMSE': [rmse],
    'MAE': [mae],
    'R2': [r2]
})

metrics_file = './github_project/hp_test_metrics.csv'
if os.path.isfile(metrics_file):
    existing_metrics_df = pd.read_csv(metrics_file)
    updated_metrics_df = pd.concat([existing_metrics_df, metrics_df], ignore_index=True)
else:
    updated_metrics_df = metrics_df

updated_metrics_df.to_csv(metrics_file, index=False)

metrics = ['RMSE', 'MAE', 'R2']
for metric in metrics:
    plt.plot(updated_metrics_df['Build_Number'], updated_metrics_df[metric], marker='o')
    plt.title(f'{metric} vs Builds')
    plt.xlabel('Build Number')
    plt.ylabel(metric)
    plt.grid(True)
    plot_file = f'plot_{metric.lower()}.png'
    plt.savefig(plot_file)
    plt.close()

with mlflow.start_run() as run:
    mlflow.log_metric('RMSE', rmse)
    mlflow.log_metric('MAE', mae)
    mlflow.log_metric('R2', r2)
