import React, {useEffect, useState} from "react";
import "../../../../../style/pages/homepage/components/sections/meetingslistmenusection/MeetingsListMenuSection.scss"
import {MeetingListMenuItemProps} from './MeetingsListMenuItem';
import MeetingsListMenuItemsLoader from "./MeetingsListMenuItemsLoader";
import {useAuth0} from "@auth0/auth0-react";
import getUsersMeetings from "../../../MeetingsProvider";

export interface MeetingListMenuSectionProps {
    readonly meetingListItems: Array<MeetingListMenuItemProps>
}

const MeetingsListMenuSection = () => {

    const starterStateArray: Array<MeetingListMenuItemProps> = []
    const [meetingListMenuSectionProps, setMeetingListMenuSectionProps] =
        useState(starterStateArray);

    const {getAccessTokenSilently} = useAuth0();

    useEffect(() => {
        const getMeetingItems = async () => {
            const accessToken = await getAccessTokenSilently();
            const meetingItems = await getUsersMeetings(accessToken);
            setMeetingListMenuSectionProps(meetingItems);
        }
        getMeetingItems()
    }, []);

    return (
        <div className="meetingslistmenusection">
            <div className="inner-meetingslistmenusection">
                <div className="toprow-meetingslistmenusection longways">
                    <div className="title-toprow-meetingslistmenusection">
                        <h1 className="heading-title-toprow-meetingslistmenusection">Your Meetings:</h1>
                    </div>
                    <div className="button-toprow-meetingslistmenusection">
                        <button
                            className="button-button-toprow-meetingslistmenusection button-standard text-normalish-thin"
                            onClick={() => {window.location.replace(window.location.origin + "/new-meeting")}}>
                            New Meeting
                        </button>
                    </div>
                </div>
                <div className="meeetinglist-meetingslistmenusection">
                    <MeetingsListMenuItemsLoader  meetingListItems={meetingListMenuSectionProps}/>
                </div>
            </div>
        </div>
    )
}

// function generateMeetingItems(items: List): React.Component {
//     for (let item in items) {
//         return item
//     }
// }

export default MeetingsListMenuSection