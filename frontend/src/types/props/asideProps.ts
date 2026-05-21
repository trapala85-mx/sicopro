import type { Module } from "../module";

export interface AsideProps {
    modules: Module[];
    selectedModule: Module | null;
    setSelectedModule: (module: Module) => void;
}