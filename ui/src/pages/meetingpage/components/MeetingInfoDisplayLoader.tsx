import {useEffect, useState} from "react";
import {useAuth0} from "@auth0/auth0-react";
import getMeetingById, {MeetingInfo} from "../MeetingProvider";
import Constants from "../../../global/Constants";
import MeetingInfoDisplay from "./meetinginfodisplay/MeetingInfoDisplay";

interface MeetingInfoDisplayProps {
    readonly meetingId: number
}

function MeetingInfoDisplayLoader(props: MeetingInfoDisplayProps) {

    const starterMeeting: MeetingInfo = {
            meetingID: Constants.LOADING,
            meetingTitle: "",
            meetingDate: "",
            numberOfPeople: 0,
            meetingTranscript: "",
            meetingNotes: ""
        }

    const meetingId = useState(props.meetingId)
    const [isEditMode, setIsEditMode] = useState(false)
    const {getAccessTokenSilently} = useAuth0();
    const [meetingInfoState, setMeetingInfoState] = useState(starterMeeting)

    useEffect(() => {
        const getMeetingInfo = async () => {
            const accessToken = await getAccessTokenSilently();
            const meetingId: number = props.meetingId;
            const meetingInfo: MeetingInfo = await getMeetingById(accessToken, meetingId)

            setMeetingInfoState(meetingInfo)
        }

        if (!isEditMode) {
            console.log("Calling update")
            getMeetingInfo()
        }
    }, [])

    // return section
    if (meetingInfoState.meetingID == Constants.LOADING) {
        return (
            <div>
                <h1>LOADING...</h1>
            </div>
        )
    } else if (meetingInfoState.meetingID == Constants.DOES_NOT_EXIST) {
        return (
            <div>
                <h1>Sorry - We couldn't find that meeting :(</h1>
                <button className="button-standard" onClick={() => {window.location.assign('/')}}>
                    Click here to return home
                </button>
            </div>
        )
    } else {
        if (isEditMode) {
            return (
                <div className="meeting-info-display-edit">
                    <h1>EDIT MODE</h1>
                    <button onClick={() => {setIsEditMode(false)}}>SAVE</button>
                </div>
            )
        } else {
            return (
                <div className="meeting-info-display">
                    <h1>NORMAL MODE - MEETING ID: {meetingId}</h1>
                    <button onClick={() => {setIsEditMode(true)}}>EDIT</button>
                    <MeetingInfoDisplay meetingInfo={meetingInfoState} />
                </div>
            )
        }
    }
}

export default MeetingInfoDisplayLoader
