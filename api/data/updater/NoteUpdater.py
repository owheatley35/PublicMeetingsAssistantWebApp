from api.database.DBConfigurationProvider import DBConfigurationProvider
from api.database.DatabaseConnectionHelper import DatabaseConnectionHelper
from api.database.MySQLQueryExecutor import MySQLQueryExecutor
from api.helper.SQLValidationHelper import validate_user_id, validate_meeting_id, validate_input_string

SQL_QUERY = """UPDATE MeetingsAssistantInitial.meetings
SET MeetingNotes = %(new_note)s
WHERE UserId = %(user_id)s AND MeetingId = %(meeting_id)s;"""


class NoteUpdater:
    """
    Class to update a note content string in the database.
    """

    def __init__(self, user_id: str, meeting_id: int, new_note: str):
        """
        Initiates vars and a connection to the database.

        :param user_id: string id of the user provided by Auth0
        :param meeting_id: int of the meeting id as a number in the string
        :param new_note: String of the new meeting note
        """
        self._user_id: str = user_id
        self._meeting_id: int = meeting_id
        self._new_note: str = new_note

        db_config = DBConfigurationProvider().get_configuration_from_local()
        self._connection_helper = DatabaseConnectionHelper(db_config)

    def send_note(self) -> None:
        """
        Executes the query to add a new note. Only if the connection is open and the parameters are valid.

        :return: None
        """
        if self._connection_helper.is_connection_open() and self._is_params_valid():
            query_helper = MySQLQueryExecutor(self._connection_helper.get_connection_cursor())
            result = query_helper.execute_query(SQL_QUERY, {
                'user_id': self._user_id,
                'meeting_id': self._meeting_id,
                'new_note': self._new_note
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
        Checks whether the parameters to be added to the database are valid against the requirements for the database
        data schema.

        Meeting note validation happens in endpoint class since it must be checked before the string is concatenated
        Meeting note checks in this method are more basic than the full checks.

        :return: boolean whether the parameters are valid
        """

        return validate_user_id(self._user_id) and validate_meeting_id(self._meeting_id) and \
               validate_input_string(self._new_note)
