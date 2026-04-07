import styles from './Modal.module.css';

export default function Modal() {
    return (
        <div className={styles["modal-overlay"]}>
            <div className={styles["modal-content"]}>
                <div className={styles["modal-header"]}>
                    <h3>Title</h3>
                    <button>Close</button>
                </div>
                <div className={styles["modal-body"]}>

                </div>
            </div>
        </div>
    );
}