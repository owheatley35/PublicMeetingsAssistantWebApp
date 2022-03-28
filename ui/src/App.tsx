import React from 'react';
import './App.css';
import HomePage from "./pages/homepage/HomePage";
import "./style/global.scss"
import {Route, BrowserRouter, Routes} from "react-router-dom";
import LoginPage from "./pages/loginpage/LoginPage";
import NewMeetingPage from "./pages/newmeetingpage/NewMeetingPage";
import MeetingPage from "./pages/meetingpage/MeetingPage";
import LocalView from "./global/LocalView";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage/>} />
                <Route path="/login" element={<LoginPage/>} />
                <Route path="/new-meeting" element={<NewMeetingPage/>} />
                <Route path="/meeting/:meeting_id" element={<MeetingPage/>} />

                <Route path="/local" element={<LocalView/>} />
            </Routes>
        </BrowserRouter>
    )
}

export default App;
