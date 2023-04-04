import React, { useState, useEffect} from 'react';
import { Form } from 'react-router-dom';
import "../styles/Login.css";
import axios from 'axios';

function Login() {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [userdata, setUserdata] = useState('');
    useEffect(()=>{
        async function getalluser(){
            try {
                const userdata = await axios.get('http://localhost:8000/login/')
                console.log(userdata.data)
                setUserdata(userdata.data)
            } catch (error) {
                console.log(error)
            }
        } getalluser();
        if(!userdata){
            return(<p>Prices are shown in their respective country's currency.</p>)
        }
        
    },[])

    const handleUsernameChange = (event) => {
        setUsername(event.target.value);
    };

    const handlePasswordChange = (event) => {
        setPassword(event.target.value);
    };

    const handleSubmit = (event) => {
        event.preventDefault();
        let formfield = new FormData()
        formfield.append('username',username)
        formfield.append('password',password)
        axios.post('http://localhost:8000/login/', formfield)
        .then(res=> {
            console.log(`Submitting login form with username: ${username} and password: ${password}`);
            console.log(res.data)
            window.location.href = '/dashboard';
        })
        .catch(error =>{
            console.log(error)
        })
        
        // Add your login logic here
        
    }


    return (
        <form onSubmit={handleSubmit}>
            <label>
                Username:
                <input type="text" value={username} onChange={handleUsernameChange} />
            </label>
            <label>
                Password:
                <input type="password" value={password} onChange={handlePasswordChange} />
            </label>
            <button type="submit">Log in</button>
        </form>
    );
}

export default Login;
