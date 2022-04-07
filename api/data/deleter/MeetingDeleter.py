import logging

from api.data.MeetingDataManipulator import MeetingDataManipulator
from api.database.MySQLQueryExecutor import MySQLQueryExecutor
from api.helper.SQLValidationHelper import validate_user_id, validate_meeting_id

SQL_QUERY = "DELETE FROM MeetingsAssistantInitial.meetings WHERE MeetingId = %(meeting_id)s AND UserId = %(user_id)s;"


class MeetingDeleter(MeetingDataManipulator):
    """
    Class to delete a meeting from the database using a user id and a meeting id
    """

    def __init__(self, user_id: str, meeting_id: int):
        """
        Opens the connection to the database and sets the parameters

        :param user_id: string of the user id provided by Auth0
        :param meeting_id: int of the meeting id as a number in the string
        """
        super().__init__(user_id, meeting_id)

    def delete_meeting(self):
        """
        Executes the delete query.

        :return: None
        """
        if self._connection_helper.is_connection_open() and self._is_params_valid():

            logging.info("MeetingDeleter: Connection open and params valid")

            query_helper = MySQLQueryExecutor(self._connection_helper.get_connection_cursor())
            query_helper.execute_query(SQL_QUERY, {
                'user_id': self._user_id,
                'meeting_id': self._meeting_id,
            })

            self._connection_helper.commit_connection()
        else:
            logging.error("MeetingDeleter: Meeting was not deleted from the database due to one of the following being "
                          "'flase': \n Connection Open: %s \n Parameters Valid: %s",
                          str(self._connection_helper.is_connection_open()), str(self._is_params_valid()))

    def _is_params_valid(self) -> bool:
        """
        Checks whether the parameters are valid.

        :return: boolean whether the parameters are valid
        """

        return validate_user_id(self._user_id) and validate_meeting_id(self._meeting_id)
