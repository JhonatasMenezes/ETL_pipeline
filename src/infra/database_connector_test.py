from .database_connector import DatabaseConnecor

def test_connect():
    assert DatabaseConnecor.connection is None
    DatabaseConnecor.connect()
    assert DatabaseConnecor.connection is not None
