import sqlite3
import pandas as pd

# Conexión a la base de datos SQLite
conn = sqlite3.connect('C:/Users/artu_/Documents/tarea/ESCOM/4S/BDA/Prac6_ETL/sales_data.db')

# Leer los datos de la vista clean_sales
df_clean_sales = pd.read_sql_query("SELECT * FROM clean_sales", conn)

# Cerrar la conexión
conn.close()

# Exportar el DataFrame a un archivo XML
output_path = 'C:/Users/artu_/Documents/tarea/ESCOM/4S/BDA/Prac6_ETL/datos_limpios/clean_sales.xml'
df_clean_sales.to_xml(output_path, index=False)

print(f"Datos exportados a: {output_path}")
