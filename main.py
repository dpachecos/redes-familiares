import argparse
from dataclasses import dataclass, field
from pathlib import Path

from redesfam.importing import import_data
from redesfam.exporting import export_data



@dataclass
class MainArgs:
    command: str
    files: list[str] = field(default_factory=list)
    output: str = None


def parse_args() -> MainArgs:
    """Interpreta los argumentos de la línea de comandos"""
    parser = argparse.ArgumentParser(description="Aplicación para procesar archivos y gestionar Neo4j")
    subparsers = parser.add_subparsers(dest='command', required=True)
    
    # Comando "import"
    import_parser = subparsers.add_parser("import", help="Importar archivos de texto a la base de datos")
    import_parser.add_argument("files", nargs='+', help="Ruta(s) de archivo(s) de entrada", type=Path)
    
    # Comando "export"
    export_parser = subparsers.add_parser("export", help="Exportar datos de la base de datos a un archivo")
    export_parser.add_argument("output", help="Ruta del archivo de salida", type=Path)
    
    args = parser.parse_args()
    if args.command == "import":
        out = MainArgs(command=args.command, files=args.files)
    else:
        out = MainArgs(command=args.command, output=args.output)

    return out


def main():
    
    args = parse_args()

    match args.command:
        case "import":
            if not args.files:
                raise ValueError("Error: Se requieren archivos para importar.")
            import_data(args.files)
        case "export":
            if not args.output:
                raise ValueError("Error: Se requiere un archivo de salida.")
            export_data(args.output)
        case _:
            ValueError("Comando no reconocido.")
    

if __name__ == "__main__":
    main()
