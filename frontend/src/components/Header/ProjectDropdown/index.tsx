import type { ProjectDropdownProps } from '../../../types/projectDropdownProps';
import styles from './ProjectDropdown.module.css';

const ProjectDropdown = ({ isOpen, selected, projects, onClick, selectProject }: ProjectDropdownProps) => {

    const renderProjectList = () => {
        if (!isOpen) return null;
        if (projects.length === 0) return null;

        return (
            <ul>
                {
                    projects.map(project => (
                        <li
                            key={project.id}
                            onClick={() => selectProject(project)}
                        >
                            {project.name}
                        </li>
                    ))
                }
            </ul >
        )
    }
    return (
        < div className={styles.dropdown_container} >
            <button onClick={onClick} className={styles.button}>
                {selected}
            </button>
            {renderProjectList()}
        </div >
    )
}

export { ProjectDropdown }