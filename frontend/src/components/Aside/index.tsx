import type { AsideProps } from '../../types/asideProps';
import styles from './Aside.module.css';

const Aside = ({ modules, setSelectedModule }: AsideProps) => (
    <aside className={styles.aside_container}>
        {modules.map(
            module => (
                <div
                    key={module.id}
                    className={styles.module_item}
                    onClick={() => setSelectedModule(module)}
                >
                    {module.name}
                </div>
            )
        )

        }
    </aside>
)

export { Aside }