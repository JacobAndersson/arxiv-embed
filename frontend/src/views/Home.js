import { useState, useCallback } from 'react';
import styles from './Home.module.css';

import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import SearchIcon from '@mui/icons-material/Search';

import { useNavigate } from 'react-router-dom';

export default function Home() {
  const [value, setValue] = useState('');
  const navigate = useNavigate();

  const handleSearch = useCallback((e) => {
    e.preventDefault();
    navigate(`/search?q=${value}`);
  }, [value, navigate]);

  return (
    <div
      className={styles.container}
    >
      <div
        className={styles.content}
      >
        <p>Semantic UI React</p>
        <form
          onSubmit={handleSearch}
        >
          <TextField
            value={value}
            onChange={(e) => setValue(e.target.value)}
            label="Search"
            variant="outlined"
            autoFocus
            InputProps={{
              startAdornment: (
                <SearchIcon />
              ),
            }}
            fullWidth
          />
          <Button
            type="submit"
            variant="contained"
          >
            Search
          </Button>
        </form>
      </div>
    </div>
  );
}
