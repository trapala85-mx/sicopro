import type { Project } from "./project"

export interface HeaderProps {
    isOpen: boolean
    selected: string
    projects: Project[]
    onClick: () => void;
    selectProject: (project: Project) => void;
}