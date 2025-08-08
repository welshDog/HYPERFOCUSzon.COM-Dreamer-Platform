'use client'

import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import {
    Brain,
    TrendingUp,
    Target,
    Zap,
    Eye,
    Activity,
    BarChart3,
    PieChart,
    LineChart,
    Radar,
    AlertTriangle,
    CheckCircle,
    Clock,
    Star,
    Lightbulb,
    ArrowUp,
    ArrowDown,
    Minus
} from 'lucide-react'

interface PatternData {
    id: string
    name: string
    type: 'success' | 'optimization' | 'risk' | 'opportunity'
    confidence: number
    impact: 'high' | 'medium' | 'low'
    trend: 'increasing' | 'decreasing' | 'stable'
    description: string
    recommendations: string[]
    related_crystals: string[]
    prediction_accuracy: number
    last_updated: string
}

interface PredictiveModel {
    model_name: string
    accuracy: number
    predictions: Array<{
        category: string
        outcome: string
        probability: number
        timeframe: string
        factors: string[]
    }>
}

interface IntelligenceMetrics {
    pattern_detection_rate: number
    prediction_accuracy: number
    decision_optimization: number
    learning_velocity: number
    system_intelligence_quotient: number
}

export default function AIPatternRecognition() {
    const [patterns, setPatterns] = useState<PatternData[]>([])
    const [predictiveModels, setPredictiveModels] = useState<PredictiveModel[]>([])
    const [metrics, setMetrics] = useState<IntelligenceMetrics | null>(null)
    const [selectedPattern, setSelectedPattern] = useState<string | null>(null)
    const [isAnalyzing, setIsAnalyzing] = useState(false)
    const [activeView, setActiveView] = useState<'patterns' | 'predictions' | 'intelligence'>('patterns')

    // Simulate AI pattern analysis
    useEffect(() => {
        const runPatternAnalysis = () => {
            setIsAnalyzing(true)

            setTimeout(() => {
                const mockPatterns: PatternData[] = [
                    {
                        id: 'pattern_001',
                        name: 'Legendary Enhancement Cascade',
                        type: 'success',
                        confidence: 0.94,
                        impact: 'high',
                        trend: 'increasing',
                        description: 'System shows consistent pattern of compound enhancement success when combining multiple advanced features simultaneously.',
                        recommendations: [
                            'Continue multi-system integration approach',
                            'Scale enhancement sequences to 4-5 simultaneous systems',
                            'Implement automated cascade triggers'
                        ],
                        related_crystals: ['quantum_12345', 'quantum_67890'],
                        prediction_accuracy: 0.87,
                        last_updated: '2025-08-04T11:30:00Z'
                    },
                    {
                        id: 'pattern_002',
                        name: 'ADHD Optimization Amplification',
                        type: 'optimization',
                        confidence: 0.91,
                        impact: 'high',
                        trend: 'increasing',
                        description: 'Neurodivergent-focused design patterns consistently deliver 3x higher engagement and 2.5x better retention rates.',
                        recommendations: [
                            'Apply ADHD optimization principles to all new features',
                            'Develop adaptive UI based on user attention patterns',
                            'Create personalized dopamine reward algorithms'
                        ],
                        related_crystals: ['quantum_67890'],
                        prediction_accuracy: 0.92,
                        last_updated: '2025-08-04T11:25:00Z'
                    },
                    {
                        id: 'pattern_003',
                        name: 'Agent Coordination Scaling Threshold',
                        type: 'risk',
                        confidence: 0.78,
                        impact: 'medium',
                        trend: 'stable',
                        description: 'Performance optimization becomes critical when agent count exceeds 800+ units. Proactive scaling required.',
                        recommendations: [
                            'Implement predictive load balancing at 750+ agents',
                            'Deploy regional agent distribution architecture',
                            'Create agent performance monitoring dashboard'
                        ],
                        related_crystals: ['quantum_11111'],
                        prediction_accuracy: 0.83,
                        last_updated: '2025-08-04T11:20:00Z'
                    },
                    {
                        id: 'pattern_004',
                        name: 'Quantum Memory Crystal Fusion Potential',
                        type: 'opportunity',
                        confidence: 0.89,
                        impact: 'high',
                        trend: 'increasing',
                        description: 'Cross-crystal pattern analysis reveals opportunity for creating super-crystals with 10x enhanced knowledge capacity.',
                        recommendations: [
                            'Develop quantum crystal fusion laboratory',
                            'Create AI-guided fusion recommendations',
                            'Implement community crystal sharing network'
                        ],
                        related_crystals: ['quantum_12345', 'quantum_67890', 'quantum_11111'],
                        prediction_accuracy: 0.91,
                        last_updated: '2025-08-04T11:35:00Z'
                    }
                ]

                const mockPredictiveModels: PredictiveModel[] = [
                    {
                        model_name: 'Success Pattern Predictor',
                        accuracy: 0.87,
                        predictions: [
                            {
                                category: 'Enhancement Success',
                                outcome: 'Next 5-system integration will achieve 95%+ success rate',
                                probability: 0.89,
                                timeframe: '1-2 weeks',
                                factors: ['proven cascade pattern', 'team coordination', 'infrastructure readiness']
                            },
                            {
                                category: 'Revenue Growth',
                                outcome: 'Monthly revenue will exceed $2M with global expansion',
                                probability: 0.82,
                                timeframe: '2-3 months',
                                factors: ['premium service demand', 'international scaling', 'agent army growth']
                            }
                        ]
                    },
                    {
                        model_name: 'Risk Assessment Engine',
                        accuracy: 0.83,
                        predictions: [
                            {
                                category: 'System Bottlenecks',
                                outcome: 'Performance degradation likely at 1000+ agents without optimization',
                                probability: 0.78,
                                timeframe: '3-4 weeks',
                                factors: ['current growth rate', 'resource allocation', 'scaling patterns']
                            },
                            {
                                category: 'User Engagement',
                                outcome: 'ADHD optimization features will drive 300% engagement increase',
                                probability: 0.92,
                                timeframe: '1-2 weeks',
                                factors: ['dopamine architecture success', 'user feedback patterns', 'neurodivergent focus']
                            }
                        ]
                    }
                ]

                const mockMetrics: IntelligenceMetrics = {
                    pattern_detection_rate: 0.89,
                    prediction_accuracy: 0.85,
                    decision_optimization: 0.92,
                    learning_velocity: 0.88,
                    system_intelligence_quotient: 0.90
                }

                setPatterns(mockPatterns)
                setPredictiveModels(mockPredictiveModels)
                setMetrics(mockMetrics)
                setIsAnalyzing(false)
            }, 2000)
        }

        runPatternAnalysis()
    }, [])

    const getPatternColor = (type: string, trend: string) => {
        const baseColors = {
            success: 'from-green-400 to-emerald-500',
            optimization: 'from-blue-400 to-cyan-500',
            risk: 'from-red-400 to-orange-500',
            opportunity: 'from-purple-400 to-pink-500'
        }
        return baseColors[type as keyof typeof baseColors] || 'from-gray-400 to-gray-500'
    }

    const getPatternIcon = (type: string) => {
        const icons = {
            success: CheckCircle,
            optimization: TrendingUp,
            risk: AlertTriangle,
            opportunity: Lightbulb
        }
        return icons[type as keyof typeof icons] || Target
    }

    const getTrendIcon = (trend: string) => {
        const icons = {
            increasing: ArrowUp,
            decreasing: ArrowDown,
            stable: Minus
        }
        return icons[trend as keyof typeof icons] || Minus
    }

    const renderPatternsView = () => (
        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
            {patterns.map((pattern) => {
                const PatternIcon = getPatternIcon(pattern.type)
                const TrendIcon = getTrendIcon(pattern.trend)

                return (
                    <motion.div
                        key={pattern.id}
                        layoutId={pattern.id}
                        className={`bg-gradient-to-br from-slate-800/80 to-slate-900/80 backdrop-blur-sm 
                       border-2 border-gray-600 rounded-xl p-6 cursor-pointer transition-all duration-300
                       hover:scale-105 hover:shadow-2xl hover:border-cyan-400/50`}
                        onClick={() => setSelectedPattern(selectedPattern === pattern.id ? null : pattern.id)}
                        whileHover={{ y: -5 }}
                        whileTap={{ scale: 0.95 }}
                    >
                        {/* Pattern Header */}
                        <div className="flex items-start justify-between mb-4">
                            <div className="flex items-center space-x-3">
                                <motion.div
                                    className={`p-3 rounded-full bg-gradient-to-br ${getPatternColor(pattern.type, pattern.trend)}`}
                                    whileHover={{ rotate: 360 }}
                                    transition={{ duration: 0.5 }}
                                >
                                    <PatternIcon className="w-6 h-6 text-white" />
                                </motion.div>
                                <div>
                                    <h3 className="text-lg font-bold text-white mb-1">
                                        {pattern.name}
                                    </h3>
                                    <div className="flex items-center space-x-2">
                                        <span className={`px-2 py-1 rounded text-xs font-semibold capitalize bg-gradient-to-r ${getPatternColor(pattern.type, pattern.trend)} text-white`}>
                                            {pattern.type}
                                        </span>
                                        <div className="flex items-center space-x-1 text-gray-400">
                                            <TrendIcon className="w-4 h-4" />
                                            <span className="text-xs">{pattern.trend}</span>
                                        </div>
                                    </div>
                                </div>
                            </div>
                            <div className="text-right">
                                <div className="text-xs text-gray-400 mb-1">Confidence</div>
                                <div className="text-xl font-bold text-cyan-400">
                                    {(pattern.confidence * 100).toFixed(0)}%
                                </div>
                            </div>
                        </div>

                        {/* Metrics */}
                        <div className="grid grid-cols-3 gap-4 mb-4">
                            <div className="text-center">
                                <div className="text-xs text-gray-400 mb-1">Impact</div>
                                <div className={`text-sm font-semibold ${pattern.impact === 'high' ? 'text-red-400' :
                                        pattern.impact === 'medium' ? 'text-yellow-400' : 'text-green-400'
                                    }`}>
                                    {pattern.impact.toUpperCase()}
                                </div>
                            </div>
                            <div className="text-center">
                                <div className="text-xs text-gray-400 mb-1">Accuracy</div>
                                <div className="text-sm font-semibold text-purple-400">
                                    {(pattern.prediction_accuracy * 100).toFixed(0)}%
                                </div>
                            </div>
                            <div className="text-center">
                                <div className="text-xs text-gray-400 mb-1">Crystals</div>
                                <div className="text-sm font-semibold text-blue-400">
                                    {pattern.related_crystals.length}
                                </div>
                            </div>
                        </div>

                        {/* Description */}
                        <p className="text-gray-300 text-sm mb-4 line-clamp-3">
                            {pattern.description}
                        </p>

                        {/* Expanded Content */}
                        <AnimatePresence>
                            {selectedPattern === pattern.id && (
                                <motion.div
                                    initial={{ opacity: 0, height: 0 }}
                                    animate={{ opacity: 1, height: 'auto' }}
                                    exit={{ opacity: 0, height: 0 }}
                                    className="mt-6 pt-6 border-t border-gray-600"
                                >
                                    <h4 className="text-sm font-semibold text-cyan-400 mb-3">AI Recommendations</h4>
                                    <div className="space-y-2 mb-4">
                                        {pattern.recommendations.map((rec, idx) => (
                                            <motion.div
                                                key={idx}
                                                initial={{ opacity: 0, x: -20 }}
                                                animate={{ opacity: 1, x: 0 }}
                                                transition={{ delay: idx * 0.1 }}
                                                className="flex items-start space-x-2 text-sm"
                                            >
                                                <CheckCircle className="w-4 h-4 text-green-400 mt-0.5 flex-shrink-0" />
                                                <span className="text-gray-300">{rec}</span>
                                            </motion.div>
                                        ))}
                                    </div>

                                    <div className="flex items-center justify-between text-xs text-gray-400">
                                        <span>Last Updated: {new Date(pattern.last_updated).toLocaleString()}</span>
                                        <span>Pattern ID: {pattern.id}</span>
                                    </div>
                                </motion.div>
                            )}
                        </AnimatePresence>
                    </motion.div>
                )
            })}
        </div>
    )

    const renderPredictionsView = () => (
        <div className="space-y-6">
            {predictiveModels.map((model, modelIdx) => (
                <motion.div
                    key={model.model_name}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    transition={{ delay: modelIdx * 0.1 }}
                    className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600"
                >
                    <div className="flex items-center justify-between mb-6">
                        <div className="flex items-center space-x-3">
                            <Brain className="w-8 h-8 text-purple-400" />
                            <div>
                                <h3 className="text-xl font-bold text-white">{model.model_name}</h3>
                                <p className="text-gray-400 text-sm">Predictive AI Model</p>
                            </div>
                        </div>
                        <div className="text-right">
                            <div className="text-xs text-gray-400 mb-1">Model Accuracy</div>
                            <div className="text-2xl font-bold text-green-400">
                                {(model.accuracy * 100).toFixed(0)}%
                            </div>
                        </div>
                    </div>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                        {model.predictions.map((prediction, idx) => (
                            <motion.div
                                key={idx}
                                initial={{ opacity: 0, scale: 0.9 }}
                                animate={{ opacity: 1, scale: 1 }}
                                transition={{ delay: (modelIdx * 0.5) + (idx * 0.1) }}
                                className="bg-slate-700/50 rounded-lg p-5"
                            >
                                <div className="flex items-center justify-between mb-3">
                                    <h4 className="font-semibold text-white">{prediction.category}</h4>
                                    <span className={`px-2 py-1 rounded text-xs font-semibold ${prediction.probability >= 0.8 ? 'bg-green-500/20 text-green-300' :
                                            prediction.probability >= 0.6 ? 'bg-yellow-500/20 text-yellow-300' :
                                                'bg-red-500/20 text-red-300'
                                        }`}>
                                        {(prediction.probability * 100).toFixed(0)}%
                                    </span>
                                </div>

                                <p className="text-gray-300 text-sm mb-4">{prediction.outcome}</p>

                                <div className="space-y-2">
                                    <div className="flex items-center justify-between text-xs">
                                        <span className="text-gray-400">Timeframe:</span>
                                        <span className="text-cyan-400">{prediction.timeframe}</span>
                                    </div>

                                    <div className="pt-2 border-t border-gray-600">
                                        <div className="text-xs text-gray-400 mb-2">Key Factors:</div>
                                        <div className="flex flex-wrap gap-1">
                                            {prediction.factors.map((factor, factorIdx) => (
                                                <span
                                                    key={factorIdx}
                                                    className="px-2 py-1 bg-blue-500/20 text-blue-300 text-xs rounded"
                                                >
                                                    {factor}
                                                </span>
                                            ))}
                                        </div>
                                    </div>
                                </div>
                            </motion.div>
                        ))}
                    </div>
                </motion.div>
            ))}
        </div>
    )

    const renderIntelligenceView = () => {
        if (!metrics) return null

        const metricItems = [
            { key: 'pattern_detection_rate', label: 'Pattern Detection', icon: Eye, color: 'text-blue-400' },
            { key: 'prediction_accuracy', label: 'Prediction Accuracy', icon: Target, color: 'text-green-400' },
            { key: 'decision_optimization', label: 'Decision Optimization', icon: TrendingUp, color: 'text-purple-400' },
            { key: 'learning_velocity', label: 'Learning Velocity', icon: Zap, color: 'text-yellow-400' },
            { key: 'system_intelligence_quotient', label: 'System IQ', icon: Brain, color: 'text-cyan-400' }
        ]

        return (
            <div className="space-y-6">
                {/* Intelligence Overview */}
                <div className="bg-gradient-to-br from-purple-900/30 to-blue-900/30 border border-purple-500/30 rounded-xl p-6">
                    <div className="flex items-center space-x-3 mb-6">
                        <Brain className="w-8 h-8 text-purple-400" />
                        <div>
                            <h3 className="text-2xl font-bold text-white">System Intelligence Quotient</h3>
                            <p className="text-gray-400">Real-time AI performance metrics and optimization analysis</p>
                        </div>
                    </div>

                    {/* Overall IQ Score */}
                    <div className="text-center mb-8">
                        <motion.div
                            className="relative w-32 h-32 mx-auto mb-4"
                            initial={{ scale: 0 }}
                            animate={{ scale: 1 }}
                            transition={{ duration: 1, type: "spring" }}
                        >
                            <svg className="w-32 h-32 transform -rotate-90" viewBox="0 0 36 36">
                                <path
                                    className="text-gray-700"
                                    stroke="currentColor"
                                    strokeWidth="3"
                                    fill="none"
                                    d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                                />
                                <motion.path
                                    className="text-purple-400"
                                    stroke="currentColor"
                                    strokeWidth="3"
                                    fill="none"
                                    strokeLinecap="round"
                                    d="M18 2.0845 a 15.9155 15.9155 0 0 1 0 31.831 a 15.9155 15.9155 0 0 1 0 -31.831"
                                    initial={{ strokeDasharray: "0 100" }}
                                    animate={{ strokeDasharray: `${metrics.system_intelligence_quotient * 100} 100` }}
                                    transition={{ duration: 2, ease: "easeOut" }}
                                />
                            </svg>
                            <div className="absolute inset-0 flex items-center justify-center">
                                <span className="text-3xl font-bold text-white">
                                    {(metrics.system_intelligence_quotient * 100).toFixed(0)}
                                </span>
                            </div>
                        </motion.div>
                        <div className="text-sm text-gray-400">System Intelligence Quotient</div>
                        <div className="text-lg font-semibold text-purple-400">LEGENDARY LEVEL</div>
                    </div>

                    {/* Detailed Metrics */}
                    <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-4">
                        {metricItems.map((item, idx) => {
                            const value = metrics[item.key as keyof IntelligenceMetrics]
                            const Icon = item.icon

                            return (
                                <motion.div
                                    key={item.key}
                                    initial={{ opacity: 0, y: 20 }}
                                    animate={{ opacity: 1, y: 0 }}
                                    transition={{ delay: idx * 0.1 }}
                                    className="bg-slate-800/50 rounded-lg p-4 text-center"
                                >
                                    <Icon className={`w-8 h-8 mx-auto mb-3 ${item.color}`} />
                                    <div className="text-2xl font-bold text-white mb-1">
                                        {(value * 100).toFixed(0)}%
                                    </div>
                                    <div className="text-xs text-gray-400">{item.label}</div>

                                    {/* Progress Bar */}
                                    <div className="mt-3 bg-gray-700 rounded-full h-2">
                                        <motion.div
                                            className={`h-2 rounded-full bg-gradient-to-r ${value >= 0.9 ? 'from-green-400 to-emerald-500' :
                                                    value >= 0.8 ? 'from-blue-400 to-cyan-500' :
                                                        value >= 0.7 ? 'from-yellow-400 to-orange-500' :
                                                            'from-red-400 to-pink-500'
                                                }`}
                                            initial={{ width: 0 }}
                                            animate={{ width: `${value * 100}%` }}
                                            transition={{ duration: 1.5, delay: idx * 0.1 }}
                                        />
                                    </div>
                                </motion.div>
                            )
                        })}
                    </div>
                </div>

                {/* Intelligence Insights */}
                <div className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600">
                    <h3 className="text-xl font-bold text-white mb-4 flex items-center space-x-2">
                        <Lightbulb className="w-6 h-6 text-yellow-400" />
                        <span>AI Intelligence Insights</span>
                    </h3>

                    <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <h4 className="font-semibold text-green-400 mb-3">🚀 Optimization Opportunities</h4>
                            <div className="space-y-2 text-sm text-gray-300">
                                <div className="flex items-start space-x-2">
                                    <CheckCircle className="w-4 h-4 text-green-400 mt-0.5 flex-shrink-0" />
                                    <span>Pattern detection rate shows 11% improvement potential through enhanced data sampling</span>
                                </div>
                                <div className="flex items-start space-x-2">
                                    <CheckCircle className="w-4 h-4 text-green-400 mt-0.5 flex-shrink-0" />
                                    <span>Learning velocity can be accelerated with parallel processing implementation</span>
                                </div>
                                <div className="flex items-start space-x-2">
                                    <CheckCircle className="w-4 h-4 text-green-400 mt-0.5 flex-shrink-0" />
                                    <span>Decision optimization shows readiness for autonomous recommendation deployment</span>
                                </div>
                            </div>
                        </div>

                        <div>
                            <h4 className="font-semibold text-blue-400 mb-3">🧠 System Intelligence Status</h4>
                            <div className="space-y-2 text-sm text-gray-300">
                                <div className="flex items-start space-x-2">
                                    <Star className="w-4 h-4 text-blue-400 mt-0.5 flex-shrink-0" />
                                    <span>Current IQ level places system in top 5% of AI coordination platforms</span>
                                </div>
                                <div className="flex items-start space-x-2">
                                    <Star className="w-4 h-4 text-blue-400 mt-0.5 flex-shrink-0" />
                                    <span>Predictive modeling accuracy exceeds industry standards by 23%</span>
                                </div>
                                <div className="flex items-start space-x-2">
                                    <Star className="w-4 h-4 text-blue-400 mt-0.5 flex-shrink-0" />
                                    <span>Multi-domain pattern recognition achieving research-level performance</span>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        )
    }

    if (isAnalyzing) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 flex items-center justify-center">
                <motion.div
                    className="text-center"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                >
                    <motion.div
                        className="relative mb-8"
                        animate={{ rotate: 360 }}
                        transition={{ duration: 2, repeat: Infinity, ease: "linear" }}
                    >
                        <Brain className="w-16 h-16 text-blue-400 mx-auto" />
                        <motion.div
                            className="absolute inset-0 w-16 h-16 border-4 border-blue-400/30 rounded-full mx-auto"
                            animate={{ scale: [1, 1.5, 1] }}
                            transition={{ duration: 1.5, repeat: Infinity }}
                        />
                    </motion.div>
                    <h2 className="text-2xl font-bold text-white mb-2">AI Pattern Analysis</h2>
                    <p className="text-gray-400">Analyzing system intelligence and predictive patterns...</p>
                    <div className="flex justify-center space-x-2 mt-4">
                        {[...Array(3)].map((_, i) => (
                            <motion.div
                                key={i}
                                className="w-2 h-2 bg-blue-400 rounded-full"
                                animate={{ opacity: [0.3, 1, 0.3] }}
                                transition={{ duration: 1, repeat: Infinity, delay: i * 0.2 }}
                            />
                        ))}
                    </div>
                </motion.div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-900 via-blue-900 to-slate-900 p-6">
            {/* Header */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="mb-8"
            >
                <div className="flex items-center space-x-4 mb-4">
                    <motion.div
                        animate={{
                            rotate: [0, 360],
                            scale: [1, 1.1, 1]
                        }}
                        transition={{
                            rotate: { duration: 20, repeat: Infinity, ease: "linear" },
                            scale: { duration: 2, repeat: Infinity }
                        }}
                    >
                        <Brain className="w-10 h-10 text-blue-400" />
                    </motion.div>
                    <div>
                        <h1 className="text-4xl font-bold text-white">
                            🧠⚡ AI Pattern Recognition Engine ⚡🧠
                        </h1>
                        <p className="text-gray-400">
                            Predictive Intelligence • Success Modeling • Decision Optimization
                        </p>
                    </div>
                </div>

                {/* Quick Stats */}
                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                    <div className="bg-slate-800/50 rounded-xl p-4 text-center">
                        <Target className="w-6 h-6 text-green-400 mx-auto mb-2" />
                        <div className="text-2xl font-bold text-white">{patterns.length}</div>
                        <div className="text-sm text-gray-400">Active Patterns</div>
                    </div>
                    <div className="bg-slate-800/50 rounded-xl p-4 text-center">
                        <TrendingUp className="w-6 h-6 text-blue-400 mx-auto mb-2" />
                        <div className="text-2xl font-bold text-white">
                            {metrics ? (metrics.prediction_accuracy * 100).toFixed(0) : 0}%
                        </div>
                        <div className="text-sm text-gray-400">Prediction Accuracy</div>
                    </div>
                    <div className="bg-slate-800/50 rounded-xl p-4 text-center">
                        <Brain className="w-6 h-6 text-purple-400 mx-auto mb-2" />
                        <div className="text-2xl font-bold text-white">
                            {predictiveModels.reduce((sum, model) => sum + model.predictions.length, 0)}
                        </div>
                        <div className="text-sm text-gray-400">Predictions</div>
                    </div>
                    <div className="bg-slate-800/50 rounded-xl p-4 text-center">
                        <Activity className="w-6 h-6 text-cyan-400 mx-auto mb-2" />
                        <div className="text-2xl font-bold text-white">
                            {metrics ? (metrics.system_intelligence_quotient * 100).toFixed(0) : 0}
                        </div>
                        <div className="text-sm text-gray-400">System IQ</div>
                    </div>
                </div>
            </motion.div>

            {/* View Controls */}
            <div className="flex flex-wrap gap-2 mb-6">
                {[
                    { view: 'patterns', icon: Target, label: 'Pattern Analysis' },
                    { view: 'predictions', icon: TrendingUp, label: 'Predictive Models' },
                    { view: 'intelligence', icon: Brain, label: 'Intelligence Metrics' }
                ].map(({ view, icon: Icon, label }) => (
                    <motion.button
                        key={view}
                        className={`flex items-center space-x-2 px-4 py-2 rounded-lg font-semibold transition-all ${activeView === view
                                ? 'bg-gradient-to-r from-blue-500 to-purple-500 text-white'
                                : 'bg-slate-800/50 text-gray-400 hover:text-white hover:bg-slate-700/50'
                            }`}
                        onClick={() => setActiveView(view as any)}
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                    >
                        <Icon className="w-4 h-4" />
                        <span>{label}</span>
                    </motion.button>
                ))}
            </div>

            {/* Content Views */}
            <AnimatePresence mode="wait">
                <motion.div
                    key={activeView}
                    initial={{ opacity: 0, y: 20 }}
                    animate={{ opacity: 1, y: 0 }}
                    exit={{ opacity: 0, y: -20 }}
                    transition={{ duration: 0.3 }}
                >
                    {activeView === 'patterns' && renderPatternsView()}
                    {activeView === 'predictions' && renderPredictionsView()}
                    {activeView === 'intelligence' && renderIntelligenceView()}
                </motion.div>
            </AnimatePresence>
        </div>
    )
}
