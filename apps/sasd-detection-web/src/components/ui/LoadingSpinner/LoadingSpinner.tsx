import { FaSpinner } from "react-icons/fa";
import styles from "./LoadingSpinner.module.css";

interface LoadingSpinnerProps {
    loading: boolean
}

export default function LoadingSpinner({ loading }: LoadingSpinnerProps) {
    if (!loading) return null;

    return (
        <div className={styles["loading-overlay"]}>
            <div className={styles["spinner-container"]}>
                <FaSpinner className={styles["spinner-icon"]} />
                <p className={styles["loading-text"]}>Loading...</p>
            </div>
        </div>
    );
}