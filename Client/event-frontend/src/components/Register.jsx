// src/components/Register.jsx
import React, { useState } from 'react';
import { register } from '../services/authService';

const Register = () => {
    const [username, setUsername] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        await register(username, email, password);
        // Handle successful registration (e.g., redirect or show message)
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} required />
            <input type="email" placeholder="Email" onChange={(e) => setEmail(e.target.value)} required />
            <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} required />
            <button type="submit">Register</button>
        </form>
    );
};

export default Register;
