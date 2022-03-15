
class MySQLQueryExecutor:
    """
    Class to manage execution of queries on DB.
    """

    def __init__(self, cursor):
        self._cursor = cursor

    def execute_query(self, query):
        rows = []

        try:
            self._cursor.execute(query)
        except Exception:
            # TODO: Add custom exception
            print("Invalid Query")

        for row in self._cursor:
            rows.append(row)

        self._cursor.reset()
        return rows
