import styles from './FileBrowser.module.css';
import FileTree from './FileTree';
import RepositoryInput from './RepositoryInput';

export default function FileBrowser() {
    return (
        <section className={styles.fileBrowser}>
            <div>
                <RepositoryInput />
            </div>
            <div>
                <FileTree />
            </div>
        </section>
    );
}
