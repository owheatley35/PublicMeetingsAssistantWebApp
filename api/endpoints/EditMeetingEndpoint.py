import logging
from datetime import datetime

from api.Constants import STRING_DATE_SPLITTER
from api.data.model.Response import Response
from api.data.provider.meeting.MeetingDateTimeProvider import MeetingDateTimeProvider
from api.data.updater.MeetingUpdater import MeetingUpdater
from api.endpoints.Endpoint import Endpoint


class EditMeetingEndpoint(Endpoint):
    """
    Endpoint to update the meeting information.
    """

    def __init__(self, user_id: str, meeting_id: str, new_meeting_title: str, new_meeting_description: str,
                 new_meeting_date: str):
        """
        Converts data types for the database and gathers the time for the datetime object.

        :param user_id:
        :param meeting_id:
        :param new_meeting_title:
        :param new_meeting_description:
        :param new_meeting_date:
        """
        super().__init__()

        self._user_id: str = user_id
        self._meeting_id: int = int(meeting_id)
        self._meeting_title: str = new_meeting_title
        self._meeting_description: str = new_meeting_description

        # Get the current meeting date time
        meeting_datetime_provider = MeetingDateTimeProvider(self._user_id, self._meeting_id)
        self._current_date_time: datetime = meeting_datetime_provider.get_meeting_datetime()
        meeting_datetime_provider.finish()
        logging.info("EditMeetingEndpoint: Retrieved Current datetime")

        year, month, day = new_meeting_date.split(STRING_DATE_SPLITTER)
        self._meeting_date_time: datetime = datetime(int(year), int(month), int(day), self._current_date_time.hour,
                                                     self._current_date_time.minute, 0)

        self._updater = MeetingUpdater(self._user_id, self._meeting_id, self._meeting_title, self._meeting_description,
                                       self._meeting_date_time)

    def update_meeting(self) -> Response:
        """
        Run the update query on the database.

        :return: Response with success status
        """

        logging.info("EditMeetingEndpoint: Starting update")

        if self._endpoint_status:
            result = self._updater.send_update()
            self._endpoint_status = False
            return Response(result)

        logging.warning("EditMeetingEndpoint: Meeting note edited as Endpoint Closed")
        return Response(False)

    def close_endpoint(self) -> None:
        """
        Close the Endpoint

        :return: None
        """
        self._endpoint_status = False
        self._updater.finish()
        logging.info("EditMeetingEndpoint: Closed Endpoint")
