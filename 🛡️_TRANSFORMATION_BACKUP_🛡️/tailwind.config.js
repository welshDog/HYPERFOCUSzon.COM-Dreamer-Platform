/** @type {import('tailwindcss').Config} */
module.exports = {
    content: [
        './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
        './src/components/**/*.{js,ts,jsx,tsx,mdx}',
        './src/app/**/*.{js,ts,jsx,tsx,mdx}',
        './pages/**/*.{js,ts,jsx,tsx,mdx}',
        './components/**/*.{js,ts,jsx,tsx,mdx}',
    ],
    theme: {
        extend: {
            // 🧠 ADHD-friendly color scheme
            colors: {
                'hyperfocus-blue': '#0066CC',
                'calm-green': '#22C55E',
                'focus-purple': '#8B5CF6',
                'energy-orange': '#F97316',
                'mindful-teal': '#14B8A6',
                'gentle-gray': '#6B7280',
                'soft-yellow': '#FEF3C7',
                'peaceful-indigo': '#6366F1',
            },

            // 🌈 Autism-friendly spacing and sizing
            spacing: {
                '18': '4.5rem',
                '22': '5.5rem',
                '88': '22rem',
                '104': '26rem',
            },

            // 🔤 Neurodivergent-optimized typography
            fontFamily: {
                'dyslexic-friendly': ['Inter', 'Open Sans', 'Arial', 'sans-serif'],
                'reading': ['Georgia', 'Times New Roman', 'serif'],
                'mono-accessible': ['JetBrains Mono', 'Consolas', 'Monaco', 'monospace'],
            },

            fontSize: {
                '2xs': ['0.625rem', { lineHeight: '0.875rem' }],
                'xs': ['0.75rem', { lineHeight: '1rem' }],
                'sm': ['0.875rem', { lineHeight: '1.25rem' }],
                'base': ['1rem', { lineHeight: '1.5rem' }],
                'lg': ['1.125rem', { lineHeight: '1.75rem' }],
                'xl': ['1.25rem', { lineHeight: '1.75rem' }],
                '2xl': ['1.5rem', { lineHeight: '2rem' }],
                '3xl': ['1.875rem', { lineHeight: '2.25rem' }],
                '4xl': ['2.25rem', { lineHeight: '2.5rem' }],
            },

            // 🎯 Enhanced focus states for ADHD users
            ringWidth: {
                '3': '3px',
                '4': '4px',
                '5': '5px',
            },

            ringColor: {
                'focus': '#0066CC',
                'focus-strong': '#003D7A',
                'success': '#22C55E',
                'warning': '#F97316',
            },

            // ⏱️ Animation timing for sensory considerations
            transitionDuration: {
                '75': '75ms',
                '100': '100ms',
                '150': '150ms',
                '200': '200ms',
                '300': '300ms',
                '500': '500ms',
                '700': '700ms',
                '1000': '1000ms',
                '2000': '2000ms',
            },

            // 🎬 Reduced motion support animations
            animation: {
                'gentle-bounce': 'gentle-bounce 2s ease-in-out infinite',
                'focus-pulse': 'focus-pulse 2s ease-in-out infinite',
                'soft-fade': 'soft-fade 0.3s ease-in-out',
                'slide-in': 'slide-in 0.3s ease-out',
            },

            // 📏 Improved contrast and readability
            lineHeight: {
                'tight': '1.25',
                'snug': '1.375',
                'normal': '1.5',
                'relaxed': '1.625',
                'loose': '2',
                'extra-loose': '2.5',
            },

            // 🎨 High contrast mode colors
            backgroundColor: {
                'high-contrast': '#000000',
                'high-contrast-alt': '#FFFFFF',
            },

            textColor: {
                'high-contrast': '#FFFFFF',
                'high-contrast-alt': '#000000',
            },
        },
    },
    plugins: [
        require('@tailwindcss/forms'),
        require('@tailwindcss/typography'),

        // 🧠 Custom plugin for neurodivergent accessibility
        function ({ addUtilities, addComponents, theme }) {
            // Skip link utility for keyboard navigation
            const skipLinkUtilities = {
                '.skip-link': {
                    position: 'absolute',
                    top: '-40px',
                    left: '6px',
                    background: theme('colors.hyperfocus-blue'),
                    color: 'white',
                    padding: '8px 16px',
                    textDecoration: 'none',
                    borderRadius: '4px',
                    fontSize: '14px',
                    fontWeight: '600',
                    zIndex: '9999',
                    transition: 'top 0.3s ease',
                    '&:focus': {
                        top: '6px',
                    },
                },
            };

            // Enhanced focus utilities for ADHD users
            const focusUtilities = {
                '.focus-enhanced': {
                    '&:focus': {
                        outline: `3px solid ${theme('colors.focus')}`,
                        outlineOffset: '2px',
                        borderRadius: '4px',
                    },
                },
                '.focus-strong': {
                    '&:focus': {
                        outline: `4px solid ${theme('colors.focus-strong')}`,
                        outlineOffset: '3px',
                        borderRadius: '6px',
                        boxShadow: `0 0 0 6px ${theme('colors.focus')}33`,
                    },
                },
            };

            // Reduced motion utilities for autism sensory support
            const motionUtilities = {
                '.reduced-motion': {
                    '@media (prefers-reduced-motion: reduce)': {
                        animation: 'none !important',
                        transition: 'none !important',
                    },
                },
                '.respect-motion-preference': {
                    '@media (prefers-reduced-motion: reduce)': {
                        animationDuration: '0.01ms !important',
                        animationIterationCount: '1 !important',
                        transitionDuration: '0.01ms !important',
                    },
                },
            };

            // High contrast mode utilities
            const contrastUtilities = {
                '.high-contrast-mode': {
                    backgroundColor: theme('backgroundColor.high-contrast'),
                    color: theme('textColor.high-contrast'),
                    '& *': {
                        borderColor: theme('textColor.high-contrast'),
                    },
                },
            };

            // Cognitive load reduction utilities
            const cognitiveUtilities = {
                '.cognitive-friendly': {
                    maxWidth: '65ch',
                    lineHeight: theme('lineHeight.relaxed'),
                    fontSize: theme('fontSize.lg'),
                },
                '.minimal-decision': {
                    '& button:not(:first-child)': {
                        display: 'none',
                    },
                },
            };

            addUtilities({
                ...skipLinkUtilities,
                ...focusUtilities,
                ...motionUtilities,
                ...contrastUtilities,
                ...cognitiveUtilities,
            });

            // Neurodivergent-friendly component styles
            const neurodivergentComponents = {
                '.btn-neurodivergent': {
                    padding: theme('spacing.3') + ' ' + theme('spacing.6'),
                    borderRadius: theme('borderRadius.md'),
                    fontWeight: theme('fontWeight.semibold'),
                    transition: 'all 200ms ease',
                    '&:focus': {
                        outline: `3px solid ${theme('colors.focus')}`,
                        outlineOffset: '2px',
                    },
                    '&:hover': {
                        transform: 'translateY(-1px)',
                        boxShadow: theme('boxShadow.md'),
                    },
                    '&:active': {
                        transform: 'translateY(0)',
                    },
                },
                '.card-neurodivergent': {
                    padding: theme('spacing.6'),
                    borderRadius: theme('borderRadius.lg'),
                    backgroundColor: theme('colors.white'),
                    boxShadow: theme('boxShadow.sm'),
                    border: `1px solid ${theme('colors.gray.200')}`,
                    '&:focus-within': {
                        outline: `2px solid ${theme('colors.focus')}`,
                        outlineOffset: '2px',
                    },
                },
            };

            addComponents(neurodivergentComponents);
        },
    ],

    // 🌙 Dark mode support for sensory preferences
    darkMode: 'media',

    // 🎨 Respect user preferences
    future: {
        respectDefaultRingColorOpacity: true,
        respectDefaultOutlineWidths: true,
    },
};
