import {MeetingListMenuSectionProps} from "./MeetingsListMenuSection";
import React from "react";
import MeetingsListMenuItem from "./MeetingsListMenuItem";

const MeetingsListMenuItemsLoader = (meetingsProps: MeetingListMenuSectionProps) => {
    if (meetingsProps.meetingListItems.length < 1) {
        return (
            <h1>LOADING . . .</h1>
        )
    } else {
        return (
            <ul>
                {
                    meetingsProps.meetingListItems.map((item) => {
                        return <MeetingsListMenuItem {...item}/>
                    })
                }
            </ul>
        )
    }
}

export default MeetingsListMenuItemsLoader
