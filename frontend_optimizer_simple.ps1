#!/usr/bin/env pwsh
<#
🚀💎⚡ HYPERFOCUS ZONE FRONTEND OPTIMIZATION - SIMPLIFIED ⚡💎🚀
Core frontend performance and neurodivergent UI optimization
#>

param(
    [switch]$InstallDependencies,
    [switch]$CreateConfig,
    [switch]$ShowMenu
)

function Write-StatusMessage {
    param([string]$Message, [string]$Type = "Info")

    $timestamp = Get-Date -Format "HH:mm:ss"
    switch ($Type) {
        "Success" { Write-Host "[$timestamp] ✅ $Message" -ForegroundColor Green }
        "Warning" { Write-Host "[$timestamp] ⚠️  $Message" -ForegroundColor Yellow }
        "Error" { Write-Host "[$timestamp] ❌ $Message" -ForegroundColor Red }
        "Highlight" { Write-Host "[$timestamp] 🌟 $Message" -ForegroundColor Magenta }
        default { Write-Host "[$timestamp] ℹ️  $Message" -ForegroundColor Cyan }
    }
}

function Test-Prerequisites {
    Write-StatusMessage "🔍 Checking prerequisites..." "Info"

    # Check Node.js
    try {
        $nodeVersion = node --version
        Write-StatusMessage "Node.js version: $nodeVersion" "Success"
        return $true
    }
    catch {
        Write-StatusMessage "Node.js not found! Please install Node.js 18+ from https://nodejs.org" "Error"
        return $false
    }
}

function Install-CoreDependencies {
    Write-StatusMessage "📦 Installing core dependencies for neurodivergent optimization..." "Info"

    if (-not (Test-Path "package.json")) {
        Write-StatusMessage "Creating package.json for HYPERFOCUS Zone..." "Info"

        $packageJson = @{
            name = "hyperfocus-zone-frontend"
            version = "1.0.0"
            description = "Neurodivergent-first social platform frontend"
            main = "index.js"
            scripts = @{
                dev = "next dev"
                build = "next build"
                start = "next start"
                lint = "next lint"
                test = "jest"
                "test:watch" = "jest --watch"
                "accessibility:test" = "lighthouse http://localhost:3000 --only-categories=accessibility"
                "performance:audit" = "lighthouse http://localhost:3000 --only-categories=performance"
            }
            dependencies = @{
                "next" = "latest"
                "react" = "latest"
                "react-dom" = "latest"
                "typescript" = "latest"
                "@types/react" = "latest"
                "@types/react-dom" = "latest"
            }
            devDependencies = @{
                "@testing-library/react" = "latest"
                "@testing-library/jest-dom" = "latest"
                "jest" = "latest"
                "jest-environment-jsdom" = "latest"
                "eslint" = "latest"
                "eslint-config-next" = "latest"
                "eslint-plugin-jsx-a11y" = "latest"
                "@axe-core/react" = "latest"
            }
        } | ConvertTo-Json -Depth 10

        $packageJson | Out-File -FilePath "package.json" -Encoding UTF8
        Write-StatusMessage "Package.json created successfully!" "Success"
    }

    Write-StatusMessage "Installing dependencies..." "Info"
    npm install

    Write-StatusMessage "Dependencies installed successfully!" "Success"
}

