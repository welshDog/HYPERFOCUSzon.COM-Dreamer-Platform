"use client";

import React, { useEffect, useRef, useState } from 'react';
import { useAccessibility } from './AccessibilityProvider';

interface NeurodivergentButtonProps {
    children: React.ReactNode;
    onClick?: () => void;
    variant?: 'primary' | 'secondary' | 'success' | 'warning' | 'minimal';
    size?: 'small' | 'medium' | 'large';
    disabled?: boolean;
    loading?: boolean;
    soundFeedback?: boolean;
    hapticFeedback?: boolean;
    cognitiveHint?: string;
    adhdFriendly?: boolean;
    autismFriendly?: boolean;
    className?: string;
    type?: 'button' | 'submit' | 'reset';
    ariaLabel?: string;
}

// 🧠 Neurodivergent-Optimized Button Component
export function NeurodivergentButton({
    children,
    onClick,
    variant = 'primary',
    size = 'medium',
    disabled = false,
    loading = false,
    soundFeedback = true,
    hapticFeedback = true,
    cognitiveHint,
    adhdFriendly = true,
    autismFriendly = true,
    className = '',
    type = 'button',
    ariaLabel,
}: NeurodivergentButtonProps) {
    const { state } = useAccessibility();
    const [isPressed, setIsPressed] = useState(false);
    const [focusVisible, setFocusVisible] = useState(false);
    const buttonRef = useRef<HTMLButtonElement>(null);
    const pressTimer = useRef<NodeJS.Timeout>();

    // 🎨 Dynamic styling based on variant and state
    const getButtonClasses = () => {
        const baseClasses = [
            'relative inline-flex items-center justify-center',
            'font-semibold rounded-lg transition-all duration-200',
            'focus:outline-none focus-enhanced',
            'transform-gpu', // GPU acceleration for ADHD users
        ];

        // 📏 Size classes
        const sizeClasses = {
            small: 'px-3 py-2 text-sm',
            medium: 'px-4 py-3 text-base',
            large: 'px-6 py-4 text-lg',
        };

        // 🎨 Variant classes
        const variantClasses = {
            primary: [
                'bg-hyperfocus-blue text-white',
                'hover:bg-blue-700 active:bg-blue-800',
                'shadow-md hover:shadow-lg',
            ],
            secondary: [
                'bg-gray-100 text-gray-900 border border-gray-300',
                'hover:bg-gray-200 active:bg-gray-300',
                'shadow-sm hover:shadow-md',
            ],
            success: [
                'bg-calm-green text-white',
                'hover:bg-green-600 active:bg-green-700',
                'shadow-md hover:shadow-lg',
            ],
            warning: [
                'bg-energy-orange text-white',
                'hover:bg-orange-600 active:bg-orange-700',
                'shadow-md hover:shadow-lg',
            ],
            minimal: [
                'bg-transparent text-hyperfocus-blue',
                'hover:bg-blue-50 active:bg-blue-100',
                'border border-transparent hover:border-blue-200',
            ],
        };

        // 🧠 ADHD-specific optimizations
        const adhdClasses = state.adhdMode && adhdFriendly ? [
            'ring-2 ring-transparent hover:ring-hyperfocus-blue/30',
            'hover:scale-105 active:scale-95',
            'shadow-lg hover:shadow-xl',
        ] : [];

        // 🌈 Autism-specific optimizations
        const autismClasses = state.autismMode && autismFriendly ? [
            'border-2 border-solid',
            'transition-all duration-300',
        ] : [];

        // 🎯 High contrast mode
        const contrastClasses = state.highContrast ? [
            'border-2 border-white',
            'shadow-none',
        ] : [];

        // 🔄 Loading state
        const loadingClasses = loading ? [
            'cursor-not-allowed opacity-75',
        ] : [];

        // 🚫 Disabled state
        const disabledClasses = disabled ? [
            'cursor-not-allowed opacity-50',
            'hover:transform-none hover:shadow-none',
        ] : [];

        return [
            ...baseClasses,
            sizeClasses[size],
            ...variantClasses[variant],
            ...adhdClasses,
            ...autismClasses,
            ...contrastClasses,
            ...loadingClasses,
            ...disabledClasses,
            className,
        ].filter(Boolean).join(' ');
    };

    // 🔊 Audio feedback for interactions
    const playSound = (type: 'click' | 'hover' | 'focus') => {
        if (!state.soundEnabled || !soundFeedback) return;

        try {
            // Create AudioContext for precise sound generation
            const audioContext = new (window.AudioContext || (window as any).webkitAudioContext)();
            const oscillator = audioContext.createOscillator();
            const gainNode = audioContext.createGain();

            oscillator.connect(gainNode);
            gainNode.connect(audioContext.destination);

            // Different frequencies for different interactions
            const frequencies = {
                click: 800,
                hover: 600,
                focus: 400,
            };

            oscillator.frequency.setValueAtTime(frequencies[type], audioContext.currentTime);
            oscillator.type = 'sine';

            gainNode.gain.setValueAtTime(0, audioContext.currentTime);
            gainNode.gain.linearRampToValueAtTime(0.1, audioContext.currentTime + 0.01);
            gainNode.gain.linearRampToValueAtTime(0, audioContext.currentTime + 0.1);

            oscillator.start(audioContext.currentTime);
            oscillator.stop(audioContext.currentTime + 0.1);
        } catch (error) {
            // Silent fail for audio feedback
        }
    };

    // 📱 Haptic feedback for supported devices
    const triggerHaptic = (intensity: 'light' | 'medium' | 'heavy' = 'medium') => {
        if (!hapticFeedback || !navigator.vibrate) return;

        const patterns = {
            light: [10],
            medium: [20],
            heavy: [30],
        };

        navigator.vibrate(patterns[intensity]);
    };

    // 🎯 Enhanced click handler with accessibility features
    const handleClick = () => {
        if (disabled || loading) return;

        setIsPressed(true);

        // Audio feedback
        playSound('click');

        // Haptic feedback
        triggerHaptic('medium');

        // Visual feedback timing
        pressTimer.current = setTimeout(() => {
            setIsPressed(false);
        }, 150);

        // Call the actual click handler
        onClick?.();
    };

    // 🖱️ Mouse/touch interaction handlers
    const handleMouseEnter = () => {
        if (disabled || loading) return;
        playSound('hover');
        triggerHaptic('light');
    };

    const handleFocus = () => {
        setFocusVisible(true);
        playSound('focus');
    };

    const handleBlur = () => {
        setFocusVisible(false);
    };

    // ⌨️ Keyboard interaction handlers
    const handleKeyDown = (event: React.KeyboardEvent) => {
        if (event.key === 'Enter' || event.key === ' ') {
            event.preventDefault();
            handleClick();
        }
    };

    // 🧹 Cleanup effect
    useEffect(() => {
        return () => {
            if (pressTimer.current) {
                clearTimeout(pressTimer.current);
            }
        };
    }, []);

    return (
        <div className="relative">
            {/* 🧠 Cognitive hint tooltip for autism-friendly UX */}
            {cognitiveHint && state.autismMode && (
                <div className="absolute -top-12 left-1/2 transform -translate-x-1/2 bg-peaceful-indigo text-white px-3 py-1 rounded-md text-xs whitespace-nowrap opacity-0 group-hover:opacity-100 transition-opacity z-10">
                    {cognitiveHint}
                    <div className="absolute top-full left-1/2 transform -translate-x-1/2 border-4 border-transparent border-t-peaceful-indigo"></div>
                </div>
            )}

            <button
                ref={buttonRef}
                type={type}
                className={`${getButtonClasses()} ${cognitiveHint ? 'group' : ''}`}
                onClick={handleClick}
                onMouseEnter={handleMouseEnter}
                onFocus={handleFocus}
                onBlur={handleBlur}
                onKeyDown={handleKeyDown}
                disabled={disabled || loading}
                aria-label={ariaLabel}
                aria-pressed={isPressed ? "true" : "false"}
                aria-busy={loading ? "true" : "false"}
                data-adhd-friendly={adhdFriendly}
                data-autism-friendly={autismFriendly}
            >
                {/* 🔄 Loading spinner */}
                {loading && (
                    <div className="absolute inset-0 flex items-center justify-center">
                        <div className="w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin" />
                    </div>
                )}

                {/* 📝 Button content */}
                <span className={`${loading ? 'opacity-0' : 'opacity-100'} transition-opacity flex items-center space-x-2`}>
                    {children}
                </span>

                {/* 🎯 Focus ring for enhanced visibility */}
                {focusVisible && state.focusEnhancement && (
                    <div className="absolute inset-0 rounded-lg ring-4 ring-hyperfocus-blue ring-opacity-50 pointer-events-none" />
                )}

                {/* ⚡ ADHD attention pulse effect */}
                {state.adhdMode && adhdFriendly && (
                    <div className="absolute inset-0 rounded-lg bg-hyperfocus-blue opacity-0 animate-pulse pointer-events-none" />
                )}
            </button>
        </div>
    );
}

