import { Header } from '../../components/Header';
import { Aside } from '../../components/Aside';
import { Main } from '../../components/Main';
import { useProjectDropdown } from '../../hooks/useProjectDropdown';
import styles from './Dashboard.module.css';
import { useProjectModules } from '../../hooks/useProjectModules';
import { useEffect, useState } from 'react';
import type { Module } from '../../types/module';

const Dashboard = () => {

    const { isOpen, selected, projects, isLoading, error, toogleDropdown, selectProject } = useProjectDropdown();
    const { modules, isLoading: isModuleLoading, error: moduleError } = useProjectModules(selected)
    const [moduleSelected, setModuleSelected] = useState<Module | null>(null);

    useEffect(() => {

        const searched = modules.find(module => module.order === 0);
        setModuleSelected(searched ?? null);

    }, [modules]);


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
                <Aside
                    modules={modules}
                    selectedModule={moduleSelected}
                    setSelectedModule={setModuleSelected}
                />

                <Main
                    error={moduleError}
                    isLoading={isModuleLoading}
                    selectedModule={moduleSelected}
                />
            </div>

        </>)
}
export { Dashboard };