"use client";

import React, { createContext, useContext, useEffect, useReducer } from 'react';

// 🧠 Accessibility Context for Neurodivergent Users
interface AccessibilityState {
    reducedMotion: boolean;
    highContrast: boolean;
    fontSize: 'small' | 'medium' | 'large' | 'extra-large';
    dyslexicFont: boolean;
    soundEnabled: boolean;
    cognitiveSupport: boolean;
    adhdMode: boolean;
    autismMode: boolean;
    focusEnhancement: boolean;
    colorScheme: 'light' | 'dark' | 'auto';
}

interface AccessibilityContextType {
    state: AccessibilityState;
    updateSetting: (key: keyof AccessibilityState, value: any) => void;
    resetToDefaults: () => void;
}

const defaultState: AccessibilityState = {
    reducedMotion: false,
    highContrast: false,
    fontSize: 'medium',
    dyslexicFont: false,
    soundEnabled: true,
    cognitiveSupport: false,
    adhdMode: false,
    autismMode: false,
    focusEnhancement: false,
    colorScheme: 'auto',
};

type AccessibilityAction =
    | { type: 'UPDATE_SETTING'; key: keyof AccessibilityState; value: any }
    | { type: 'RESET_TO_DEFAULTS' }
    | { type: 'LOAD_FROM_STORAGE'; state: AccessibilityState };

function accessibilityReducer(state: AccessibilityState, action: AccessibilityAction): AccessibilityState {
    switch (action.type) {
        case 'UPDATE_SETTING':
            return { ...state, [action.key]: action.value };
        case 'RESET_TO_DEFAULTS':
            return defaultState;
        case 'LOAD_FROM_STORAGE':
            return action.state;
        default:
            return state;
    }
}

const AccessibilityContext = createContext<AccessibilityContextType | undefined>(undefined);

// 🌈 Accessibility Provider Component
export function AccessibilityProvider({ children }: { children: React.ReactNode }) {
    const [state, dispatch] = useReducer(accessibilityReducer, defaultState);

    // 💾 Load settings from localStorage on mount
    useEffect(() => {
        try {
            const saved = localStorage.getItem('hyperfocus-accessibility-settings');
            if (saved) {
                const savedState = JSON.parse(saved);
                dispatch({ type: 'LOAD_FROM_STORAGE', state: { ...defaultState, ...savedState } });
            }
        } catch (error) {
            console.warn('Failed to load accessibility settings:', error);
        }

        // 🔍 Detect user's motion preference
        const mediaQuery = window.matchMedia('(prefers-reduced-motion: reduce)');
        if (mediaQuery.matches) {
            dispatch({ type: 'UPDATE_SETTING', key: 'reducedMotion', value: true });
        }

        // 🌙 Detect user's color scheme preference
        const colorSchemeQuery = window.matchMedia('(prefers-color-scheme: dark)');
        const updateColorScheme = () => {
            if (state.colorScheme === 'auto') {
                document.documentElement.classList.toggle('dark', colorSchemeQuery.matches);
            }
        };

        updateColorScheme();
        colorSchemeQuery.addEventListener('change', updateColorScheme);

        return () => {
            colorSchemeQuery.removeEventListener('change', updateColorScheme);
        };
    }, []);

    // 💾 Save settings to localStorage when state changes
    useEffect(() => {
        try {
            localStorage.setItem('hyperfocus-accessibility-settings', JSON.stringify(state));
        } catch (error) {
            console.warn('Failed to save accessibility settings:', error);
        }

        // 🎨 Apply CSS classes based on settings
        const root = document.documentElement;

        // High contrast mode
        root.classList.toggle('high-contrast-mode', state.highContrast);

        // Dyslexic-friendly font
        root.classList.toggle('font-dyslexic-friendly', state.dyslexicFont);

        // ADHD mode optimizations
        root.classList.toggle('adhd-mode', state.adhdMode);

        // Autism mode optimizations
        root.classList.toggle('autism-mode', state.autismMode);

        // Cognitive support mode
        root.classList.toggle('cognitive-support', state.cognitiveSupport);

        // Focus enhancement
        root.classList.toggle('focus-enhanced', state.focusEnhancement);

        // Font size adjustment
        root.setAttribute('data-font-size', state.fontSize);

        // Color scheme
        if (state.colorScheme !== 'auto') {
            root.classList.toggle('dark', state.colorScheme === 'dark');
        }

        // Reduced motion
        if (state.reducedMotion) {
            root.style.setProperty('--motion-duration', '0.01ms');
        } else {
            root.style.removeProperty('--motion-duration');
        }
    }, [state]);

    const updateSetting = (key: keyof AccessibilityState, value: any) => {
        dispatch({ type: 'UPDATE_SETTING', key, value });

        // 🔊 Provide audio feedback if enabled
        if (state.soundEnabled && typeof window !== 'undefined' && 'speechSynthesis' in window) {
            try {
                const utterance = new SpeechSynthesisUtterance(`${key} ${value ? 'enabled' : 'disabled'}`);
                utterance.volume = 0.3;
                utterance.rate = 1.2;
                speechSynthesis.speak(utterance);
            } catch (error) {
                // Silent fail for audio feedback
            }
        }
    };

    const resetToDefaults = () => {
        dispatch({ type: 'RESET_TO_DEFAULTS' });
    };

    return (
        <AccessibilityContext.Provider value={{ state, updateSetting, resetToDefaults }}>
            {children}
        </AccessibilityContext.Provider>
    );
}

