import type { MainProps } from "../../types/main"



const Main = ({ error, isLoading }: MainProps) => {

    const renderContext = () => {
        if (error) {
            return (<p>Error: revise su conexión.</p>);
        } else if (isLoading) {
            return (<p>Cargando ...</p>);
        } else {
            return (<p>Main</p>);
        }
    }
    return (
        <main>
            {renderContext()}
        </main >)
};

export { Main }