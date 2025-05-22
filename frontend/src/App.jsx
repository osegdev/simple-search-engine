import { useState } from 'react';
import styles from './App.module.css';

function App() {
  const [query, setQuery] = useState('');
  const [results, setResults] = useState([]);

    const search = async () => {
      const cleaned = query.trim().toLowerCase();

      if (!cleaned || cleaned.length < 2) {
        alert("Por favor ingresa al menos 2 caracteres válidos.");
        return;
      }

      try {
        const response = await fetch(`http://localhost:8001/search?q=${encodeURIComponent(cleaned)}`);
        
        if (!response.ok) {
          const error = await response.json();
          alert(`Error ${response.status}: ${error.detail || "Error desconocido"}`);
          return;
        }

        const data = await response.json();
        console.log("Resultados:", data);
        setResults(data);
      } catch (error) {
        console.error("Error al hacer fetch:", error);
        alert("No se pudo conectar al servidor");
      }
    };

  return (
    <div className={styles.container}>
      <h1 className={styles.title}>Search Engine</h1>

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

      <ul className={styles.results}>
        {results.map((r, idx) => (
          <li key={idx} className={styles.result}>
            {r}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;

