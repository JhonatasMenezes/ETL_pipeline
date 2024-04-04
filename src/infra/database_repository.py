from typing import Dict
from src.infra.database_connector import DatabaseConnecor
from .interfaces.database_repository import DatabaseRepositoryInterface


class DatabaseRepository(DatabaseRepositoryInterface):

    @classmethod
    def insert_artist(cls, data: Dict) -> None: # pylint: disable=arguments-differ
        query = '''
            INSERT INTO artists
                (first_name, second_name, surname, artist_id, link, extraction_date)
            VALUES
                (%s, %s, %s, %s, %s, %s)    
        '''

        cursor = DatabaseConnecor.connection.cursor()
        cursor.execute(query, list(data.values()))

        DatabaseConnecor.connection.commit()