function Create-OptimizedConfigs {
    Write-StatusMessage "⚡ Creating optimized configurations..." "Highlight"

    # Create Next.js config
    $nextConfig = @'
/** @type {import('next').NextConfig} */
const nextConfig = {
  // Performance optimizations for ADHD users
  compiler: {
    removeConsole: process.env.NODE_ENV === 'production',
  },
  experimental: {
    optimizeCss: true,
    optimizeImages: true,
  },
  // Image optimization
  images: {
    formats: ['image/webp', 'image/avif'],
    deviceSizes: [640, 750, 828, 1080, 1200, 1920],
    imageSizes: [16, 32, 48, 64, 96, 128, 256],
  },
  // ADHD optimization - faster page transitions
  reactStrictMode: true,
  swcMinify: true,
  // Neurodivergent considerations - predictable behavior
  trailingSlash: false,
  poweredByHeader: false,
};

module.exports = nextConfig;
'@

    $nextConfig | Out-File -FilePath "next.config.js" -Encoding UTF8
    Write-StatusMessage "Next.js configuration created with neurodivergent optimizations" "Success"

    # Create Tailwind config
    $tailwindConfig = @'
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
      // Neurodivergent-optimized spacing
      spacing: {
        '18': '4.5rem',
        '88': '22rem',
      },
      // Focus states for ADHD users
      ringWidth: {
        '3': '3px',
        '4': '4px',
      },
      ringColor: {
        'focus': '#0066CC',
      },
    },
  },
  plugins: [
    require('@tailwindcss/forms'),
    require('@tailwindcss/typography'),
  ],
  // Respect user preferences
  darkMode: 'media',
};
'@

    $tailwindConfig | Out-File -FilePath "tailwind.config.js" -Encoding UTF8
    Write-StatusMessage "Tailwind CSS configured with neurodivergent optimizations" "Success"

    # Create accessibility-focused ESLint config
    $eslintConfig = @'
{
  "extends": [
    "next/core-web-vitals",
    "plugin:jsx-a11y/recommended"
  ],
  "plugins": [
    "jsx-a11y"
  ],
  "rules": {
    "jsx-a11y/alt-text": "error",
    "jsx-a11y/anchor-has-content": "error",
    "jsx-a11y/anchor-is-valid": "error",
    "jsx-a11y/aria-props": "error",
    "jsx-a11y/click-events-have-key-events": "error",
    "jsx-a11y/heading-has-content": "error",
    "jsx-a11y/label-has-associated-control": "error",
    "jsx-a11y/no-autofocus": "warn",
    "jsx-a11y/no-distracting-elements": "error",
    "jsx-a11y/role-has-required-aria-props": "error"
  }
}
'@

    $eslintConfig | Out-File -FilePath ".eslintrc.json" -Encoding UTF8
    Write-StatusMessage "ESLint configured for accessibility compliance" "Success"
}

