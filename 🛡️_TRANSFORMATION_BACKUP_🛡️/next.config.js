/** @type {import('next').NextConfig} */
const nextConfig = {
  // Performance optimizations
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },
  experimental: {
    optimizeCss: true,
    optimizeImages: true,
    modernMode: true,
  },
  // Image optimization
  images: {
    formats: ['image/webp', 'image/avif'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920, 2048, 3840],
    imageSizes: [16, 32, 48, 64, 96, 128, 256, 384],
  },
  // Bundle analysis
  webpack: (config, { buildId, dev, isServer, defaultLoaders, webpack }) => {
    // Analyze bundle size in development
    if (process.env.ANALYZE === 'true') {
      const { BundleAnalyzerPlugin } = require('webpack-bundle-analyzer');
      config.plugins.push(
        new BundleAnalyzerPlugin({
          analyzerMode: 'static',
          openAnalyzer: false,
        })
      );
    }

    // ADHD/Autism optimizations - reduce bundle size for faster loading
    config.optimization.splitChunks = {
      chunks: 'all',
      cacheGroups: {
        accessibility: {
          name: 'accessibility',
          test: /[\\/]node_modules[\\/](@radix-ui|@headlessui|react-aria)[\\/]/,
          priority: 30,
        },
        neurodivergent: {
          name: 'neurodivergent',
          test: /[\\/]node_modules[\\/](framer-motion|react-spring|react-use-gesture)[\\/]/,
          priority: 25,
        },
      },
    };

    return config;
  },
  // ADHD optimization - faster page transitions
  pageExtensions: ['ts', 'tsx', 'js', 'jsx'],
  poweredByHeader: false,
  reactStrictMode: true,
  swcMinify: true,
  // Neurodivergent considerations - predictable behavior
  trailingSlash: false,
  // Performance headers
  headers: async () => [
    {
      source: '/(.*)',
      headers: [
        {
          key: 'X-Frame-Options',
          value: 'DENY',
        },
        {
          key: 'X-Content-Type-Options',
          value: 'nosniff',
        },
        {
          key: 'Referrer-Policy',
          value: 'strict-origin-when-cross-origin',
        },
      ],
    },
  ],
};

module.exports = nextConfig;
