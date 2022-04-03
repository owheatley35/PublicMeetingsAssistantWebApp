from datetime import datetime
from typing import List

from api.data.creator.MeetingCreator import MeetingCreator
from api.helper.JSONHelper import convert_custom_object_to_dict
from api.helper.StringHelper import convert_str_to_datetime, convert_comma_seperated_string_to_list


class CreateMeetingEndpoint:
    def __init__(self, user_id: str, meeting_title: str, meeting_transcript: str, meeting_date: str, meeting_time: str, attendees: str):
        self._user_id: str = user_id
        self._meeting_title: str = meeting_title
        self._meeting_date_time: datetime = convert_str_to_datetime(meeting_date, meeting_time)
        self._attendees = convert_comma_seperated_string_to_list(attendees)
        self._meeting_transcript = meeting_transcript
        self._endpoint_status: bool = True
        self._meeting_creator = MeetingCreator(self._user_id, self._meeting_title, self._meeting_transcript, self._meeting_date_time, self._attendees)

    def create_meeting(self):
        if self._endpoint_status:
            self._meeting_creator.send_meeting()

    def close_endpoint(self) -> None:
        self._meeting_creator.finish()
        self._endpoint_status = False
