import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Importar datos desde archivo externo
import sys
sys.path.append(r"C:\Users\QueresUnMate\Desktop\K-means\K-means_2\K-means_data")

from datos_estudiantes import estudiantes


# 1 Cargar datos
df = pd.DataFrame(estudiantes)

# 2 Estandarizar los datos
scaler = StandardScaler()
X_scaled = scaler.fit_transform(df[['edad', 'horas_estudio', 'promedio_academico']])

# 3 Aplicar K-Means
kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

# 4 Visualización
plt.figure(figsize=(8,6))
plt.scatter(df['edad'], df['promedio_academico'], c=df['cluster'], cmap='viridis', s=100)
plt.xlabel('Edad')
plt.ylabel('Promedio Académico')
plt.title('Agrupamiento de Estudiantes Universitarios (K-Means, 4 Clusters)')
plt.grid(True)
plt.tight_layout()
plt.show()

# 5 Informe
centroides = scaler.inverse_transform(kmeans.cluster_centers_)
df_clusters = pd.DataFrame(centroides, columns=['Edad Promedio', 'Horas de Estudio', 'Promedio Académico'])
print("\nCentroides por cluster:\n", df_clusters.round(2))
print("\nCantidad de estudiantes por grupo:")
print(df['cluster'].value_counts().sort_index())
print("\nMuestra de los primeros estudiantes clasificados:")
print(df.head(10))