// 🎮 Quick Action Button for ADHD hyperfocus preservation
export function QuickActionButton({
    children,
    onClick,
    hotkey,
    className = '',
    ...props
}: NeurodivergentButtonProps & { hotkey?: string }) {
    const { state } = useAccessibility();

    useEffect(() => {
        if (!hotkey || !state.adhdMode) return;

        const handleKeyPress = (event: KeyboardEvent) => {
            if (event.ctrlKey && event.key.toLowerCase() === hotkey.toLowerCase()) {
                event.preventDefault();
                onClick?.();
            }
        };

        document.addEventListener('keydown', handleKeyPress);
        return () => document.removeEventListener('keydown', handleKeyPress);
    }, [hotkey, onClick, state.adhdMode]);

    return (
        <NeurodivergentButton
            {...props}
            onClick={onClick}
            className={`quick-action ${className}`}
            adhdFriendly={true}
            aria-keyshortcuts={hotkey ? `Control+${hotkey}` : undefined}
        >
            <span className="flex items-center space-x-2">
                {children}
                {hotkey && state.adhdMode && (
                    <span className="text-xs opacity-70 bg-white/20 rounded px-1">
                        Ctrl+{hotkey.toUpperCase()}
                    </span>
                )}
            </span>
        </NeurodivergentButton>
    );
}

export default NeurodivergentButton;
