import styles from './RepositoryInput.module.css';

export default function RepositoryInput() {
    return (
        <form className={styles.repositoryInputForm}>
            <input
                type="text"
                placeholder="Enter Repository URL ('owner/repository-name')"
            />
            <button type="submit">Load Repository Tree</button>
        </form>
    );
}
