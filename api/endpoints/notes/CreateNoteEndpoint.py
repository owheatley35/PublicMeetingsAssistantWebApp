from api.Constants import STRING_SPLITTER
from api.data.provider.meeting.MeetingProvider import MeetingProvider
from api.data.provider.updater.NoteUpdater import NoteUpdater
from api.helper.SQLValidationHelper import validate_meeting_note


class CreateNoteEndpoint:
    def __init__(self, user_id: str, meeting_id: str, meeting_note_content: str):
        self._user_id: str = user_id
        self._meeting_id: int = int(meeting_id)
        self._endpoint_status: bool = True
        self._new_note_content: str = meeting_note_content
        self._existing_notes: str = MeetingProvider(self._user_id, self._meeting_id).retrieve_meetings().meeting_notes

    def create_note(self) -> bool:
        if self._endpoint_status and validate_meeting_note(self._new_note_content):
            new_notes_string = self._form_new_notes_string()
            note_updater = NoteUpdater(self._user_id, self._meeting_id, new_notes_string)
            note_updater.send_note()
            note_updater.finish()
        else:
            print("Failed to add new note.")
            return False

    def close_endpoint(self) -> None:
        self._endpoint_status = False

    def _form_new_notes_string(self):
        if self._existing_notes:
            return self._existing_notes + STRING_SPLITTER + self._new_note_content.strip()
        else:
            return STRING_SPLITTER + self._new_note_content.strip()
