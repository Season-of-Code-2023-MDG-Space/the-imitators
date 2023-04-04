import "../styles/NavigationBar.css";
import logo from "../images/Bullbear logo.png";
import React, { useState } from 'react';
import { Link } from 'react-router-dom';
import axios from 'axios';
import Button from 'react-bootstrap/Button';

function Navigationbar() {

    const [searchQuery, setSearchQuery] = useState('');

    function showTicker(){
        axios.get('http://127.0.0.1:8000/ticker/')
        .then((res)=>{
            console.log(res.data)
            this.setState({ticker_name:res.data})
        })
    }showTicker();
    

    function handleSearchInputChange(event) {
        setSearchQuery(event.target.value);
    }


    

    function handleSearchEnter(event) {
        window.location.href = '/search/:ticker';
        // let formfield= new FormData()
        // formfield.append('ticker_name', event.target.value)
        // if(event.code === "Enter") {
        //     if(formfield){
        //         axios.post('http://127.0.0.1:8000/ticker/', formfield)
        //         .then((response)=>{
        //             console.log(response.data);
        //             window.location.href = '/search/:ticker';
        //         })
        //         .catch((error)=>{
        //             console.log(error)
        //         })
        //     }
            
        // }
    };

    

    function handleSignUpClick() {
        window.location.href = '/signup';
    }

    function handleLoginClick() {
        window.location.href = '/login';
    }

    return (
        <nav>
            <div className="logo">
                <img src={logo} alt="Company Logo" />
                <h1>Bulls and Bears</h1>
            </div>
            <div className="historic-data">
                {/* <input
                    type="text"
                    placeholder="Search your Stock here..."
                    name="ticer_name"
                    value={searchQuery}
                    onChange={handleSearchInputChange}
                    onKeyDown={handleSearchEnter}
                        // {showTickerData}

                /> */}
                <Button variant="success" onClick={handleSearchEnter}>Go to Historical Data Analysis</Button>
                
            </div>
            <div className="auth-buttons">
                <button onClick={handleSignUpClick}>Sign Up</button>
                <button onClick={handleLoginClick}>Log in</button>
            </div>
        </nav>
    );
}

export default Navigationbar;


