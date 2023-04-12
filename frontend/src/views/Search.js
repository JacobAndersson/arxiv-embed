import { useQuery } from "../utils/hooks";
import { get } from '../utils/api';
import { useQuery as useReactQuery } from 'react-query';

import styles from './Search.module.css';

import Text from '@mui/material/Typography';
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
  const { searchResults, isLoading, error } = useSearch(query);
  console.log(searchResults?.[0]);

  return (
    <div>
      <h1>Search</h1>
      {isLoading && <p>Loading...</p>}
      { searchResults && searchResults.map((result) => (
        <SearchResult
          item={result}
        />
      ))}
    </div>
  );
}
