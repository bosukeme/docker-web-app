import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react-swc';
import dns from 'dns';

dns.setDefaultResultOrder('verbatim');

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  server: {
    proxy: {
      '/api/flask': {
        target: 'http://api-flask:5000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/flask/, ''),
        secure: false,
      },
      '/api/node': {
        target: 'http://api-node:3000',
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api\/node/, ''),
        secure: false,
      },
    },
  },
});
