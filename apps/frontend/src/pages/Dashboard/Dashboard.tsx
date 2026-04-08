import FileBrowser from '@/components/sections/FileBrowser';
import styles from './Dashboard.module.css';
import Workspace from '@/components/sections/Workspace';

export default function Dashboard() {
    return (
        <main className={styles.dashboard}>
            <FileBrowser />
            <Workspace />
        </main>
    );
}
