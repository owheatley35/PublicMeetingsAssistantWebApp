import logging


class MySQLQueryExecutor:
    """
    Class to manage execution of queries on DB.
    """

    def __init__(self, cursor):
        """
        :param cursor: A cursor object, should be created from the DatabaseConnectionHelper
        """
        self._cursor = cursor

    def execute_query(self, query, parameters={}):
        """
        Run a SQL query on a database using the cursor provided.
        Resets the cursor when done.

        :param query: String containing the SQL query
        :param parameters: optional - dictionary containing the parameters
        :return: list of rows retrieved from the result of the database
        """
        rows = []

        try:
            if parameters:
                self._cursor.execute(query, parameters)
            else:
                self._cursor.execute(query)

            logging.info("MySQLQueryExecutor: Query Successfully Executed")

        except Exception as e:
            logging.error("MySQLQueryExecutor: ", e)

        for row in self._cursor:
            rows.append(row)

        self._cursor.reset()
        return rows
