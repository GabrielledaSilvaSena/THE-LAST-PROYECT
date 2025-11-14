"""
PROYECTO FINAL - ANALISIS DE PELICULAS TMDB
Autor: [Tu Nombre]
Fecha: Noviembre 2024
"""

import pandas as pd

print("PROYECTO FINAL - ANALISIS DE PELICULAS TMDB")
print("=" * 60)


# ===================================================================
# BLOQUE 1: CARGA DE DATOS
# ===================================================================

print("\nCARGANDO DATASETS...")
print("-" * 60)

# Cargar datasets
movies = pd.read_csv('data/raw/tmdb_5000_movies.csv')
print(f"Movies: {movies.shape[0]} filas, {movies.shape[1]} columnas")

credits = pd.read_csv('data/raw/tmdb_5000_credits.csv')
print(f"Credits: {credits.shape[0]} filas, {credits.shape[1]} columnas")


# ===================================================================
# BLOQUE 2: EXPLORACION INICIAL
# ===================================================================

print("\n" + "=" * 60)
print("EXPLORACION INICIAL")
print("=" * 60)

# Ver primeras filas
print("\nPrimeras 5 peliculas:")
print(movies.head())

# Ver columnas
print("\nColumnas en Movies:")
print(movies.columns.tolist())

print("\nColumnas en Credits:")
print(credits.columns.tolist())

# Informacion general
print("\nInformacion del dataset Movies:")
print(movies.info())

# Valores nulos
print("\nValores nulos en Movies:")
print(movies.isnull().sum())

# Estadisticas descriptivas
print("\nEstadisticas descriptivas:")
print(movies.describe())


# ===================================================================
# BLOQUE 3: UNION DE DATASETS
# ===================================================================

print("\n" + "=" * 60)
print("UNION DE DATASETS")
print("=" * 60)

# Unir movies y credits por el ID
df = pd.merge(movies, credits, left_on='id', right_on='movie_id', how='inner')

print(f"\nDataset unido: {df.shape[0]} filas, {df.shape[1]} columnas")

# Ver columnas finales
print("\nColumnas del dataset final:")
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")


# ===================================================================
# BLOQUE 4: LIMPIEZA DE DATOS
# ===================================================================

print("\n" + "=" * 60)
print("LIMPIEZA DE DATOS")
print("=" * 60)

# Crear copia para trabajar
df_clean = df.copy()

# Convertir fechas
print("\nConvirtiendo fechas...")
df_clean['release_date'] = pd.to_datetime(df_clean['release_date'], errors='coerce')

# Extraer año, mes, dia
df_clean['year'] = df_clean['release_date'].dt.year
df_clean['month'] = df_clean['release_date'].dt.month
df_clean['day'] = df_clean['release_date'].dt.day

print("Fechas procesadas correctamente")

# Calcular ganancia
print("\nCalculando metricas financieras...")
df_clean['profit'] = df_clean['revenue'] - df_clean['budget']

# Calcular ROI (Return on Investment)
# Evitar division por cero
df_clean['roi'] = 0
mask = df_clean['budget'] > 0
df_clean.loc[mask, 'roi'] = ((df_clean.loc[mask, 'revenue'] - df_clean.loc[mask, 'budget']) / df_clean.loc[mask, 'budget']) * 100

print("Metricas calculadas correctamente")

# Ver valores nulos
print("\nValores nulos en el dataset limpio:")
print(df_clean.isnull().sum())

# Analizar peliculas con presupuesto o ingresos en 0
print(f"\nPeliculas con budget = 0: {(df_clean['budget'] == 0).sum()}")
print(f"Peliculas con revenue = 0: {(df_clean['revenue'] == 0).sum()}")


# ===================================================================
# BLOQUE 5: TRANSFORMACION DE DATOS
# ===================================================================

print("\n" + "=" * 60)
print("TRANSFORMACION DE DATOS")
print("=" * 60)

# Crear categorias de presupuesto
print("\nCreando categoria de presupuesto...")
df_clean['budget_cat'] = 'Sin datos'
df_clean.loc[df_clean['budget'] < 10000000, 'budget_cat'] = 'Bajo'
df_clean.loc[(df_clean['budget'] >= 10000000) & (df_clean['budget'] < 50000000), 'budget_cat'] = 'Medio'
df_clean.loc[(df_clean['budget'] >= 50000000) & (df_clean['budget'] < 100000000), 'budget_cat'] = 'Alto'
df_clean.loc[df_clean['budget'] >= 100000000, 'budget_cat'] = 'Blockbuster'

