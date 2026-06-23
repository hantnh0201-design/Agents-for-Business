export interface GenerateRequest {
  project_name: string;
  description: string;
  tech_stack: string;
}

export interface Task {
  title: string;
  description: string;
  priority: string;
  status: string;
  estimated_hours: number;
  dependencies: string[];
}

export interface GenerateResponse {
  project_id: string;
  status: string;
  summary: string;
  modules: string[];
  complexity: string;
  roadmap: string[];
  tasks: Task[];
  tech_stack_recommendation: {
    frontend?: string[];
    backend?: string[];
    database?: string[];
    deployment?: string[];
    reason?: string;
  };
  generated_files: {
    path: string;
    purpose: string;
  }[];
  workspace_path?: string;
  export_zip_path?: string;
  review_result: {
    status?: string;
    strengths?: string[];
    risks?: string[];
    suggestions?: string[];
  };
  readme_content: string;
}
