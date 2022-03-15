from datetime import datetime
from typing import List

from api.data.model.meeting.BasicMeeting import BasicMeeting
from api.database.DBConfigurationProvider import DBConfigurationProvider
from api.database.DatabaseConnectionHelper import DatabaseConnectionHelper
from api.database.MySQLQueryExecutor import MySQLQueryExecutor

BASIC_MEETING_QUERY = """SELECT MeetingId, MeetingTitle, NumberOfAttendees, MeetingDateTime FROM MeetingsAssistantInitial.meetings WHERE UserId = """
f = '%Y-%m-%d %H:%M:%S'


class BasicMeetingProvider:

    def __init__(self, user_id: str):
        self._result: List[BasicMeeting] = []
        self._user_id = user_id

        db_config = DBConfigurationProvider().get_configuration_from_local()
        self._connection_helper = DatabaseConnectionHelper(db_config)
        self._result = self._get_meeting_information()

    def refresh_data(self) -> None:
        self._result = self._get_meeting_information()

    def get_meeting_info(self) -> List[BasicMeeting]:
        return self._result

    def finish(self):
        self._connection_helper.close_connection()

    def _get_meeting_information(self) -> List[BasicMeeting]:
        result = []
        query = BASIC_MEETING_QUERY + '\'' + self._user_id + '\''

        if self._connection_helper.is_connection_open():
            query_helper = MySQLQueryExecutor(self._connection_helper.get_connection_cursor())
            rows_returned = query_helper.execute_query(query)

            for row in rows_returned:
                temp_meeting = BasicMeeting(row[0], row[1], row[3], row[2])
                result.append(temp_meeting)

        return result
