import { useState } from 'react';
import { useQuery } from "../utils/hooks";
import { get } from '../utils/api';
import { useQuery as useReactQuery } from 'react-query';

import styles from './Search.module.css';

import Text from '@mui/material/Typography';
import TextField from '@mui/material/TextField';
import IconButton from '@mui/material/IconButton';
import SearchIcon from '@mui/icons-material/Search';

import SearchResult from '../components/SearchResult';


async function getSearchResults(query) {
  const res = await get(`/search?q=${query}`);
  return res?.data?.hits;
}

function useSearch(query) {
  const { data, isLoading, error } = useReactQuery(
    ['search', query],
    () => getSearchResults(query),
    {
      enabled: !!query,
    }
  );

  return {
    searchResults: data,
    isLoading,
    error,
  };
}

export default function Search() {
  const { q: query } = useQuery();
  const [search, setSearch] = useState(query);

  const { searchResults, isLoading, error } = useSearch(query);
  
  return (
    <div>
      <h1>Search</h1>
      <form>
        <TextField
          label="Search"
          variant="outlined"
          value={search}
          onChange={(e) => {
            setSearch(e.target.value);
          }}
        />
        <IconButton
          type="submit"
          onClick={(e) => {
            e.preventDefault();
            window.location.href = `/search?q=${search}`;
          }}
        >
          <SearchIcon />
        </IconButton>
      </form>
      {isLoading && <p>Loading...</p>}
      { searchResults && searchResults.map((result) => (
        <SearchResult
          item={result}
        />
      ))}
    </div>
  );
}
