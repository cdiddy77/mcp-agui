"use client";

import { useEffect, useState } from "react";

interface ApiResponse {
  message: string;
  data?: Record<string, unknown>;
}

export default function Home() {
  const [apiData, setApiData] = useState<ApiResponse | null>(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetch("/api/v1/example/")
      .then((res) => res.json())
      .then((data) => {
        setApiData(data);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching API:", error);
        setLoading(false);
      });
  }, []);

  return (
    <main className="flex min-h-screen flex-col items-center justify-center p-24">
      <div className="z-10 max-w-5xl w-full items-center justify-between font-mono text-sm">
        <h1 className="text-4xl font-bold mb-8 text-center">MCP AGUI</h1>
        
        <div className="mb-32 grid text-center lg:max-w-5xl lg:w-full lg:mb-0 lg:grid-cols-2 lg:text-left gap-4">
          <div className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30">
            <h2 className="mb-3 text-2xl font-semibold">
              Frontend{" "}
              <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
                →
              </span>
            </h2>
            <p className="m-0 max-w-[30ch] text-sm opacity-50">
              Next.js 15 with TypeScript and Tailwind CSS
            </p>
          </div>

          <div className="group rounded-lg border border-transparent px-5 py-4 transition-colors hover:border-gray-300 hover:bg-gray-100 hover:dark:border-neutral-700 hover:dark:bg-neutral-800/30">
            <h2 className="mb-3 text-2xl font-semibold">
              Backend{" "}
              <span className="inline-block transition-transform group-hover:translate-x-1 motion-reduce:transform-none">
                →
              </span>
            </h2>
            <p className="m-0 max-w-[30ch] text-sm opacity-50">
              FastAPI with Python 3.12 and Pydantic
            </p>
          </div>
        </div>

        <div className="mt-8 p-6 rounded-lg border border-gray-300 dark:border-neutral-700">
          <h3 className="text-xl font-semibold mb-4">API Status</h3>
          {loading ? (
            <p className="text-sm opacity-50">Connecting to backend...</p>
          ) : apiData ? (
            <div>
              <p className="text-sm mb-2">
                <span className="font-semibold">Message:</span> {apiData.message}
              </p>
              {apiData.data && (
                <p className="text-sm opacity-70">
                  <span className="font-semibold">Data:</span>{" "}
                  {JSON.stringify(apiData.data, null, 2)}
                </p>
              )}
            </div>
          ) : (
            <p className="text-sm text-red-500">Failed to connect to backend</p>
          )}
        </div>
      </div>
    </main>
  );
}