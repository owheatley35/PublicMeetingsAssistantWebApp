import MeetingInfoDisplayProps from "./MeetingInfoDisplayProps";
import "../../../../style/pages/meetingpage/components/meetinginfodisplay/MeetingInfoDisplay.scss"
import Constants from "../../../../global/Constants";

function MeetingInfoDisplay(props: MeetingInfoDisplayProps) {

    const listOfNotes = formatNotes(props.meetingInfo.meetingNotes)
    const elementNotesList = listOfNotes.map((note) =>  <li className="note-item star-bullet-point"><p>{note}</p></li>)

    return (
        <div className="meeting-info-display">
            <div className="inner-meeting-info-display">
                <div className="title-section-meeting-info-display">
                    <div className="inner-title-section-meeting-info-display">
                        <div className="info-title-section-meeting-info-display">
                            <div className="date-wrapper-info-title-section-meeting-info-display">
                                <p className="date-text-title text-large-bold">{props.meetingInfo.meetingDate}</p>
                            </div>
                            <div className="title-wrapper-info-title-section-meeting-info-display">
                                <p className="meeting-title-text text-header-small-thin">{props.meetingInfo.meetingTitle}</p>
                            </div>
                        </div>
                        <div className="options-title-section-meeting-info-display">
                            <div className="inner-options-title-section-meeting-info-display">
                                <div className="horizontal-options-title-section-meeting-info-display">
                                    <div className="button-wrap">
                                        <button className="button-standard">EDIT</button>
                                    </div>
                                    <div className="button-wrap">
                                        <button className="button-standard">DELETE</button>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
                <div className="body-section-meeting-info-display">
                    <div className="inner-body-section-meeting-info-display">
                        <div className="horizontal-body-section-meeting-info-display">
                            <div className="main-body-section-meeting-info-display">
                                <div className="inner-main-body-section-meeting-info-display">
                                    <div className="transcript-wrap-main-body-section-meeting-info-display">
                                        <p>{props.meetingInfo.meetingTranscript}</p>
                                    </div>
                                    <div className="notes-section-main-body-section-meeting-info-display">
                                        <div className="notes-title-section">
                                            <div className="inner-title-section">
                                                <p className="notes-title text-large-bold">Notes:</p>
                                            </div>
                                        </div>
                                        <div className="notes-body-section">
                                            <div className="inner-notes-body-section">
                                                <ul className="notes-list">
                                                    {elementNotesList}
                                                </ul>
                                            </div>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className="side-panel-body-section-meeting-info-display">
                                <div className="vertical-side-panel-body-section-meeting-info-display">
                                    <div className="actions-side-panel-body-section-meeting-info-display">

                                    </div>
                                    <div className="notes-side-panel-body-section-meeting-info-display">

                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    )
}

function formatNotes(notes: string): string[] {
    let splitNotes = notes.split(Constants.NOTE_SPLITTER)
    return splitNotes.splice(1)
}

export default MeetingInfoDisplay