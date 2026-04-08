import styles from './FileBrowser.module.css';
import RepositoryInput from './RepositoryInput';

export default function FileBrowser() {
    return (
        <section className={styles.fileBrowser}>
            <div>
                <RepositoryInput />
            </div>
            <div>

            </div>
        </section>
    );
}
