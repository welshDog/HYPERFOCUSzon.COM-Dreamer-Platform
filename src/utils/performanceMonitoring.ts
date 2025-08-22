// 🧠 ADHD Performance Monitoring Configuration
export const ADHDPerformanceConfig = {
    // Critical timing thresholds for ADHD attention preservation
    thresholds: {
        // Initial load - must be under 1 second for hyperfocus preservation
        initialLoad: 1000,
        // Interaction response - must be under 100ms to maintain flow state
        interactionResponse: 100,
        // Route navigation - must be under 500ms for seamless experience
        routeNavigation: 500,
        // Form validation - must be immediate for executive function support
        formValidation: 50,
    },

    // Performance monitoring configuration
    monitoring: {
        // Track Core Web Vitals with ADHD-specific extensions
        coreWebVitals: {
            // Largest Contentful Paint - critical for initial engagement
            lcp: { target: 800, adhd_critical: true },
            // First Input Delay - essential for maintaining attention
            fid: { target: 50, adhd_critical: true },
            // Cumulative Layout Shift - prevents distraction from unexpected movement
            cls: { target: 0.05, autism_critical: true },
            // First Contentful Paint - for immediate visual feedback
            fcp: { target: 500, adhd_critical: true },
        },

        // ADHD-specific metrics
        adhdMetrics: {
            // Time to interactive - when user can actually start working
            tti: { target: 1200, description: 'Time until hyperfocus can begin' },
            // Attention retention score - based on bounce rate and engagement
            attentionRetention: { target: 85, description: 'Percentage of maintained focus' },
            // Flow state preservation - uninterrupted work time
            flowStateTime: { target: 1800000, description: 'Milliseconds of uninterrupted flow' }, // 30 minutes
            // Distraction events - unexpected UI changes or interruptions
            distractionEvents: { target: 0, description: 'Number of focus-breaking events' },
        },

        // Autism-specific metrics
        autismMetrics: {
            // Predictability score - consistency of interface behavior
            predictabilityScore: { target: 95, description: 'Interface behavior consistency' },
            // Sensory load - amount of visual/audio stimulation
            sensoryLoad: { target: 30, description: 'Percentage of sensory stimulation' },
            // Navigation consistency - same paths lead to same results
            navigationConsistency: { target: 100, description: 'Route behavior reliability' },
            // Error prevention - proactive error handling
            errorPrevention: { target: 98, description: 'Percentage of errors prevented' },
        },
    },

    // Real-time monitoring alerts
    alerts: {
        // Critical alerts that require immediate attention
        critical: [
            {
                metric: 'initialLoad',
                threshold: 1000,
                message: '🚨 ADHD CRITICAL: Page load exceeding hyperfocus threshold!',
                action: 'optimize_critical_path',
            },
            {
                metric: 'interactionResponse',
                threshold: 100,
                message: '🚨 ADHD CRITICAL: Interaction delay breaking flow state!',
                action: 'reduce_main_thread_work',
            },
        ],

        // Warning alerts for attention management
        warning: [
            {
                metric: 'attentionRetention',
                threshold: 80,
                message: '⚠️ ADHD WARNING: Attention retention dropping',
                action: 'enhance_engagement_patterns',
            },
            {
                metric: 'sensoryLoad',
                threshold: 50,
                message: '⚠️ AUTISM WARNING: Sensory overload risk detected',
                action: 'reduce_visual_complexity',
            },
        ],
    },

    // Optimization strategies
    optimizations: {
        // ADHD performance optimizations
        adhd: {
            // Preload likely next actions to reduce wait time
            predictivePreloading: true,
            // Cache frequently accessed content
            hyperfocusCaching: true,
            // Minimize JavaScript bundle size
            bundleOptimization: true,
            // Enable service worker for offline access
            offlineSupport: true,
            // Optimize images for faster loading
            imageOptimization: true,
        },

        // Autism predictability optimizations
        autism: {
            // Ensure consistent timing for all animations
            consistentTiming: true,
            // Preload all critical resources to prevent layout shifts
            stableLayoutPreload: true,
            // Cache navigation state for predictable back/forward behavior
            navigationCaching: true,
            // Progressive enhancement instead of hydration surprises
            progressiveEnhancement: true,
        },

        // Universal accessibility optimizations
        accessibility: {
            // Ensure minimum contrast ratios
            contrastOptimization: true,
            // Optimize for screen readers
            screenReaderOptimization: true,
            // Keyboard navigation performance
            keyboardOptimization: true,
            // Focus management optimization
            focusOptimization: true,
        },
    },

    // Performance budgets with neurodivergent considerations
    budgets: {
        // JavaScript budget - smaller is better for ADHD attention
        javascript: {
            initial: '150kb', // Initial bundle
            total: '500kb',   // Total JS across all chunks
            adhd_rationale: 'Smaller bundles = faster parse time = quicker to flow state',
        },

        // CSS budget - minimize render blocking
        css: {
            initial: '50kb',  // Critical CSS
            total: '150kb',   // Total CSS
            autism_rationale: 'Consistent styling loads = predictable visual experience',
        },

        // Image budget - optimize for mobile and slow connections
        images: {
            initial: '200kb', // Above-the-fold images
            total: '2mb',     // Total image weight per page
            accessibility_rationale: 'Faster image loads = better experience for users with slow connections',
        },

        // Font budget - essential for readability
        fonts: {
            initial: '100kb', // Critical fonts
            total: '300kb',   // All fonts
            dyslexia_rationale: 'Optimized fonts improve readability for neurodivergent users',
        },
    },
};

