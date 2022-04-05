from typing import List

from api.data.provider.meeting.MeetingProvider import MeetingProvider
from api.data.updater.NoteUpdater import NoteUpdater
from api.helper.StringHelper import break_string_into_list, convert_list_into_string


class DeleteNoteEndpoint:
    """
    Endpoint to delete a specific note from our database using the user id, meeting id and note index
    """

    def __init__(self, user_id: str, meeting_id: str, meeting_note_index: int):
        """
        Retrieves and Converts data to the needed types for addition to the database, including validation.

        :param user_id: string id of the user provided by Auth0
        :param meeting_id: string containing the meeting id as a number in the string
        :param meeting_note_index: int containing the index of the note to delete
        """

        self._user_id: str = user_id
        self._meeting_id: int = int(meeting_id)
        self._endpoint_status: bool = True

        meeting_notes: str = MeetingProvider(self._user_id, self._meeting_id).retrieve_meetings().meeting_notes
        self._meeting_notes: List[str] = break_string_into_list(meeting_notes)

        # Only delete a note if the index exists
        if 0 <= meeting_note_index < len(self._meeting_notes):
            del self._meeting_notes[meeting_note_index]
            print("Changed index:", str(meeting_note_index), "resulting in", self._meeting_notes)
        else:
            # TODO: Add some monitoring here
            print("invalid index")
            self.close_endpoint()

    def delete_note(self) -> None:
        """
        Complete the deletion of the note.

        :return: None
        """
        if self._endpoint_status:
            new_note: str = convert_list_into_string(self._meeting_notes)
            note_updater = NoteUpdater(self._user_id, self._meeting_id, new_note)
            note_updater.send_note()
            note_updater.finish()

    def close_endpoint(self) -> None:
        """
        Close the endpoint.

        :return: None
        """
        self._endpoint_status = False
