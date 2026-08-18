import styles from './Navbar.module.css';

export default function Navbar() {
    return (
        <div className={styles.navbar}>
            <div className={styles.navLogo}>SASD Detection Tool: Web Client</div>
            <nav>
                <ul className={styles.navLinks}>
                    <li><a href="#">Usage</a></li>
                    <li><a href="#">API Docs</a></li>
                    <li><a href="#">Contact</a></li>
                </ul>
            </nav>
        </div>
    );
}
