import { useState } from "react";
import type { ModuleItemProps } from "../../../types/moduleItemProps";

function ModuleItem({ module, expandedId, setExpandedId, selectedModule, setSelectedModule }: ModuleItemProps) {

    const [expandedChild, setExpandedChild] = useState<string | null>(null);

    function hasChildren() {
        return (module.submodules.length > 0)
    }
    function isExpanded() {
        return (module.id === expandedId);
    }

    function toogleExpand() {
        if (hasChildren()) {
            isExpanded() ? setExpandedId(null) : setExpandedId(module.id);
        } else {
            setSelectedModule(module);
            setExpandedId(null);
        }
    }


    return (
        <div>
            <div onClick={toogleExpand}>{module.name}</div>

            {
                isExpanded() && hasChildren() && (
                    <div>
                        {module.submodules.map(sub => (
                            <ModuleItem
                                key={sub.id}
                                module={sub}
                                expandedId={expandedChild}
                                setExpandedId={setExpandedChild}
                                selectedModule={selectedModule}
                                setSelectedModule={setSelectedModule}
                            />
                        ))}
                    </div>
                )
            }
        </div>
    )
}

export { ModuleItem };