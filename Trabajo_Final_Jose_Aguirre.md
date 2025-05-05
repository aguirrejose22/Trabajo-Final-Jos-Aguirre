
# Trabajo académico final escrito

**Universidad Técnica Particular de Loja**  
**Maestría en Inteligencia Artificial Aplicada**  
**Módulo:** Herramientas para Inteligencia Artificial  
**Estudiante:** Ing. José Gabriel Aguirre Andrade Msc.  
**Docente:** PhD. Gonzalez Eras Alexandra Cristina  
**Fecha de entrega:** 4 de mayo de 2025  
**Repositorio GitHub:** Trabajo Final José Aguirre

## Archivos cargados al repositorio

- Dataset inicial: `eventos_paletizador.csv`  
- SQL de la base de datos: `paletizador_db.sql`  
- Script para generar la base de datos: `insertar_paletizadores.sql`  
- Notebook principal: `analisis_paletizador.ipynb`  
- Dataset final: `dataset_final.csv`

---

## 1. Introducción

La automatización industrial contemporánea demanda metodologías analíticas robustas que permitan extraer valor estratégico de los volúmenes crecientes de datos operativos. En este contexto, el presente trabajo explora la aplicación de técnicas avanzadas de análisis de datos para optimizar el funcionamiento de paletizadores industriales. Para ello, se integraron entornos locales y colaborativos (PyCharm, PgAdmin, Google Colab, Render), combinando información de bases de datos y archivos CSV.

---

## 2. Marco teórico

### 2.1 Librerías utilizadas

- **Pandas:** Biblioteca para manipulación de datos tabulares. Se usó para leer archivos CSV y consultas SQL, transformar datos, hacer agrupaciones y merges.  
- **SQLAlchemy:** ORM para conectar Python con bases de datos relacionales como PostgreSQL. Se usó para establecer conexiones y ejecutar queries.  
- **Matplotlib:** Biblioteca para visualización de datos. Se utilizó para generar gráficos de barras, personalizar estilos, insertar logos y textos.  
- **psycopg2-binary:** Driver necesario para que SQLAlchemy se comunique con PostgreSQL.  
- **Google Colab:** Plataforma colaborativa basada en notebooks. Permite ejecutar código Python en la nube.  
- **Render:** Servicio en la nube que permite desplegar bases de datos PostgreSQL accesibles desde Colab.

### 2.2 Comparativa de entornos

| Aspecto                | PyCharm + PgAdmin (Local) | Colab + Render (Nube)         |
|------------------------|----------------------------|-------------------------------|
| Instalación            | Requiere instalación local | Sin instalación, uso web      |
| Acceso a BD            | Local                      | Remoto, requiere configuración|
| Rendimiento            | Alto si PC es potente      | Depende de conexión internet  |
| Visualización          | Ventanas locales           | En el navegador               |
| Reproducibilidad       | Menor (dependencia de PC)  | Mayor (acceso global)         |

---

## 3. Descripción del dataset usado

### 3.1 Dataset CSV
`eventos_paletizador.csv` contiene registros de eventos operativos de los paletizadores. Campos:
- `machine_id`, `evento`, `fecha`, `operario`, `tiempo_segundos`.

### 3.2 Dataset SQL
`palletizer_info` contiene información técnica de cada máquina. Campos:
- `machine_id`, `model`, `location`, `install_date`, `last_maintenance`, `certified_operator`.

Ambos se integran mediante `machine_id`.

---

## 4. Descripción de los pasos realizados

### 4.1 Instalación de librerías

**Google Colab:**
```python
!pip install sqlalchemy psycopg2-binary pandas matplotlib
```

**PyCharm/local:**
```bash
pip install sqlalchemy psycopg2-binary pandas matplotlib
```

### 4.2 Conexión a la base de datos

**Colab (Render):**
```python
from sqlalchemy import create_engine
conexion = create_engine('postgresql+psycopg2://usuario:contraseña@host:5432/paletizador_db')
```

**PyCharm (pgAdmin):**
```python
conexion = create_engine('postgresql+psycopg2://postgres:1234@localhost:5432/paletizado_db')
```

### 4.3 Lectura y combinación de datasets
```python
import pandas as pd

# Cargar CSV y SQL
df_csv = pd.read_csv('eventos_paletizador.csv')
df_sql = pd.read_sql('SELECT * FROM palletizer_info', conexion)

# Asegurar mismo tipo
df_csv['machine_id'] = df_csv['machine_id'].astype(str)
df_sql['machine_id'] = df_sql['machine_id'].astype(str)

# Unir y filtrar
df_combinado = pd.merge(df_csv, df_sql, on='machine_id', how='left')
df_combinado_filtrado = df_combinado.dropna(subset=['model'])
```

### 4.4 Visualizaciones generadas
Se crearon 6 gráficos en Matplotlib:
1. Tiempo promedio por modelo
2. Cantidad de eventos por modelo
3. Eventos por operario
4. Duración promedio por operario
5. Eventos por tipo
6. Duración promedio por tipo

Cada gráfico incluye:
- Paleta `tab10`
- Logo UTPL
- Textos institucionales

---

## 5. Conclusiones

- El uso de librerías libres facilita el análisis avanzado sin altos costos.
- La integración de datos locales y en la nube permite mayor flexibilidad y reproducibilidad.
- Las visualizaciones generadas permiten una lectura clara de patrones operativos.
- Colab y Render mostraron ser ideales para trabajo colaborativo y presentación en la nube.

---

## 6. Bibliografía

McKinney, W. (2010). *Data Structures for Statistical Computing in Python*. Proceedings of the 9th Python in Science Conference, 51–56.  
Render. (2024). *Render PostgreSQL Documentation*. https://render.com/docs/databases  
Google. (2024). *Colaboratory: Welcome to Colab*. https://colab.research.google.com  
Pandas Documentation. (2024). https://pandas.pydata.org  
Matplotlib Documentation. (2024). https://matplotlib.org  
SQLAlchemy Documentation. (2024). https://www.sqlalchemy.org
