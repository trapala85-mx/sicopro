import { useState } from "react";
import type { ModuleItemProps } from "../../../types/moduleItemProps";
import styles from "./ModuleItem.module.css";

function ModuleItem({ module, expandedId, setExpandedId, selectedModule, setSelectedModule, depth = 0 }: ModuleItemProps) {
    const [expandedChild, setExpandedChild] = useState<string | null>(null);

    function hasChildren() {
        return (module.submodules.length > 0)
    }
    function isExpanded() {
        return (module.id === expandedId);
    }
    function isActive() {
        return selectedModule?.id === module.id;
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
        <div className={styles.item_container}>
            <div 
                className={`${styles.item} ${isActive() ? styles.item_active : ""} ${depth > 0 ? styles.item_child : ""}`} 
                onClick={toogleExpand}
            >
                <div className={styles.content}>
                    <span className={`${styles.text} ${depth > 0 ? styles.text_sm : ""}`}>{module.name}</span>
                </div>
                {hasChildren() && (
                    <span className={`${styles.chevron} ${isExpanded() ? styles.chevron_expanded : ""}`}>
                        <span className="material-symbols-outlined">expand_more</span>
                    </span>
                )}
            </div>

            {
                isExpanded() && hasChildren() && (
                    <div className={styles.children_container}>
                        {module.submodules.map(sub => (
                            <ModuleItem
                                key={sub.id}
                                module={sub}
                                expandedId={expandedChild}
                                setExpandedId={setExpandedChild}
                                selectedModule={selectedModule}
                                setSelectedModule={setSelectedModule}
                                depth={depth + 1}
                            />
                        ))}
                    </div>
                )
            }
        </div>
    )
}

export { ModuleItem };