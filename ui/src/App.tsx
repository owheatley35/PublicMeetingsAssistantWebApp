import React from 'react';
import './App.css';
import HomePage from "./pages/homepage/HomePage";
import "./style/global.scss"
import {Route, BrowserRouter, Routes} from "react-router-dom";
import LoginPage from "./pages/loginpage/LoginPage";
import NewMeetingPage from "./pages/newmeetingpage/NewMeetingPage";

function App() {
    return (
        <BrowserRouter>
            <Routes>
                <Route path="/" element={<HomePage/>} />
                <Route path="/login" element={<LoginPage/>} />
                <Route path="/new-meeting" element={<NewMeetingPage/>} />
            </Routes>
        </BrowserRouter>
    )
}

export default App;
