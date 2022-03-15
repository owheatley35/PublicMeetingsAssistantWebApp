
from api.database.DBConfigurationProvider import DBConfigurationProvider
from api.database.DatabaseConnectionHelper import DatabaseConnectionHelper
from api.database.MySQLQueryExecutor import MySQLQueryExecutor

PIZZA_QUERY = """SELECT Pizza from exampleDatabase.pizza
WHERE UserID = """


def get_fave_pizza(user_id: str):

    query = PIZZA_QUERY + "\'" + user_id + "\'"

    db_config = DBConfigurationProvider().get_configuration_from_local()
    connection_helper = DatabaseConnectionHelper(db_config)

    # Print all the databases
    try:
        sql_executor = MySQLQueryExecutor(connection_helper.get_connection_cursor())
        return sql_executor.execute_query(query)[0]

    finally:
        connection_helper.close_connection()
