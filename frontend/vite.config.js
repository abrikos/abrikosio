import {fileURLToPath, URL} from 'node:url'

import {defineConfig} from 'vite'
import vue from '@vitejs/plugin-vue'
import vueDevTools from 'vite-plugin-vue-devtools'
import path from 'path'
// https://vite.dev/config/
export default defineConfig({
    plugins: [
        vue(),
        vueDevTools(),
    ],
    build: {
        outDir: '../blog/templates',
        assetsDir: 'static/blog'
    },
    resolve: {
        alias: {
            '@': fileURLToPath(new URL('./src', import.meta.url))
        },
    },
    test: {
        environment: 'jsdom',
        // change the path below to to the location of your setup.ts file:
        setupFiles: path.resolve(__dirname, './setup.ts'),
    }
})
