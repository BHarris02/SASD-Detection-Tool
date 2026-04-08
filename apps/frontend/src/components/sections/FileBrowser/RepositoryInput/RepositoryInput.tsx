import styles from './RepositoryInput.module.css';

interface RepositoryInputProps {
    repoUrl: string;
    setRepoUrl: (url: string) => void;
    onLoadRepoStructure: () => void;
}

export default function RepositoryInput({ repoUrl, setRepoUrl, onLoadRepoStructure }: RepositoryInputProps) {
    // handlers
    const handleSubmit = (event: React.SubmitEvent) => {
        event.preventDefault();
        onLoadRepoStructure();
    }

    return (
        <form onSubmit={handleSubmit} className={styles.repositoryInputForm}>
            <input
                type="text"
                placeholder="Enter Repository URL ('owner/repository-name')"
                value={repoUrl}
                onChange={ (event) => setRepoUrl(event.target.value) }
            />
            <button type="submit">Load Repository Tree</button>
        </form>
    );
}
