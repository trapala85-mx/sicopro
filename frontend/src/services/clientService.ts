import axios from 'axios';
import type { ApiResponse } from '../types/api';
import type { Client } from '../types/client';

export async function getAllClients() {
    const response = await axios.get<ApiResponse<Client[]>>('http://localhost:8000/api/v1/clients/')
    return response.data
}