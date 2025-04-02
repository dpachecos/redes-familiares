from redesfam.database import connect_db



def import_data(file_paths):
    with connect_db() as driver:
        # Lógica para leer archivos de texto y cargar datos en Neo4j
        for path in file_paths:
            print(f"Importando datos desde {path}")
            # ...código para leer el archivo e insertar en la base de datos usando driver...