# Análisis de Películas TMDB - Proyecto Final

## Tabla de Contenidos

1. [Descripción del Proyecto](#descripción-del-proyecto)
2. [Objetivos](#objetivos)
3. [Justificación del Dataset](#justificación-del-dataset)
4. [Datasets Utilizados](#datasets-utilizados)
5. [Tecnologías y Herramientas](#tecnologías-y-herramientas)
6. [Estructura del Proyecto](#estructura-del-proyecto)
7. [Proceso de Análisis](#proceso-de-análisis)
8. [Principales Hallazgos](#principales-hallazgos)
9. [Cómo Ejecutar el Proyecto](#cómo-ejecutar-el-proyecto)
10. [Dashboard](#dashboard)
11. [Metodología](#metodología)
12. [Insights y Conclusiones](#insights-y-conclusiones)
13. [Desafíos y Soluciones](#desafíos-y-soluciones)
14. [Limitaciones del Estudio](#limitaciones-del-estudio)
15. [Trabajo Futuro](#trabajo-futuro)
16. [Requisitos del Proyecto](#requisitos-del-proyecto)
17. [Referencias](#referencias)
18. [Autor](#autor)
19. [Licencia](#licencia)
20. [Agradecimientos](#agradecimientos)
21. [Contacto](#contacto)

---

## Descripción del Proyecto

Este proyecto representa el trabajo final del Bootcamp de Data & Analytics, donde se realiza un análisis exhaustivo de datos de películas de la base de datos TMDB (The Movie Database). El objetivo es demostrar competencias en análisis de datos, transformación, limpieza, visualización y creación de dashboards operativos.

El análisis explora más de 4,800 películas, examinando sus características financieras, temporales y de recepción del público, identificando patrones y tendencias en la industria cinematográfica.

---

## Objetivos

- **Análisis Exploratorio de Datos (EDA)**: Comprender la estructura y características del dataset
- **Limpieza y Transformación**: Procesar y preparar los datos para análisis
- **Análisis Estadístico**: Identificar correlaciones, tendencias y patrones
- **Visualización**: Crear gráficos significativos que comuniquen hallazgos
- **Dashboard Operativo**: Desarrollar un dashboard interactivo en Power BI

---

## Justificación del Dataset

### ¿Por qué películas de TMDB?

La elección del dataset de películas TMDB se fundamenta en varios criterios:

**1. Relevancia del dominio:**
- La industria cinematográfica es un sector económico significativo con datos públicos accesibles
- Permite análisis multidimensional: financiero, temporal, calidad y audiencia
- Resultados comprensibles y comunicables para cualquier audiencia

**2. Calidad de los datos:**
- Dataset bien documentado y mantenido en Kaggle
- Información verificable y procedente de fuente confiable (TMDB)
- Diversidad de variables que permiten análisis profundos

**3. Complejidad adecuada:**
- Requiere limpieza y transformación de datos (fechas, JSON, valores nulos)
- Permite crear métricas derivadas (ROI, profit, categorías)
- Ofrece oportunidades para análisis estadístico significativo

**4. Aplicabilidad práctica:**
- Los insights generados tienen valor real para productores, inversores y analistas
- Permite responder preguntas de negocio concretas
- Facilita la creación de un dashboard operativo útil

---

## Datasets Utilizados

### Fuente de Datos
- **Origen**: [Kaggle - TMDB 5000 Movie Dataset](https://www.kaggle.com/tmdb/tmdb-movie-metadata)
- **Datasets originales**:
  - `tmdb_5000_movies.csv` (4,803 películas, 20 columnas)
  - `tmdb_5000_credits.csv` (4,803 películas, 4 columnas)

### Características del Dataset Final
- **Total de filas**: 4,803 películas
- **Total de columnas**: 28 columnas (tras transformaciones)
- **Período temporal**: Películas desde 1916 hasta 2017
- **Variables clave**: Presupuesto, ingresos, rating, duración, géneros, elenco

---

## Tecnologías y Herramientas

### Análisis de Datos
- **Python 3.x**
- **Pandas**: Manipulación y análisis de datos
- **Matplotlib**: Visualización de datos
- **Visual Studio Code**: IDE de desarrollo

### Dashboard
- **Power BI Desktop**: Creación de dashboard interactivo

### Control de Versiones
- **Git/GitHub**: Gestión del repositorio

---

## Estructura del Proyecto

```
proyecto-final-tmdb/
│
├── data/
│   ├── raw/                          # Datos originales
│   │   ├── tmdb_5000_movies.csv
│   │   └── tmdb_5000_credits.csv
│   │
│   └── processed/                    # Datos procesados
│       ├── dataset_final.csv         # Dataset completo procesado
│       ├── analisis_por_presupuesto.csv
│       ├── analisis_por_rating.csv
│       ├── analisis_por_decada.csv
│       ├── correlaciones.csv
│       ├── top_revenue.csv
│       ├── top_roi.csv
│       └── top_rating.csv
│
├── reports/                          # Visualizaciones y reportes
│   ├── grafico_1_presupuesto.png
│   ├── grafico_2_presupuesto_vs_ingresos.png
│   ├── grafico_3_evolucion_temporal.png
│   ├── grafico_4_top_10_ingresos.png
│   ├── grafico_5_ratings.png
│   ├── grafico_6_ingresos_promedio.png
│   └── grafico_7_duracion_vs_rating.png
│
├── analisis.py                       # Script principal de análisis
├── dashboard_tmdb.pbix               # Dashboard de Power BI
├── README.md                         # Este archivo
└── requirements.txt                  # Dependencias de Python
```

---

## Proceso de Análisis

### 1. Carga de Datos
- Importación de dos datasets de TMDB
- Verificación de dimensiones y estructura inicial

### 2. Exploración Inicial
- Análisis de columnas y tipos de datos
- Identificación de valores nulos
- Estadísticas descriptivas básicas

### 3. Unión de Datasets
- Merge de `movies` y `credits` por ID de película
- Dataset consolidado con información completa

### 4. Limpieza de Datos
- Conversión de fechas a formato datetime
- Extracción de año, mes y día
- Cálculo de métricas financieras:
  - **Profit**: Ganancia neta (revenue - budget)
  - **ROI**: Retorno de inversión ((revenue - budget) / budget × 100)

### 5. Transformación de Datos
Creación de variables categóricas:

**Categorías de Presupuesto:**
- Bajo: < $10M
- Medio: $10M - $50M
- Alto: $50M - $100M
- Blockbuster: > $100M

**Categorías de Rating:**
- Malo: < 5
- Regular: 5 - 6
- Bueno: 6 - 7
- Muy Bueno: 7 - 8
- Excelente: ≥ 8

**Categorías de Duración:**
- Corta: < 90 min
- Media: 90 - 120 min
- Larga: 120 - 150 min
- Muy Larga: ≥ 150 min

### 6. Análisis Estadístico
- Análisis descriptivo por categorías
- Estudio de correlaciones entre variables
- Análisis temporal por década
- Identificación de top performers

### 7. Visualización
Creación de 7 gráficos clave:
1. Distribución por categoría de presupuesto
2. Relación presupuesto vs ingresos
3. Evolución temporal de películas
4. Top 10 películas por ingresos
5. Distribución por rating
6. Ingresos promedio por categoría
7. Relación duración vs rating

### 8. Dashboard Interactivo
- Desarrollo en Power BI Desktop
- KPIs principales
- Visualizaciones interactivas
- Filtros dinámicos

---

## Principales Hallazgos

### Análisis Financiero
- **Presupuesto promedio**: ~$30M
- **Ingresos promedio**: ~$82M
- **Correlación presupuesto-ingresos**: 0.73 (fuerte relación positiva)
- Las películas tipo "Blockbuster" generan los mayores ingresos promedio

### Análisis de Calidad
- **Rating promedio**: 6.09/10
- **Correlación rating-ingresos**: 0.19 (relación débil)
- Las películas "Excelentes" (rating ≥ 8) no necesariamente son las más taquilleras
- La calidad artística y el éxito comercial son relativamente independientes

### Análisis Temporal
- **Período analizado**: 1916 - 2017 (101 años)
- **Década con más producciones**: 2000-2010
- Incremento exponencial en producción desde 1980
- Los presupuestos han aumentado significativamente en décadas recientes

### Rendimiento (ROI)
- Películas de bajo presupuesto pueden tener ROI excepcionales
- El ROI no correlaciona directamente con el presupuesto invertido
- Casos destacados de películas con presupuestos modestos y retornos extraordinarios

---

## Cómo Ejecutar el Proyecto

### Prerrequisitos
```bash
Python 3.7 o superior
pandas
matplotlib
Power BI Desktop (para visualizar el dashboard)
```

### Instalación

1. **Clonar el repositorio**
```bash
git clone https://github.com/[tu-usuario]/proyecto-final-tmdb.git
cd proyecto-final-tmdb
```

2. **Instalar dependencias**
```bash
pip install -r requirements.txt
```

3. **Ejecutar el análisis**
```bash
python analisis.py
```

### Salidas Generadas
- Dataset procesado: `data/processed/dataset_final.csv`
- Archivos de análisis: `data/processed/*.csv`
- Gráficos: `reports/*.png`

---

## Dashboard

El dashboard de Power BI incluye:

### Páginas
1. **Overview General**: KPIs principales y métricas resumen
2. **Análisis Financiero**: Presupuestos, ingresos y ROI
3. **Análisis de Calidad**: Ratings y recepción del público
4. **Análisis Temporal**: Evolución histórica de la industria

### KPIs Principales
- Total de películas analizadas
- Presupuesto total invertido
- Ingresos totales generados
- Rating promedio
- ROI promedio

### Interactividad
- Filtros por año, género, categoría de presupuesto
- Top N películas dinámico
- Comparativas entre categorías
- Análisis de correlaciones visual

---

## Metodología

### Enfoque de Análisis
1. **Análisis Univariado**: Estudio individual de cada variable
2. **Análisis Bivariado**: Relaciones entre pares de variables
3. **Análisis Temporal**: Evolución y tendencias a lo largo del tiempo
4. **Análisis Categórico**: Comparaciones entre grupos

### Criterios de Calidad
- Limpieza exhaustiva de datos nulos e inconsistentes
- Validación de rangos y valores lógicos
- Documentación clara de todas las transformaciones
- Reproducibilidad del análisis completo

---

## Insights y Conclusiones

### Conclusiones Clave

1. **El presupuesto importa**: Existe una correlación fuerte (0.73) entre presupuesto e ingresos, confirmando que la inversión en producción suele traducirse en mayores ganancias.

2. **Calidad ≠ Taquilla**: La correlación débil entre rating e ingresos (0.19) demuestra que las películas mejor valoradas por crítica y público no son necesariamente las más rentables.

3. **La industria ha crecido exponencialmente**: El número de producciones se ha multiplicado desde los años 80, reflejando la expansión global del cine.

4. **El ROI es impredecible**: Las películas con mayores retornos de inversión no son necesariamente las de mayor presupuesto, demostrando que la creatividad puede superar al capital.

### Aplicaciones Prácticas

- **Para productores**: Invertir en presupuesto correlaciona con ingresos, pero no garantiza éxito
- **Para inversores**: Diversificar entre blockbusters y producciones de presupuesto medio-bajo
- **Para distribuidores**: El rating puede no predecir éxito comercial
- **Para analistas**: La industria cinematográfica es multifactorial y requiere análisis holístico

---

## Desafíos y Soluciones

### Desafíos Técnicos Encontrados

**1. Valores nulos y datos inconsistentes**
- **Problema**: Películas con presupuesto y/o ingresos en 0, fechas mal formateadas
- **Solución**: Implementación de filtros condicionales para métricas (ROI solo cuando budget > 0), conversión robusta de fechas con manejo de errores

**2. Creación de métricas derivadas**
- **Problema**: División por cero al calcular ROI
- **Solución**: Uso de máscaras booleanas en pandas para aplicar cálculos solo a valores válidos

**3. Categorización de variables continuas**
- **Problema**: Definir umbrales significativos para presupuesto, rating y duración
- **Solución**: Análisis de percentiles y distribución de datos para establecer categorías equilibradas

**4. Formato de columnas JSON**
- **Problema**: Columnas como 'genres' y 'cast' almacenadas como strings JSON
- **Solución**: Pendiente de procesamiento para análisis más profundo (columnas mantenidas para referencia)

**5. Tamaño del dataset vs requisitos del proyecto**
- **Problema**: El proyecto requería mínimo 50,000 filas pero el dataset tiene 4,803
- **Solución**: Consulta con instructores del bootcamp, confirmando que la calidad y profundidad del análisis compensan el menor número de filas

### Aprendizajes Clave

- Importancia de exploración exhaustiva antes de iniciar transformaciones
- Valor de la documentación detallada del código
- Necesidad de validación constante de resultados
- Beneficio de crear análisis incrementales y verificables

---

## Limitaciones del Estudio

### Limitaciones del Dataset

1. **Período temporal limitado**: 
   - Datos hasta 2017, no incluye películas recientes ni impacto de streaming

2. **Películas con presupuesto/ingresos en cero**:
   - ~1,400 películas sin datos financieros completos
   - Sesgo hacia producciones con información pública disponible

3. **Datos estructurados no procesados**:
   - Columnas JSON (géneros, cast, crew) no fueron parseadas completamente
   - Análisis por género o director limitado

4. **Información de marketing ausente**:
   - No incluye datos de inversión en marketing
   - Falta información sobre estrategias de distribución

### Limitaciones del Análisis

1. **Correlación no implica causalidad**:
   - Las relaciones encontradas son asociaciones, no causas directas

2. **Factores externos no considerados**:
   - Competencia en fechas de estreno
   - Eventos globales (económicos, sociales)
   - Cambios en hábitos de consumo

3. **Sesgo de supervivencia**:
   - Dataset puede sobre-representar películas exitosas o con información pública

---

## Trabajo Futuro

### Mejoras Propuestas

**Análisis Adicionales:**
- Procesamiento de columnas JSON para análisis por género y director
- Análisis de redes sociales: actores que colaboran frecuentemente
- Estudio de franquicias y secuelas
- Análisis de rentabilidad por mes de estreno (estacionalidad)

**Mejoras Técnicas:**
- Implementación de modelos predictivos (regresión para predecir ingresos)
- Análisis de texto en descripciones y taglines
- Clustering de películas por características similares
- Dashboard con actualización automática desde API de TMDB

**Expansión del Dataset:**
- Integración con datos más recientes (2018-2024)
- Incorporación de datos de streaming
- Añadir información de presupuestos de marketing
- Incluir datos de redes sociales y menciones

---

## Requisitos del Proyecto

### Checklist de Requisitos Cumplidos

**Requisitos Técnicos:**
- ✅ Dos conjuntos de datos en bruto (`tmdb_5000_movies.csv` y `tmdb_5000_credits.csv`)
- ✅ Conjunto de datos final procesado (`dataset_final.csv`)
- ✅ Análisis exhaustivo del conjunto de datos
- ✅ Dashboard operativo en Power BI
- ✅ Informe del análisis (este README)
- ✅ README.md con documentación completa
- ✅ Organización profesional del repositorio

**Procesamiento de Datos:**
- ✅ Transformación y limpieza profunda
- ✅ Análisis descriptivo de los datos
- ✅ Análisis estadístico (correlaciones, distribuciones)
- ✅ Visualizaciones significativas (7 gráficos)
- ✅ Dashboard operativo interactivo

**Herramientas Utilizadas:**
- ✅ Python para EDA y análisis
- ✅ Pandas para manipulación de datos
- ✅ Visual Studio Code como IDE
- ✅ Power BI para dashboard y visualización

**Nota sobre el tamaño del dataset:**
Aunque el requisito especificaba 50,000 filas, este proyecto utiliza 4,803 películas. Esta discrepancia fue consultada y aprobada por los instructores del bootcamp, considerando que:
- La calidad y profundidad del análisis compensa el menor volumen
- El dataset permite cubrir todos los objetivos de aprendizaje
- La complejidad de las transformaciones y análisis es equivalente

---

## Referencias

- [TMDB Dataset - Kaggle](https://www.kaggle.com/tmdb/tmdb-movie-metadata)
- [The Movie Database (TMDB) API](https://www.themoviedb.org/)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [Matplotlib Documentation](https://matplotlib.org/stable/contents.html)
- [Power BI Documentation](https://docs.microsoft.com/en-us/power-bi/)

---

## Autor

**[Gabrielle da Silva Sena]**
- Bootcamp: Data & Analytics
- Proyecto: Análisis de Películas TMDB
- Fecha: Diciembre 2025

---

## Licencia

Este proyecto fue desarrollado con fines educativos como parte del Bootcamp de Data & Analytics.

Los datos utilizados pertenecen a TMDB y están sujetos a sus términos de uso.

---

## Agradecimientos

- A los instructores del Bootcamp de Data & Analytics por su guía
- A Kaggle y TMDB por proporcionar los datos
- A la comunidad de data science por recursos y aprendizaje compartido

---

## Contacto

Para preguntas o comentarios sobre este proyecto:
- GitHub: [tu-usuario]
- Email: [tu-email]
- LinkedIn: [tu-linkedin]

---

*Última actualización: Diciembre 2024*