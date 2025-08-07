import { FlatCompat } from "@eslint/eslintrc";
import path from "path";
import { fileURLToPath } from "url";
import tsPlugin from "@typescript-eslint/eslint-plugin";

// Mimic __dirname for ESM
const __filename = fileURLToPath(import.meta.url);
const __dirname = path.dirname(__filename);

const compat = new FlatCompat({
  baseDirectory: path.resolve(__dirname, "frontend"),
});

export default [
  // 1. Load the recommended Next.js config as the base
  ...compat.extends("next/core-web-vitals"),

  // 2. Add our own configuration for TypeScript files
  {
    files: ["**/*.ts", "**/*.tsx"],
    plugins: {
      "@typescript-eslint": tsPlugin,
    },
    rules: {
      // Now ESLint knows what "@typescript-eslint" refers to.
      "@typescript-eslint/no-explicit-any": "warn",

      // This rule will catch the `var` in `global.d.ts`
      "no-var": "error",
    },
  },
];
