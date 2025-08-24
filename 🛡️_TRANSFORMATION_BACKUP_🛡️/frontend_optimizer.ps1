#!/usr/bin/env pwsh
<#
🚀💎⚡ HYPERFOCUS ZONE FRONTEND OPTIMIZATION ENGINE ⚡💎🚀
Advanced frontend performance and neurodivergent UI optimization script
#>

param(
    [string]$ProjectPath = ".",
    [switch]$InstallDependencies,
    [switch]$OptimizePerformance,
    [switch]$EnableNeurodivergentMode,
    [switch]$RunTests,
    [switch]$Deploy
)

# Set strict mode and error handling
Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

# Define colors for output
$ColorSuccess = "Green"
$ColorWarning = "Yellow"
$ColorError = "Red"
$ColorInfo = "Cyan"
$ColorHighlight = "Magenta"

function Write-StatusMessage {
    param([string]$Message, [string]$Type = "Info")

    $timestamp = Get-Date -Format "HH:mm:ss"
    switch ($Type) {
        "Success" { Write-Host "[$timestamp] ✅ $Message" -ForegroundColor $ColorSuccess }
        "Warning" { Write-Host "[$timestamp] ⚠️  $Message" -ForegroundColor $ColorWarning }
        "Error" { Write-Host "[$timestamp] ❌ $Message" -ForegroundColor $ColorError }
        "Highlight" { Write-Host "[$timestamp] 🌟 $Message" -ForegroundColor $ColorHighlight }
        default { Write-Host "[$timestamp] ℹ️  $Message" -ForegroundColor $ColorInfo }
    }
}

function Test-Prerequisites {
    Write-StatusMessage "🔍 Checking prerequisites..." "Info"

    # Check Node.js
    try {
        $nodeVersion = node --version
        Write-StatusMessage "Node.js version: $nodeVersion" "Success"
    }
    catch {
        Write-StatusMessage "Node.js not found! Please install Node.js 18+ from https://nodejs.org" "Error"
        exit 1
    }

    # Check npm
    try {
        $npmVersion = npm --version
        Write-StatusMessage "npm version: $npmVersion" "Success"
    }
    catch {
        Write-StatusMessage "npm not found! Please install npm" "Error"
        exit 1
    }

    # Check if we're in a valid project directory
    if (-not (Test-Path "package.json")) {
        Write-StatusMessage "No package.json found. Please run this script from your project root." "Warning"

        # Offer to create a new React/Next.js project
        $createNew = Read-Host "Would you like to create a new HYPERFOCUS Zone project? (y/n)"
        if ($createNew -eq "y" -or $createNew -eq "Y") {
            Initialize-HyperfocusProject
        }
        else {
            exit 1
        }
    }
}

function Initialize-HyperfocusProject {
    Write-StatusMessage "🚀 Initializing HYPERFOCUS Zone project..." "Highlight"

    $projectName = Read-Host "Enter project name (or press Enter for 'hyperfocus-zone')"
    if (-not $projectName) { $projectName = "hyperfocus-zone" }

    # Create Next.js project with TypeScript
    Write-StatusMessage "Creating Next.js project with TypeScript..." "Info"
    npx create-next-app@latest $projectName --typescript --tailwind --eslint --app --src-dir --import-alias "@/*"

    Set-Location $projectName

    # Install additional dependencies for accessibility and neurodivergent support
    Write-StatusMessage "Installing accessibility and neurodivergent support packages..." "Info"
    npm install --save `
        "@radix-ui/react-accessible-icon" `
        "@radix-ui/react-focus-scope" `
        "@radix-ui/react-roving-focus" `
        "framer-motion" `
        "react-spring" `
        "@headlessui/react" `
        "react-aria" `
        "@react-aria/utils" `
        "react-intersection-observer" `
        "react-use-gesture"

    npm install --save-dev `
        "@testing-library/react" `
        "@testing-library/jest-dom" `
        "@testing-library/user-event" `
        "jest" `
        "jest-environment-jsdom" `
        "@axe-core/react" `
        "lighthouse" `
        "web-vitals"

    Write-StatusMessage "HYPERFOCUS Zone project initialized successfully!" "Success"
}

