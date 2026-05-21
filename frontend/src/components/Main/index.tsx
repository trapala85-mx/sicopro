import type { MainProps } from "../../types/props/mainProps"
import type { Project } from "../../types/project";
import styles from './Main.module.css';
import type { ComponentType } from "react";

type ModuleDict = { [key: string]: ComponentType<{ projectSelected: Project | null }> }



const Main = ({ error, isLoading, selectedModule, projectSelected }: MainProps) => {
    /* const MODULE_MAP: ModuleDict = {
        "Contrato": Contract,
        "Convenio": Convenio,
    } */

    const renderContext = () => {
        if (error) {
            return (<p className={styles.text_content}>Error de conexión con el servidor.</p>); // TODO: <ServerError/>
        } else if (isLoading) {
            return (<p className={styles.text_content}>Cargando ...</p>); //TODO: <Loading />
        } else {
            // const Component = MODULE_MAP[selectedModule?.name ?? ""];
            // return Component ? <Component projectSelected={projectSelected} /> : null;
            return (<p className={styles.text_content}>Main</p>);
        }
    }

    return (
        <main className={styles.main_container}>
            {renderContext()}
            {selectedModule && <p className={styles.text_content}>{selectedModule.name}</p>}
        </main >)
};

export { Main }