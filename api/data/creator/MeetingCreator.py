from datetime import datetime
from typing import List

from api.database.DBConfigurationProvider import DBConfigurationProvider
from api.database.DatabaseConnectionHelper import DatabaseConnectionHelper
from api.database.MySQLQueryExecutor import MySQLQueryExecutor
from api.helper.SQLValidationHelper import validate_user_id, validate_meeting_id, validate_input_string, \
    validate_sql_text, validate_sql_longtext
from api.helper.StringHelper import convert_list_to_comma_seperated_string

SQL_QUERY = """insert into MeetingsAssistantInitial.meetings (UserId, MeetingDateTime, NumberOfAttendees, MeetingTranscript, MeetingTitle, attendees)
values (%(user_id)s, %(meeting_date_time)s, %(number_of_attendees)s, %(meeting_description)s, %(meeting_title)s, %(attendees)s);"""


class MeetingCreator:
    """
    Class to create a Meeting.
    """

    def __init__(self, user_id: str, meeting_title: str, meeting_description: str, meeting_date_time: datetime,
                 attendees: List[str]):
        """
        Sets up dependencies and data required to  create a new meeting, including opening a DB connection

        :param user_id: string id of the user provided by Auth0
        :param meeting_title: string describing the meeting title
        :param meeting_description: string describing the meeting description
        :param meeting_date_time: datetime object for the date and time of the meeting taking place
        :param attendees: List of string containing names or alias' of those who attended the meeting
        """

        self._user_id = user_id
        self._meeting_title = meeting_title
        self._meeting_description = meeting_description
        self._meeting_date_time = meeting_date_time
        self._attendees = convert_list_to_comma_seperated_string(attendees)
        self._number_of_attendees = len(attendees)

        db_config = DBConfigurationProvider().get_configuration_from_local()
        self._connection_helper = DatabaseConnectionHelper(db_config)

    def send_meeting(self) -> None:
        """
        Creates a new meeting in the database.
        Only runs if a connection is open and the parameters are valid

        :return: None
        """
        if self._connection_helper.is_connection_open() and self._is_params_valid():
            query_helper = MySQLQueryExecutor(self._connection_helper.get_connection_cursor())
            result = query_helper.execute_query(SQL_QUERY, {
                'user_id': self._user_id,
                'meeting_title': self._meeting_title,
                'meeting_description': self._meeting_description,
                'meeting_date_time': self._meeting_date_time,
                'attendees': self._attendees,
                'number_of_attendees': self._number_of_attendees
            })

            self._connection_helper.commit_connection()

            # TODO: Else return error

    def finish(self) -> None:
        """
        Closes the connection to the database.

        :return: None
        """
        self._connection_helper.close_connection()

    def _is_params_valid(self) -> bool:
        """
        Checks whether the parameters to be added to the database are valid against the database data schema.

        :return: boolean describing if the parameters are valid
        """
        return validate_user_id(self._user_id) and validate_sql_text(self._meeting_title) and \
               validate_sql_longtext(self._meeting_description) and validate_sql_longtext(self._attendees)
