import type { Project } from './project';

export interface ProjectDropdownProps {
    isOpen: boolean;
    selected: string;
    projects: Project[];
    onClick: () => void;
    selectProject: (project: Project) => void;
}