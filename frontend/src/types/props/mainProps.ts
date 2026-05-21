import type { Module } from "../module";
import type { Project } from "../project";

export interface MainProps {
    error: string | null;
    isLoading: boolean;
    selectedModule: Module | null
    projectSelected: Project | null
}