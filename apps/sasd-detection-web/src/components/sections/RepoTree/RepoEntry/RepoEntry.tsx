import Button from '@/components/ui/Button';
import styles from './RepoEntry.module.css';

export default function RepoEntry() {
    return (
        <div className={styles.repoEntry}>
            <input 
                type="text" 
                className={styles.repoInput} 
                placeholder="owner/repository" 
            />
            <Button text="Load Repository" />
        </div>
    );
}
