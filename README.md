Para los datos y el proceso lleva el siguiente proceso:
1 - hacer el proceso del csv hacia el DB con el codigo "process_csv.py" cambia solamente el path de la ruta
2 - una vez subida instalar "dbt" y tambien "dbt-sqlite" para poder aplicar ETL
3 - ya instalado vamos a la carpeta de usuario del sistema y configuramos en base donde esten las rutas del esquema
4 - ya ubicadas las rutas en el cmd abrimos la ruta de la practica y metemos los comandos dbt seed, dbt debug, dbt run
5 - si no salieron errores podemos ir a la DB y revisar desde un visualizador y ver los datos visualizados
6 - una vez tenemos los datos visualizados usamos el script "save_xml.py" para guardar el xml de los datos nuevos, cambia solamente el path de la ruta
