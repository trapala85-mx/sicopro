export interface Module {
    id: string;
    name: string;
    order: number;
    is_active: boolean;
    parent: string | null;
    submodules: Module[];
}