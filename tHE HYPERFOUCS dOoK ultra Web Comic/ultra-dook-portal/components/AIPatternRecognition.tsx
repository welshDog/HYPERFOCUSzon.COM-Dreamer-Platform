'use client';

import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
    Brain,
    Zap,
    TrendingUp,
    Activity,
    Target,
    Lightbulb,
    AlertTriangle,
    CheckCircle,
    BarChart3,
    Network,
    Cpu,
    Eye
} from 'lucide-react';

interface PatternData {
    id: string;
    type: 'behavioral' | 'cognitive' | 'performance' | 'predictive';
    pattern: string;
    confidence: number;
    impact: 'low' | 'medium' | 'high' | 'critical';
    timestamp: Date;
    recommendation: string;
}

interface AIInsight {
    id: string;
    title: string;
    insight: string;
    accuracy: number;
    category: 'optimization' | 'warning' | 'opportunity' | 'prediction';
    actionable: boolean;
}

const AIPatternRecognition: React.FC = () => {
    const [activeTab, setActiveTab] = useState<'patterns' | 'insights' | 'analytics' | 'predictions'>('patterns');
    const [patterns, setPatterns] = useState<PatternData[]>([]);
    const [insights, setInsights] = useState<AIInsight[]>([]);
    const [isAnalyzing, setIsAnalyzing] = useState(false);
    const [recognitionMetrics, setRecognitionMetrics] = useState({
        accuracy: 97.8,
        patternsDetected: 1247,
        insightsGenerated: 89,
        predictiveAccuracy: 94.2
    });

    useEffect(() => {
        // Simulate real-time pattern detection
        const interval = setInterval(() => {
            generateMockPattern();
        }, 3000);

        // Initialize with sample data
        initializeSampleData();

        return () => clearInterval(interval);
    }, []);

    const initializeSampleData = () => {
        const samplePatterns: PatternData[] = [
            {
                id: '1',
                type: 'behavioral',
                pattern: 'Hyperfocus periods increase 340% when quantum memory crystals are active',
                confidence: 98.7,
                impact: 'critical',
                timestamp: new Date(),
                recommendation: 'Optimize quantum crystal timing for maximum productivity'
            },
            {
                id: '2',
                type: 'cognitive',
                pattern: 'Decision-making improves 89% with visual dopamine feedback loops',
                confidence: 94.2,
                impact: 'high',
                timestamp: new Date(),
                recommendation: 'Enhance visual feedback systems across all interfaces'
            },
            {
                id: '3',
                type: 'performance',
                pattern: 'Memory retention peaks during 42-minute hyperfocus sessions',
                confidence: 91.5,
                impact: 'high',
                timestamp: new Date(),
                recommendation: 'Implement 42-minute work blocks with strategic breaks'
            }
        ];

        const sampleInsights: AIInsight[] = [
            {
                id: '1',
                title: 'ADHD Flow State Optimization',
                insight: 'Your productivity spikes 340% when combining quantum crystals with visual progress tracking',
                accuracy: 97.8,
                category: 'optimization',
                actionable: true
            },
            {
                id: '2',
                title: 'Cognitive Load Prediction',
                insight: 'High cognitive load detected in 15 minutes - recommend dopamine break',
                accuracy: 89.3,
                category: 'prediction',
                actionable: true
            },
            {
                id: '3',
                title: 'Global Expansion Opportunity',
                insight: 'Pattern indicates 89% success probability for European market entry',
                accuracy: 92.7,
                category: 'opportunity',
                actionable: true
            }
        ];

        setPatterns(samplePatterns);
        setInsights(sampleInsights);
    };

    const generateMockPattern = () => {
        const types: PatternData['type'][] = ['behavioral', 'cognitive', 'performance', 'predictive'];
        const impacts: PatternData['impact'][] = ['low', 'medium', 'high', 'critical'];

        const patternExamples = [
            'Agent coordination efficiency increases 67% during quantum synchronization',
            'Memory crystal formation accelerates with emotional engagement patterns',
            'ADHD brain responds 234% better to gamified feedback systems',
            'Hyperfocus duration extends 89% with optimal dopamine architecture',
            'Strategic decisions improve 78% with AI pattern recognition active'
        ];

        const newPattern: PatternData = {
            id: Date.now().toString(),
            type: types[Math.floor(Math.random() * types.length)],
            pattern: patternExamples[Math.floor(Math.random() * patternExamples.length)],
            confidence: 85 + Math.random() * 15,
            impact: impacts[Math.floor(Math.random() * impacts.length)],
            timestamp: new Date(),
            recommendation: 'AI recommends implementing this pattern for optimal performance'
        };

        setPatterns(prev => [newPattern, ...prev.slice(0, 9)]);

        // Update metrics
        setRecognitionMetrics(prev => ({
            ...prev,
            patternsDetected: prev.patternsDetected + 1,
            accuracy: 85 + Math.random() * 15
        }));
    };

    const runAnalysis = async () => {
        setIsAnalyzing(true);

        // Simulate AI analysis
        setTimeout(() => {
            setIsAnalyzing(false);
            generateMockPattern();

            // Generate new insight
            const newInsight: AIInsight = {
                id: Date.now().toString(),
                title: 'Fresh AI Insight',
                insight: 'Analysis complete: New optimization opportunity detected with 94.7% confidence',
                accuracy: 94.7,
                category: 'optimization',
                actionable: true
            };

            setInsights(prev => [newInsight, ...prev.slice(0, 4)]);
            setRecognitionMetrics(prev => ({
                ...prev,
                insightsGenerated: prev.insightsGenerated + 1
            }));
        }, 2000);
    };

    const getImpactColor = (impact: PatternData['impact']) => {
        switch (impact) {
            case 'critical': return 'text-red-400 bg-red-500/20 border-red-500';
            case 'high': return 'text-orange-400 bg-orange-500/20 border-orange-500';
            case 'medium': return 'text-yellow-400 bg-yellow-500/20 border-yellow-500';
            case 'low': return 'text-blue-400 bg-blue-500/20 border-blue-500';
        }
    };

    const getCategoryIcon = (category: AIInsight['category']) => {
        switch (category) {
            case 'optimization': return <TrendingUp className="w-5 h-5" />;
            case 'warning': return <AlertTriangle className="w-5 h-5" />;
            case 'opportunity': return <Lightbulb className="w-5 h-5" />;
            case 'prediction': return <Eye className="w-5 h-5" />;
        }
    };

    return (
        <div className="min-h-screen bg-gradient-to-br from-purple-900 via-blue-900 to-indigo-900 p-6">
            <div className="max-w-6xl mx-auto">

                {/* Header */}
                <motion.div
                    initial={{ opacity: 0, y: -20 }}
                    animate={{ opacity: 1, y: 0 }}
                    className="mb-8"
                >
                    <div className="flex items-center gap-4 mb-4">
                        <div className="relative">
                            <Brain className="w-12 h-12 text-cyan-400" />
                            <motion.div
                                animate={{ rotate: 360 }}
                                transition={{ duration: 4, repeat: Infinity, ease: 'linear' }}
                                className="absolute -top-1 -right-1"
                            >
                                <Zap className="w-6 h-6 text-yellow-400" />
                            </motion.div>
                        </div>
                        <div>
                            <h1 className="text-4xl font-bold bg-gradient-to-r from-cyan-400 via-purple-400 to-pink-400 bg-clip-text text-transparent">
                                AI Pattern Recognition Engine
                            </h1>
                            <p className="text-gray-300 text-lg">
                                Advanced intelligence amplification through predictive pattern analysis
                            </p>
                        </div>
                    </div>

                    {/* Metrics Dashboard */}
                    <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                        {[
                            { label: 'Recognition Accuracy', value: `${recognitionMetrics.accuracy.toFixed(1)}%`, icon: Target, color: 'text-green-400' },
                            { label: 'Patterns Detected', value: recognitionMetrics.patternsDetected, icon: Network, color: 'text-blue-400' },
                            { label: 'Insights Generated', value: recognitionMetrics.insightsGenerated, icon: Lightbulb, color: 'text-yellow-400' },
                            { label: 'Predictive Accuracy', value: `${recognitionMetrics.predictiveAccuracy.toFixed(1)}%`, icon: Eye, color: 'text-purple-400' }
                        ].map((metric, index) => (
                            <motion.div
                                key={index}
                                initial={{ opacity: 0, scale: 0.9 }}
                                animate={{ opacity: 1, scale: 1 }}
                                transition={{ delay: index * 0.1 }}
                                className="bg-white/10 backdrop-blur-md rounded-xl p-4 border border-white/20"
                            >
                                <div className="flex items-center gap-3">
                                    <metric.icon className={`w-6 h-6 ${metric.color}`} />
                                    <div>
                                        <div className={`text-xl font-bold ${metric.color}`}>{metric.value}</div>
                                        <div className="text-gray-300 text-sm">{metric.label}</div>
                                    </div>
                                </div>
                            </motion.div>
                        ))}
                    </div>
                </motion.div>

                {/* Navigation Tabs */}
                <div className="flex flex-wrap gap-2 mb-6">
                    {[
                        { id: 'patterns', label: 'Pattern Detection', icon: Activity },
                        { id: 'insights', label: 'AI Insights', icon: Brain },
                        { id: 'analytics', label: 'Analytics', icon: BarChart3 },
                        { id: 'predictions', label: 'Predictions', icon: Eye }
                    ].map((tab) => (
                        <motion.button
                            key={tab.id}
                            onClick={() => setActiveTab(tab.id as typeof activeTab)}
                            className={`flex items-center gap-2 px-4 py-2 rounded-lg transition-all ${activeTab === tab.id
                                    ? 'bg-gradient-to-r from-purple-600 to-blue-600 text-white shadow-lg'
                                    : 'bg-white/10 text-gray-300 hover:bg-white/20'
                                }`}
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                        >
                            <tab.icon className="w-4 h-4" />
                            {tab.label}
                        </motion.button>
                    ))}
                </div>

                {/* Content Area */}
                <AnimatePresence mode="wait">
                    <motion.div
                        key={activeTab}
                        initial={{ opacity: 0, x: 20 }}
                        animate={{ opacity: 1, x: 0 }}
                        exit={{ opacity: 0, x: -20 }}
                        transition={{ duration: 0.3 }}
                    >

                        {/* Pattern Detection Tab */}
                        {activeTab === 'patterns' && (
                            <div className="space-y-6">
                                <div className="flex justify-between items-center">
                                    <h2 className="text-2xl font-bold text-white">Real-Time Pattern Detection</h2>
                                    <motion.button
                                        onClick={runAnalysis}
                                        disabled={isAnalyzing}
                                        className="flex items-center gap-2 px-6 py-3 bg-gradient-to-r from-green-600 to-blue-600 text-white rounded-lg hover:shadow-lg transition-all disabled:opacity-50"
                                        whileHover={{ scale: 1.02 }}
                                        whileTap={{ scale: 0.98 }}
                                    >
                                        {isAnalyzing ? (
                                            <>
                                                <motion.div
                                                    animate={{ rotate: 360 }}
                                                    transition={{ duration: 1, repeat: Infinity, ease: 'linear' }}
                                                >
                                                    <Cpu className="w-5 h-5" />
                                                </motion.div>
                                                Analyzing...
                                            </>
                                        ) : (
                                            <>
                                                <Brain className="w-5 h-5" />
                                                Run Deep Analysis
                                            </>
                                        )}
                                    </motion.button>
                                </div>

                                <div className="grid gap-4">
                                    {patterns.map((pattern, index) => (
                                        <motion.div
                                            key={pattern.id}
                                            initial={{ opacity: 0, y: 20 }}
                                            animate={{ opacity: 1, y: 0 }}
                                            transition={{ delay: index * 0.1 }}
                                            className="bg-white/10 backdrop-blur-md rounded-xl p-6 border border-white/20 hover:border-purple-400/50 transition-all"
                                        >
                                            <div className="flex justify-between items-start mb-4">
                                                <div className="flex items-center gap-3">
                                                    <div className={`px-3 py-1 rounded-full text-xs font-medium ${getImpactColor(pattern.impact)} border`}>
                                                        {pattern.impact.toUpperCase()} IMPACT
                                                    </div>
                                                    <div className="text-gray-400 text-sm">
                                                        {pattern.type.charAt(0).toUpperCase() + pattern.type.slice(1)} Pattern
                                                    </div>
                                                </div>
                                                <div className="text-green-400 font-bold">
                                                    {pattern.confidence.toFixed(1)}% confidence
                                                </div>
                                            </div>

                                            <p className="text-white text-lg mb-3">{pattern.pattern}</p>

                                            <div className="flex justify-between items-center">
                                                <p className="text-gray-300 text-sm italic">
                                                    💡 {pattern.recommendation}
                                                </p>
                                                <span className="text-gray-400 text-xs">
                                                    {pattern.timestamp.toLocaleTimeString()}
                                                </span>
                                            </div>
                                        </motion.div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {/* AI Insights Tab */}
                        {activeTab === 'insights' && (
                            <div className="space-y-6">
                                <h2 className="text-2xl font-bold text-white">AI-Generated Insights</h2>

                                <div className="grid gap-4">
                                    {insights.map((insight, index) => (
                                        <motion.div
                                            key={insight.id}
                                            initial={{ opacity: 0, x: -20 }}
                                            animate={{ opacity: 1, x: 0 }}
                                            transition={{ delay: index * 0.1 }}
                                            className="bg-white/10 backdrop-blur-md rounded-xl p-6 border border-white/20 hover:border-cyan-400/50 transition-all"
                                        >
                                            <div className="flex items-start gap-4">
                                                <div className="p-3 bg-gradient-to-r from-purple-600 to-blue-600 rounded-lg">
                                                    {getCategoryIcon(insight.category)}
                                                </div>
                                                <div className="flex-1">
                                                    <div className="flex justify-between items-start mb-2">
                                                        <h3 className="text-xl font-bold text-white">{insight.title}</h3>
                                                        <div className="flex items-center gap-2">
                                                            <div className="text-green-400 font-bold text-sm">
                                                                {insight.accuracy.toFixed(1)}% accurate
                                                            </div>
                                                            {insight.actionable && (
                                                                <CheckCircle className="w-5 h-5 text-green-400" />
                                                            )}
                                                        </div>
                                                    </div>
                                                    <p className="text-gray-300 mb-3">{insight.insight}</p>
                                                    <div className="flex items-center gap-2">
                                                        <span className={`px-3 py-1 rounded-full text-xs font-medium ${insight.category === 'optimization' ? 'bg-green-500/20 text-green-400 border border-green-500' :
                                                                insight.category === 'warning' ? 'bg-red-500/20 text-red-400 border border-red-500' :
                                                                    insight.category === 'opportunity' ? 'bg-yellow-500/20 text-yellow-400 border border-yellow-500' :
                                                                        'bg-purple-500/20 text-purple-400 border border-purple-500'
                                                            }`}>
                                                            {insight.category.toUpperCase()}
                                                        </span>
                                                        {insight.actionable && (
                                                            <motion.button
                                                                className="px-4 py-1 bg-gradient-to-r from-blue-600 to-purple-600 text-white rounded-lg text-sm hover:shadow-lg transition-all"
                                                                whileHover={{ scale: 1.02 }}
                                                                whileTap={{ scale: 0.98 }}
                                                            >
                                                                Take Action
                                                            </motion.button>
                                                        )}
                                                    </div>
                                                </div>
                                            </div>
                                        </motion.div>
                                    ))}
                                </div>
                            </div>
                        )}

                        {/* Analytics Tab */}
                        {activeTab === 'analytics' && (
                            <div className="space-y-6">
                                <h2 className="text-2xl font-bold text-white">Pattern Analytics</h2>

                                <div className="grid md:grid-cols-2 gap-6">
                                    <div className="bg-white/10 backdrop-blur-md rounded-xl p-6 border border-white/20">
                                        <h3 className="text-xl font-bold text-white mb-4">Recognition Performance</h3>
                                        <div className="space-y-4">
                                            {[
                                                { label: 'ADHD Pattern Detection', value: 97.8, color: 'from-green-500 to-green-600' },
                                                { label: 'Behavioral Analysis', value: 94.2, color: 'from-blue-500 to-blue-600' },
                                                { label: 'Cognitive Load Prediction', value: 91.5, color: 'from-purple-500 to-purple-600' },
                                                { label: 'Performance Optimization', value: 89.3, color: 'from-yellow-500 to-yellow-600' }
                                            ].map((metric, index) => (
                                                <div key={index}>
                                                    <div className="flex justify-between mb-2">
                                                        <span className="text-gray-300">{metric.label}</span>
                                                        <span className="text-white font-bold">{metric.value}%</span>
                                                    </div>
                                                    <div className="w-full bg-gray-700 rounded-full h-2">
                                                        <motion.div
                                                            initial={{ width: 0 }}
                                                            animate={{ width: `${metric.value}%` }}
                                                            transition={{ duration: 1.5, delay: index * 0.2 }}
                                                            className={`h-2 rounded-full bg-gradient-to-r ${metric.color}`}
                                                        />
                                                    </div>
                                                </div>
                                            ))}
                                        </div>
                                    </div>

                                    <div className="bg-white/10 backdrop-blur-md rounded-xl p-6 border border-white/20">
                                        <h3 className="text-xl font-bold text-white mb-4">Pattern Distribution</h3>
                                        <div className="space-y-3">
                                            {[
                                                { type: 'Behavioral', count: 342, color: 'text-blue-400' },
                                                { type: 'Cognitive', count: 298, color: 'text-purple-400' },
                                                { type: 'Performance', count: 264, color: 'text-green-400' },
                                                { type: 'Predictive', count: 187, color: 'text-yellow-400' }
                                            ].map((item, index) => (
                                                <div key={index} className="flex justify-between items-center">
                                                    <span className="text-gray-300">{item.type} Patterns</span>
                                                    <span className={`font-bold ${item.color}`}>{item.count}</span>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                </div>
                            </div>
                        )}

                        {/* Predictions Tab */}
                        {activeTab === 'predictions' && (
                            <div className="space-y-6">
                                <h2 className="text-2xl font-bold text-white">Predictive Intelligence</h2>

                                <div className="grid gap-4">
                                    {[
                                        {
                                            title: 'Hyperfocus Session Optimization',
                                            prediction: 'Next optimal session: 42 minutes starting in 18 minutes',
                                            confidence: 96.7,
                                            timeframe: '15-30 minutes',
                                            impact: 'High productivity boost expected'
                                        },
                                        {
                                            title: 'Cognitive Load Management',
                                            prediction: 'Mental fatigue threshold approaching in 23 minutes',
                                            confidence: 89.2,
                                            timeframe: '20-25 minutes',
                                            impact: 'Recommend dopamine break before threshold'
                                        },
                                        {
                                            title: 'Memory Crystal Formation',
                                            prediction: 'Optimal crystal creation window opening in 1.2 hours',
                                            confidence: 92.4,
                                            timeframe: '1-2 hours',
                                            impact: 'Enhanced memory retention opportunity'
                                        }
                                    ].map((prediction, index) => (
                                        <motion.div
                                            key={index}
                                            initial={{ opacity: 0, y: 20 }}
                                            animate={{ opacity: 1, y: 0 }}
                                            transition={{ delay: index * 0.2 }}
                                            className="bg-white/10 backdrop-blur-md rounded-xl p-6 border border-white/20 hover:border-cyan-400/50 transition-all"
                                        >
                                            <div className="flex justify-between items-start mb-4">
                                                <h3 className="text-xl font-bold text-white">{prediction.title}</h3>
                                                <div className="text-green-400 font-bold">{prediction.confidence}%</div>
                                            </div>
                                            <p className="text-gray-300 mb-3">{prediction.prediction}</p>
                                            <div className="flex justify-between items-center">
                                                <span className="text-purple-400 text-sm">⏰ {prediction.timeframe}</span>
                                                <span className="text-yellow-400 text-sm">💡 {prediction.impact}</span>
                                            </div>
                                        </motion.div>
                                    ))}
                                </div>
                            </div>
                        )}

                    </motion.div>
                </AnimatePresence>
            </div>
        </div>
    );
};

export default AIPatternRecognition;
