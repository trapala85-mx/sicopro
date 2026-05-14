import { useState, useEffect } from 'react';
import { getAllModules, getProjectModules } from '../services/moduleService';
import type { Project } from '../types/project';
import type { Module } from '../types/module';

export function useProjectModules(selected: Project | null) {

    const [modules, setModules] = useState<Module[]>([])
    const [error, setError] = useState<string | null>(null)
    const [isLoading, setIsLoading] = useState(false)

    useEffect(() => {

        const fetchProjectModules = async () => {
            try {
                setIsLoading(true)
                const response = !selected ? await getAllModules() : await getProjectModules(selected.id);
                setModules(response.data)
            } catch (err) {
                const e = err as Error
                setError(e.message)
            } finally {
                setIsLoading(false)
            }
        }
        fetchProjectModules()

    }, [selected]);

    return {
        modules,
        isLoading,
        error,
    }
}
