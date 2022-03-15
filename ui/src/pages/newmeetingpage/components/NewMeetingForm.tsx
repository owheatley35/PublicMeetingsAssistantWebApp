import "../../../style/pages/newmeetingpage/NewMeetingForm.scss"

const NewMeetingForm = () => {
    return (
         <form id="new-meeting-form" className="center-content vertical" action="/api/new/meeting">
            <div className="title-form-section-new-meting-page center-content longways">
                <p className="form-label-text">Meeting Title:</p>
                <input name="title-meeting" className="form-item" type="text" />
            </div>
            <div className="date-form-section-new-meting-page center-content longways">
                <p className="form-label-text">Meeting Date:</p>
                <input name="date-of-meeting" className="form-item" type="date" />
            </div>
            <div className="attendees-form-section-new-meting-page center-content longways">
                <p className="form-label-text">Meeting Attendee Names (Comma Seperated.):</p>
                <input name="attendees-meeting" className="form-item" type="text" />
            </div>
            <div className="start-time-form-section-new-meting-page center-content longways">
                <p className="form-label-text">Meeting Time:</p>
                <input name="time-meeting" className="form-item" type="time" />
            </div>
            <div className="submit-button-form-section-new-meting-page center-content longways">
                <input className="form-item button-standard" type="submit" />
            </div>
        </form>
    )
}

export default NewMeetingForm;
