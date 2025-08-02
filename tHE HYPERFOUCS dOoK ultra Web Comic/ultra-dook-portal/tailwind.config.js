/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
        './app/**/*.{js,ts,jsx,tsx,mdx}',
        './src/**/*.{js,ts,jsx,tsx,mdx}',
    ],
    theme: {
        extend: {
            colors: {
                // ADHD-optimized color palette
                'broski': {
                    50: '#f0f9ff',
                    100: '#e0f2fe',
                    500: '#3b82f6',
                    600: '#2563eb',
                    700: '#1d4ed8',
                    900: '#1e3a8a',
                },
                'hyperfocus': {
                    50: '#fdf4ff',
                    100: '#fae8ff',
                    500: '#a855f7',
                    600: '#9333ea',
                    700: '#7c3aed',
                    900: '#581c87',
                },
                'crystal': {
                    50: '#f7fee7',
                    100: '#ecfccb',
                    500: '#65a30d',
                    600: '#16a34a',
                    700: '#15803d',
                    900: '#14532d',
                },
                'celebration': {
                    50: '#fef3c7',
                    100: '#fde68a',
                    500: '#f59e0b',
                    600: '#d97706',
                    700: '#b45309',
                    900: '#78350f',
                }
            },
            fontFamily: {
                'adhd': ['Inter', 'system-ui', 'sans-serif'],
                'dook': ['JetBrains Mono', 'Monaco', 'monospace'],
            },
            animation: {
                'bounce-slow': 'bounce 3s infinite',
                'pulse-fast': 'pulse 1s infinite',
                'celebration': 'celebration 0.5s ease-out',
                'hyperfocus': 'hyperfocus 2s ease-in-out infinite',
            },
            keyframes: {
                celebration: {
                    '0%': { transform: 'scale(1)', opacity: '1' },
                    '50%': { transform: 'scale(1.2)', opacity: '0.8' },
                    '100%': { transform: 'scale(1)', opacity: '1' },
                },
                hyperfocus: {
                    '0%, 100%': {
                        boxShadow: '0 0 0 0 rgba(168, 85, 247, 0.4)'
                    },
                    '50%': {
                        boxShadow: '0 0 0 20px rgba(168, 85, 247, 0)'
                    },
                }
            },
            spacing: {
                '18': '4.5rem',
                '88': '22rem',
            },
            borderRadius: {
                'xl': '1rem',
                '2xl': '1.5rem',
                '3xl': '2rem',
            }
        },
    },
    plugins: [
        require('@tailwindcss/typography'),
    ],
}
