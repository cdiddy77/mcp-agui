const API_BASE_URL = process.env.NEXT_PUBLIC_API_URL || "";

export interface ApiResponse<T = any> {
  message: string;
  data?: T;
}

export async function fetchAPI<T = any>(
  endpoint: string,
  options?: RequestInit
): Promise<ApiResponse<T>> {
  const url = `${API_BASE_URL}/api/v1${endpoint}`;
  
  const response = await fetch(url, {
    headers: {
      "Content-Type": "application/json",
      ...options?.headers,
    },
    ...options,
  });

  if (!response.ok) {
    throw new Error(`API Error: ${response.status} ${response.statusText}`);
  }

  return response.json();
}

export const api = {
  example: {
    get: () => fetchAPI("/example/"),
    create: (data: { name: string; description?: string }) =>
      fetchAPI("/example/", {
        method: "POST",
        body: JSON.stringify(data),
      }),
  },
};