import styles from './Button.module.css';

interface ButtonProps {
    text: string;
    onClick?: () => void;
    disabled?: boolean;
}

export default function Button({ text, onClick, disabled }: ButtonProps) {
    return (
        <button
            className={styles.button}
            onClick={onClick}
            disabled={disabled}
        >
            { text }
        </button>
    );
}
