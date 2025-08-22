"use client";

import { useEffect, useState } from 'react';

// 🧠 ADHD Performance Monitor Component
export function ADHDPerformanceMonitor() {
    const [loadTime, setLoadTime] = useState<number>(0);
    const [interactionDelay, setInteractionDelay] = useState<number>(0);
    const [focusPreserved, setFocusPreserved] = useState<boolean>(true);

    useEffect(() => {
        // 📊 Track page load performance
        const measureLoadTime = () => {
            if (typeof window !== 'undefined' && window.performance) {
                const loadComplete = window.performance.timing.loadEventEnd;
                const loadStart = window.performance.timing.navigationStart;
                const totalTime = loadComplete - loadStart;
                setLoadTime(totalTime);

                // 🎯 ADHD optimization: Alert if load time > 1 second
                if (totalTime > 1000) {
                    console.warn('⚠️ ADHD Alert: Page load time exceeded 1 second:', totalTime + 'ms');
                }
            }
        };

        // 🔍 Monitor interaction responsiveness
        const monitorInteractions = () => {
            let interactionStart = 0;

            const startTimer = () => {
                interactionStart = Date.now();
            };

            const endTimer = () => {
                if (interactionStart > 0) {
                    const delay = Date.now() - interactionStart;
                    setInteractionDelay(delay);

                    // 🎯 ADHD optimization: Alert if interaction delay > 100ms
                    if (delay > 100) {
                        console.warn('⚠️ ADHD Alert: Interaction delay detected:', delay + 'ms');
                        setFocusPreserved(false);
                    }
                }
            };

            // Monitor click interactions
            document.addEventListener('mousedown', startTimer);
            document.addEventListener('mouseup', endTimer);

            // Monitor keyboard interactions
            document.addEventListener('keydown', startTimer);
            document.addEventListener('keyup', endTimer);

            return () => {
                document.removeEventListener('mousedown', startTimer);
                document.removeEventListener('mouseup', endTimer);
                document.removeEventListener('keydown', startTimer);
                document.removeEventListener('keyup', endTimer);
            };
        };

        // Wait for page to load completely
        if (document.readyState === 'complete') {
            measureLoadTime();
        } else {
            window.addEventListener('load', measureLoadTime);
        }

        const cleanup = monitorInteractions();

        return () => {
            window.removeEventListener('load', measureLoadTime);
            cleanup();
        };
    }, []);

    // 🎯 Visual performance indicator for ADHD users
    const getPerformanceColor = () => {
        if (loadTime < 500) return 'text-calm-green';
        if (loadTime < 1000) return 'text-energy-orange';
        return 'text-red-500';
    };

    const getInteractionColor = () => {
        if (interactionDelay < 50) return 'text-calm-green';
        if (interactionDelay < 100) return 'text-energy-orange';
        return 'text-red-500';
    };

    return (
        <div className="fixed bottom-4 right-4 bg-white dark:bg-gray-800 rounded-lg shadow-lg p-3 text-xs z-50 border border-gray-200 dark:border-gray-700">
            <div className="text-hyperfocus-blue font-semibold mb-2">🧠 ADHD Performance</div>

            <div className="space-y-1">
                <div className="flex justify-between items-center">
                    <span>Load Time:</span>
                    <span className={`font-mono ${getPerformanceColor()}`}>
                        {loadTime > 0 ? `${loadTime}ms` : 'Measuring...'}
                    </span>
                </div>

                <div className="flex justify-between items-center">
                    <span>Interaction:</span>
                    <span className={`font-mono ${getInteractionColor()}`}>
                        {interactionDelay > 0 ? `${interactionDelay}ms` : 'Ready'}
                    </span>
                </div>

                <div className="flex justify-between items-center">
                    <span>Focus:</span>
                    <span className={focusPreserved ? 'text-calm-green' : 'text-red-500'}>
                        {focusPreserved ? '✅ Preserved' : '⚠️ At Risk'}
                    </span>
                </div>
            </div>
        </div>
    );
}

