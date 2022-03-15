from api.data.provider.meeting.BasicMeetingProvider import BasicMeetingProvider
from api.helper.JSONHelper import convert_custom_object_list_to_dict


class GetBasicMeetingsEndpoint:

    def __init__(self, user_id: str):
        self._user_id = user_id
        self._meetings_provider = BasicMeetingProvider(self._user_id)
        self._endpoint_status = True

    def get_endpoint_result(self):
        if self._endpoint_status:
            return convert_custom_object_list_to_dict(self._meetings_provider.get_meeting_info())

    def close_endpoint(self):
        self._meetings_provider.finish()
        self._endpoint_status = False
