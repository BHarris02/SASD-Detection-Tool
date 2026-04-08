import AnalysisActions from './AnalysisActions';
import FileViewer from './FileViewer';
import styles from './Workspace.module.css';

export default function Workspace() {
    return (
        <section className={styles.workspace}>
            <div>
                <AnalysisActions />
            </div>
            <div>
                <FileViewer />
            </div>
        </section>
    );
}
