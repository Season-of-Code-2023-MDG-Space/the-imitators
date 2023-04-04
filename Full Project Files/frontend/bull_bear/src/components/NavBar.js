import React, { useState, useEffect } from "react";
import logo from "../images/Bullbear logo.png";
import "../styles/NavBar.css";
import {Link} from "react-router-dom";
import axios from 'axios';

function NavBar() {
    const [userName, setUserName] = useState("Sumit Raj");

    useEffect(()=>{
        async function getportfolio(){
            try {
                const userName = await axios.get('http://localhost:8000/portfoliodata/')
                console.log(userName.data)
                setUserName(userName.data)
                
            } catch (error) {
                console.log(error)
            }
        } getportfolio();

    
        
    },[])

    return (
        <div className="navigation-bar">
            <div className="company-logo">
                <img src={logo} alt="Company Logo" />
                <h1>Bulls and Bears</h1>
            </div>
            <ul className="navigation-links">
                <li>
                    <Link to="http://127.0.0.1:5500/frontend/bull_bear/src/htmlfiles/Dashboard.html">Dashboard</Link>
                </li>
                <li>
                    <Link to="/dashboard/watchlist">Watchlist</Link>
                </li>
                <li>
                    <Link to="/dashboard/portfolio">Portfolio</Link>
                </li>
                <li>
                    <Link to="/dashboard/news">News</Link>
                </li>
                <li>
                    <Link to="http://127.0.0.1:5500/frontend/bull_bear/src/htmlfiles/Stockinsights.html">Stocks Insights</Link>
                </li>

            </ul>
            <div className="user-name">
                
                <p>Welcome, {userName[0].name} :)</p>
                <h5><Link to="/">Log out</Link></h5>
            </div>
        </div>
    );
}

export default NavBar;
