import { useState, useEffect } from "react";

import type { Project } from "../types/project";

import { getProjects } from "../services/projectService";

// - - - - - 

export function useProjects() {

    const [projects, setProjects] = useState<Project[]>([]);
    const [error, setError] = useState<string | null>(null)
    const [isLoading, setIsLoading] = useState(false)

    useEffect(() => {
        const fetcData = async () => {
            try {
                setIsLoading(true)
                const response = await getProjects();
                setProjects(response.data)
            } catch (err) {
                const er = err as Error
                setError(er.message)
            } finally {
                setIsLoading(false)
            }
        };
        fetcData()
    }, [])

    return {
        projects,
        error,
        isLoading,
    }
}