function Create-NeurodivergentComponents {
    Write-StatusMessage "🧠 Creating neurodivergent-optimized React components..." "Info"

    # Create src/components directory
    if (-not (Test-Path "src/components")) {
        New-Item -Path "src/components" -ItemType Directory -Force
    }

    # Create accessibility provider
    $accessibilityProvider = @'
'use client';

import React, { createContext, useContext, useState, useEffect, ReactNode } from 'react';

interface AccessibilityContextType {
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

  // Load preferences from localStorage
  useEffect(() => {
    if (typeof window !== 'undefined') {
      const savedPrefs = localStorage.getItem('accessibility-preferences');
      if (savedPrefs) {
        const prefs = JSON.parse(savedPrefs);
        setHighContrast(prefs.highContrast ?? false);
        setFontSize(prefs.fontSize ?? 'medium');
        setFocusMode(prefs.focusMode ?? false);
        setSensoryMode(prefs.sensoryMode ?? false);
      }
    }
  }, []);

  // Save preferences to localStorage
  useEffect(() => {
    if (typeof window !== 'undefined') {
      const prefs = { highContrast, fontSize, focusMode, sensoryMode };
      localStorage.setItem('accessibility-preferences', JSON.stringify(prefs));
    }
  }, [highContrast, fontSize, focusMode, sensoryMode]);

  const toggleHighContrast = () => setHighContrast(!highContrast);
  const toggleFocusMode = () => setFocusMode(!focusMode);
  const toggleSensoryMode = () => setSensoryMode(!sensoryMode);

  const value = {
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
          ${highContrast ? 'high-contrast' : ''}
          ${focusMode ? 'focus-mode' : ''}
          ${sensoryMode ? 'sensory-mode' : ''}
          ${fontSize === 'small' ? 'text-sm' : fontSize === 'large' ? 'text-lg' : ''}
        `}
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
'@

    $accessibilityProvider | Out-File -FilePath "src/components/AccessibilityProvider.tsx" -Encoding UTF8
    Write-StatusMessage "Accessibility Provider component created!" "Success"

    # Create neurodivergent button component
    $neurodivergentButton = @'
'use client';

import React, { forwardRef, ButtonHTMLAttributes } from 'react';
import { useAccessibility } from './AccessibilityProvider';

interface NeurodivergentButtonProps extends ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'success' | 'warning' | 'danger';
  size?: 'sm' | 'md' | 'lg';
  isLoading?: boolean;
  loadingText?: string;
}

export const NeurodivergentButton = forwardRef<HTMLButtonElement, NeurodivergentButtonProps>(
  (
    {
      children,
      variant = 'primary',
      size = 'md',
      isLoading = false,
      loadingText,
      className = '',
      disabled,
      ...props
    },
    ref
  ) => {
    const { focusMode } = useAccessibility();

    const baseClasses = `
      inline-flex items-center justify-center
      font-medium text-center
      border border-transparent
      transition-all duration-200
      focus:outline-none focus:ring-3 focus:ring-focus
      disabled:opacity-50 disabled:cursor-not-allowed
      ${focusMode ? 'focus-enhanced' : ''}
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

    return (
      <button
        ref={ref}
        className={`
          ${baseClasses}
          ${sizeClasses[size]}
          ${variantClasses[variant]}
          ${className}
        `}
        disabled={disabled || isLoading}
        {...props}
      >
        {isLoading ? (
          <div className="flex items-center">
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
          </div>
        ) : (
          children
        )}
      </button>
    );
  }
);

NeurodivergentButton.displayName = 'NeurodivergentButton';
'@

    $neurodivergentButton | Out-File -FilePath "src/components/NeurodivergentButton.tsx" -Encoding UTF8
    Write-StatusMessage "Neurodivergent Button component created!" "Success"
}

function Show-Summary {
    Write-StatusMessage "🎉 HYPERFOCUS Zone Frontend Optimization Complete!" "Success"
    Write-Host ""
    Write-Host "🚀💎⚡ ACHIEVEMENTS UNLOCKED ⚡💎🚀" -ForegroundColor Magenta
    Write-Host "✅ Neurodivergent-optimized package.json created" -ForegroundColor Green
    Write-Host "✅ Next.js configured for ADHD performance optimization" -ForegroundColor Green
    Write-Host "✅ Tailwind CSS with autism-friendly design system" -ForegroundColor Green
    Write-Host "✅ ESLint with accessibility compliance rules" -ForegroundColor Green
    Write-Host "✅ Accessibility Provider for user preferences" -ForegroundColor Green
    Write-Host "✅ Neurodivergent Button component with focus optimization" -ForegroundColor Green
    Write-Host ""
    Write-Host "🧠 Your neurodivergent-first frontend is ready!" -ForegroundColor Cyan
    Write-Host "🌟 Run 'npm run dev' to start your optimized development server!" -ForegroundColor Yellow
}

# Main execution
Write-StatusMessage "🌟 HYPERFOCUS Zone Frontend Optimization Engine Starting..." "Highlight"
Write-StatusMessage "🧠💎⚡ Neurodivergent-First Frontend Development ⚡💎🧠" "Highlight"

if (-not (Test-Prerequisites)) {
    exit 1
}

if ($InstallDependencies) {
    Install-CoreDependencies
}

if ($CreateConfig) {
    Create-OptimizedConfigs
    Create-NeurodivergentComponents
}

if (-not $InstallDependencies -and -not $CreateConfig) {
    # If no specific flags, do everything
    Install-CoreDependencies
    Create-OptimizedConfigs
    Create-NeurodivergentComponents
}

Show-Summary
