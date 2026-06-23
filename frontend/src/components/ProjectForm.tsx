import { useState, FormEvent } from 'react';
import { GenerateRequest } from '../types';

interface ProjectFormProps {
  onSubmit: (data: GenerateRequest) => void;
  loading: boolean;
}

export default function ProjectForm({ onSubmit, loading }: ProjectFormProps) {
  const [projectName, setProjectName] = useState('');
  const [description, setDescription] = useState('');
  const [techStack, setTechStack] = useState('');

  const handleSubmit = (e: FormEvent) => {
    e.preventDefault();
    if (!projectName || !description) return;

    onSubmit({
      project_name: projectName,
      description: description,
      tech_stack: techStack || 'Any modern stack',
    });
  };

  return (
    <div className="glass-panel" style={{ maxWidth: '700px', margin: '0 auto' }}>
      <h2 className="section-title">Describe Your Project</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label htmlFor="projectName">Project Name <span style={{color: 'var(--danger)'}}>*</span></label>
          <input
            id="projectName"
            type="text"
            className="form-input"
            value={projectName}
            onChange={(e) => setProjectName(e.target.value)}
            placeholder="e.g. Hospital Management System"
            required
            disabled={loading}
          />
        </div>

        <div className="form-group">
          <label htmlFor="description">Detailed Description <span style={{color: 'var(--danger)'}}>*</span></label>
          <textarea
            id="description"
            className="form-textarea"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            placeholder="Describe the core features, target audience, and main goals..."
            required
            disabled={loading}
          />
        </div>

        <div className="form-group">
          <label htmlFor="techStack">Preferred Tech Stack (Optional)</label>
          <input
            id="techStack"
            type="text"
            className="form-input"
            value={techStack}
            onChange={(e) => setTechStack(e.target.value)}
            placeholder="e.g. React, Node.js, PostgreSQL"
            disabled={loading}
          />
        </div>

        <button type="submit" className="btn-primary" disabled={loading || !projectName || !description}>
          {loading ? (
            <>
              <div className="spinner"></div>
              Generating...
            </>
          ) : (
            'Generate Project'
          )}
        </button>
      </form>
    </div>
  );
}
