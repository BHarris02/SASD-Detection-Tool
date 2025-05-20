import React, { useState } from "react";

const RepoInput = ({ repoUrl, setRepoUrl, fetchRepoStructure }) => {
    const [inputValue, setInputValue ] = useState(repoUrl || "");

    const handleSubmit = (event) => {
        event.preventDefault();

        if (!inputValue.trim()) {
            alert("Enter a valid Repository URL (e.g, owner/repo). TEST");
            return;
        }
        setRepoUrl(inputValue);
        fetchRepoStructure(inputValue);
    };

    return (
        <form onSubmit={handleSubmit} className="repo-input-form">
            <input
                type="text"
                placeholder="Enter Repository URL (e.g., owner/repo)"
                value={inputValue}
                onChange={(event) => setInputValue(event.target.value)}
            />
            <button type="submit">Load Repository</button>
        </form> 
    );
};

export default RepoInput;