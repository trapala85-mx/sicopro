import type { Module } from './module';

export interface ModuleItemProps {
    module: Module;
    expandedId: string | null;
    setExpandedId: (id: string | null) => void;
    selectedModule: Module | null;
    setSelectedModule: (module: Module) => void;
    depth?: number;
}