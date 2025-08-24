/** @type {import('next').NextConfig} */
const nextConfig = {
    // 🧠 ADHD Performance Optimizations
    experimental: {
        // Enable modern bundling for faster load times
        turbo: {
            loaders: {
                '.svg': ['@svgr/webpack'],
            },
        },
        // Optimize for ADHD attention spans
        optimizeCss: true,
        optimizePackageImports: ['react-icons', 'lucide-react'],
    },

    // 🚀 Performance optimizations for neurodivergent users
    compiler: {
        // Remove console logs in production for cleaner experience
        removeConsole: process.env.NODE_ENV === 'production',
    },

    // 🎯 ADHD-friendly bundle optimization
    webpack: (config, { dev, isServer }) => {
        // Optimize bundle splitting for faster perceived load times
        if (!dev && !isServer) {
            config.optimization.splitChunks = {
                chunks: 'all',
                cacheGroups: {
                    // Critical components loaded first
                    critical: {
                        name: 'critical',
                        chunks: 'all',
                        test: /[\\/]src[\\/]components[\\/](AccessibilityProvider|NeurodivergentButton)/,
                        priority: 30,
                    },
                    // Neurodivergent optimizations
                    neurodivergent: {
                        name: 'neurodivergent',
                        chunks: 'all',
                        test: /[\\/]src[\\/]components[\\/]NeurodivergentOptimization/,
                        priority: 25,
                    },
                    // Vendor libraries
                    vendor: {
                        name: 'vendor',
                        chunks: 'all',
                        test: /[\\/]node_modules[\\/]/,
                        priority: 20,
                    },
                },
            };
        }

        // Add SVG support for icons
        config.module.rules.push({
            test: /\.svg$/,
            use: ['@svgr/webpack'],
        });

        return config;
    },

    // 🌈 Autism-friendly predictable routing
    trailingSlash: true,

    // 📱 PWA support for consistent experience
    pwa: {
        dest: 'public',
        register: true,
        skipWaiting: true,
        runtimeCaching: [
            {
                urlPattern: /^https?.*/,
                handler: 'NetworkFirst',
                options: {
                    cacheName: 'hyperfocus-zone-cache',
                    expiration: {
                        maxEntries: 100,
                        maxAgeSeconds: 30 * 24 * 60 * 60, // 30 days
                    },
                },
            },
        ],
    },

    // 🔧 Headers for performance and accessibility
    async headers() {
        return [
            {
                source: '/(.*)',
                headers: [
                    // Performance headers
                    {
                        key: 'X-DNS-Prefetch-Control',
                        value: 'on'
                    },
                    {
                        key: 'X-XSS-Protection',
                        value: '1; mode=block'
                    },
                    {
                        key: 'X-Frame-Options',
                        value: 'SAMEORIGIN'
                    },
                    {
                        key: 'X-Content-Type-Options',
                        value: 'nosniff'
                    },
                    // Accessibility headers
                    {
                        key: 'Cross-Origin-Embedder-Policy',
                        value: 'unsafe-none'
                    },
                    // ADHD performance optimization
                    {
                        key: 'Cache-Control',
                        value: 'public, max-age=31536000, immutable'
                    }
                ],
            },
        ];
    },

    // 🎯 Image optimization for faster loading
    images: {
        domains: ['hyperfocuszone.com', 'images.unsplash.com'],
        formats: ['image/webp', 'image/avif'],
        deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
        imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
        minimumCacheTTL: 60 * 60 * 24 * 30, // 30 days
    },

    // 🌐 Internationalization for global neurodivergent community
    i18n: {
        locales: ['en', 'es', 'fr', 'de', 'it', 'pt', 'ja', 'ko', 'zh'],
        defaultLocale: 'en',
        localeDetection: false, // Autism-friendly: consistent behavior
    },

    // 🔄 Redirects for smooth navigation
    async redirects() {
        return [
            {
                source: '/home',
                destination: '/',
                permanent: true,
            },
        ];
    },

    // 🎨 Custom page extensions for organization
    pageExtensions: ['tsx', 'ts', 'jsx', 'js'],

    // 🚀 Production optimizations
    productionBrowserSourceMaps: false,
    poweredByHeader: false,
    generateEtags: true,
    compress: true,

    // 🧠 Environment variables for neurodivergent features
    env: {
        ADHD_MODE_ENABLED: process.env.ADHD_MODE_ENABLED || 'true',
        AUTISM_MODE_ENABLED: process.env.AUTISM_MODE_ENABLED || 'true',
        ACCESSIBILITY_LEVEL: process.env.ACCESSIBILITY_LEVEL || 'AAA',
        PERFORMANCE_MONITORING: process.env.PERFORMANCE_MONITORING || 'true',
    },
};

module.exports = nextConfig;
