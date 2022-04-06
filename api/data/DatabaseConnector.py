from api.database.DBConfigurationProvider import DBConfigurationProvider
from api.database.DatabaseConnectionHelper import DatabaseConnectionHelper


class DatabaseConnector:

    def __init__(self):
        db_config = DBConfigurationProvider().get_configuration_from_local()
        self._connection_helper = DatabaseConnectionHelper(db_config)

    def finish(self) -> None:
        """
        Close the connection.

        :return: None
        """
        self._connection_helper.close_connection()
