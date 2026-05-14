import type { ModuleItemProps } from "../../../types/moduleItemProps";

const ModuleItem = ({ module, setSelectedModule }: ModuleItemProps) => (
    <div
        onClick={() => setSelectedModule(module)}
    >
        {module.name}
    </div>
);

export { ModuleItem };