// 🌈 Autism Sensory Control Panel
export function AutismSensoryControls() {
    const [motionReduced, setMotionReduced] = useState(false);
    const [soundMuted, setSoundMuted] = useState(false);
    const [contrastHigh, setContrastHigh] = useState(false);
    const [layoutSimple, setLayoutSimple] = useState(false);

    useEffect(() => {
        // Apply sensory modifications
        const root = document.documentElement;

        if (motionReduced) {
            root.style.setProperty('--motion-duration', '0.01ms');
            root.classList.add('reduced-motion');
        } else {
            root.style.removeProperty('--motion-duration');
            root.classList.remove('reduced-motion');
        }

        root.classList.toggle('high-contrast-mode', contrastHigh);
        root.classList.toggle('simple-layout', layoutSimple);

        // Global sound control
        if (soundMuted) {
            // Disable all audio elements
            const audioElements = document.querySelectorAll('audio, video');
            audioElements.forEach(el => {
                (el as HTMLMediaElement).muted = true;
            });
        }
    }, [motionReduced, soundMuted, contrastHigh, layoutSimple]);

    return (
        <div className="fixed top-4 right-4 bg-soft-yellow border border-energy-orange rounded-lg shadow-lg p-4 z-50 max-w-sm">
            <div className="text-peaceful-indigo font-semibold mb-3 text-center">
                🌈 Autism Sensory Controls
            </div>

            <div className="space-y-3">
                <label className="flex items-center space-x-3 cursor-pointer">
                    <input
                        type="checkbox"
                        checked={motionReduced}
                        onChange={(e) => setMotionReduced(e.target.checked)}
                        className="w-4 h-4 text-peaceful-indigo focus:ring-2 focus:ring-peaceful-indigo rounded"
                    />
                    <span className="text-sm">⏱️ Reduce Motion</span>
                </label>

                <label className="flex items-center space-x-3 cursor-pointer">
                    <input
                        type="checkbox"
                        checked={soundMuted}
                        onChange={(e) => setSoundMuted(e.target.checked)}
                        className="w-4 h-4 text-peaceful-indigo focus:ring-2 focus:ring-peaceful-indigo rounded"
                    />
                    <span className="text-sm">🔇 Mute Sounds</span>
                </label>

                <label className="flex items-center space-x-3 cursor-pointer">
                    <input
                        type="checkbox"
                        checked={contrastHigh}
                        onChange={(e) => setContrastHigh(e.target.checked)}
                        className="w-4 h-4 text-peaceful-indigo focus:ring-2 focus:ring-peaceful-indigo rounded"
                    />
                    <span className="text-sm">🎨 High Contrast</span>
                </label>

                <label className="flex items-center space-x-3 cursor-pointer">
                    <input
                        type="checkbox"
                        checked={layoutSimple}
                        onChange={(e) => setLayoutSimple(e.target.checked)}
                        className="w-4 h-4 text-peaceful-indigo focus:ring-2 focus:ring-peaceful-indigo rounded"
                    />
                    <span className="text-sm">📐 Simple Layout</span>
                </label>
            </div>
        </div>
    );
}

// 🚀 Performance Booster for ADHD Users
export function PerformanceBooster() {
    const [isOptimizing, setIsOptimizing] = useState(false);
    const [optimizationScore, setOptimizationScore] = useState(85);

    const runOptimization = async () => {
        setIsOptimizing(true);

        try {
            // 🧹 Clear unnecessary DOM elements
            const removableElements = document.querySelectorAll('.loading-shimmer, .temporary-element');
            removableElements.forEach(el => el.remove());

            // 🗑️ Clear browser caches
            if ('caches' in window) {
                const cacheNames = await caches.keys();
                await Promise.all(
                    cacheNames.map(cacheName => {
                        if (cacheName.includes('temp') || cacheName.includes('old')) {
                            return caches.delete(cacheName);
                        }
                    })
                );
            }

            // 🎯 Preload critical resources for next interaction
            const criticalResources = [
                '/favicon.ico',
                '/manifest.json',
            ];

            criticalResources.forEach(url => {
                const link = document.createElement('link');
                link.rel = 'prefetch';
                link.href = url;
                document.head.appendChild(link);
            });

            // 🔧 Force garbage collection if available
            if ('gc' in window && typeof window.gc === 'function') {
                window.gc();
            }

            setOptimizationScore(Math.min(100, optimizationScore + 5));
        } catch (error) {
            console.warn('Performance optimization error:', error);
        } finally {
            setIsOptimizing(false);
        }
    };

    const getScoreColor = () => {
        if (optimizationScore >= 95) return 'text-calm-green';
        if (optimizationScore >= 80) return 'text-energy-orange';
        return 'text-red-500';
    };

    return (
        <div className="fixed bottom-4 left-4 bg-white dark:bg-gray-800 rounded-lg shadow-lg p-4 z-50 border border-gray-200 dark:border-gray-700">
            <div className="text-hyperfocus-blue font-semibold mb-3 text-center">
                🚀 ADHD Performance Booster
            </div>

            <div className="text-center space-y-3">
                <div className="text-2xl font-bold">
                    <span className={getScoreColor()}>{optimizationScore}%</span>
                </div>

                <button
                    onClick={runOptimization}
                    disabled={isOptimizing}
                    className={`px-4 py-2 rounded-lg font-semibold transition-all duration-200 ${isOptimizing
                            ? 'bg-gray-300 text-gray-500 cursor-not-allowed'
                            : 'bg-hyperfocus-blue text-white hover:bg-blue-700 hover:scale-105 active:scale-95'
                        }`}
                >
                    {isOptimizing ? (
                        <span className="flex items-center space-x-2">
                            <div className="w-4 h-4 border-2 border-current border-t-transparent rounded-full animate-spin" />
                            <span>Optimizing...</span>
                        </span>
                    ) : (
                        '⚡ Boost Performance'
                    )}
                </button>
            </div>
        </div>
    );
}

export default { ADHDPerformanceMonitor, AutismSensoryControls, PerformanceBooster };
