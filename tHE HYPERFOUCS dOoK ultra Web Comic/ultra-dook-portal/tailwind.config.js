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
                // ADVANCED DOPAMINE ARCHITECTURE - ADHD-optimized color palette
                'broski': {
                    50: '#f0f9ff',
                    100: '#e0f2fe',
                    200: '#bae6fd',
                    300: '#7dd3fc',
                    400: '#38bdf8',
                    500: '#3b82f6',
                    600: '#2563eb',
                    700: '#1d4ed8',
                    800: '#1e3a8a',
                    900: '#1e3a8a',
                },
                'hyperfocus': {
                    50: '#fdf4ff',
                    100: '#fae8ff',
                    200: '#f5d0fe',
                    300: '#f0abfc',
                    400: '#e879f9',
                    500: '#a855f7',
                    600: '#9333ea',
                    700: '#7c3aed',
                    800: '#6b21a8',
                    900: '#581c87',
                },
                'crystal': {
                    50: '#f7fee7',
                    100: '#ecfccb',
                    200: '#d9f99d',
                    300: '#bef264',
                    400: '#a3e635',
                    500: '#65a30d',
                    600: '#16a34a',
                    700: '#15803d',
                    800: '#166534',
                    900: '#14532d',
                },
                'celebration': {
                    50: '#fef3c7',
                    100: '#fde68a',
                    200: '#fcd34d',
                    300: '#fbbf24',
                    400: '#f59e0b',
                    500: '#f59e0b',
                    600: '#d97706',
                    700: '#b45309',
                    800: '#92400e',
                    900: '#78350f',
                },
                // NEURODIVERGENT-SPECIFIC COLORS
                'dopamine': {
                    50: '#fff7ed',
                    100: '#ffedd5',
                    200: '#fed7aa',
                    300: '#fdba74',
                    400: '#fb923c',
                    500: '#f97316',
                    600: '#ea580c',
                    700: '#c2410c',
                    800: '#9a3412',
                    900: '#7c2d12',
                },
                'focus': {
                    50: '#f0fdf4',
                    100: '#dcfce7',
                    200: '#bbf7d0',
                    300: '#86efac',
                    400: '#4ade80',
                    500: '#22c55e',
                    600: '#16a34a',
                    700: '#15803d',
                    800: '#166534',
                    900: '#14532d',
                },
                'energy': {
                    50: '#fef2f2',
                    100: '#fee2e2',
                    200: '#fecaca',
                    300: '#fca5a5',
                    400: '#f87171',
                    500: '#ef4444',
                    600: '#dc2626',
                    700: '#b91c1c',
                    800: '#991b1b',
                    900: '#7f1d1d',
                }
            },
            fontFamily: {
                'adhd': ['Inter', 'system-ui', 'sans-serif'],
                'dook': ['JetBrains Mono', 'Monaco', 'monospace'],
                'dyslexic': ['OpenDyslexic', 'Arial', 'sans-serif'], // Dyslexia-friendly
            },
            animation: {
                // ENHANCED DOPAMINE ANIMATIONS
                'bounce-slow': 'bounce 3s infinite',
                'pulse-fast': 'pulse 1s infinite',
                'celebration': 'celebration 0.6s ease-out',
                'celebration-epic': 'celebration-epic 1.2s ease-out',
                'hyperfocus': 'hyperfocus 2s ease-in-out infinite',
                'dopamine-pulse': 'dopamine-pulse 1.5s ease-in-out infinite',
                'focus-glow': 'focus-glow 3s ease-in-out infinite',
                'energy-wave': 'energy-wave 2s ease-in-out infinite',
                'micro-bounce': 'micro-bounce 0.3s ease-out',
                'gentle-float': 'gentle-float 4s ease-in-out infinite',
                'particle-drift': 'particle-drift 6s linear infinite',
            },
            keyframes: {
                // ADVANCED DOPAMINE ARCHITECTURE ANIMATIONS
                celebration: {
                    '0%': { transform: 'scale(1) rotate(0deg)', opacity: '1' },
                    '25%': { transform: 'scale(1.1) rotate(5deg)', opacity: '0.9' },
                    '50%': { transform: 'scale(1.2) rotate(-5deg)', opacity: '0.8' },
                    '75%': { transform: 'scale(1.1) rotate(3deg)', opacity: '0.9' },
                    '100%': { transform: 'scale(1) rotate(0deg)', opacity: '1' },
                },
                'celebration-epic': {
                    '0%': { transform: 'scale(1) rotate(0deg)', opacity: '1', filter: 'hue-rotate(0deg)' },
                    '20%': { transform: 'scale(1.3) rotate(72deg)', opacity: '0.8', filter: 'hue-rotate(72deg)' },
                    '40%': { transform: 'scale(0.9) rotate(144deg)', opacity: '0.9', filter: 'hue-rotate(144deg)' },
                    '60%': { transform: 'scale(1.4) rotate(216deg)', opacity: '0.7', filter: 'hue-rotate(216deg)' },
                    '80%': { transform: 'scale(1.1) rotate(288deg)', opacity: '0.9', filter: 'hue-rotate(288deg)' },
                    '100%': { transform: 'scale(1) rotate(360deg)', opacity: '1', filter: 'hue-rotate(360deg)' },
                },
                hyperfocus: {
                    '0%, 100%': {
                        boxShadow: '0 0 0 0 rgba(168, 85, 247, 0.4)',
                        backgroundColor: 'rgba(168, 85, 247, 0.1)'
                    },
                    '50%': {
                        boxShadow: '0 0 0 20px rgba(168, 85, 247, 0)',
                        backgroundColor: 'rgba(168, 85, 247, 0.2)'
                    },
                },
                'dopamine-pulse': {
                    '0%, 100%': {
                        transform: 'scale(1)',
                        boxShadow: '0 0 0 0 rgba(249, 115, 22, 0.4)'
                    },
                    '50%': {
                        transform: 'scale(1.02)',
                        boxShadow: '0 0 0 10px rgba(249, 115, 22, 0)'
                    },
                },
                'focus-glow': {
                    '0%, 100%': {
                        boxShadow: '0 0 5px rgba(34, 197, 94, 0.3)'
                    },
                    '50%': {
                        boxShadow: '0 0 20px rgba(34, 197, 94, 0.6), 0 0 30px rgba(34, 197, 94, 0.3)'
                    },
                },
                'energy-wave': {
                    '0%': {
                        transform: 'translateX(-100%)',
                        opacity: '0'
                    },
                    '50%': {
                        transform: 'translateX(0%)',
                        opacity: '1'
                    },
                    '100%': {
                        transform: 'translateX(100%)',
                        opacity: '0'
                    },
                },
                'micro-bounce': {
                    '0%': { transform: 'translateY(0px)' },
                    '50%': { transform: 'translateY(-4px)' },
                    '100%': { transform: 'translateY(0px)' },
                },
                'gentle-float': {
                    '0%, 100%': { transform: 'translateY(0px) rotate(0deg)' },
                    '25%': { transform: 'translateY(-5px) rotate(1deg)' },
                    '50%': { transform: 'translateY(-10px) rotate(0deg)' },
                    '75%': { transform: 'translateY(-5px) rotate(-1deg)' },
                },
                'particle-drift': {
                    '0%': {
                        transform: 'translateX(0px) translateY(0px) rotate(0deg)',
                        opacity: '0'
                    },
                    '10%': {
                        opacity: '1'
                    },
                    '90%': {
                        opacity: '1'
                    },
                    '100%': {
                        transform: 'translateX(100px) translateY(-100px) rotate(360deg)',
                        opacity: '0'
                    },
                }
            },
            spacing: {
                '18': '4.5rem',
                '88': '22rem',
                '128': '32rem',
            },
            borderRadius: {
                'xl': '1rem',
                '2xl': '1.5rem',
                '3xl': '2rem',
                '4xl': '2.5rem',
            },
            // ACCESSIBILITY & ADHD OPTIMIZATION
            fontSize: {
                'adhd-xs': ['0.75rem', { lineHeight: '1.5', letterSpacing: '0.025em' }],
                'adhd-sm': ['0.875rem', { lineHeight: '1.6', letterSpacing: '0.025em' }],
                'adhd-base': ['1rem', { lineHeight: '1.7', letterSpacing: '0.025em' }],
                'adhd-lg': ['1.125rem', { lineHeight: '1.7', letterSpacing: '0.025em' }],
            },
            boxShadow: {
                'dopamine': '0 4px 14px 0 rgba(249, 115, 22, 0.15)',
                'focus': '0 4px 14px 0 rgba(34, 197, 94, 0.15)',
                'hyperfocus': '0 8px 25px 0 rgba(168, 85, 247, 0.25)',
                'celebration': '0 10px 40px 0 rgba(245, 158, 11, 0.3)',
            }
        },
    },
    plugins: [
        require('@tailwindcss/typography'),
    ],
}
