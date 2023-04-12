import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import { QueryClient, QueryClientProvider } from 'react-query';

import Home from './views/Home';
import Search from './views/Search';

const queryClient = new QueryClient();

function App() {
  return (
    <QueryClientProvider client={queryClient}>
      <Router>
        <Routes>
          <Route
            path="/"
            element={<Home />}
          />
          <Route
            path="/search"
            element={<Search />}
          />
        </Routes>
      </Router>
    </QueryClientProvider>
  );
}

export default App;
