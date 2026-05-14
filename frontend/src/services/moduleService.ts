import axios from 'axios';
import type { ApiResponse } from '../types/api';
import type { Module } from '../types/module';

export async function getProjectModules(project_id: string) {
    const response = await axios.get<ApiResponse<Module[]>>(`http://localhost:8000/api/v1/projects/${project_id}/modules/?active=true`)
    return response.data
}

export async function getAllModules() {
    const response = await axios.get<ApiResponse<Module[]>>(`http://localhost:8000/api/v1/modules/?active=true`)
    return response.data
}