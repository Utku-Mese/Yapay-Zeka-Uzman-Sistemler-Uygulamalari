import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.model_selection import train_test_split, cross_val_score, StratifiedKFold
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import roc_curve, auc
from sklearn.neural_network import MLPClassifier


veri = pd.read_csv("C:\Users\admin\Desktop\KLASÖRLER\üniversite\4. sınıf 2. dönem\Yapay Zeka ve Uzman Sistemler\Uygulama 4\train.csv")


label_encoder = LabelEncoder().fit(veri.price_range)
labels = label_encoder.transform(veri.price_range)
classes = list(label_encoder.classes_)


X = veri.drop(["price_range"], axis=1)
y = labels

sc = StandardScaler()
X = sc.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)


y_train = to_categorical(y_train)
y_test = to_categorical(y_test)

model = Sequential()
model.add(Dense(32, input_dim=X.shape[1], activation="relu"))  
model.add(Dense(16, activation="relu"))
model.add(Dense(4, activation="softmax")) 
model.summary()

model.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])

history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=150, batch_size=16)

skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
mlp = MLPClassifier(hidden_layer_sizes=(32, 16), max_iter=150, activation="relu", solver="adam")

cv_scores = cross_val_score(mlp, X, y, cv=skf, scoring="accuracy")
print(f"Çapraz Doğrulama Başarım Ortalaması: {cv_scores.mean():.4f}")

X_reduced = veri.drop(["price_range", "blue", "fc", "int_memory", "ram", "wifi"], axis=1)
X_reduced = sc.fit_transform(X_reduced)

X_train_red, X_test_red, y_train_red, y_test_red = train_test_split(X_reduced, y, test_size=0.2)

y_train_red = to_categorical(y_train_red)
y_test_red = to_categorical(y_test_red)

model_reduced = Sequential()
model_reduced.add(Dense(32, input_dim=X_reduced.shape[1], activation="relu"))
model_reduced.add(Dense(16, activation="relu"))
model_reduced.add(Dense(4, activation="softmax"))

model_reduced.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
history_reduced = model_reduced.fit(X_train_red, y_train_red, validation_data=(X_test_red, y_test_red), epochs=150, batch_size=16)



diabetes_data = pd.read_csv("diabetes.csv") 
X_diabetes = diabetes_data.drop(["Outcome"], axis=1)
y_diabetes = diabetes_data["Outcome"]

X_diabetes = sc.fit_transform(X_diabetes)

X_train_dia, X_test_dia, y_train_dia, y_test_dia = train_test_split(X_diabetes, y_diabetes, test_size=0.2)

y_train_dia = to_categorical(y_train_dia)
y_test_dia = to_categorical(y_test_dia)

model_diabetes = Sequential()
model_diabetes.add(Dense(16, input_dim=X_diabetes.shape[1], activation="relu"))
model_diabetes.add(Dense(8, activation="relu"))
model_diabetes.add(Dense(2, activation="softmax")) 

model_diabetes.compile(loss="categorical_crossentropy", optimizer="adam", metrics=["accuracy"])
history_diabetes = model_diabetes.fit(X_train_dia, y_train_dia, validation_data=(X_test_dia, y_test_dia), epochs=150, batch_size=16)

plt.plot(history_diabetes.history["accuracy"])
plt.plot(history_diabetes.history["val_accuracy"])
plt.title("Diyabet Veri Seti Model Başarımları")
plt.xlabel("Epok Sayısı")
plt.ylabel("Başarım")
plt.legend(["Eğitim", "Test"], loc="upper left")
plt.show()

y_pred_prob = model_diabetes.predict(X_test_dia)

fpr, tpr, _ = roc_curve(y_test_dia[:, 1], y_pred_prob[:, 1])  
roc_auc = auc(fpr, tpr)

plt.figure()
plt.plot(fpr, tpr, color="blue", lw=2, label=f"ROC eğrisi (AUC = {roc_auc:.2f})")
plt.plot([0, 1], [0, 1], color="gray", linestyle="--")  
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel("False Positive Rate (Yanlış Pozitif Oranı)")
plt.ylabel("True Positive Rate (Doğru Pozitif Oranı)")
plt.title("ROC Eğrisi")
plt.legend(loc="lower right")
plt.show()
