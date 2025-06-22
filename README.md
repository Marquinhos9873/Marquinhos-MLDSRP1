# DSRP-MLE1: Regresión Logistica, Wisconsin_Breast_cancer data.

![release](https://img.shields.io/badge/release-v1.0.0-blue.svg)
![python](https://img.shields.io/badge/Python-3.11%2B-blue)
![framework](https://img.shields.io/badge/Framework-Scikit--learn-orange)


![image](https://github.com/user-attachments/assets/5f57dff5-40e7-4c4b-9653-f2f25aaed5bb)


Este proyecto académico sobre el dataset wisconsin_breastcancer.csv(Data.csv) reecuperado de https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data tiene como objetivo
realizar un modelo de regresión logística para poder predecir si el paciente dado a los datos, si padece cancer de mama o no.

## 🧠 1. Problema y Objetivo del Proyecto
###     Contexto del problema:
###     El cáncer de mama es una de las enfermedades más comunes y preocupantes a nivel mundial, representando un desafío significativo para los sistemas de salud debido a su alta incidencia y mortalidad asociada. Una detección temprana y precisa es fundamental para mejorar el pronóstico de los pacientes y permitir un tratamiento oportuno y eficaz.
###    En este proyecto, se trabaja con el conjunto de datos Wisconsin Breast Cancer (data.csv), con el objetivo de desarrollar un modelo de clasificación supervisado capaz de predecir la posible presencia de células cancerígenas benignas o malignas (tumor benigno o maligno). El propósito es facilitar herramientas automatizadas de apoyo al diagnóstico médico que permitan reducir el tiempo de respuesta y mejorar la toma de decisiones clínicas.
###    Objetivo del trabajo: 
###    El objetivo principal de este proyecto es desarrollar un modelo de clasificación supervisado utilizando regresión logística, orientado a predecir la variable diagnosis del conjunto de datos Wisconsin Breast Cancer. Una vez entrenado, el modelo será serializado en formato .joblib para su reutilización.
###    Para evaluar su desempeño, se utilizará el informe de clasificación (classification_report) que proporciona métricas como precisión, recall, f1-score y exactitud, con el fin de asegurar que el modelo minimice los errores de predicción y sea clínicamente útil como herramienta de apoyo diagnóstico.

## 🪧 2. Project Flowchart
###       El proyecto sigue el presente diagrama de flujo que muestra su funcionamiento
   ![image](https://github.com/user-attachments/assets/bbcd8fc2-cf17-4635-b26b-0116937d1e6b)

## ✍️ 3. Descripción del dataset
###    Este dataset es recuperado de Kaggle (Kaggle.com) mas específicamente de "Breast Cancer Wisconsin (Diagnostic) Data Set" (https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data) \nconteniendo datos provechosos para este ejercicio, como la morfología de los casos.

| Ítem                | Detalle                                                                                                                                               |
|---------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Fuente**          | [Página de Kaggle](https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data) Autores: UCI Machine Learning (2014)                                          |
| **Licencia**        | CC BY-4.0 – permite redistribución y obras derivadas con atribución                                                                                   |
| **Filas utilizadas**| Todas                              |
| **Variable objetivo**| `diagnosis` – Diagnostico respecto al tipo de masa estudiado , si es un tumor maligno o benigno.                                                                                                 |
| **Familias de variables** | **Morfológicas**: `radius_mean`, `perimeter_mean`, `area_mean`, `compactness_mean`, `concavity_mean`, `concave points_mean`<br>**Texturales**: `texture_mean`, `smoothness_mean` |
| **Valores faltantes**| Ninguno                                                                                                            |
| **Unidades**         | No especifica, pero como es un dataset de Winsconsin, USA. Se interpretará con el sistema métrico local.                                                                           |

| Variable               | Descripción                                                                 | Tipo de dato     | Familia de Variable   |
|------------------------|-----------------------------------------------------------------------------|------------------|------------------------|
| `diagnosis`            | Diagnóstico del tejido mamario (`M`: maligno, `B`: benigno)                | `object`         | Etiqueta/objetivo      |
| `radius_mean`          | Promedio de la distancia del centro a los puntos del perímetro             | `float`          | Morfológica            |
| `texture_mean`         | Desviación estándar de los valores de escala de grises                     | `float`          | Textural               |
| `perimeter_mean`       | Promedio del perímetro del tumor                                            | `float`          | Morfológica            |
| `area_mean`            | Promedio del área del tumor                                                 | `float`          | Morfológica            |
| `smoothness_mean`      | Variación local en las longitudes del radio                                 | `float`          | Morfológica            |
| `compactness_mean`     | (Perímetro² / Área) - 1.0                                                   | `float`          | Morfológica            |
| `concavity_mean`       | Severidad promedio de las partes cóncavas del contorno                     | `float`          | Morfológica            |
| `concave points_mean`  | Promedio de puntos cóncavos del contorno                                   | `float`          | Morfológica            |
Nota: Hay otras 23 variables adicionales en el dataset, todas del tipo 'float'.

## ✉️ 4. Model Card :  Regresión_Logistica_breastcancer v_1
### Detalles :


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── Makefile           <- Makefile with convenience commands like `make data` or `make train`
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── docs               <- A default mkdocs project; see www.mkdocs.org for details
│
├── models             <- Trained and serialized models, model predictions, or model summaries
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering),
│                         the creator's initials, and a short `-` delimited description, e.g.
│                         `1.0-jqp-initial-data-exploration`.
│
├── pyproject.toml     <- Project configuration file with package metadata for 
│                         package-dsrp-mle1 and configuration for tools like black
│
├── references         <- Data dictionaries, manuals, and all other explanatory materials.
│
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
│
└── package-dsrp-mle1   <- Source code for use in this project.
    │
    ├── __init__.py             <- Makes package-dsrp-mle1 a Python module
    │
    ├── config.py               <- Store useful variables and configuration
    │
    ├── dataset.py              <- Scripts to download or generate data
    │
    ├── features.py             <- Code to create features for modeling
    │
    ├── modeling                
    │   ├── __init__.py 
    │   ├── predict.py          <- Code to run model inference with trained models          
    │   └── train.py            <- Code to train models
    │
    └── plots.py                <- Code to create visualizations
```

--------