function Install-Dependencies {
    Write-StatusMessage "📦 Installing and updating dependencies..." "Info"

    # Core React/Next.js dependencies
    $coreDeps = @(
        "react@latest",
        "react-dom@latest",
        "next@latest",
        "@types/react@latest",
        "@types/react-dom@latest",
        "typescript@latest"
    )

    # Accessibility dependencies
    $accessibilityDeps = @(
        "@radix-ui/react-accessible-icon",
        "@radix-ui/react-focus-scope",
        "@radix-ui/react-roving-focus",
        "@radix-ui/react-slot",
        "@headlessui/react",
        "react-aria",
        "@react-aria/utils",
        "@react-aria/focus",
        "focus-trap-react"
    )

    # Neurodivergent-specific dependencies
    $neurodivergentDeps = @(
        "framer-motion",
        "react-spring",
        "react-intersection-observer",
        "react-use-gesture",
        "react-hotkeys-hook",
        "use-sound",
        "react-idle-timer"
    )

    # Performance dependencies
    $performanceDeps = @(
        "web-vitals",
        "react-window",
        "react-virtualized-auto-sizer",
        "workbox-webpack-plugin",
        "@next/bundle-analyzer"
    )

    # Development dependencies
    $devDeps = @(
        "@testing-library/react",
        "@testing-library/jest-dom",
        "@testing-library/user-event",
        "jest",
        "jest-environment-jsdom",
        "@axe-core/react",
        "lighthouse",
        "prettier",
        "eslint-plugin-jsx-a11y",
        "eslint-plugin-react-hooks"
    )

    Write-StatusMessage "Installing core dependencies..." "Info"
    npm install $coreDeps

    Write-StatusMessage "Installing accessibility dependencies..." "Info"
    npm install $accessibilityDeps

    Write-StatusMessage "Installing neurodivergent support dependencies..." "Info"
    npm install $neurodivergentDeps

    Write-StatusMessage "Installing performance dependencies..." "Info"
    npm install $performanceDeps

    Write-StatusMessage "Installing development dependencies..." "Info"
    npm install --save-dev $devDeps

    Write-StatusMessage "All dependencies installed successfully!" "Success"
}

