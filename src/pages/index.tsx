import Head from 'next/head';
import { PredictabilityIndicator, useAccessibility } from '../components/AccessibilityProvider';
import { NeurodivergentButton, QuickActionButton } from '../components/NeurodivergentButton';

// 🚀 HYPERFOCUS ZONE Main Page with Full Neurodivergent Optimization
export default function Home() {
    const { state, updateSetting } = useAccessibility();

    const handleFocusMode = () => {
        console.log('🎯 Entering hyperfocus mode...');
        // Implement focus mode logic
    };

    const handleBreakTimer = () => {
        console.log('⏰ Starting break timer...');
        // Implement break timer logic
    };

    return (
        <>
            <Head>
                <title>HYPERFOCUS ZONE - Neurodivergent Productivity Empire</title>
                <meta name="description" content="Revolutionary productivity platform designed for 1.1 billion neurodivergent individuals. ADHD-friendly, autism-optimized, accessible to all." />
            </Head>

            {/* 🌟 Header with Accessibility Controls */}
            <header className="bg-white dark:bg-gray-800 shadow-sm border-b border-gray-200 dark:border-gray-700 sticky top-0 z-40">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
                    <div className="flex justify-between items-center h-16">
                        {/* 💎 Logo */}
                        <div className="flex items-center">
                            <h1 className="text-2xl font-bold text-hyperfocus-blue">
                                🚀 HYPERFOCUS ZONE
                            </h1>
                        </div>

                        {/* 🎯 Quick Actions */}
                        <div className="flex items-center space-x-3">
                            <QuickActionButton
                                hotkey="f"
                                onClick={handleFocusMode}
                                variant="primary"
                                cognitiveHint="Start focused work session"
                                className="hidden sm:flex"
                            >
                                🎯 Focus Mode
                            </QuickActionButton>

                            <QuickActionButton
                                hotkey="b"
                                onClick={handleBreakTimer}
                                variant="secondary"
                                cognitiveHint="Take a mindful break"
                                className="hidden sm:flex"
                            >
                                ⏰ Break Timer
                            </QuickActionButton>

                            {/* 🔧 Accessibility Menu Toggle */}
                            <NeurodivergentButton
                                onClick={() => updateSetting('cognitiveSupport', !state.cognitiveSupport)}
                                variant="minimal"
                                size="small"
                                cognitiveHint="Open accessibility settings"
                                ariaLabel="Toggle accessibility menu"
                            >
                                ⚙️ A11y
                            </NeurodivergentButton>
                        </div>
                    </div>
                </div>
            </header>

            {/* 📱 Main Content Area */}
            <main id="main-content" className="min-h-screen bg-gray-50 dark:bg-gray-900">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-8">

                    {/* 🧠 Predictability Indicator for Autism-Friendly UX */}
                    <PredictabilityIndicator
                        label="HYPERFOCUS ZONE Empire Status"
                        isLoading={false}
                        estimatedTime="Ready for action"
                    />

                    {/* 🌟 Hero Section */}
                    <section className="text-center py-12">
                        <div className="cognitive-friendly">
                            <h2 className="text-4xl sm:text-5xl lg:text-6xl font-bold text-gray-900 dark:text-white mb-6">
                                Welcome to Your
                                <span className="block text-hyperfocus-blue">
                                    🧠💎⚡ LEGENDARY EMPIRE ⚡💎🧠
                                </span>
                            </h2>

                            <p className="text-xl text-gray-600 dark:text-gray-300 mb-8 max-w-3xl mx-auto">
                                Revolutionary productivity platform designed for{' '}
                                <strong className="text-hyperfocus-blue">1.1 billion neurodivergent individuals</strong>.
                                ADHD-friendly, autism-optimized, accessible to all.
                            </p>

                            {/* 🚀 Primary Action Buttons */}
                            <div className="flex flex-col sm:flex-row gap-4 justify-center items-center">
                                <QuickActionButton
                                    hotkey="s"
                                    onClick={() => console.log('🌟 Starting empire journey...')}
                                    variant="primary"
                                    size="large"
                                    cognitiveHint="Begin your productivity transformation"
                                >
                                    🌟 Start Your Empire
                                </QuickActionButton>

                                <NeurodivergentButton
                                    onClick={() => console.log('📖 Opening guide...')}
                                    variant="secondary"
                                    size="large"
                                    cognitiveHint="Learn how to use HYPERFOCUS ZONE"
                                >
                                    📖 Quick Start Guide
                                </NeurodivergentButton>
                            </div>
                        </div>
                    </section>

                    {/* 🎯 Features Grid */}
                    <section className="py-12">
                        <h3 className="text-3xl font-bold text-center text-gray-900 dark:text-white mb-12">
                            🧠 Neurodivergent-Optimized Features
                        </h3>

                        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                            {/* 🎯 ADHD Support */}
                            <div className="card-neurodivergent">
                                <div className="text-4xl mb-4">🎯</div>
                                <h4 className="text-xl font-semibold mb-3 text-gray-900 dark:text-white">
                                    ADHD Hyperfocus Support
                                </h4>
                                <p className="text-gray-600 dark:text-gray-300 mb-4">
                                    Smart focus sessions, attention management, and hyperfocus preservation tools.
                                </p>
                                <NeurodivergentButton
                                    onClick={() => console.log('🎯 ADHD tools activated')}
                                    variant="primary"
                                    size="small"
                                    cognitiveHint="Access ADHD-specific tools"
                                >
                                    Explore ADHD Tools
                                </NeurodivergentButton>
                            </div>

                            {/* 🌈 Autism Support */}
                            <div className="card-neurodivergent">
                                <div className="text-4xl mb-4">🌈</div>
                                <h4 className="text-xl font-semibold mb-3 text-gray-900 dark:text-white">
                                    Autism-Friendly Interface
                                </h4>
                                <p className="text-gray-600 dark:text-gray-300 mb-4">
                                    Predictable navigation, sensory considerations, and clear communication patterns.
                                </p>
                                <NeurodivergentButton
                                    onClick={() => console.log('🌈 Autism tools activated')}
                                    variant="success"
                                    size="small"
                                    cognitiveHint="Access autism-specific features"
                                >
                                    Explore Autism Features
                                </NeurodivergentButton>
                            </div>

                            {/* ♿ Universal Accessibility */}
                            <div className="card-neurodivergent">
                                <div className="text-4xl mb-4">♿</div>
                                <h4 className="text-xl font-semibold mb-3 text-gray-900 dark:text-white">
                                    Universal Accessibility
                                </h4>
                                <p className="text-gray-600 dark:text-gray-300 mb-4">
                                    WCAG 2.1 AAA compliance with comprehensive accessibility features.
                                </p>
                                <NeurodivergentButton
                                    onClick={() => updateSetting('cognitiveSupport', true)}
                                    variant="warning"
                                    size="small"
                                    cognitiveHint="Open accessibility settings panel"
                                >
                                    Accessibility Settings
                                </NeurodivergentButton>
                            </div>
                        </div>
                    </section>

                    {/* 🚀 Status Dashboard */}
                    <section className="py-12">
                        <div className="bg-white dark:bg-gray-800 rounded-lg shadow-lg p-8">
                            <h3 className="text-2xl font-bold text-center text-gray-900 dark:text-white mb-8">
                                🏆 Empire Status Dashboard
                            </h3>

                            <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
                                {/* Health Status */}
                                <div className="text-center">
                                    <div className="text-3xl font-bold text-calm-green mb-2">97.4%</div>
                                    <div className="text-sm text-gray-600 dark:text-gray-300">Empire Health</div>
                                </div>

                                {/* Active Users */}
                                <div className="text-center">
                                    <div className="text-3xl font-bold text-hyperfocus-blue mb-2">1.1B</div>
                                    <div className="text-sm text-gray-600 dark:text-gray-300">Neurodivergent Users</div>
                                </div>

                                {/* Features Active */}
                                <div className="text-center">
                                    <div className="text-3xl font-bold text-focus-purple mb-2">20+</div>
                                    <div className="text-sm text-gray-600 dark:text-gray-300">A11y Features</div>
                                </div>

                                {/* Performance */}
                                <div className="text-center">
                                    <div className="text-3xl font-bold text-energy-orange mb-2">&lt;1s</div>
                                    <div className="text-sm text-gray-600 dark:text-gray-300">Load Time</div>
                                </div>
                            </div>
                        </div>
                    </section>

                    {/* 🎨 Accessibility Settings Panel */}
                    {state.cognitiveSupport && (
                        <section className="py-8">
                            <div className="bg-blue-50 dark:bg-blue-900 rounded-lg p-6 border border-blue-200 dark:border-blue-700">
                                <h3 className="text-xl font-semibold text-blue-900 dark:text-blue-100 mb-4">
                                    🛠️ Accessibility Settings
                                </h3>

                                <div className="grid grid-cols-1 sm:grid-cols-2 gap-4">
                                    <label className="flex items-center space-x-3">
                                        <input
                                            type="checkbox"
                                            checked={state.adhdMode}
                                            onChange={(e) => updateSetting('adhdMode', e.target.checked)}
                                            className="w-4 h-4 text-hyperfocus-blue focus:ring-2 focus:ring-hyperfocus-blue rounded"
                                        />
                                        <span className="text-blue-900 dark:text-blue-100">🎯 ADHD Mode</span>
                                    </label>

                                    <label className="flex items-center space-x-3">
                                        <input
                                            type="checkbox"
                                            checked={state.autismMode}
                                            onChange={(e) => updateSetting('autismMode', e.target.checked)}
                                            className="w-4 h-4 text-calm-green focus:ring-2 focus:ring-calm-green rounded"
                                        />
                                        <span className="text-blue-900 dark:text-blue-100">🌈 Autism Mode</span>
                                    </label>

                                    <label className="flex items-center space-x-3">
                                        <input
                                            type="checkbox"
                                            checked={state.reducedMotion}
                                            onChange={(e) => updateSetting('reducedMotion', e.target.checked)}
                                            className="w-4 h-4 text-gentle-gray focus:ring-2 focus:ring-gentle-gray rounded"
                                        />
                                        <span className="text-blue-900 dark:text-blue-100">⏱️ Reduced Motion</span>
                                    </label>

                                    <label className="flex items-center space-x-3">
                                        <input
                                            type="checkbox"
                                            checked={state.highContrast}
                                            onChange={(e) => updateSetting('highContrast', e.target.checked)}
                                            className="w-4 h-4 text-gray-900 focus:ring-2 focus:ring-gray-900 rounded"
                                        />
                                        <span className="text-blue-900 dark:text-blue-100">🎨 High Contrast</span>
                                    </label>
                                </div>

                                <div className="mt-4 pt-4 border-t border-blue-200 dark:border-blue-700">
                                    <NeurodivergentButton
                                        onClick={() => updateSetting('cognitiveSupport', false)}
                                        variant="minimal"
                                        size="small"
                                        cognitiveHint="Close accessibility settings"
                                    >
                                        ✅ Apply Settings
                                    </NeurodivergentButton>
                                </div>
                            </div>
                        </section>
                    )}
                </div>
            </main>

            {/* 🦶 Footer */}
            <footer className="bg-gray-800 text-white py-8">
                <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 text-center">
                    <p className="text-gray-300">
                        🚀💎⚡ HYPERFOCUS ZONE Empire - Empowering 1.1 billion neurodivergent minds ⚡💎🚀
                    </p>
                    <p className="text-gray-400 text-sm mt-2">
                        Built with ❤️ for the neurodivergent community
                    </p>
                </div>
            </footer>
        </>
    );
}
