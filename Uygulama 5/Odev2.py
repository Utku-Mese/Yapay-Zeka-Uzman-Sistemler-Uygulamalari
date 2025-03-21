import kagglehub
import pandas as pd
from sklearn.preprocessing import StandardScaler
import simpsom as sps
import matplotlib.pyplot as plt

path = kagglehub.dataset_download("arjunbhasin2013/ccdata")

print("Path to dataset files:", path)

df = pd.read_csv(path + "/CC GENERAL.csv")

print(df.head())

print(df.isnull().sum())

df = df.dropna()

features = df[['BALANCE', 'BALANCE_FREQUENCY', 'PURCHASES', 'ONEOFF_PURCHASES',
               'INSTALLMENTS_PURCHASES', 'CASH_ADVANCE', 'PURCHASES_FREQUENCY',
               'ONEOFF_PURCHASES_FREQUENCY', 'PURCHASES_INSTALLMENTS_FREQUENCY',
               'CASH_ADVANCE_FREQUENCY', 'CASH_ADVANCE_TRX', 'PURCHASES_TRX',
               'CREDIT_LIMIT', 'PAYMENTS', 'MINIMUM_PAYMENTS', 'PRC_FULL_PAYMENT',
               'TENURE']]

scaler = StandardScaler()
scaled_features = scaler.fit_transform(features)

som = sps(m=20, n=20, dim=scaled_features.shape[1])

som.train(scaled_features, epochs=10000, learning_rate=0.01)

clusters = som.fit_predict(scaled_features)

df['Cluster'] = clusters

clustered_df = df.groupby('Cluster').mean()
print(clustered_df)

plt.figure(figsize=(10, 8))
plt.scatter(df['BALANCE'], df['CREDIT_LIMIT'], c=df['Cluster'], cmap='viridis')
plt.title('Kredi Kartı Kullanıcıları Kümeleme')
plt.xlabel('Bakiye')
plt.ylabel('Kredi Limiti')
plt.colorbar(label='Cluster')
plt.show()