function Optimize-Performance {
    Write-StatusMessage "⚡ Optimizing frontend performance..." "Highlight"

    # Create performance optimization configuration
    $nextConfig = @"
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
"@

    $nextConfig | Out-File -FilePath "next.config.js" -Encoding UTF8
    Write-StatusMessage "Next.js configuration optimized for performance and neurodivergent users" "Success"

    # Create Tailwind config with accessibility and neurodivergent considerations
    $tailwindConfig = @"
/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './src/pages/**/*.{js,ts,jsx,tsx,mdx}',
    './src/components/**/*.{js,ts,jsx,tsx,mdx}',
    './src/app/**/*.{js,ts,jsx,tsx,mdx}',
  ],
  theme: {
    extend: {
      // ADHD-friendly color scheme
      colors: {
        'hyperfocus-blue': '#0066CC',
        'calm-green': '#22C55E',
        'focus-purple': '#8B5CF6',
        'energy-orange': '#F97316',
        'mindful-teal': '#14B8A6',
      },
      // Autism-friendly spacing and sizing
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      },
      // Neurodivergent-optimized typography
      fontFamily: {
        'dyslexic-friendly': ['Open Sans', 'Arial', 'sans-serif'],
        'reading': ['Georgia', 'serif'],
      },
      fontSize: {
        '2xs': ['0.625rem', { lineHeight: '1' }],
      },
      // Focus states for ADHD users
      ringWidth: {
        '3': '3px',
        '4': '4px',
      },
      ringColor: {
        'focus': '#0066CC',
      },
      // Animation timing for sensory considerations
      transitionDuration: {
        '2000': '2000ms',
      },
      // Reduced motion support
      animation: {
        'gentle-bounce': 'gentle-bounce 2s ease-in-out infinite',
        'focus-pulse': 'focus-pulse 2s ease-in-out infinite',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
    require('@tailwindcss/container-queries'),
    // Custom plugin for accessibility
    function({ addUtilities, theme }) {
      const newUtilities = {
        '.skip-link': {
          position: 'absolute',
          top: '-40px',
          left: '6px',
          background: theme('colors.blue.600'),
          color: 'white',
          padding: '8px',
          textDecoration: 'none',
          transition: 'top 0.3s',
          '&:focus': {
            top: '6px',
          },
        },
        '.focus-enhanced': {
          '&:focus': {
            outline: `3px solid ${theme('colors.blue.500')}`,
            outlineOffset: '2px',
          },
        },
        '.reduced-motion': {
          '@media (prefers-reduced-motion: reduce)': {
            animation: 'none',
            transition: 'none',
          },
        },
      };
      addUtilities(newUtilities);
    },
  ],
  // Respect user preferences
  darkMode: 'media', // Respects system preference
};
"@

    $tailwindConfig | Out-File -FilePath "tailwind.config.js" -Encoding UTF8
    Write-StatusMessage "Tailwind CSS configured with neurodivergent optimizations" "Success"

    # Create accessibility-first ESLint configuration
    $eslintConfig = @"
{
  "extends": [
    "next/core-web-vitals",
    "plugin:jsx-a11y/recommended",
    "plugin:react-hooks/recommended"
  ],
  "plugins": [
    "jsx-a11y"
  ],
  "rules": {
    "jsx-a11y/alt-text": "error",
    "jsx-a11y/anchor-has-content": "error",
    "jsx-a11y/anchor-is-valid": "error",
    "jsx-a11y/aria-props": "error",
    "jsx-a11y/aria-proptypes": "error",
    "jsx-a11y/aria-unsupported-elements": "error",
    "jsx-a11y/click-events-have-key-events": "error",
    "jsx-a11y/heading-has-content": "error",
    "jsx-a11y/label-has-associated-control": "error",
    "jsx-a11y/no-aria-hidden-on-focusable": "error",
    "jsx-a11y/no-autofocus": "warn",
    "jsx-a11y/no-distracting-elements": "error",
    "jsx-a11y/no-interactive-element-to-noninteractive-role": "error",
    "jsx-a11y/no-redundant-roles": "error",
    "jsx-a11y/role-has-required-aria-props": "error",
    "jsx-a11y/role-supports-aria-props": "error"
  }
}
"@

    $eslintConfig | Out-File -FilePath ".eslintrc.json" -Encoding UTF8
    Write-StatusMessage "ESLint configured for accessibility compliance" "Success"

    Write-StatusMessage "Performance optimization complete!" "Success"
}

