import Text from '@mui/material/Typography';

import styles from './SearchResult.module.css';
import Link from '@mui/material/Link';
import Chip from '@mui/material/Chip';
import { Link as RouterLink } from 'react-router-dom';

export default function Searchresult({ item }) {
  return (
    <div
      key={item.id}
      className={styles.container}
    >
      <div
        className={styles.titleRow}
      >
        <RouterLink
          to={`/paper/${item.id}`}
        >
          <Text
            variant="h6"
          >{item.title}</Text>
        </RouterLink>
        <Text
          className={styles.score}
        >{item.score}</Text>
        <Chip
          label="arxiv"
          color="primary"
          component={Link}
          href={`https://arxiv.org/abs/${item.id}`}
        />
      </div>
      <Text
        variant="subtitle1"
      >{item.authors}</Text>
    </div>
  );
}
