import Text from '@mui/material/Typography';

import styles from './SearchResult.module.css';
import Link from '@mui/material/Link';

export default function Searchresult({ item }) {
  return (
    <div
      key={item.id}
      className={styles.container}
    >
      <div
        className={styles.titleRow}
      >
        <Link
          href={`https://arxiv.org/abs/${item.id}`}
        >
          <Text
            variant="h6"
          >{item.title}</Text>
          </Link>
        <Text
          className={styles.score}
        >{item.score}</Text>
      </div>
      <Text
        variant="subtitle1"
      >{item.authors}</Text>
    </div>
  );
}
