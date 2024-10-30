import sqlite3
import pandas as pd

# Conexión a la base de datos SQLite
conn = sqlite3.connect('C:/Users/artu_/Documents/tarea/ESCOM/4S/BDA/Prac6_ETL/sales_data.db')

# Leer y cargar el archivo CSV en fragmentos
for chunk in pd.read_csv('C:/Users/artu_/Documents/tarea/ESCOM/4S/BDA/Prac6_ETL/sales_data.csv', chunksize=500):
    chunk.to_sql('sales_data', conn, if_exists='append', index=False)

# Cerrar la conexión
conn.close()
