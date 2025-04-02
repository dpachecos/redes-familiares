import pytest
from redesfam import database as db

def test_connect_db():
    """Test para verificar la conexión a la base de datos Neo4j"""
    with db.connect_db() as driver:
        try:
            driver.verify_connectivity()
        except Exception as e:
            pytest.fail(f"Error al conectar a la base de datos: {e}")