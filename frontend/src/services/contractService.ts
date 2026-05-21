import axios from 'axios';
import type { ApiResponse } from '../types/api';
import type { Contract } from '../types/contract';
import type { ContractPayload } from '../types/contract';

export async function getContractForProject(project_id: string) {
    const response = await axios.get<ApiResponse<Contract | null>>(`http://localhost:8000/api/v1/contracts/?project=${project_id}`);
    return response.data;
}

export async function createContract(payload: ContractPayload) {
    const response = await axios.post<ApiResponse<Contract>>("http://localhost:8000/api/v1/contracts/", payload);
    return response.data;
}

export async function updateContract(contract_id: string, payload: ContractPayload) {
    const response = await axios.put<ApiResponse<Contract>>(`http://localhost:8000/api/v1/contracts/${contract_id}`, payload);
    return response.data;
}