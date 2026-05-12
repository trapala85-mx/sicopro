import imgUrl from '../../../assets/logo_solo.png';

import styles from './Logo.module.css';

const Logo = () => (
    <div>
        <img src={imgUrl} alt="SICOPRO Logo" className={styles.logo_img} />
    </div>
)

export { Logo }