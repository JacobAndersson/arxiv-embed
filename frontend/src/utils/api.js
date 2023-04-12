import axios from 'axios';

function request(params, includeToken = true) {
  const url = `/api${params.url}`;

  return axios({
    ...params,
    headers: {
      ...(params.headers || {}),
    },
    url,
  }).catch((e) => {
    throw e;
  });
}

export function get(url, { signal, includeToken, ...params } = {}) {
  return request(
    {
      method: 'GET',
      url,
      signal,
      ...params,
    },
    includeToken
  );
}

export function del(url, data = null, { includeToken, ...params } = {}) {
  return request(
    {
      method: 'DELETE',
      url,
      data,
      ...params,
    },
    includeToken
  );
}

export function post(url, data = null, { includeToken, ...params } = {}) {
  return request(
    {
      method: 'POST',
      url,
      data,
      ...params,
    },
    includeToken
  );
}

export function put(url, data = null, { includeToken, ...params } = {}) {
  return request(
    {
      method: 'PUT',
      url,
      data,
      ...params,
    },
    includeToken
  );
}
