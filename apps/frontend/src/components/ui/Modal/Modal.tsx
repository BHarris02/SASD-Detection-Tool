import styles from './Modal.module.css';

interface ModalProps {
    show: boolean;
    onClose: () => void;
    title: string;
    children: React.ReactNode;
}

export default function Modal({ show, onClose, title, children }: ModalProps) {
    if (!show)
        return null;

    return (
        <div className={styles["modal-overlay"]}>
            <div className={styles["modal-content"]}>
                <div className={styles["modal-header"]}>
                    <h3>{ title }</h3>
                    <button onClick={onClose}>Close</button>
                </div>
                <div className={styles["modal-body"]}>
                    { children }
                </div>
            </div>
        </div>
    );
}