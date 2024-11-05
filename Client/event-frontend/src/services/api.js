// src/services/api.js
import axios from 'axios';

const API = axios.create({
    baseURL: 'http://localhost:8000/users/', // Your Django API URL
});

// Set up the interceptor to include the token in every request
API.interceptors.request.use((config) => {
    const token = localStorage.getItem('token');
    if (token) {
        config.headers['Authorization'] = `Token ${token}`;
    }
    return config;
}, (error) => {
    // Handle error
    return Promise.reject(error);
});

export default API;
