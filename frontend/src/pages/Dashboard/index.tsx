import { Header } from '../../components/Header';
import { Aside } from '../../components/Aside';
import { Main } from '../../components/Main';
import { useProjectDropdown } from '../../hooks/useProjectDropdown';
import styles from './Dashboard.module.css';

const Dashboard = () => {

    const { isOpen, selected, projects, isLoading, error, toogleDropdown, selectProject } = useProjectDropdown();
    return (
        <>
            <Header
                isOpen={isOpen}
                selected={selected?.name || "Selecciona un Proyecto"}
                projects={projects}
                onClick={toogleDropdown}
                selectProject={selectProject}
            />

            <div className={styles.body_container}>
                <Aside />
                <Main
                    error={error}
                    isLoading={isLoading}
                />
            </div>

        </>)
}
export { Dashboard };