import axios from 'axios';
import type { ApiResponse } from '../types/api';
import type { Project } from '../types/project';

export async function getProjects() {
    const response = await axios.get<ApiResponse<Project[]>>('http://localhost:8000/api/v1/projects/?active=true')
    return response.data
}