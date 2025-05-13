import { useState } from 'react';
import styles from './App.module.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const search = async () => {
    if (!query.trim()) return;

    const response = await fetch(`/search?q=${query}`);
    const data = await response.json();
    setResults(data);
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>🔍 Motor de Búsqueda</h1>

      <input
        className={styles.input}
        placeholder="Escribe tu búsqueda..."
        value={query}
        onChange={(e) => setQuery(e.target.value)}
        onKeyDown={(e) => e.key === 'Enter' && search()}
      />

      <button className={styles.button} onClick={search}>
        Buscar
      </button>

      <ul>
        {results.map((r, idx) => (
          <li key={idx} className={styles.result}>
            📄 {r}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

