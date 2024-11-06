import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Checklist = ({ weddingId }) => {
    const [checklist, setChecklist] = useState([]);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        fetchChecklist();
    }, []);

    const fetchChecklist = async () => {
        try {
            const response = await axios.get(`/api/weddings/${weddingId}/checklist/`);
            setChecklist(response.data);
            setLoading(false);
        } catch (err) {
            setError("Error fetching checklist data.");
            setLoading(false);
        }
    };

    const toggleCompletion = async (itemId) => {
        try {
            const updatedChecklist = checklist.map(item => 
                item.id === itemId ? { ...item, is_completed: !item.is_completed } : item
            );
            setChecklist(updatedChecklist);

            await axios.patch(`/api/checklist/${itemId}/`, {
                is_completed: !checklist.find(item => item.id === itemId).is_completed
            });
        } catch (err) {
            setError("Error updating checklist item.");
        }
    };

    if (loading) return <p className="text-center text-gray-500">Loading checklist...</p>;
    if (error) return <p className="text-center text-red-500">{error}</p>;

    return (
        <div className="max-w-2xl mx-auto mt-10 p-6 bg-white shadow-md rounded-lg">
            <h2 className="text-2xl font-bold text-gray-700 mb-6">Wedding Checklist</h2>
            <ul className="space-y-4">
                {checklist.map(item => (
                    <li
                        key={item.id}
                        className={`flex justify-between items-center p-4 rounded-lg shadow-sm border ${item.is_completed ? 'bg-green-100' : 'bg-gray-50'}`}
                    >
                        <div>
                            <h3 className="text-lg font-semibold text-gray-800">{item.title}</h3>
                            <p className="text-sm text-gray-600">{item.description}</p>
                            <p className="text-sm text-gray-500">Due: {item.due_date}</p>
                        </div>
                        <button
                            onClick={() => toggleCompletion(item.id)}
                            className={`py-2 px-4 rounded-lg font-semibold ${
                                item.is_completed ? 'bg-red-500 text-white' : 'bg-blue-500 text-white'
                            }`}
                        >
                            {item.is_completed ? 'Mark Incomplete' : 'Mark Complete'}
                        </button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Checklist;
