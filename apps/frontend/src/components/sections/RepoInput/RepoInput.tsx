import { useState } from 'react';
import styles from './RepoInput.module.css';

interface RepoInputProps {
    repoUrl: string;
    setRepoUrl: (url: string) => void;
    fetchRepoStructure: (repoUrl: string) => void;
}

export const RepoInput = ({ repoUrl, setRepoUrl, fetchRepoStructure}: RepoInputProps) => {
    // state
    const [inputValue, setInputValue] = useState<string>(repoUrl || "");

    // handlers
    const handleSubmit = (event) => {
        event.preventDefault();
        if (!inputValue.trim()) {
            alert("Please enter a valid repository URL (e.g. owner/repository-name).");
            return;
        }
        setRepoUrl(inputValue);
        fetchRepoStructure(inputValue);
    }

    return (
        <form onSubmit={handleSubmit} className={styles["repo-input-form"]}>
            <input 
                type="text"
                placeholder="Enter Repository URL (owner/repo-name)"
                value={inputValue}
                onChange={ (event) => setInputValue(event.target.value) }
            />
            <button type="submit">Fetch Repository</button>
        </form>
    );
}