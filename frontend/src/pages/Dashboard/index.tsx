import { Header } from '../../components/Header';
import { Aside } from '../../components/Aside';
import { Main } from '../../components/Main';
import { useProjectDropdown } from '../../hooks/userProjectDropdown';

const Dashboard = () => {

    const { isOpen, selected, projects, isLoading, toogleDropdown, selectProject } = useProjectDropdown();
    return (
        <>
            <Header
                isOpen={isOpen}
                selected={selected}
                projects={projects}
                onClick={toogleDropdown}
                selectProject={selectProject}
            />
            <Aside />
            <Main
                isLoading={isLoading}
            />
        </>)
}
export { Dashboard };