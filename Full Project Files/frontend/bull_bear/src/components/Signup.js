import React, { useState } from 'react';
import "../styles/Signup.css";
import axios from 'axios';

function Signup() {
    const [name, setName] = useState('');
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');
    const [age, setAge] = useState('');

    function showuser(){
        axios.get('http://127.0.0.1:8000/userdata/')
        .then((res)=>{
            console.log(res.data)
            // this.setState({user:res.data})
        })
    }showuser();

    const handleSubmit = (event) => {
        event.preventDefault();
        let formfield= new FormData()
        formfield.append('name', name)
        formfield.append('username',username)
        formfield.append('password',password)
        formfield.append('age',age)
        if(formfield){
            axios.post('http://127.0.0.1:8000/userdata/', formfield)
            .then((response)=>{
                console.log(response.data);
                window.location.href = '/';
            })
            .catch((error)=>{
                console.log(error)
            })
        }
            
        // Handle form submission
    };

    return (
        <div className="signup-form">
            <form onSubmit={handleSubmit}>
                <label htmlFor="name">Name:</label>
                <input
                    type="text"
                    id="name"
                    value={name}
                    onChange={(event) => setName(event.target.value)}
                    required
                />

                <label htmlFor="username">Username:</label>
                <input
                    type="text"
                    id="username"
                    value={username}
                    onChange={(event) => setUsername(event.target.value)}
                    required
                />

                <label htmlFor="password">Password:</label>
                <input
                    type="password"
                    id="password"
                    value={password}
                    onChange={(event) => setPassword(event.target.value)}
                    required
                />

                <label htmlFor="age">Age:</label>
                <input
                    type="number"
                    id="age"
                    value={age}
                    onChange={(event) => setAge(event.target.value)}
                    required
                />

                <button type="submit">Sign up</button>
            </form>
        </div>
    );
}

export default Signup;
