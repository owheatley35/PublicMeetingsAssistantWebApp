import validateNoteText from "../../global/tools/ValidationTools";

async function createNewMeeting(accessToken: Promise<string>, meetingId: number, meetingNote: string) {
    try {
        const token: string = await accessToken

        if (validateNoteText(meetingNote)) {
             await fetch("/api/create/meeting-note", {
                method: "POST",
                headers: {
                    Authorization: `Bearer ${token}`,
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({
                    "meeting_id": meetingId,
                    "note_content": meetingNote,
                })
            });
        } else {
            console.log("Invalid Params");
        }
    } catch (e: any) {
        console.log(e.message);
    }
}

export default createNewMeeting

