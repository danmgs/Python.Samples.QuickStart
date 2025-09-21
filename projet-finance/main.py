import pandas as pd
import tensorflow as tf
from sklearn.model_selection import train_test_split
import numpy as np

# 1. Charger des données fictives
data = pd.read_csv("data.csv")
print("Aperçu des données :")
print(data.head())

# 2. Statistiques simples
print("\nStatistiques descriptives :")
print(data.describe())

# 3. Préparer les données (X = jours, y = prix)
X = np.array(data["Day"]).reshape(-1, 1)
y = np.array(data["Price"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# 4. Construire un modèle TensorFlow simple
model = tf.keras.Sequential([
    tf.keras.layers.Dense(10, activation="relu", input_shape=(1,)),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer="adam", loss="mse")

# 5. Entraînement
print("\nEntraînement du modèle...")
model.fit(X_train, y_train, epochs=50, verbose=0)

# 6. Évaluation
loss = model.evaluate(X_test, y_test, verbose=0)
print(f"\nErreur quadratique moyenne (MSE) sur le test set : {loss:.4f}")

# 7. Prédiction
day_to_predict = 35
pred = model.predict([[day_to_predict]], verbose=0)
print(f"\nPrix prédit pour le jour {day_to_predict} : {pred[0][0]:.2f}")
