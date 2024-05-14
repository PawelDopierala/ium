import pandas as pd
import numpy as np
import sys
import os
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from keras.models import load_model
from helper import prepare_tensors
import matplotlib.pyplot as plt

build_number = int(sys.argv[1])

hp_test = pd.read_csv('hp_test.csv')
X_test, Y_test = prepare_tensors(hp_test)

model = load_model('hp_model.h5')

test_predictions = model.predict(X_test)

predictions_df = pd.DataFrame(test_predictions, columns=["Predicted_Price"])
predictions_df.to_csv('hp_test_predictions.csv', index=False)

rmse = np.sqrt(mean_squared_error(Y_test, test_predictions))
mae = mean_absolute_error(Y_test, test_predictions)
r2 = r2_score(Y_test, test_predictions)

metrics_df = pd.DataFrame({
    'Build_Number': [build_number],
    'RMSE': [rmse],
    'MAE': [mae],
    'R2': [r2]
})

metrics_file = 'hp_test_metrics.csv'
if os.path.isfile(metrics_file):
    existing_metrics_df = pd.read_csv(metrics_file)
    updated_metrics_df = pd.concat([existing_metrics_df, metrics_df], ignore_index=True)
else:
    updated_metrics_df = metrics_df

updated_metrics_df.to_csv(metrics_file, index=False)

plt.figure(figsize=(10, 6))
plt.plot(updated_metrics_df['Build_Number'], updated_metrics_df['RMSE'], label='RMSE', marker='o')
plt.plot(updated_metrics_df['Build_Number'], updated_metrics_df['MAE'], label='MAE', marker='o')
plt.plot(updated_metrics_df['Build_Number'], updated_metrics_df['R2'], label='R2', marker='o')

plt.title('Metrics vs Builds')
plt.xlabel('Build Number')
plt.ylabel('Metric Value')
plt.legend()
plt.grid(True)

plot_file = 'metrics_plt.png'
plt.savefig(plot_file)
plt.close()
