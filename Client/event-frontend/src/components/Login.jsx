// src/components/Login.jsx
import React, { useState } from 'react';
import { login } from '../services/authService';

const Login = () => {
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleSubmit = async (e) => {
        e.preventDefault();
        try {
            const data = await login(username, password);
            localStorage.setItem('token', data.token); // Store token
            // Redirect or update UI, e.g., using react-router
            window.location.href = '/dashboard'; // Example redirect
        } catch (error) {
            console.error('Login failed:', error);
            // Handle error (e.g., show an error message)
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input type="text" placeholder="Username" onChange={(e) => setUsername(e.target.value)} required />
            <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} required />
            <button type="submit">Login</button>
        </form>
    );
};

export default Login;