function Enable-NeurodivergentMode {
    Write-StatusMessage "🧠 Enabling neurodivergent-specific optimizations..." "Highlight"

    # Create accessibility provider component
    $accessibilityProvider = @"
'use client';

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';
import { useReducedMotion } from 'framer-motion';

interface AccessibilityContextType {
  reduceMotion: boolean;
  highContrast: boolean;
  fontSize: 'small' | 'medium' | 'large';
  focusMode: boolean;
  sensoryMode: boolean;
  toggleHighContrast: () => void;
  setFontSize: (size: 'small' | 'medium' | 'large') => void;
  toggleFocusMode: () => void;
  toggleSensoryMode: () => void;
}

const AccessibilityContext = createContext<AccessibilityContextType | undefined>(undefined);

interface AccessibilityProviderProps {
  children: ReactNode;
}

export function AccessibilityProvider({ children }: AccessibilityProviderProps) {
  const [highContrast, setHighContrast] = useState(false);
  const [fontSize, setFontSize] = useState<'small' | 'medium' | 'large'>('medium');
  const [focusMode, setFocusMode] = useState(false);
  const [sensoryMode, setSensoryMode] = useState(false);
  const reduceMotion = useReducedMotion() ?? false;

  // Load preferences from localStorage
  useEffect(() => {
    const savedPrefs = localStorage.getItem('accessibility-preferences');
    if (savedPrefs) {
      const prefs = JSON.parse(savedPrefs);
      setHighContrast(prefs.highContrast ?? false);
      setFontSize(prefs.fontSize ?? 'medium');
      setFocusMode(prefs.focusMode ?? false);
      setSensoryMode(prefs.sensoryMode ?? false);
    }
  }, []);

  // Save preferences to localStorage
  useEffect(() => {
    const prefs = {
      highContrast,
      fontSize,
      focusMode,
      sensoryMode,
    };
    localStorage.setItem('accessibility-preferences', JSON.stringify(prefs));
  }, [highContrast, fontSize, focusMode, sensoryMode]);

  const toggleHighContrast = () => setHighContrast(!highContrast);
  const toggleFocusMode = () => setFocusMode(!focusMode);
  const toggleSensoryMode = () => setSensoryMode(!sensoryMode);

  const value = {
    reduceMotion,
    highContrast,
    fontSize,
    focusMode,
    sensoryMode,
    toggleHighContrast,
    setFontSize,
    toggleFocusMode,
    toggleSensoryMode,
  };

  return (
    <AccessibilityContext.Provider value={value}>
      <div
        className={`
          `${highContrast ? 'high-contrast' : ''}
          `${focusMode ? 'focus-mode' : ''}
          `${sensoryMode ? 'sensory-mode' : ''}
          `${fontSize === 'small' ? 'text-sm' : fontSize === 'large' ? 'text-lg' : ''}
        `}
        data-reduce-motion={reduceMotion}
      >
        {children}
      </div>
    </AccessibilityContext.Provider>
  );
}

export function useAccessibility() {
  const context = useContext(AccessibilityContext);
  if (context === undefined) {
    throw new Error('useAccessibility must be used within an AccessibilityProvider');
  }
  return context;
}
"@

    New-Item -Path "src/components" -ItemType Directory -Force
    $accessibilityProvider | Out-File -FilePath "src/components/AccessibilityProvider.tsx" -Encoding UTF8

    # Create neurodivergent UI components
    $neurodivergentButton = @"
'use client';

import React, { forwardRef, ButtonHTMLAttributes } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { useAccessibility } from './AccessibilityProvider';

interface NeurodivergentButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'success' | 'warning' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  loadingText?: string;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
}

