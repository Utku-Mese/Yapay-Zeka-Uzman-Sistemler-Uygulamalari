import pandas as pd
import simpsom as som
from sklearn.preprocessing import MinMaxScaler
import kagglehub

path = kagglehub.dataset_download("shwetabh123/mall-customers")
df = pd.read_csv(path + "/Mall_Customers.csv")

features = ["Annual Income (k$)", "Spending Score (1-100)"]
data = df[features]

scaler = MinMaxScaler()
data_scaled = scaler.fit_transform(data)

net = som.SOMNet(20, 20, data_scaled, PBC=True)

net.train(epochs=10000, radius_ini=1, radius_fin=0.01, learning_rate_ini=0.01, learning_rate_fin=0.001)

mapped = net.project(data_scaled)
kume_sonuc = net.cluster(mapped, type="KMeans", k=3)

df["Cluster"] = kume_sonuc

print(df[["CustomerID", "Cluster"]])

gruplar = df.groupby("Cluster").mean()
print("Müşteri grupları:")
print(gruplar)
