import ButtonGroup from '@/components/ui/ButtonGroup';
import styles from './AnalysisPanel.module.css';
import Button from '@/components/ui/Button';
import FileViewer from './FileViewer/FileViewer';

interface AnalysisPanelProps {
    fileContent: string | null;
}

export default function AnalysisPanel({ fileContent }: AnalysisPanelProps) {
    return (
        <div className={styles.analysisPanel}>
            <ButtonGroup>
                <Button text='Analyse Commits'/>
                <Button text='Analyse Issues'/>
                <Button text='Analyse File'/>
                <Button text='Analyse Code'/>
            </ButtonGroup>
            <FileViewer content={fileContent ?? "# select a file to view its contents"}/>
        </div>
    );
}
