import logging
from typing import List

from api.data.provider.meeting.BasicMeetingProvider import BasicMeetingProvider
from api.helper.JSONHelper import convert_custom_object_list_to_dict


class GetBasicMeetingsEndpoint:
    """
    Endpoint to retrieve all meetings in a basic format that the user owns. (Identified by the user's id)

    This should only be used as a secure endpoint since private data can be accessed.
    Ensure that the user ID is validated through Auth0 before sending it into the class.
    """

    def __init__(self, user_id: str):
        """
        Open an instance of the GetBasicMeetingsEndpoint Endpoint and call the meetings provider.

        :param user_id: string of the user id provided by Auth0
        """
        logging.info("GetBasicMeetingsEndpoint: Starting")
        self._user_id = user_id
        self._meetings_provider = BasicMeetingProvider(self._user_id)
        self._endpoint_status = True

    def get_endpoint_result(self) -> List[dict]:
        """
        Converts BasicMeeting list into a dictionary and

        :return: List of basic meetings in dictionary form
        """
        if self._endpoint_status:
            return convert_custom_object_list_to_dict(self._meetings_provider.get_meeting_info())

    def close_endpoint(self) -> None:
        self._meetings_provider.finish()
        self._endpoint_status = False
        logging.info("GetBasicMeetingsEndpoint: Close Endpoint")