// 🎯 Performance monitoring utilities
export class NeurodivergentPerformanceMonitor {
    private metrics: Map<string, number[]> = new Map();
    private alerts: ((alert: any) => void)[] = [];

    constructor() {
        this.initializeMonitoring();
    }

    private initializeMonitoring() {
        // Monitor Core Web Vitals
        this.observeWebVitals();

        // Monitor ADHD-specific metrics
        this.observeADHDMetrics();

        // Monitor Autism-specific metrics
        this.observeAutismMetrics();
    }

    private observeWebVitals() {
        // Use Web Vitals library to track performance
        if (typeof window !== 'undefined') {
            // LCP monitoring
            new PerformanceObserver((list) => {
                for (const entry of list.getEntries()) {
                    this.recordMetric('lcp', entry.value);
                    this.checkThreshold('lcp', entry.value);
                }
            }).observe({ entryTypes: ['largest-contentful-paint'] });

            // FID monitoring
            new PerformanceObserver((list) => {
                for (const entry of list.getEntries()) {
                    this.recordMetric('fid', entry.processingStart - entry.startTime);
                    this.checkThreshold('fid', entry.processingStart - entry.startTime);
                }
            }).observe({ entryTypes: ['first-input'] });

            // CLS monitoring
            let clsValue = 0;
            new PerformanceObserver((list) => {
                for (const entry of list.getEntries()) {
                    if (!entry.hadRecentInput) {
                        clsValue += entry.value;
                        this.recordMetric('cls', clsValue);
                        this.checkThreshold('cls', clsValue);
                    }
                }
            }).observe({ entryTypes: ['layout-shift'] });
        }
    }

    private observeADHDMetrics() {
        // Monitor flow state indicators
        let lastInteraction = Date.now();
        let flowStateStart = Date.now();

        const trackInteraction = () => {
            const now = Date.now();
            const timeSinceLastInteraction = now - lastInteraction;

            // If more than 30 seconds without interaction, flow state may be broken
            if (timeSinceLastInteraction > 30000) {
                const flowDuration = lastInteraction - flowStateStart;
                this.recordMetric('flowStateTime', flowDuration);
                flowStateStart = now;
            }

            lastInteraction = now;
        };

        if (typeof window !== 'undefined') {
            ['click', 'keydown', 'scroll', 'touchstart'].forEach(event => {
                document.addEventListener(event, trackInteraction, { passive: true });
            });
        }
    }

