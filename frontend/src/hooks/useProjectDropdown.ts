import { useState } from 'react';
import type { Project } from '../types/project';
import { useProjects } from '../hooks/useProjects';

export function useProjectDropdown() {

    const { projects, error, isLoading } = useProjects();

    // valor inicial false
    // vamos a ver el estado abierto o cerrado del Dropdown
    const [isOpen, setIsOpen] = useState(false);

    // el valor seleccionado
    const [selected, setSelected] = useState("Selecciona un Proyecto");

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
        isLoading,
        error,
        toogleDropdown,
        selectProject,
    };
}