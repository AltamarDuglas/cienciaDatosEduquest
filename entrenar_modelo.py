import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import joblib

# Cargar datos
df = pd.read_excel("datos/ROCStories_Ejemplo_Combinado.xlsx", sheet_name="Historias y Niveles")

# Preparar texto de entrada
X = df["Oración_1"] + " " + df["Oración_2"] + " " + df["Oración_3"] + " " + df["Oración_4"] + " " + df["Final_Correcto"]
y = df["Nivel_Numérico"]

# Vectorización
vectorizer = TfidfVectorizer()
X_vect = vectorizer.fit_transform(X)

# Entrenamiento
clf = LogisticRegression()
clf.fit(X_vect, y)

# Guardar modelo y vectorizador
joblib.dump(clf, "modelo/modelo_inferencia.pkl")
joblib.dump(vectorizer, "modelo/vectorizador.pkl")

print("Modelo entrenado y guardado.")
