from redesfam.database import connect_db



def export_data(output_path):
    with connect_db() as driver:
        # Lógica para consultar Neo4j y generar archivo de salida
        print(f"Exportando datos a {output_path}")
        # ...código para realizar la consulta y escribir el archivo usando driver...