export const NeurodivergentButton = forwardRef<HTMLButtonElement, NeurodivergentButtonProps>(
  (
    {
      children,
      variant = 'primary',
      size = 'md',
      isLoading = false,
      loadingText,
      leftIcon,
      rightIcon,
      className = '',
      disabled,
      ...props
    },
    ref
  ) => {
    const { reduceMotion, focusMode } = useAccessibility();

    const baseClasses = `
      inline-flex items-center justify-center
      font-medium text-center
      border border-transparent
      transition-all duration-200
      focus:outline-none focus:ring-3 focus:ring-focus
      disabled:opacity-50 disabled:cursor-not-allowed
      $`{focusMode ? 'focus-enhanced' : ''}
    `;

    const sizeClasses = {
      sm: 'px-3 py-2 text-sm',
      md: 'px-4 py-2.5 text-base',
      lg: 'px-6 py-3 text-lg',
    };

    const variantClasses = {
      primary: 'bg-hyperfocus-blue text-white hover:bg-blue-700',
      secondary: 'bg-gray-200 text-gray-900 hover:bg-gray-300',
      success: 'bg-calm-green text-white hover:bg-green-600',
      warning: 'bg-energy-orange text-white hover:bg-orange-600',
      danger: 'bg-red-500 text-white hover:bg-red-600',
    };

    const motionProps = reduceMotion
      ? {}
      : {
          whileHover: { scale: 1.02 },
          whileTap: { scale: 0.98 },
          transition: { duration: 0.1 },
        };

    return (
      <motion.button
        ref={ref}
        className={`
          $`{baseClasses}
          $`{sizeClasses[size]}
          $`{variantClasses[variant]}
          $`{className}
        `}
        disabled={disabled || isLoading}
        {...motionProps}
        {...props}
      >
        <AnimatePresence mode="wait">
          {isLoading ? (
            <motion.div
              key="loading"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex items-center"
            >
              <svg
                className="animate-spin -ml-1 mr-2 h-4 w-4"
                xmlns="http://www.w3.org/2000/svg"
                fill="none"
                viewBox="0 0 24 24"
                aria-hidden="true"
              >
                <circle
                  className="opacity-25"
                  cx="12"
                  cy="12"
                  r="10"
                  stroke="currentColor"
                  strokeWidth="4"
                />
                <path
                  className="opacity-75"
                  fill="currentColor"
                  d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"
                />
              </svg>
              {loadingText || 'Loading...'}
            </motion.div>
          ) : (
            <motion.div
              key="content"
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="flex items-center"
            >
              {leftIcon && <span className="mr-2">{leftIcon}</span>}
              {children}
              {rightIcon && <span className="ml-2">{rightIcon}</span>}
            </motion.div>
          )}
        </AnimatePresence>
      </motion.button>
    );
  }
);

NeurodivergentButton.displayName = 'NeurodivergentButton';
"@

    $neurodivergentButton | Out-File -FilePath "src/components/NeurodivergentButton.tsx" -Encoding UTF8

    Write-StatusMessage "Neurodivergent UI components created successfully!" "Success"
}

function Run-Tests {
    Write-StatusMessage "🧪 Running accessibility and performance tests..." "Info"

    # Create Jest configuration
    $jestConfig = @"
const nextJest = require('next/jest')

const createJestConfig = nextJest({
  dir: './',
})

const customJestConfig = {
  setupFilesAfterEnv: ['<rootDir>/jest.setup.js'],
  moduleNameMapping: {
    '^@/components/(.*)$': '<rootDir>/src/components/$1',
    '^@/pages/(.*)$': '<rootDir>/src/pages/$1',
    '^@/utils/(.*)$': '<rootDir>/src/utils/$1',
  },
  testEnvironment: 'jest-environment-jsdom',
}

module.exports = createJestConfig(customJestConfig)
"@

    $jestConfig | Out-File -FilePath "jest.config.js" -Encoding UTF8

    # Create Jest setup file
    $jestSetup = @"
import '@testing-library/jest-dom';
import { configure } from '@testing-library/react';
import { jest } from '@jest/globals';

// Configure testing library
configure({ testIdAttribute: 'data-testid' });

// Mock framer-motion to avoid issues in tests
jest.mock('framer-motion', () => ({
  motion: {
    div: 'div',
    button: 'button',
    span: 'span',
  },
  AnimatePresence: ({ children }) => children,
  useReducedMotion: () => false,
}));

// Mock Next.js router
jest.mock('next/router', () => ({
  useRouter() {
    return {
      route: '/',
      pathname: '/',
      query: {},
      asPath: '/',
      push: jest.fn(),
      pop: jest.fn(),
      reload: jest.fn(),
      back: jest.fn(),
      prefetch: jest.fn().mockResolvedValue(undefined),
      beforePopState: jest.fn(),
      events: {
        on: jest.fn(),
        off: jest.fn(),
        emit: jest.fn(),
      },
    };
  },
}));
"@

    $jestSetup | Out-File -FilePath "jest.setup.js" -Encoding UTF8

    # Run tests
    Write-StatusMessage "Running unit tests..." "Info"
    npm run test

    # Run accessibility audit (if available)
    if (Get-Command lighthouse -ErrorAction SilentlyContinue) {
        Write-StatusMessage "Running Lighthouse accessibility audit..." "Info"
        lighthouse http://localhost:3000 --only-categories=accessibility --output=json --output-path=./lighthouse-accessibility.json --chrome-flags="--headless"
    }
    else {
        Write-StatusMessage "Lighthouse not found. Install globally with: npm install -g lighthouse" "Warning"
    }

    Write-StatusMessage "Tests completed!" "Success"
}

function Deploy-Project {
    Write-StatusMessage "🚀 Preparing for deployment..." "Highlight"

    # Build project
    Write-StatusMessage "Building optimized production bundle..." "Info"
    npm run build

    # Check build size
    $buildStats = Get-ChildItem ".next/static" -Recurse | Measure-Object -Property Length -Sum
    $buildSizeMB = [math]::Round($buildStats.Sum / 1MB, 2)
    Write-StatusMessage "Build size: $buildSizeMB MB" "Info"

    if ($buildSizeMB -gt 10) {
        Write-StatusMessage "Large bundle size detected. Consider optimizing for better performance." "Warning"
    }

    # Create deployment checklist
    $deploymentChecklist = @"
# HYPERFOCUS Zone Deployment Checklist

## Pre-deployment Checks
- [ ] All tests passing
- [ ] Accessibility audit score > 95
- [ ] Performance audit score > 90
- [ ] Bundle size optimized
- [ ] Environment variables configured
- [ ] Error monitoring setup

## Accessibility Verification
- [ ] Keyboard navigation working
- [ ] Screen reader compatibility tested
- [ ] Color contrast ratio WCAG AA compliant
- [ ] Focus indicators visible and clear
- [ ] Reduced motion preferences respected

## Neurodivergent Features
- [ ] ADHD-friendly UI optimizations active
- [ ] Autism sensory considerations implemented
- [ ] Executive function support features working
- [ ] Break reminders and hyperfocus protection active

## Performance Metrics
- [ ] First Contentful Paint < 1.5s
- [ ] Largest Contentful Paint < 2.5s
- [ ] Cumulative Layout Shift < 0.1
- [ ] First Input Delay < 100ms

## Post-deployment
- [ ] Monitor Core Web Vitals
- [ ] Track accessibility usage metrics
- [ ] Gather neurodivergent user feedback
- [ ] Monitor error rates and performance
"@

    $deploymentChecklist | Out-File -FilePath "DEPLOYMENT-CHECKLIST.md" -Encoding UTF8
    Write-StatusMessage "Deployment checklist created!" "Success"

    Write-StatusMessage "Project ready for deployment! Review DEPLOYMENT-CHECKLIST.md before deploying." "Success"
}

# Main execution flow
function Main {
    Write-StatusMessage "🌟 HYPERFOCUS Zone Frontend Optimization Engine Starting..." "Highlight"
    Write-StatusMessage "🧠💎⚡ Neurodivergent-First Frontend Development ⚡💎🧠" "Highlight"

    try {
        # Change to project directory
        Set-Location $ProjectPath

        # Check prerequisites
        Test-Prerequisites

        # Execute requested operations
        if ($InstallDependencies) {
            Install-Dependencies
        }

        if ($OptimizePerformance) {
            Optimize-Performance
        }

        if ($EnableNeurodivergentMode) {
            Enable-NeurodivergentMode
        }

        if ($RunTests) {
            Run-Tests
        }

        if ($Deploy) {
            Deploy-Project
        }

        # If no specific operations requested, show menu
        if (-not ($InstallDependencies -or $OptimizePerformance -or $EnableNeurodivergentMode -or $RunTests -or $Deploy)) {
            Show-InteractiveMenu
        }

        Write-StatusMessage "🎉 HYPERFOCUS Zone Frontend Optimization Complete!" "Success"
        Write-StatusMessage "Your neurodivergent-first frontend is ready to empower the community!" "Highlight"
    }
    catch {
        Write-StatusMessage "Error: $($_.Exception.Message)" "Error"
        exit 1
    }
}

function Show-InteractiveMenu {
    Write-StatusMessage "🎯 HYPERFOCUS Zone Frontend Menu" "Highlight"
    Write-Host ""
    Write-Host "Choose an option:"
    Write-Host "1. 📦 Install Dependencies"
    Write-Host "2. ⚡ Optimize Performance"
    Write-Host "3. 🧠 Enable Neurodivergent Mode"
    Write-Host "4. 🧪 Run Tests"
    Write-Host "5. 🚀 Deploy Project"
    Write-Host "6. 🔄 Do Everything"
    Write-Host "0. Exit"
    Write-Host ""

    $choice = Read-Host "Enter your choice (0-6)"

    switch ($choice) {
        "1" { Install-Dependencies }
        "2" { Optimize-Performance }
        "3" { Enable-NeurodivergentMode }
        "4" { Run-Tests }
        "5" { Deploy-Project }
        "6" {
            Install-Dependencies
            Optimize-Performance
            Enable-NeurodivergentMode
            Run-Tests
            Write-StatusMessage "All optimizations complete! Ready for deployment." "Success"
        }
        "0" {
            Write-StatusMessage "Goodbye! Keep building amazing neurodivergent-first experiences! 🌟" "Highlight"
            exit 0
        }
        default {
            Write-StatusMessage "Invalid choice. Please try again." "Warning"
            Show-InteractiveMenu
        }
    }
}

# Run the main function
Main
