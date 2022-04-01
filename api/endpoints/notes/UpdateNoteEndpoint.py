from typing import List

from api.data.provider.meeting.MeetingProvider import MeetingProvider
from api.data.provider.updater.NoteUpdater import NoteUpdater
from api.helper.StringHelper import break_string_into_list, convert_list_into_string


class UpdateNoteEndpoint:
    def __init__(self, user_id: str, meeting_id: str, meeting_note_content: str, meeting_note_index: int):
        self._user_id: str = user_id
        self._meeting_id: int = int(meeting_id)
        self._endpoint_status: bool = True

        meeting_notes: str = MeetingProvider(self._user_id, self._meeting_id).retrieve_meetings().meeting_notes
        self._meeting_notes: List[str] = break_string_into_list(meeting_notes)
        self._meeting_notes[meeting_note_index] = meeting_note_content
        print("Changed index:", str(meeting_note_index), "resulting in", self._meeting_notes)

    def update_note(self) -> None:
        if self._endpoint_status:
            new_note: str = convert_list_into_string(self._meeting_notes)
            note_updater = NoteUpdater(self._user_id, self._meeting_id, new_note)
            note_updater.send_note()
            note_updater.finish()

    def close_endpoint(self) -> None:
        self._endpoint_status = False