# Crear categorias de rating
print("Creando categoria de rating...")
df_clean['rating_cat'] = 'Sin datos'
df_clean.loc[df_clean['vote_average'] < 5, 'rating_cat'] = 'Malo'
df_clean.loc[(df_clean['vote_average'] >= 5) & (df_clean['vote_average'] < 6), 'rating_cat'] = 'Regular'
df_clean.loc[(df_clean['vote_average'] >= 6) & (df_clean['vote_average'] < 7), 'rating_cat'] = 'Bueno'
df_clean.loc[(df_clean['vote_average'] >= 7) & (df_clean['vote_average'] < 8), 'rating_cat'] = 'Muy Bueno'
df_clean.loc[df_clean['vote_average'] >= 8, 'rating_cat'] = 'Excelente'

# Crear categorias de duracion
print("Creando categoria de duracion...")
df_clean['duration_cat'] = 'Sin datos'
df_clean.loc[df_clean['runtime'] < 90, 'duration_cat'] = 'Corta'
df_clean.loc[(df_clean['runtime'] >= 90) & (df_clean['runtime'] < 120), 'duration_cat'] = 'Media'
df_clean.loc[(df_clean['runtime'] >= 120) & (df_clean['runtime'] < 150), 'duration_cat'] = 'Larga'
df_clean.loc[df_clean['runtime'] >= 150, 'duration_cat'] = 'Muy Larga'

print("Categorias creadas correctamente")


# ===================================================================
# BLOQUE 6: RESUMEN DEL DATASET FINAL
# ===================================================================

print("\n" + "=" * 60)
print("DATASET FINAL")
print("=" * 60)

print(f"\nTotal de filas: {df_clean.shape[0]}")
print(f"Total de columnas: {df_clean.shape[1]}")

# Nuevas columnas creadas
print("\nColumnas creadas en el analisis:")
print("- year")
print("- month") 
print("- day")
print("- profit")
print("- roi")
print("- budget_cat")
print("- rating_cat")
print("- duration_cat")

# Mostrar muestra
print("\nMuestra de datos procesados:")
columnas_mostrar = ['title_x', 'year', 'budget', 'revenue', 'profit', 'roi', 'vote_average', 'budget_cat', 'rating_cat']
print(df_clean[columnas_mostrar].head(10))


# ===================================================================
# GUARDAR DATOS PROCESADOS
# ===================================================================

print("\n" + "=" * 60)
print("GUARDANDO DATOS")
print("=" * 60)

df_clean.to_csv('data/processed/dataset_final.csv', index=False)
print("\nDataset guardado en: data/processed/dataset_final.csv")

print("\n" + "=" * 60)
print("PROCESO COMPLETADO")
print("=" * 60)

"""
BLOQUE 7 - ANALISIS ESTADISTICO
Agregar este codigo despues del Bloque 6 en tu archivo analisis.py
"""

import pandas as pd

# Cargar el dataset limpio
df_clean = pd.read_csv('data/processed/dataset_final.csv')

print("\n" + "=" * 60)
print("ANALISIS ESTADISTICO")
print("=" * 60)


# ===================================================================
# 1. ANALISIS DESCRIPTIVO GENERAL
# ===================================================================

print("\n1. ESTADISTICAS DESCRIPTIVAS GENERALES")
print("-" * 60)

# Estadisticas de variables numericas
print("\nEstadisticas de variables financieras:")
columnas_financieras = ['budget', 'revenue', 'profit', 'roi']
print(df_clean[columnas_financieras].describe())

print("\nEstadisticas de otras variables:")
otras_columnas = ['vote_average', 'vote_count', 'runtime', 'popularity']
print(df_clean[otras_columnas].describe())


# ===================================================================
# 2. ANALISIS POR CATEGORIA DE PRESUPUESTO
# ===================================================================

print("\n" + "-" * 60)
print("2. ANALISIS POR CATEGORIA DE PRESUPUESTO")
print("-" * 60)

# Contar peliculas por categoria
print("\nDistribucion de peliculas por categoria de presupuesto:")
print(df_clean['budget_cat'].value_counts())

# Promedios por categoria de presupuesto
print("\nPromedios por categoria de presupuesto:")
agrupado_presupuesto = df_clean.groupby('budget_cat')[['budget', 'revenue', 'profit', 'roi', 'vote_average']].mean()
print(agrupado_presupuesto)


# ===================================================================
# 3. ANALISIS POR CATEGORIA DE RATING
# ===================================================================

