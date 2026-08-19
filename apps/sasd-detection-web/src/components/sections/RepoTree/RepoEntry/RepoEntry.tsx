import Button from '@/components/ui/Button';
import styles from './RepoEntry.module.css';

interface RepoEntryProps {
    value: string;
    onValueChange: (value: string) => void;
    onSubmit: () => void;
    isLoading?: boolean;
}

export default function RepoEntry({ value, onValueChange, onSubmit, isLoading }: RepoEntryProps) {
    return (
        <div className={styles.repoEntry}>
            <input 
                type="text"
                className={styles.repoInput} 
                placeholder="owner/repository"
                value={value}
                onChange={(e) => onValueChange(e.target.value)}
            />
            <Button
                text={isLoading ? "Loading..." : "Load Repository"}
                onClick={onSubmit}
                disabled={isLoading}
            />
        </div>
    );
}
