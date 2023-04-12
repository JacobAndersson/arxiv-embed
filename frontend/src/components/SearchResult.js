import Text from '@mui/material/Typography';

import styles from './SearchResult.module.css';

export default function Searchresult({ item }) {
  return (
    <div
      key={item.id}
      className={styles.container}
    >
      <div
        className={styles.titleRow}
      >
        <Text
          variant="h6"
        >{item.title}</Text>
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
