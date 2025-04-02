import subprocess
from neo4j import GraphDatabase, Driver



def connect_db() -> Driver:
    """Conecta a la base de datos Neo4j"""
    # Levanta el contenedor Neo4j a través de docker-compose antes de crear el driver
    subprocess.run(["docker-compose", "up", "-d", "neo4j"], check=True)
    uri = "bolt://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "test"))
    return driver