// src/services/authService.js
import API from './api';

export const register = async (username, email, password) => {
    const response = await API.post('register/', { username, email, password });
    return response.data;
};

export const login = async (username, password) => {
    const response = await API.post('login/', { username, password });
    return response.data;
};
