/** @type {import('next').NextConfig} */
const nextConfig = {
    reactStrictMode: true,
    swcMinify: true,
    experimental: {
        appDir: true,
    },
    env: {
        CUSTOM_KEY: 'ULTRA_DOOK_PORTAL',
        BROSKI_MODE: 'LEGENDARY',
        HYPERFOCUS_ENABLED: 'true',
    },
    async rewrites() {
        return [
            {
                source: '/api/crystals/:path*',
                destination: '/api/memory-crystals/:path*',
            },
            {
                source: '/dook/:path*',
                destination: '/chapters/:path*',
            },
        ];
    },
}

module.exports = nextConfig
