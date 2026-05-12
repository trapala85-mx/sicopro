import type { MainProps } from "../../types/mainProps"
import styles from './Main.module.css';


const Main = ({ error, isLoading }: MainProps) => {

    const renderContext = () => {
        if (error) {
            return (<p className={styles.text_content}>Error: revise su conexión.</p>);
        } else if (isLoading) {
            return (<p className={styles.text_content}>Cargando ...</p>);
        } else {
            return (<p className={styles.text_content}>Main</p>);
        }
    }
    return (
        <main className={styles.main_container}>
            {renderContext()}
        </main >)
};

export { Main }