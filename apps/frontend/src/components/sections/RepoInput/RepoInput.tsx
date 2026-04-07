import styles from './RepoInput.module.css';

export default function RepoInput() {
    return (
        <form className={styles["repo-input-form"]}>
            <input 
                type="text"
                placeholder="Enter Repository URL (owner/repo-name)"
            />
            <button type="submit">Fetch Repository</button>
        </form>
    );
}