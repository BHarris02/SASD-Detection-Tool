import styles from './LoadingSpinner.module.css';
import { FaSpinner } from 'react-icons/fa';

export default function LoadingSpinner() {
    return (
        <div className={styles.spinner}>
            <FaSpinner className={styles.spinnerIcon}/>
        </div>
    );
}
