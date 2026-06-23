import { useState } from 'react';
import ProjectForm from './components/ProjectForm';
import Dashboard from './components/Dashboard';
import { GenerateRequest, GenerateResponse } from './types';

function App() {
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const [result, setResult] = useState<GenerateResponse | null>(null);

  const handleGenerate = async (data: GenerateRequest) => {
    setLoading(true);
    setError(null);
    setResult(null);

    try {
      const response = await fetch('http://127.0.0.1:8000/generate', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(data),
      });

      if (!response.ok) {
        throw new Error(`API error: ${response.status} ${response.statusText}`);
      }

      const json = await response.json();
      setResult(json);
    } catch (err: any) {
      setError(err.message || 'An unexpected error occurred while calling the API.');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <header className="header">
        <h1>DevPilot AI</h1>
        <p>Intelligent Auto-Scaffolding & Architecture Agent</p>
      </header>

      {error && (
        <div className="alert-error">
          <strong>Error:</strong> {error}
        </div>
      )}

      {!loading && !result && (
        <ProjectForm onSubmit={handleGenerate} loading={loading} />
      )}

      {loading && (
        <div className="glass-panel" style={{ textAlign: 'center', padding: '4rem 2rem' }}>
          <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', marginBottom: '1rem' }}>
            <div className="spinner"></div>
            <h2 style={{ margin: 0, color: 'var(--accent-primary)' }}>Architecting your project...</h2>
          </div>
          <p style={{ color: 'var(--text-secondary)' }}>
            DevPilot AI is analyzing requirements, generating tasks, scaffolding code, and writing documentation.
            This may take 15-30 seconds.
          </p>
        </div>
      )}

      {result && !loading && (
        <Dashboard result={result} onReset={() => setResult(null)} />
      )}
    </div>
  );
}

export default App;
