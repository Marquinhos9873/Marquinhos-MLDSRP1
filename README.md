# DSRP-MLE1: Regresión Logistica, Wisconsin_Breast_cancer data.

![release](https://img.shields.io/badge/release-v1.0.0-blue.svg)
![python](https://img.shields.io/badge/Python-3.11%2B-blue)
![framework](https://img.shields.io/badge/Framework-Scikit--learn-orange)
![template](https://img.shields.io/badge/Template-CCDS-328F97?logo=cookiecutter)
![cloud](https://img.shields.io/badge/Cloud-Azure%20VM-007FFF?logo=microsoftazure)
![editor](https://img.shields.io/badge/Editor-JupyterLab-F37626?logo=jupyter)

![image](https://github.com/user-attachments/assets/5f57dff5-40e7-4c4b-9653-f2f25aaed5bb)


Este proyecto académico sobre el dataset wisconsin_breastcancer.csv(Data.csv) reecuperado de https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data tiene como objetivo
realizar un modelo de regresión logística para poder predecir si el paciente dado a los datos, si padece cancer de mama o no.
---
## 🧠 1. Problema y Objetivo del Proyecto
###     Contexto del problema:
###     El cáncer de mama es una de las enfermedades más comunes y preocupantes a nivel mundial, representando un desafío significativo para los sistemas de salud debido a su alta incidencia y mortalidad asociada. Una detección temprana y precisa es fundamental para mejorar el pronóstico de los pacientes y permitir un tratamiento oportuno y eficaz.
###    En este proyecto, se trabaja con el conjunto de datos Wisconsin Breast Cancer (data.csv), con el objetivo de desarrollar un modelo de clasificación supervisado capaz de predecir la posible presencia de células cancerígenas benignas o malignas (tumor benigno o maligno). El propósito es facilitar herramientas automatizadas de apoyo al diagnóstico médico que permitan reducir el tiempo de respuesta y mejorar la toma de decisiones clínicas.
###    Objetivo del trabajo: 
###    El objetivo principal de este proyecto es desarrollar un modelo de clasificación supervisado utilizando regresión logística, orientado a predecir la variable diagnosis del conjunto de datos Wisconsin Breast Cancer. Una vez entrenado, el modelo será serializado en formato .joblib para su reutilización.
###    Para evaluar su desempeño, se utilizará el informe de clasificación (classification_report) que proporciona métricas como precisión, recall, f1-score y exactitud, con el fin de asegurar que el modelo minimice los errores de predicción y sea clínicamente útil como herramienta de apoyo diagnóstico.
---
## 🪧 2. Project Flowchart

###       El proyecto sigue el presente diagrama de flujo que muestra su funcionamiento
   ![image](https://github.com/user-attachments/assets/bbcd8fc2-cf17-4635-b26b-0116937d1e6b)

---
## ✍️ 3. Descripción del dataset

###    Este dataset es recuperado de Kaggle (Kaggle.com) mas específicamente de "Breast Cancer Wisconsin (Diagnostic) Data Set" (https://www.kaggle.com/datasets/uciml/breast-cancer-wisconsin-data) conteniendo datos provechosos para este ejercicio, como la morfología de los casos.

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
---
## ✉️ 4. Model Card :  Regresión_Logistica_breastcancer v_1
### Detalles : 
- **Autor:** Marco P  
- **Fecha de release:** 22, June 2025  
- **Versión:** 1.0  
- **Model Type:** Regresión Logística
### Uso previsto:  
- **Finalidad principal:** Este modelo fue creado con el objetivo de **apoyar la predicción del tipo de tumor mamario** (benigno o maligno) basándose en mediciones morfológicas derivadas de estudios de imagen.
- **Usuarios esperados:** Está orientado a ser utilizado por **analistas de datos, investigadores en biomedicina y estudiantes de ciencia de datos o aprendizaje automático**.
- **Fuera de Alcance y Consideraciones Éticas:** Este modelo **no está diseñado para reemplazar el criterio médico profesional**, por lo que **no debe emplearse como único instrumento de diagnóstico clínico**.

### Evaluación:
### 📊 Comparación del Modelo


| Modelo              | Clase | Precision | Recall | F1-Score | Soporte |
|---------------------|--------|-----------|--------|----------|---------|
| **DummyClassifier** |   0    |   0.62     |  1.00  |   0.77    |   89    |
|                     |   1    |   0.00     |  0.00  |   0.00    |   54    |
|                     | Total  |           |        |          | **143** |
|                     | **Accuracy** |      |        |          | **0.62** |
|                     | **Macro avg** | 0.31 | 0.50 | 0.38 | 143 |
|                     | **Weighted avg** | 0.39 | 0.62 | 0.48 | 143 |

| Modelo                    | Clase | Precision | Recall | F1-Score | Soporte |
|---------------------------|--------|-----------|--------|----------|---------|
| **Regresión Logística**   |   0    |   0.99     |  0.98  |   0.98    |   89    |
|                           |   1    |   0.96     |  0.98  |   0.97    |   54    |
|                           | Total  |           |        |          | **143** |
|                           | **Accuracy** |      |        |          | **0.979** |
|                           | **Macro avg** | 0.98 | 0.98 | 0.98 | 143 |
|                           | **Weighted avg** | 0.98 | 0.98 | 0.98 | 143 |

### Datos de Entrenamiento:  
El modelo fue entrenado con la totalidad de los datos, exceptuando por la ultima y primera fila (unnamed32, id respectivamente) ya que unnamed32 es una fila con valores vacios e id es una fila con un numero identificador solamente.
![image](https://github.com/user-attachments/assets/ad8ff9b4-f6e2-40ce-93d0-2dbe28ca0d07)

---
## 🐈‍⬛ 5. Estrategia de Git:

### Ramas:
- **main:** Contiene el código de producción, estable
- **modelos_finales:** Como lo mostrado en clase, usada para poder guardar y subir los archivos .joblib/.pkl con su pull request respectiva.
---
## 💥 6. Resultados y Conclusiones
### 🧪 Evaluación del Modelo

El modelo desarrollado, basado en regresión logística, fue evaluado utilizando métricas estándar de clasificación (precision, recall, f1-score y accuracy), y los resultados fueron comparados con un modelo base (`DummyClassifier`) que predice siempre la clase más frecuente.

**DummyClassifier** presentó un rendimiento significativamente bajo:
- **Accuracy:** 62%
- **Recall en clase 1 (maligno):** 0%
- **F1-score en clase 1:** 0%

Modelo evaluado con `DummyClassifier`, clasificación errada esperada.

**Regresión Logística** mostró un rendimiento notable:
- **Accuracy:** 97.9%
- **Recall en clase 1:** 98%
- **Precision en clase 1:** 96%
- **F1-score general:** 97-98%

Esto indica que el modelo tiene un excelente desempeño en la detección tanto de casos benignos como malignos.

---

### 🧾 Conclusiones

El modelo cumple satisfactoriamente con el objetivo planteado: ofrecer un diagnóstico temprano y confiable del cáncer de mama, basado en características morfológicas. Gracias a su alto rendimiento, puede ser considerado como una posible herramienta complementaria útil en entornos clínicos para apoyar decisiones médicas.
Sin embargo, se recomienda su uso con supervisión profesional y como parte de un sistema más amplio de análisis, especialmente al considerar posibles sesgos en los datos y la importancia crítica de los falsos negativos en el diagnóstico médico.

---
## --> MODELO DE README CON COOKIECUTTER
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

