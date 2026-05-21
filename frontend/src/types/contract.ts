import type { Currency } from "./currency";
import type { Client } from "./client";

export interface Contract {
    id: string;
    contract_number: string,
    description: string;
    sign_date: string;
    expiration_date: string;
    duration_days: number;
    amount_before_tax: string;
    amount_after_tax: string;
    status: "active" | "cancelled" | "completed";
    project: string;
    clients: Client[];
    currency: Currency;
}

export interface ContractPayload {
    id: string;
    contract_number: string,
    description: string;
    sign_date: string;
    expiration_date: string;
    duration_days: number;
    amount_before_tax: string;
    amount_after_tax: string;
    status: "active" | "cancelled" | "completed";
    project: string;
    clients: String[];
    currency: Currency;
}