    private observeAutismMetrics() {
        // Monitor layout stability
        let layoutShiftCount = 0;

        if (typeof window !== 'undefined') {
            new PerformanceObserver((list) => {
                for (const entry of list.getEntries()) {
                    if (entry.value > 0.01) {  // Significant layout shift
                        layoutShiftCount++;
                        this.recordMetric('distractionEvents', layoutShiftCount);
                        this.checkThreshold('distractionEvents', layoutShiftCount);
                    }
                }
            }).observe({ entryTypes: ['layout-shift'] });
        }
    }

    private recordMetric(name: string, value: number) {
        if (!this.metrics.has(name)) {
            this.metrics.set(name, []);
        }
        this.metrics.get(name)!.push(value);

        // Keep only last 100 measurements
        if (this.metrics.get(name)!.length > 100) {
            this.metrics.get(name)!.shift();
        }
    }

    private checkThreshold(metric: string, value: number) {
        const config = ADHDPerformanceConfig.monitoring;
        let threshold: number | undefined;

        // Check core web vitals thresholds
        if (config.coreWebVitals[metric as keyof typeof config.coreWebVitals]) {
            threshold = config.coreWebVitals[metric as keyof typeof config.coreWebVitals].target;
        }

        // Check ADHD-specific thresholds
        if (config.adhdMetrics[metric as keyof typeof config.adhdMetrics]) {
            threshold = config.adhdMetrics[metric as keyof typeof config.adhdMetrics].target;
        }

        // Check autism-specific thresholds
        if (config.autismMetrics[metric as keyof typeof config.autismMetrics]) {
            threshold = config.autismMetrics[metric as keyof typeof config.autismMetrics].target;
        }

        if (threshold && value > threshold) {
            this.triggerAlert({
                metric,
                value,
                threshold,
                severity: value > threshold * 1.5 ? 'critical' : 'warning',
                timestamp: Date.now(),
            });
        }
    }

    private triggerAlert(alert: any) {
        console.warn(`🧠 Neurodivergent Performance Alert:`, alert);
        this.alerts.forEach(callback => callback(alert));
    }

    public onAlert(callback: (alert: any) => void) {
        this.alerts.push(callback);
    }

    public getMetrics() {
        const summary: Record<string, any> = {};

        for (const [name, values] of this.metrics.entries()) {
            summary[name] = {
                current: values[values.length - 1] || 0,
                average: values.reduce((a, b) => a + b, 0) / values.length || 0,
                min: Math.min(...values) || 0,
                max: Math.max(...values) || 0,
            };
        }

        return summary;
    }

    public getADHDScore(): number {
        const metrics = this.getMetrics();
        const weights = {
            lcp: 0.25,          // Loading performance
            fid: 0.25,          // Interaction responsiveness
            flowStateTime: 0.3, // Flow state preservation
            attentionRetention: 0.2, // Attention management
        };

        let score = 100;

        // Deduct points for poor performance
        if (metrics.lcp?.current > 1000) score -= 20;
        if (metrics.fid?.current > 100) score -= 20;
        if (metrics.flowStateTime?.current < 600000) score -= 15; // Less than 10 minutes
        if (metrics.attentionRetention?.current < 80) score -= 25;

        return Math.max(0, score);
    }

    public getAutismScore(): number {
        const metrics = this.getMetrics();
        let score = 100;

        // Deduct points for unpredictability
        if (metrics.cls?.current > 0.1) score -= 30;
        if (metrics.distractionEvents?.current > 5) score -= 25;
        if (metrics.predictabilityScore?.current < 90) score -= 20;
        if (metrics.navigationConsistency?.current < 95) score -= 25;

        return Math.max(0, score);
    }
}

export default ADHDPerformanceConfig;
