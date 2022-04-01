import validateNoteText from "../../global/tools/ValidationTools";

async function updateMeetingNote(accessToken: Promise<string>, meetingId: number, meetingNoteIndex: number, meetingNote: string) {
    try {
        const token: string = await accessToken

        if (validateNote(meetingNoteIndex, meetingNote)) {
             await fetch("/api/update/meeting-note", {
                method: "POST",
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    "meeting_id": meetingId,
                    "note_content": meetingNote,
                    "note_index": meetingNoteIndex
                })
            });
        } else {
            console.log("Invalid Params");
        }
    } catch (e: any) {
        console.log(e.message);
    }
}

export function validateNote(meetingNoteIndex: number, meetingNote: string): boolean {
    return (meetingNoteIndex >= 0) && validateNoteText(meetingNote)
}

export default updateMeetingNote