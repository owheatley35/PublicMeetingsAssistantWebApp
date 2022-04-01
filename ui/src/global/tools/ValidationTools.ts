import Constants from "../Constants";

function validateNoteText(meetingNote: string): boolean {
    return meetingNote != null && meetingNote != "" && (!meetingNote.includes("<script>"))
        && (!meetingNote.includes(Constants.NOTE_SPLITTER));
}

export default validateNoteText;
