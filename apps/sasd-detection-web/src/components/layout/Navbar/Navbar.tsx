import styles from './Navbar.module.css';

export default function Navbar() {
    return (
        <header>
            <div className={styles.navbarContainer}>
                <div className={styles.navbarLogo}>SASD Detection Tool: Web</div>
                <nav>
                    <ul className={styles.navLinks}>
                        <li><a href="#">Docs</a></li>
                        <li><a href="#">Contribute</a></li>
                    </ul>
                </nav>
            </div>
        </header>
    );
}
