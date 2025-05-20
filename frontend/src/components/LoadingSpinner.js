import React from "react";
import { FaSpinner } from "react-icons/fa";

const LoadingSpinner = ({ loading }) => {
    if (!loading) return null;

    return (
    <div className="loading-overlay">
        <div className="spinner-container">
          <FaSpinner className="spinner-icon" />
          <p className="loading-text">Loading...</p>
        </div>
    </div> 
    );
};

export default LoadingSpinner;