from api.database.DBConfigurationProvider import DBConfigurationProvider
from api.database.DatabaseConnectionHelper import DatabaseConnectionHelper


class DatabaseConnector:
    """
    Super Class of classes that need to make a database connection.
    """

    def __init__(self):
        db_config = DBConfigurationProvider().get_configuration_from_local()
        self._connection_helper = DatabaseConnectionHelper(db_config)

    def finish(self) -> None:
        """
        Close the connection to the database and the SSH tunnel.

        :return: None
        """
        self._connection_helper.close_connection()
