import { useState } from 'react';
import type { Project } from '../types/project';

const projects: Project[] = [
    {
        id: "9cc5a10b-0403-41be-a46e-27d8cbc6650d",
        can_show: true,
        name: "Tren Querétaro Irapuato T1 (Supervisión)",
        is_active: true,
        project_type: "3d6923aa-e635-41e1-b09b-5e606afe3464"
    },
    {
        id: "12390a9e-e180-4518-9736-7c79ad0ee4aa",
        can_show: true,
        name: "Tren Querétaro Irapuato T1 (Supervisión de Obra)",
        is_active: true,
        project_type: "824da2be-bbb9-4a0e-a978-9287824b1163"
    }
]

export function useProjectDropdown() {

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
        toogleDropdown,
        selectProject,
    };
}