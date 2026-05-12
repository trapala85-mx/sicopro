import styles from './ProjectDropdown.module.css';
import { useProjectDropdown } from '../../../hooks/userProjectDropdown';


const ProjectDropdown = () => {
    // desestructurar
    const { isOpen, selected, projects, toogleDropdown, selectProject } = useProjectDropdown();

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
            <button onClick={toogleDropdown} className={styles.button}>
                {selected}
            </button>
            {renderProjectList()}
        </div >
    )
}

export { ProjectDropdown }