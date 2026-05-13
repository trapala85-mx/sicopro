import { Logo } from './Logo';
import { SystemName } from './SystemName';
import { ProjectDropdown } from './ProjectDropdown';
import styles from './Header.module.css'
import type { HeaderProps } from '../../types/headerProps';

const Header = ({ isOpen, selected, projects, onClick, selectProject }: HeaderProps) => (
    <header className={styles.header_container}>
        <div className={styles.left_group}>
            <Logo />
            <SystemName />
        </div>

        <div className={styles.right_group}>
            <ProjectDropdown
                isOpen={isOpen}
                selected={selected}
                projects={projects}
                onClick={onClick}
                selectProject={selectProject} />
        </div>
    </header>
)

export { Header }
