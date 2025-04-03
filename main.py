import argparse
from dataclasses import dataclass, field
from enum import Enum
from pathlib import Path

from redesfam.importing import import_data
from redesfam.exporting import export_data



class Command(Enum):
    """Comandos disponibles para la aplicación"""
    IMPORT = "import"
    EXPORT = "export"


@dataclass
class MainArgs:
    command: Command
    files: list[Path] = field(default_factory=list)
    output: Path | None = None


def parse_args() -> MainArgs:
    """Interpreta los argumentos de la línea de comandos"""
    parser = argparse.ArgumentParser(description="Aplicación para procesar archivos y gestionar Neo4j")
    subparsers = parser.add_subparsers(dest='command', help="Comandos disponibles", required=True)
    
    # Comando "import"
    import_parser = subparsers.add_parser("import", help="Importar archivos de texto a la base de datos")
    import_parser.add_argument("files", nargs='+', help="Ruta(s) de archivo(s) de entrada", type=Path)
    
    # Comando "export"
    export_parser = subparsers.add_parser("export", help="Exportar datos de la base de datos a un archivo")
    export_parser.add_argument("output", help="Ruta del archivo de salida", type=Path)
    
    args = parser.parse_args()
    if args.command == "import":
        out = MainArgs(command=Command.IMPORT, files=args.files)
    else:
        out = MainArgs(command=Command.EXPORT, output=args.output)

    return out


def main():
    
    args = parse_args()

    match args.command:
        case Command.IMPORT:
            if not args.files:
                raise ValueError("Error: Se requieren archivos para importar.")
            import_data(args.files)
        case Command.EXPORT:
            if not args.output:
                raise ValueError("Error: Se requiere un archivo de salida.")
            export_data(args.output)
        case _:
            ValueError("Comando no reconocido.")
    

if __name__ == "__main__":
    main()
