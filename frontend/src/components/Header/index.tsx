import { Logo } from './Logo';
import { SystemName } from './SystemName';
import { ProjectDropdown } from './ProjectDropdown';

import styles from './Header.module.css'

const Header = () => (
    <header className={styles.header_container}>
        <Logo />

        <div className={styles.logo_dropdown_container}>
            <SystemName />
            <ProjectDropdown />
        </div>
    </header>
)

export { Header }