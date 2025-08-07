export interface User {
  id: string;
  name: string;
  email: string;
}

export interface ApiError {
  message: string;
  details?: Record<string, unknown>;
}