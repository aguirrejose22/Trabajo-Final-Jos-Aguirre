# Importamos las librerías necesarias
import pandas as pd  # Para manipular y analizar datos tabulares
import sqlalchemy  # Para conectarse a la base de datos PostgreSQL
import matplotlib.pyplot as plt  # Para graficar
import matplotlib.image as mpimg  # Para insertar imágenes (logo) en los gráficos
from mpl_toolkits.axes_grid1.inset_locator import inset_axes  # Para insertar el logo dentro del área del gráfico
import os  # Para trabajar con archivos y rutas

# Configuración de conexión a PostgreSQL
usuario = 'postgres'  # Usuario de la base de datos
contraseña = '1234'  # Contraseña del usuario
host = 'localhost'  # Dirección del servidor (localhost si es local)
puerto = '5432'  # Puerto de PostgreSQL
basededatos = 'paletizado_db'  # Nombre de la base de datos

# Crear el motor de conexión SQLAlchemy
conexion = sqlalchemy.create_engine(f'postgresql+psycopg2://{usuario}:{contraseña}@{host}:{puerto}/{basededatos}')

# Leer tabla desde PostgreSQL y archivo CSV
df_sql = pd.read_sql('SELECT * FROM palletizer_info', conexion)  # Cargar tabla de PostgreSQL
df_csv = pd.read_csv('eventos_paletizador.csv')  # Cargar archivo CSV con eventos

# Imprimir columnas disponibles para verificación
print("Columnas de df_csv:", df_csv.columns.tolist())
print("Columnas de df_sql:", df_sql.columns.tolist())

# Convertir machine_id a texto en ambos DataFrames para asegurar compatibilidad en el merge
df_csv['machine_id'] = df_csv['machine_id'].astype(str)
df_sql['machine_id'] = df_sql['machine_id'].astype(str)

# Unir los datos en un solo DataFrame
df_combinado = pd.merge(df_csv, df_sql, on='machine_id', how='left')

# Mostrar vista previa y verificación
print("\nPreview del DataFrame combinado:")
print(df_combinado.head(10))
print("Valores únicos de 'model':", df_combinado['model'].unique())
print("Cantidad de valores nulos en 'model':", df_combinado['model'].isnull().sum())

# Eliminar filas que no tienen valor en 'model'
df_combinado_filtrado = df_combinado.dropna(subset=['model'])

# Definir paleta de colores variada
colores = plt.cm.tab10.colors  # Paleta de colores 'tab10'

# Definir ruta al logo
logo_path = 'logo_utpl.png'  # Nombre del archivo del logo en la misma carpeta del script

# Función para agregar el logo y los textos institucionales en cada gráfico
def agregar_logo_texto(fig, ax, titulo):
    ax.set_title(titulo, fontsize=10)  # Título del gráfico con tamaño de fuente adecuado

    # Insertar logo en la parte superior izquierda
    if os.path.exists(logo_path):
        logo = mpimg.imread(logo_path)
        axins = inset_axes(ax, width="10%", height="10%", loc='upper left')
        axins.imshow(logo)
        axins.axis('off')  # Ocultar bordes del logo

    # Insertar textos institucionales en la parte inferior derecha
    fig.text(0.99, 0.02, "Universidad Técnica Particular de Loja", fontsize=6, ha='right')
    fig.text(0.99, 0.045, "Maestría en Inteligencia Artificial Aplicada", fontsize=6, ha='right')
    fig.text(0.99, 0.07, "Módulo: Herramientas para Inteligencia Artificial", fontsize=6, ha='right')
    fig.text(0.99, 0.095, "Estudiante: Ing. José Gabriel Aguirre Andrade, MSc.", fontsize=6, ha='right')
    fig.text(0.99, 0.12, "Docente: PhD. Alexandra Cristina Gonzalez Eras", fontsize=6, ha='right')

# --- GRÁFICO 1: Tiempo promedio por modelo ---
fig1, ax1 = plt.subplots(figsize=(8, 4))
df_combinado_filtrado.groupby('model')['tiempo_segundos'].mean().plot(kind='bar', ax=ax1, color=colores)
ax1.set_ylabel('Tiempo (segundos)')
ax1.set_xlabel('Modelo de Máquina', fontsize=8)
ax1.tick_params(axis='x', labelrotation=90, labelsize=7)  # Etiquetas en vertical con fuente más pequeña
agregar_logo_texto(fig1, ax1, 'Tiempo Promedio de Eventos por Modelo de Máquina')
plt.tight_layout()
plt.show()

# --- GRÁFICO 2: Cantidad de eventos por modelo ---
fig2, ax2 = plt.subplots(figsize=(8, 4))
df_combinado_filtrado['model'].value_counts().plot(kind='bar', ax=ax2, color=colores)
ax2.set_ylabel('Número de Eventos')
ax2.set_xlabel('Modelo de Máquina', fontsize=8)
ax2.tick_params(axis='x', labelrotation=90, labelsize=7)
agregar_logo_texto(fig2, ax2, 'Cantidad de Eventos por Modelo de Máquina')
plt.tight_layout()
plt.show()

# --- GRÁFICO 3: Eventos por operario ---
fig3, ax3 = plt.subplots(figsize=(8, 4))
df_combinado_filtrado['operario'].value_counts().plot(kind='bar', ax=ax3, color=colores)
ax3.set_ylabel('Cantidad de Eventos')
ax3.set_xlabel('Operario', fontsize=8)
ax3.tick_params(axis='x', labelrotation=90, labelsize=7)
agregar_logo_texto(fig3, ax3, 'Eventos Registrados por Operario')
plt.tight_layout()
plt.show()

# --- GRÁFICO 4: Duración promedio por operario ---
fig4, ax4 = plt.subplots(figsize=(8, 4))
df_combinado_filtrado.groupby('operario')['tiempo_segundos'].mean().plot(kind='bar', ax=ax4, color=colores)
ax4.set_ylabel('Tiempo Promedio (segundos)')
ax4.set_xlabel('Operario', fontsize=8)
ax4.tick_params(axis='x', labelrotation=90, labelsize=7)
agregar_logo_texto(fig4, ax4, 'Duración Promedio de Eventos por Operario')
plt.tight_layout()
plt.show()

# --- GRÁFICO 5: Eventos por tipo de evento ---
fig5, ax5 = plt.subplots(figsize=(8, 4))
df_combinado_filtrado['evento'].value_counts().plot(kind='bar', ax=ax5, color=colores)
ax5.set_ylabel('Cantidad')
ax5.set_xlabel('Tipo de Evento', fontsize=8)
ax5.tick_params(axis='x', labelrotation=90, labelsize=7)
agregar_logo_texto(fig5, ax5, 'Eventos por Tipo de Evento')
plt.tight_layout()
plt.show()

# --- GRÁFICO 6: Duración promedio por tipo de evento ---
fig6, ax6 = plt.subplots(figsize=(8, 4))
df_combinado_filtrado.groupby('evento')['tiempo_segundos'].mean().plot(kind='bar', ax=ax6, color=colores)
ax6.set_ylabel('Tiempo Promedio (segundos)')
ax6.set_xlabel('Tipo de Evento', fontsize=8)
ax6.tick_params(axis='x', labelrotation=90, labelsize=7)
agregar_logo_texto(fig6, ax6, 'Duración Promedio por Tipo de Evento')
plt.tight_layout()
plt.show()
