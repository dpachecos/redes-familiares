import argparse
import subprocess
from neo4j import GraphDatabase, Driver

def connect_db() -> Driver:
    """Conecta a la base de datos Neo4j"""
    # Levanta el contenedor Neo4j a través de docker-compose antes de crear el driver
    subprocess.run(["docker-compose", "up", "-d", "neo4j"], check=True)
    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "test"))
    return driver

def import_data(file_paths):
    with connect_db() as driver:
        # Lógica para leer archivos de texto y cargar datos en Neo4j
        for path in file_paths:
            print(f"Importando datos desde {path}")
            # ...código para leer el archivo e insertar en la base de datos usando driver...

def export_data(output_path):
    with connect_db() as driver:
        # Lógica para consultar Neo4j y generar archivo de salida
        print(f"Exportando datos a {output_path}")
        # ...código para realizar la consulta y escribir el archivo usando driver...

def main():
    parser = argparse.ArgumentParser(description="Aplicación para procesar archivos y gestionar Neo4j")
    subparsers = parser.add_subparsers(dest='command')
    
    # Comando "import"
    import_parser = subparsers.add_parser("import", help="Importar archivos de texto a la base de datos")
    import_parser.add_argument("files", nargs='+', help="Ruta(s) de archivo(s) de entrada")
    
    # Comando "export"
    export_parser = subparsers.add_parser("export", help="Exportar datos de la base de datos a un archivo")
    export_parser.add_argument("output", help="Ruta del archivo de salida")
    
    args = parser.parse_args()
    
    if args.command == "import":
        import_data(args.files)
    elif args.command == "export":
        export_data(args.output)
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
