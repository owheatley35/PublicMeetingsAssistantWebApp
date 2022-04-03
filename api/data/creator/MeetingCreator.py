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

    def __init__(self, user_id: str, meeting_title: str, meeting_description: str, meeting_date_time: datetime,
                 attendees: List[str]):
        self._user_id = user_id
        self._meeting_title = meeting_title
        self._meeting_description = meeting_description
        self._meeting_date_time = meeting_date_time
        self._attendees = convert_list_to_comma_seperated_string(attendees)
        self._number_of_attendees = len(attendees)

        db_config = DBConfigurationProvider().get_configuration_from_local()
        self._connection_helper = DatabaseConnectionHelper(db_config)

    def send_meeting(self):
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
        self._connection_helper.close_connection()

    def _is_params_valid(self) -> bool:
        return validate_user_id(self._user_id) and validate_sql_text(self._meeting_title) and \
               validate_sql_longtext(self._meeting_description) and validate_sql_longtext(self._attendees)
