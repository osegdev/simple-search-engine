import { useState } from 'react';
import styles from './App.module.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

  const search = async () => {
    const cleaned = query.trim().toLowerCase().replace(/[^a-z0-9áéíóúüñ\s]/gi, "");
    if (!cleaned || cleaned.length < 2) {
      setResults([])
      return alert("Por favor ingresa al menos 2 caracteres válidos.");
    }

    try {
      const response = await fetch(`/search?q=${encodeURIComponent(cleaned)}`);
      const data = await response.json();
      setResults(data);
    } catch (error) {
      console.error("Error al buscar", error);
      alert("Hubo un error al hacer la busqueda.");
    }
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>🔍 Search Engine</h1>

      <input
        className={styles.input}
        placeholder="Write your query..."
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

