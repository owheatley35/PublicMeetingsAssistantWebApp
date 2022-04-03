from api.Constants import STRING_SPLITTER
from api.data.provider.meeting.MeetingProvider import MeetingProvider
from api.data.provider.updater.NoteUpdater import NoteUpdater
from api.helper.SQLValidationHelper import validate_meeting_note


class CreateNoteEndpoint:
    """
    Endpoint to create a new note, facilitates data type transfers.
    """

    def __init__(self, user_id: str, meeting_id: str, meeting_note_content: str):
        """
        Instantiates a meeting provider endpoint and converts the needed datatypes for saving to the database.

        :param user_id: string id of the user provided by Auth0
        :param meeting_id: string containing the meeting id as a number in the string
        :param meeting_note_content: String of the new meeting note
        """
        self._user_id: str = user_id
        self._meeting_id: int = int(meeting_id)
        self._endpoint_status: bool = True
        self._new_note_content: str = meeting_note_content
        self._existing_notes: str = MeetingProvider(self._user_id, self._meeting_id).retrieve_meetings().meeting_notes

    def create_note(self) -> bool:
        """
        If the endpoint is open and the meeting note is valid then create the new meeting note.

        :return: boolean whether adding the new note was successful
        """
        if self._endpoint_status and validate_meeting_note(self._new_note_content):
            new_notes_string = self._form_new_notes_string()
            note_updater = NoteUpdater(self._user_id, self._meeting_id, new_notes_string)
            note_updater.send_note()
            note_updater.finish()
            return True
        else:
            print("Failed to add new note.")
            return False

    def close_endpoint(self) -> None:
        """
        Close the endpoint.

        :return: None
        """
        self._endpoint_status = False

    def _form_new_notes_string(self) -> str:
        """
        Adds the new note to the existing notes string or creates a new notes string if one doesn't already exist.

        :return: String of new note string
        """

        if self._existing_notes:
            return self._existing_notes + STRING_SPLITTER + self._new_note_content.strip()
        else:
            return STRING_SPLITTER + self._new_note_content.strip()
