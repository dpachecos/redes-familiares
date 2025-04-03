from neo4j import GraphDatabase, Driver



def connect_db() -> Driver:
    """Conecta a la base de datos Neo4j"""
    uri = "neo4j://localhost:7687"
    driver = GraphDatabase.driver(uri, auth=("neo4j", "redesfam"))
    return driver