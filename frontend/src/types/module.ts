export interface Module {
    id: string;
    name: string;
    order: number;
    is_active: boolean;
    submodules: Module[];
}