import { useState, useEffect } from 'react';
import type { Project } from '../types/project';
import { getProjects } from '../services/projectService';


export function useProjectDropdown() {

    // valor inicial false
    // vamos a ver el estado abierto o cerrado del Dropdown
    const [isOpen, setIsOpen] = useState(false);

    // el valor seleccionado
    const [selected, setSelected] = useState("Selecciona un Proyecto");

    const [projects, setProjects] = useState<Project[]>([]);

    //const [error, setError] = useState<string | null>(null)

    // useEffect no acepta async functions por lo que se debe declarar una nueva función
    // y esta nueva función llama a la async function
    useEffect(() => {
        const fetchData = async () => {
            try {
                const response = await getProjects();
                setProjects(response.data);
            } catch (err) {
                console.error('Error fetching projects:', err);
            }
        };
        fetchData();
    },[])

    // logica para cambiar el estado
    const toogleDropdown = () => (
        setIsOpen(!isOpen)
    );

    const selectProject = (project: Project) => {
        setSelected(project.name);
        setIsOpen(false);
    };

    return {
        isOpen,
        selected,
        projects,
        toogleDropdown,
        selectProject,
    };
}