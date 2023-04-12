import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

import Home from './views/Home';
import Search from './views/Search';

function App() {
  return (
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
  );
}

export default App;
