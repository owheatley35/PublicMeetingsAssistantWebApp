import datetime
from typing import List

from api.data.model.meeting.Meeting import Meeting
from api.database.DBConfigurationProvider import DBConfigurationProvider
from api.database.DatabaseConnectionHelper import DatabaseConnectionHelper
from api.database.MySQLQueryExecutor import MySQLQueryExecutor
from api.helper.SQLValidationHelper import validate_meeting_id, validate_user_id

SQL_QUERY = """SELECT MeetingId, MeetingTitle, NumberOfAttendees, MeetingDateTime, MeetingTranscript, MeetingNotes 
FROM MeetingsAssistantInitial.meetings WHERE UserId = %(user_id)s AND MeetingId = %(meeting_id)s"""


class MeetingProvider:

    def __init__(self, user_id: str, meeting_id: int):
        self._user_id: str = user_id
        self._meeting_id: int = meeting_id
        self._result: Meeting = Meeting(0, "", datetime.datetime.now(), 0, "", "")

        db_config = DBConfigurationProvider().get_configuration_from_local()
        self._connection_helper = DatabaseConnectionHelper(db_config)

        if self._is_params_valid():
            print("Valid Params")
            self._result = self._get_meeting_information()
        else:
            print("Invalid Params")

    def retrieve_meetings(self) -> Meeting:
        return self._result

    def _is_params_valid(self) -> bool:
        return validate_user_id(self._user_id) and validate_meeting_id(self._meeting_id)

    def _get_meeting_information(self) -> Meeting:

        if self._connection_helper.is_connection_open():
            query_helper = MySQLQueryExecutor(self._connection_helper.get_connection_cursor())
            rows_returned = query_helper.execute_query(SQL_QUERY, {
                'user_id': self._user_id,
                'meeting_id': self._meeting_id
            })

            for row in rows_returned:
                temp_meeting = Meeting(row[0], row[1], row[3], row[2], row[4], row[5])
                print(temp_meeting)
                return temp_meeting

            # TODO: Raise Exception || Log error

    def finish(self) -> None:
        self._connection_helper.close_connection()