print("\n" + "-" * 60)
print("3. ANALISIS POR CATEGORIA DE RATING")
print("-" * 60)

# Contar peliculas por rating
print("\nDistribucion de peliculas por rating:")
print(df_clean['rating_cat'].value_counts())

# Promedios por categoria de rating
print("\nPromedios por categoria de rating:")
agrupado_rating = df_clean.groupby('rating_cat')[['budget', 'revenue', 'profit', 'vote_count']].mean()
print(agrupado_rating)


# ===================================================================
# 4. ANALISIS TEMPORAL (POR AÑO)
# ===================================================================

print("\n" + "-" * 60)
print("4. ANALISIS TEMPORAL")
print("-" * 60)

# Peliculas por año
print("\nPeliculas por decada:")
df_clean['decade'] = (df_clean['year'] // 10) * 10
peliculas_por_decada = df_clean.groupby('decade').size()
print(peliculas_por_decada)

# Promedios por decada
print("\nPromedios por decada:")
promedios_decada = df_clean.groupby('decade')[['budget', 'revenue', 'vote_average']].mean()
print(promedios_decada)


# ===================================================================
# 5. CORRELACIONES
# ===================================================================

print("\n" + "-" * 60)
print("5. ANALISIS DE CORRELACIONES")
print("-" * 60)

# Calcular correlaciones entre variables numericas
columnas_para_corr = ['budget', 'revenue', 'profit', 'vote_average', 'vote_count', 'runtime', 'popularity']
correlaciones = df_clean[columnas_para_corr].corr()

print("\nMatriz de correlaciones:")
print(correlaciones)

# Mostrar las correlaciones mas fuertes con revenue
print("\nCorrelaciones con revenue (ingresos):")
corr_revenue = correlaciones['revenue'].sort_values(ascending=False)
print(corr_revenue)


# ===================================================================
# 6. TOP 10 PELICULAS
# ===================================================================

print("\n" + "-" * 60)
print("6. RANKINGS - TOP 10")
print("-" * 60)

# Top 10 por ingresos
print("\nTop 10 peliculas por ingresos:")
top_revenue = df_clean.nlargest(10, 'revenue')[['title_x', 'year', 'revenue', 'budget', 'profit']]
print(top_revenue)

# Top 10 por ROI
print("\nTop 10 peliculas por ROI:")
# Filtrar ROI validos (mayores a 0 y no infinitos)
df_valid_roi = df_clean[(df_clean['roi'] > 0) & (df_clean['roi'] < 10000)]
top_roi = df_valid_roi.nlargest(10, 'roi')[['title_x', 'year', 'budget', 'revenue', 'roi']]
print(top_roi)

# Top 10 por rating
print("\nTop 10 peliculas por rating (con minimo 100 votos):")
df_min_votos = df_clean[df_clean['vote_count'] >= 100]
top_rating = df_min_votos.nlargest(10, 'vote_average')[['title_x', 'year', 'vote_average', 'vote_count']]
print(top_rating)


# ===================================================================
# 7. ANALISIS DE DURACION
# ===================================================================

print("\n" + "-" * 60)
print("7. ANALISIS DE DURACION")
print("-" * 60)

print("\nDistribucion por categoria de duracion:")
print(df_clean['duration_cat'].value_counts())

print("\nPromedio de rating por duracion:")
rating_por_duracion = df_clean.groupby('duration_cat')['vote_average'].mean().sort_values(ascending=False)
print(rating_por_duracion)


# ===================================================================
# 8. RESUMEN DE HALLAZGOS
# ===================================================================

print("\n" + "=" * 60)
print("RESUMEN DE HALLAZGOS ESTADISTICOS")
print("=" * 60)

print("\nDatos generales:")
print(f"- Total de peliculas analizadas: {len(df_clean)}")
print(f"- Rango de años: {df_clean['year'].min():.0f} - {df_clean['year'].max():.0f}")
print(f"- Presupuesto promedio: ${df_clean['budget'].mean():,.0f}")
print(f"- Ingresos promedio: ${df_clean['revenue'].mean():,.0f}")
print(f"- Rating promedio: {df_clean['vote_average'].mean():.2f}")

print("\nCategoria de presupuesto mas comun:")
print(f"- {df_clean['budget_cat'].mode()[0]}")

print("\nCategoria de rating mas comun:")
print(f"- {df_clean['rating_cat'].mode()[0]}")

print("\nCorrelacion mas fuerte con ingresos:")
corr_sin_revenue = corr_revenue.drop('revenue')
print(f"- {corr_sin_revenue.index[0]}: {corr_sin_revenue.iloc[0]:.3f}")


# ===================================================================
# GUARDAR RESULTADOS
# ===================================================================

print("\n" + "=" * 60)
print("GUARDANDO RESULTADOS ESTADISTICOS")
print("=" * 60)

# Guardar cada tabla en CSV separado
agrupado_presupuesto.to_csv('data/processed/analisis_por_presupuesto.csv')
print("Guardado: analisis_por_presupuesto.csv")

agrupado_rating.to_csv('data/processed/analisis_por_rating.csv')
print("Guardado: analisis_por_rating.csv")

promedios_decada.to_csv('data/processed/analisis_por_decada.csv')
print("Guardado: analisis_por_decada.csv")

correlaciones.to_csv('data/processed/correlaciones.csv')
print("Guardado: correlaciones.csv")

top_revenue.to_csv('data/processed/top_revenue.csv', index=False)
print("Guardado: top_revenue.csv")

top_roi.to_csv('data/processed/top_roi.csv', index=False)
print("Guardado: top_roi.csv")

top_rating.to_csv('data/processed/top_rating.csv', index=False)
print("Guardado: top_rating.csv")

print("\nTodos los archivos guardados en: data/processed/")

print("\n" + "=" * 60)
print("ANALISIS ESTADISTICO COMPLETADO")
print("=" * 60)

"""
BLOQUE 8 - VISUALIZACIONES
Agregar este codigo despues del Bloque 7 en tu archivo analisis.py
"""

import pandas as pd
import matplotlib.pyplot as plt

# Cargar el dataset limpio
df_clean = pd.read_csv('data/processed/dataset_final.csv')

print("\n" + "=" * 60)
print("CREANDO VISUALIZACIONES")
print("=" * 60)

# Crear carpeta para guardar graficos
import os
if not os.path.exists('reports'):
    os.makedirs('reports')


# ===================================================================
# GRAFICO 1: PELICULAS POR CATEGORIA DE PRESUPUESTO
# ===================================================================

print("\n1. Creando grafico de peliculas por categoria de presupuesto...")

plt.figure(figsize=(10, 6))

# Contar peliculas por categoria
conteo_presupuesto = df_clean['budget_cat'].value_counts()

# Crear grafico de barras
conteo_presupuesto.plot(kind='bar', color='steelblue')
plt.title('Distribucion de Peliculas por Categoria de Presupuesto', fontsize=14, fontweight='bold')
plt.xlabel('Categoria de Presupuesto', fontsize=12)
plt.ylabel('Cantidad de Peliculas', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Guardar
plt.savefig('reports/grafico_1_presupuesto.png', dpi=300, bbox_inches='tight')
print("   Guardado: grafico_1_presupuesto.png")
plt.close()


# ===================================================================
# GRAFICO 2: PRESUPUESTO VS INGRESOS (DISPERSION)
# ===================================================================

print("2. Creando grafico de presupuesto vs ingresos...")

plt.figure(figsize=(10, 6))

# Filtrar peliculas con presupuesto e ingresos validos
df_valido = df_clean[(df_clean['budget'] > 0) & (df_clean['revenue'] > 0)]

# Grafico de dispersion
plt.scatter(df_valido['budget'], df_valido['revenue'], alpha=0.5, color='coral')
plt.title('Relacion entre Presupuesto e Ingresos', fontsize=14, fontweight='bold')
plt.xlabel('Presupuesto ($)', fontsize=12)
plt.ylabel('Ingresos ($)', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Guardar
plt.savefig('reports/grafico_2_presupuesto_vs_ingresos.png', dpi=300, bbox_inches='tight')
print("   Guardado: grafico_2_presupuesto_vs_ingresos.png")
plt.close()


# ===================================================================
# GRAFICO 3: EVOLUCION TEMPORAL (PELICULAS POR DECADA)
# ===================================================================

print("3. Creando grafico de evolucion temporal...")

plt.figure(figsize=(12, 6))

# Contar peliculas por decada
df_clean['decade'] = (df_clean['year'] // 10) * 10
peliculas_por_decada = df_clean.groupby('decade').size()

# Grafico de lineas
plt.plot(peliculas_por_decada.index, peliculas_por_decada.values, marker='o', linewidth=2, markersize=8, color='green')
plt.title('Evolucion del Numero de Peliculas por Decada', fontsize=14, fontweight='bold')
plt.xlabel('Decada', fontsize=12)
plt.ylabel('Numero de Peliculas', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Guardar
plt.savefig('reports/grafico_3_evolucion_temporal.png', dpi=300, bbox_inches='tight')
print("   Guardado: grafico_3_evolucion_temporal.png")
plt.close()


# ===================================================================
# GRAFICO 4: TOP 10 PELICULAS POR INGRESOS
# ===================================================================

print("4. Creando grafico de top 10 peliculas por ingresos...")

plt.figure(figsize=(12, 8))

# Obtener top 10
top_10 = df_clean.nlargest(10, 'revenue')[['title_x', 'revenue']].sort_values('revenue')

# Grafico de barras horizontales
plt.barh(top_10['title_x'], top_10['revenue'], color='purple')
plt.title('Top 10 Peliculas por Ingresos', fontsize=14, fontweight='bold')
plt.xlabel('Ingresos ($)', fontsize=12)
plt.ylabel('Pelicula', fontsize=12)
plt.grid(axis='x', alpha=0.3)
plt.tight_layout()

# Guardar
plt.savefig('reports/grafico_4_top_10_ingresos.png', dpi=300, bbox_inches='tight')
print("   Guardado: grafico_4_top_10_ingresos.png")
plt.close()


# ===================================================================
# GRAFICO 5: DISTRIBUCION DE RATINGS
# ===================================================================

print("5. Creando grafico de distribucion de ratings...")

plt.figure(figsize=(10, 6))

# Contar peliculas por categoria de rating
conteo_rating = df_clean['rating_cat'].value_counts()

# Grafico de barras
conteo_rating.plot(kind='bar', color='teal')
plt.title('Distribucion de Peliculas por Categoria de Rating', fontsize=14, fontweight='bold')
plt.xlabel('Categoria de Rating', fontsize=12)
plt.ylabel('Cantidad de Peliculas', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Guardar
plt.savefig('reports/grafico_5_ratings.png', dpi=300, bbox_inches='tight')
print("   Guardado: grafico_5_ratings.png")
plt.close()


# ===================================================================
# GRAFICO 6: INGRESOS PROMEDIO POR CATEGORIA DE PRESUPUESTO
# ===================================================================

print("6. Creando grafico de ingresos promedio por categoria...")

plt.figure(figsize=(10, 6))

# Calcular promedio de ingresos por categoria
ingresos_por_categoria = df_clean.groupby('budget_cat')['revenue'].mean().sort_values()

# Grafico de barras
ingresos_por_categoria.plot(kind='bar', color='orange')
plt.title('Ingresos Promedio por Categoria de Presupuesto', fontsize=14, fontweight='bold')
plt.xlabel('Categoria de Presupuesto', fontsize=12)
plt.ylabel('Ingresos Promedio ($)', fontsize=12)
plt.xticks(rotation=45)
plt.grid(axis='y', alpha=0.3)
plt.tight_layout()

# Guardar
plt.savefig('reports/grafico_6_ingresos_promedio.png', dpi=300, bbox_inches='tight')
print("   Guardado: grafico_6_ingresos_promedio.png")
plt.close()


# ===================================================================
# GRAFICO 7: DURACION VS RATING
# ===================================================================

print("7. Creando grafico de duracion vs rating...")

plt.figure(figsize=(10, 6))

# Filtrar datos validos
df_valido_rating = df_clean[df_clean['runtime'] > 0]

# Grafico de dispersion
plt.scatter(df_valido_rating['runtime'], df_valido_rating['vote_average'], alpha=0.5, color='crimson')
plt.title('Relacion entre Duracion y Rating', fontsize=14, fontweight='bold')
plt.xlabel('Duracion (minutos)', fontsize=12)
plt.ylabel('Rating Promedio', fontsize=12)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Guardar
plt.savefig('reports/grafico_7_duracion_vs_rating.png', dpi=300, bbox_inches='tight')
print("   Guardado: grafico_7_duracion_vs_rating.png")
plt.close()


# ===================================================================
# RESUMEN
# ===================================================================

print("\n" + "=" * 60)
print("VISUALIZACIONES COMPLETADAS")
print("=" * 60)
print("\nSe han creado 7 graficos en la carpeta 'reports/':")
print("1. grafico_1_presupuesto.png")
print("2. grafico_2_presupuesto_vs_ingresos.png")
print("3. grafico_3_evolucion_temporal.png")
print("4. grafico_4_top_10_ingresos.png")
print("5. grafico_5_ratings.png")
print("6. grafico_6_ingresos_promedio.png")
print("7. grafico_7_duracion_vs_rating.png")
print("\nEstos graficos pueden ser usados en tu informe y dashboard.")
print("=" * 60)