import logging
from typing import List

from api.data.provider.meeting.MeetingProvider import MeetingProvider
from api.data.updater.NoteUpdater import NoteUpdater
from api.helper.SQLValidationHelper import validate_meeting_note
from api.helper.StringHelper import break_string_into_list, convert_list_into_string


class UpdateNoteEndpoint:
    """
    Endpoint to Update a specific note in the database.

    This should only be used as a secure endpoint since private data can be accessed.
    Ensure that the user ID is validated through Auth0 before sending it into the class.
    """

    def __init__(self, user_id: str, meeting_id: str, meeting_note_content: str, meeting_note_index: int):
        """
        Updates the meeting note string to include the new note provided. It does this by converting the existing string
        into a List and then updates the intended index with the new value.

        :param user_id: string id of the user provided by Auth0
        :param meeting_id: string containing the meeting id as a number in the string
        :param meeting_note_content: String of the new meeting note
        :param meeting_note_index: int of the index of the note to update
        """
        self._user_id: str = user_id
        self._meeting_id: int = int(meeting_id)
        self._endpoint_status: bool = True

        meeting_notes: str = MeetingProvider(self._user_id, self._meeting_id).retrieve_meetings().meeting_notes
        self._meeting_notes: List[str] = break_string_into_list(meeting_notes)

        if validate_meeting_note(meeting_note_content):
            logging.info("UpdateNoteEndpoint: Meeting Note Valid")
            self._meeting_notes[meeting_note_index] = meeting_note_content
        else:
            logging.error("UpdateNoteEndpoint: Invalid note")
            self.close_endpoint()

    def update_note(self) -> None:
        """
        Calls the note updater to update the note value at the configured index.
        Only runs if the endpoint is active.

        :return: None
        """

        if self._endpoint_status:
            logging.info("UpdateNoteEndpoint: Starting update")
            new_note: str = convert_list_into_string(self._meeting_notes)
            note_updater = NoteUpdater(self._user_id, self._meeting_id, new_note)
            note_updater.send_note()
            note_updater.finish()
        else:
            logging.warning("UpdateNoteEndpoint: Endpoint Closed")

    def close_endpoint(self) -> None:
        """
        Closes the Endpoint.
        :return: None
        """
        self._endpoint_status = False
        logging.info("UpdateNoteEndpoint: Endpoint Closed")
