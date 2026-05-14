import type { AsideProps } from '../../types/asideProps';
import { ModuleItem } from './ModuleItem';
import styles from './Aside.module.css';
import { useState } from 'react';

const Aside = ({ modules, selectedModule, setSelectedModule }: AsideProps) => {

    const [expandedChild, setExpandedChild] = useState<string | null>(null);

    return (
        <aside className={styles.aside_container}>
            {modules.filter(m => m.parent === null).map(
                m => (
                    <ModuleItem
                        key={m.id}
                        module={m}
                        expandedId={expandedChild}
                        setExpandedId={setExpandedChild}
                        selectedModule={selectedModule}
                        setSelectedModule={setSelectedModule}
                    />
                )
            )

            }
        </aside>
    )
}
export { Aside }