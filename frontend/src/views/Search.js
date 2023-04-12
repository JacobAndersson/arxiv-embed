import { useEffect, useState } from "react";

import { useQuery } from "../utils/hooks";
import { get } from '../utils/api';

async function getSearchResults(query) {
  const res = await get(`/search?q=${query}`);
  return res.data;
}

export default function Search() {
  const { q: query } = useQuery();
  const [searchResults, setSearchResults] = useState([]);
  console.log(query);

  useEffect(() => {
    if (query) {
      getSearchResults(query).then((res) => {
        setSearchResults(res);
      });
    }
  }, [query]);

  return (
    <div>
      <h1>Search</h1>
    </div>
  );
}
