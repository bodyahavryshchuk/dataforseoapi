export interface Task {
  engine: string;
  location: string;
  keyword: string;
}

export interface TaskData {
  task: string;
  api: string;
  function: string;
  se: string;
  se_type: string;
  language_code: string;
  location_code: string;
  keyword: string;
  device: string;
  os: string;
}

export interface TaskResult {
  task: string;
  type: string;
  rank_group: string;
  rank_absolute: string;
  domain: string;
  title: string;
  description: string;
  url: string;
  breadcrumb: string;
}
