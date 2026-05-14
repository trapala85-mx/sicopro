import type { Project } from './project';
import type { Module } from './module';

export interface ProjectModule {
    project: Project;
    module: Module;
    is_active: boolean;
}