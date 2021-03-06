import logging

from api.Constants import ADMIN_ROLE_NAME
from api.data.deleter.MeetingDeleter import MeetingDeleter
from api.data.model.Response import Response
from api.data.provider.UserRoleProvider import UserRoleProvider


class DeleteMeetingEndpoint:
    """
    Endpoint to delete meeting from the database from its id

    This should only be used as a secure endpoint since private data can be accessed.
    Ensure that the user ID is validated through Auth0 before sending it into the class.
    """

    def __init__(self, user_id: str, meeting_id: str):
        """
        Created instance of deleter and formats parameters.

        :param user_id: string of the user id provided by Auth0
        :param meeting_id: Unique identifier of the meeting, generated by the database
        """
        self._user_id: str = user_id
        self._meeting_id: int = int(meeting_id)
        self._meeting_deleter: MeetingDeleter = MeetingDeleter(self._user_id, self._meeting_id)
        self._endpoint_status: bool = True
        self._user_role: str = UserRoleProvider(self._user_id).get_user_role()

    def delete_meeting(self) -> Response:
        """
        Use the meeting deleter to delete the desired meeting.

        :return: None
        """
        if self._user_role != ADMIN_ROLE_NAME:
            logging.warning("DeleteMeetingEndpoint: invalid Permissions to access this resource.")
            return Response(False, "Invalid Permissions to access this resource")

        if self._endpoint_status:
            self._meeting_deleter.delete_meeting()
            logging.info("DeleteMeetingEndpoint: Delete Started")
            return Response(True)

        logging.warning("DeleteMeetingsEndpoint: Delete did not commence")
        return Response(False)

    def close_endpoint(self) -> None:
        """
        Close this endpoint.

        :return: None
        """
        self._meeting_deleter.finish()
        self._endpoint_status = False
        logging.info("DeleteMeetingEndpoint: Endpoint Closed")
