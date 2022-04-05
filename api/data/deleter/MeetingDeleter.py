from api.database.DBConfigurationProvider import DBConfigurationProvider
from api.database.DatabaseConnectionHelper import DatabaseConnectionHelper
from api.database.MySQLQueryExecutor import MySQLQueryExecutor
from api.helper.SQLValidationHelper import validate_user_id, validate_meeting_id

SQL_QUERY = "DELETE FROM MeetingsAssistantInitial.meetings WHERE MeetingId = %(meeting_id)s AND UserId = %(user_id)s;"


class MeetingDeleter:
    """
    Class to delete a meeting from the database using a user id and a meeting id
    """

    def __init__(self, user_id: str, meeting_id: int):
        """
        Opens the connection to the database and sets the parameters

        :param user_id: string of the user id provided by Auth0
        :param meeting_id: int of the meeting id as a number in the string
        """
        self._user_id: str = user_id
        self._meeting_id: int = meeting_id

        db_config = DBConfigurationProvider().get_configuration_from_local()
        self._connection_helper = DatabaseConnectionHelper(db_config)

    def delete_meeting(self):
        """
        Executes the delete query.

        :return: None
        """
        if self._connection_helper.is_connection_open() and self._is_params_valid():
            query_helper = MySQLQueryExecutor(self._connection_helper.get_connection_cursor())
            result = query_helper.execute_query(SQL_QUERY, {
                'user_id': self._user_id,
                'meeting_id': self._meeting_id,
            })

            self._connection_helper.commit_connection()

            # TODO: Else return error

    def finish(self) -> None:
        """
        Close the connection.

        :return: None
        """
        self._connection_helper.close_connection()

    def _is_params_valid(self) -> bool:
        """
        Checks whether the parameters are valid.

        :return: boolean whether the parameters are valid
        """

        return validate_user_id(self._user_id) and validate_meeting_id(self._meeting_id)
