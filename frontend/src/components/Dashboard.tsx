import ReactMarkdown from 'react-markdown';
import { GenerateResponse } from '../types';

interface DashboardProps {
  result: GenerateResponse;
  onReset: () => void;
}

export default function Dashboard({ result, onReset }: DashboardProps) {
  return (
    <div style={{ animation: 'fadeIn 0.5s ease' }}>
      <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '2rem' }}>
        <h2 style={{ fontSize: '2rem', margin: 0, color: 'var(--accent-primary)' }}>Architecture Ready</h2>
        <button onClick={onReset} className="btn-primary" style={{ width: 'auto', padding: '0.75rem 1.5rem' }}>
          Start New
        </button>
      </div>

      {(result.workspace_path || result.export_zip_path) && (
        <div className="glass-panel" style={{ marginBottom: '2rem', background: 'rgba(16, 185, 129, 0.1)', borderColor: 'rgba(16, 185, 129, 0.3)' }}>
          <h3 style={{ marginTop: 0, color: 'var(--success)' }}>Project Exported!</h3>
          {result.workspace_path && <p><strong>Workspace:</strong> {result.workspace_path}</p>}
          {result.export_zip_path && (
            <p><strong>Download Ready:</strong> <a href={result.export_zip_path} style={{color: 'var(--accent-primary)'}}>{result.export_zip_path}</a></p>
          )}
        </div>
      )}

      <div className="dashboard-grid">
        {/* Overview Section */}
        <div className="glass-panel full-width">
          <h3 className="section-title">Overview</h3>
          <p style={{ fontSize: '1.1rem', lineHeight: '1.6' }}>{result.summary}</p>
          <div style={{ marginTop: '1.5rem' }}>
            <span className="badge badge-blue">Complexity: {result.complexity}</span>
            <span className="badge badge-green">Project ID: {result.project_id}</span>
            <span className="badge badge-yellow">Status: {result.status}</span>
          </div>
        </div>

        {/* Modules Section */}
        <div className="glass-panel">
          <h3 className="section-title">Core Modules</h3>
          <ul className="item-list">
            {result.modules?.map((mod, i) => (
              <li key={i}>{mod}</li>
            ))}
          </ul>
        </div>

        {/* Roadmap Section */}
        <div className="glass-panel">
          <h3 className="section-title">Project Roadmap</h3>
          <ul className="item-list">
            {result.roadmap?.map((phase, i) => (
              <li key={i} style={{ fontWeight: '500' }}>{phase}</li>
            ))}
          </ul>
        </div>

        {/* Tech Stack Section */}
        <div className="glass-panel full-width">
          <h3 className="section-title">Recommended Tech Stack</h3>
          <p style={{ marginBottom: '1.5rem', fontStyle: 'italic', color: 'var(--text-secondary)' }}>
            {result.tech_stack_recommendation?.reason || "Based on the requirements, this is the optimal architecture."}
          </p>
          
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(200px, 1fr))', gap: '1.5rem' }}>
            <div>
              <h4 style={{ color: 'var(--accent-primary)', marginBottom: '0.5rem' }}>Frontend</h4>
              <div>{result.tech_stack_recommendation?.frontend?.map(t => <span key={t} className="badge">{t}</span>)}</div>
            </div>
            <div>
              <h4 style={{ color: 'var(--accent-secondary)', marginBottom: '0.5rem' }}>Backend</h4>
              <div>{result.tech_stack_recommendation?.backend?.map(t => <span key={t} className="badge">{t}</span>)}</div>
            </div>
            <div>
              <h4 style={{ color: 'var(--success)', marginBottom: '0.5rem' }}>Database</h4>
              <div>{result.tech_stack_recommendation?.database?.map(t => <span key={t} className="badge">{t}</span>)}</div>
            </div>
            <div>
              <h4 style={{ color: 'var(--warning)', marginBottom: '0.5rem' }}>Deployment</h4>
              <div>{result.tech_stack_recommendation?.deployment?.map(t => <span key={t} className="badge">{t}</span>)}</div>
            </div>
          </div>
        </div>

        {/* Tasks Section */}
        <div className="glass-panel full-width">
          <h3 className="section-title">Actionable Tasks ({result.tasks?.length || 0})</h3>
          <div className="task-grid">
            {result.tasks?.map((task, i) => (
              <div key={i} className="task-card">
                <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'flex-start', marginBottom: '0.5rem' }}>
                  <h4 className="task-title">{task.title}</h4>
                  <span className={`badge ${task.priority.toLowerCase() === 'high' ? 'badge-red' : task.priority.toLowerCase() === 'medium' ? 'badge-yellow' : 'badge-blue'}`} style={{ margin: 0 }}>
                    {task.priority}
                  </span>
                </div>
                <p className="task-desc">{task.description}</p>
                <div className="task-meta">
                  <span>⏱ {task.estimated_hours} hrs</span>
                  <span style={{ color: 'var(--accent-secondary)' }}>{task.status}</span>
                </div>
                {task.dependencies && task.dependencies.length > 0 && (
                  <div style={{ marginTop: '0.75rem', fontSize: '0.8rem', color: 'var(--text-secondary)' }}>
                    <strong>Deps:</strong> {task.dependencies.join(', ')}
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>

        {/* Generated Files & Review */}
        <div className="glass-panel">
          <h3 className="section-title">Scaffolded Files</h3>
          <ul className="item-list" style={{ fontSize: '0.9rem' }}>
            {result.generated_files?.map((file, i) => (
              <li key={i}>
                <strong style={{ color: 'var(--accent-primary)' }}>{file.path}</strong>
                <br/>
                <span style={{ color: 'var(--text-secondary)' }}>{file.purpose}</span>
              </li>
            ))}
          </ul>
        </div>

        <div className="glass-panel">
          <h3 className="section-title">Architectural Review</h3>
          <div style={{ marginBottom: '1rem' }}>
            <h4 style={{ color: 'var(--success)', margin: '0 0 0.5rem 0' }}>Strengths</h4>
            <ul style={{ margin: 0, paddingLeft: '1.25rem', fontSize: '0.9rem' }}>
              {result.review_result?.strengths?.map((s, i) => <li key={i}>{s}</li>)}
            </ul>
          </div>
          <div style={{ marginBottom: '1rem' }}>
            <h4 style={{ color: 'var(--danger)', margin: '0 0 0.5rem 0' }}>Risks</h4>
            <ul style={{ margin: 0, paddingLeft: '1.25rem', fontSize: '0.9rem' }}>
              {result.review_result?.risks?.map((r, i) => <li key={i}>{r}</li>)}
            </ul>
          </div>
          <div>
            <h4 style={{ color: 'var(--warning)', margin: '0 0 0.5rem 0' }}>Suggestions</h4>
            <ul style={{ margin: 0, paddingLeft: '1.25rem', fontSize: '0.9rem' }}>
              {result.review_result?.suggestions?.map((s, i) => <li key={i}>{s}</li>)}
            </ul>
          </div>
        </div>

        {/* Readme Section */}
        <div className="glass-panel full-width">
          <h3 className="section-title">Generated README.md</h3>
          <div className="markdown-body">
            <ReactMarkdown>{result.readme_content}</ReactMarkdown>
          </div>
        </div>

      </div>
    </div>
  );
}
