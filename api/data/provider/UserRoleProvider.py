import logging

from api.database.DBConfigurationProvider import DBConfigurationProvider
from api.database.DatabaseConnectionHelper import DatabaseConnectionHelper
from api.database.MySQLQueryExecutor import MySQLQueryExecutor
from api.helper.SQLValidationHelper import validate_user_id

SQL_QUERY = "SELECT RoleName FROM MeetingsAssistantInitial.users WHERE UserId = %(user_id)s"


class UserRoleProvider:

    def __init__(self, user_id: str):
        self._user_id = user_id
        self._result = ""

        db_config = DBConfigurationProvider().get_configuration_from_local()
        self._connection_helper = DatabaseConnectionHelper(db_config)

        if self._is_params_valid():
            self._result = self._get_role()
        else:
            logging.warning("Invalid Parameters")

    def get_user_role(self) -> str:
        return self._result if self._result else ""

    def _is_params_valid(self) -> bool:
        return validate_user_id(self._user_id)

    def _get_role(self):

        if self._connection_helper.is_connection_open():
            query_helper = MySQLQueryExecutor(self._connection_helper.get_connection_cursor())
            rows_returned = query_helper.execute_query(SQL_QUERY, {
                'user_id': self._user_id,
            })

            for row in rows_returned:
                role = rows_returned[0][0]
                print(role)
                return role

        logging.warning("No Open Connection")

    def finish(self):
        self._connection_helper.close_connection()
