import type { MainProps } from "../../types/mainProps"
import styles from './Main.module.css';


const Main = ({ error, isLoading, selectedModule }: MainProps) => {

    const renderContext = () => {
        if (error) {
            return (<p className={styles.text_content}>Error de conexión con el servidor.</p>);
        } else if (isLoading) {
            return (<p className={styles.text_content}>Cargando ...</p>);
        } else {
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