import type { Module } from "./module";

export interface AsideProps {
    modules: Module[];
    setSelectedModule: (module: Module) => void;
}