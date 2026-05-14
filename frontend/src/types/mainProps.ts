import type { Module } from "./module";

export interface MainProps {
    error: string | null;
    isLoading: boolean;
    selectedModule: Module | null
}