import React, { useEffect, useState } from "react";

function App() {
  const [movies, setMovies] = useState([]);
  const [recs, setRecs] = useState([]);

  useEffect(() => {
    fetch("http://localhost:8000/movies/").then(r => r.json()).then(setMovies);
  }, []);

  const loadRecs = () => {
    fetch("http://localhost:8000/recommendations/user/1")
      .then(r => r.json())
      .then(d => setRecs(d.movie_ids));
  };

  return (
    <div>
      <h1>Movie Recommendations</h1>
      <button onClick={loadRecs}>Load Recommendations</button>
      <pre>{JSON.stringify({ movies, recs }, null, 2)}</pre>
    </div>
  );
}

export default App;