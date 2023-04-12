import { useMemo } from "react";
import { useSearchParams } from "react-router-dom";

export function useQuery() {
  const [params] = useSearchParams()

  const data = useMemo(() => {
    const query = {};
    for (const [key, value] of params) {
      query[key] = value;
    }
    return query;
  }, [params]);

  return data;
}
