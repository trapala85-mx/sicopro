import { Logo } from './Logo';
import { SystemName } from './SystemName';
import { ProjectDropdown } from './ProjectDropdown';
import type { ProjectDropdownProps } from '../../types/projectDropdown';
import styles from './Header.module.css'

const Header = ({ isOpen, selected, projects, onClick, selectProject }: ProjectDropdownProps) => (
    <header className={styles.header_container}>
        <Logo />

        <div className={styles.logo_dropdown_container}>
            <SystemName />
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