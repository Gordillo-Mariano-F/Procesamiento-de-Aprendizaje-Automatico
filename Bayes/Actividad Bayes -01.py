import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, confusion_matrix

# Datos de ejemplo: noticias y etiquetas
data = {
    'texto': [
        "El presidente anunció una nueva reforma educativa",
        "Descubren que la vacuna convierte a las personas en robots",
        "La NASA confirma el hallazgo de agua en Marte",
        "Científicos afirman que la Tierra es plana",
        "El ministerio de salud lanza campaña contra el dengue",
        "Celebridades usan crema milagrosa para rejuvenecer 30 años",
        "Se inaugura el nuevo hospital en la ciudad",
        "Estudio revela que comer chocolate cura el cáncer",
        "Gobierno aprueba ley de protección ambiental",
        "Investigadores aseguran que los teléfonos espían nuestros sueños"
    ],
    'etiqueta': [
        'real', 'fake', 'real', 'fake', 'real',
        'fake', 'real', 'fake', 'real', 'fake'
    ]
}

# Crear DataFrame
df = pd.DataFrame(data)

# Separar características (X) y etiquetas (y)
X = df['texto']
y = df['etiqueta']

# Vectorización del texto
vectorizer = CountVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# División en conjunto de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized, y, test_size=0.2, random_state=42
)

# Crear y entrenar el modelo Naive Bayes
model = MultinomialNB()
model.fit(X_train, y_train)

# Realizar predicciones
y_pred = model.predict(X_test)

# Evaluar el modelo
accuracy = accuracy_score(y_test, y_pred)
conf_matrix = confusion_matrix(y_test, y_pred, labels=['real', 'fake'])

# Nuevas noticias a clasificar
nuevas_noticias = [
    "Nuevo estudio demuestra que el café mejora la memoria",
    "Expertos afirman que los gatos pueden hablar con humanos"
]
nuevas_noticias_vect = vectorizer.transform(nuevas_noticias)
predicciones_nuevas = model.predict(nuevas_noticias_vect)

# Mostrar resultados
print("\n Evaluación del modelo")
print(f"Precisión: {accuracy:.2f}")
print("Matriz de confusión:")
print(conf_matrix)

print("\n Predicciones para nuevas noticias:")
for noticia, etiqueta in zip(nuevas_noticias, predicciones_nuevas):
    print(f"• Noticia: '{noticia}' → Predicción: {etiqueta}")

