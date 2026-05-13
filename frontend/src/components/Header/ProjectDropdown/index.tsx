import type { ProjectDropdownProps } from '../../../types/projectDropdownProps';
import styles from './ProjectDropdown.module.css';

const ProjectDropdown = ({ isOpen, selected, projects, onClick, selectProject }: ProjectDropdownProps) => {

    const renderProjectList = () => {
        if (!isOpen) return null;
        if (projects.length === 0) return null;

        return (
            <div className={styles.dropdown_list}>
                <div className={styles.dropdown_header}>
                    <div className={styles.search_wrapper}>
                        <svg className={styles.search_icon} width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round">
                            <circle cx="11" cy="11" r="8"></circle>
                            <line x1="21" y1="21" x2="16.65" y2="16.65"></line>
                        </svg>
                        <input 
                            type="text" 
                            placeholder="Buscar proyecto..." 
                            className={styles.search_input}
                        />
                    </div>
                </div>
                
                <ul className={styles.projects_ul}>
                    {
                        projects.map(project => (
                            <li className={styles.dropdown_item}
                                key={project.id}
                                onClick={() => selectProject(project)}
                            >
                                {project.name}
                            </li>
                        ))
                    }
                </ul>
            </div>
        )
    }
    return (
        < div className={styles.dropdown_container} >
            <span className={styles.label}>PROYECTO ACTIVO</span>
            <button onClick={onClick} className={styles.button}>
                {selected}
                <svg className={styles.arrow} width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="3" strokeLinecap="round" strokeLinejoin="round">
                    <path d="m6 9 6 6 6-6"/>
                </svg>
            </button>
            {renderProjectList()}
        </div >
    )
}

export { ProjectDropdown }
