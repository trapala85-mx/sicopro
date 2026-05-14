import type { AsideProps } from '../../types/asideProps';
import { ModuleItem } from './ModuleItem';
import styles from './Aside.module.css';

const Aside = ({ modules, setSelectedModule }: AsideProps) => (
    <aside className={styles.aside_container}>
        {modules.filter(m => m.parent === null).map(
            m => (
                <ModuleItem
                    key={m.id}
                    module={m}
                    setSelectedModule={setSelectedModule}
                />
            )
        )

        }
    </aside>
)

export { Aside }