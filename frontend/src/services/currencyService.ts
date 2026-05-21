import axios from 'axios';
import type { ApiResponse } from '../types/api';
import type { Currency } from '../types/currency';

export async function getAllCurrencies() {
    const response = await axios.get<ApiResponse<Currency[]>>('http://localhost:8000/api/v1/currencies/')
    return response.data
}