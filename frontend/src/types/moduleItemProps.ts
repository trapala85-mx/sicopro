import type { Module } from './module';

export interface ModuleItemProps {
    module: Module;
    setSelectedModule: (module: Module) => void;
}