// 🪝 Hook to use accessibility context
export function useAccessibility() {
    const context = useContext(AccessibilityContext);
    if (context === undefined) {
        throw new Error('useAccessibility must be used within an AccessibilityProvider');
    }
    return context;
}

// 🎯 Skip Link Component for Keyboard Navigation
export function SkipLink({ href = "#main-content", children = "Skip to main content" }: {
    href?: string;
    children?: React.ReactNode;
}) {
    return (
        <a
            href={href}
            className="skip-link sr-only focus:not-sr-only focus:absolute focus:top-2 focus:left-2 focus:z-50 bg-hyperfocus-blue text-white px-4 py-2 rounded-md font-semibold"
        >
            {children}
        </a>
    );
}

// 🧠 ADHD-Optimized Focus Manager Component
export function FocusManager({ children }: { children: React.ReactNode }) {
    const { state } = useAccessibility();

    useEffect(() => {
        if (!state.adhdMode) return;

        // 🎯 Enhanced focus management for ADHD users
        const handleFocusChange = (event: FocusEvent) => {
            const target = event.target as HTMLElement;
            if (target) {
                // Add visual focus enhancement
                target.classList.add('adhd-focus-active');

                // Remove enhancement after delay
                setTimeout(() => {
                    target.classList.remove('adhd-focus-active');
                }, 3000);
            }
        };

        document.addEventListener('focusin', handleFocusChange);
        return () => document.removeEventListener('focusin', handleFocusChange);
    }, [state.adhdMode]);

    return <>{children}</>;
}

// 🌈 Autism-Friendly Predictability Indicator
export function PredictabilityIndicator({
    label,
    isLoading = false,
    estimatedTime
}: {
    label: string;
    isLoading?: boolean;
    estimatedTime?: string;
}) {
    const { state } = useAccessibility();

    if (!state.autismMode) return null;

    return (
        <div className="predictability-indicator bg-soft-yellow border border-energy-orange rounded-md p-3 mb-4">
            <div className="flex items-center space-x-2">
                <div className={`w-3 h-3 rounded-full ${isLoading ? 'bg-energy-orange animate-pulse' : 'bg-calm-green'}`} />
                <span className="font-medium text-sm">{label}</span>
                {estimatedTime && (
                    <span className="text-xs text-gentle-gray">Est. {estimatedTime}</span>
                )}
            </div>
        </div>
    );
}

export default AccessibilityProvider;
