
from api.data.provider.meeting.MeetingProvider import MeetingProvider
from api.helper.JSONHelper import convert_custom_object_to_dict


class GetMeetingEndpoint:

    def __init__(self, user_id: str, meeting_id: str):
        self._user_id: str = user_id
        self._meeting_id: int = int(meeting_id)
        self._endpoint_status: bool = True
        self._meetings_provider: MeetingProvider = MeetingProvider(self._user_id, self._meeting_id)

    def get_endpoint_result(self) -> dict:
        if self._endpoint_status:
            return convert_custom_object_to_dict(self._meetings_provider.retrieve_meetings())

    def close_endpoint(self) -> None:
        self._meetings_provider.finish()
        self._endpoint_status = False
