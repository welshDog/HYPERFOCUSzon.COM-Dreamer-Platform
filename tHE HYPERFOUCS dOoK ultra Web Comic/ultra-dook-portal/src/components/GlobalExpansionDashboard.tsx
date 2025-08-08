'use client'

import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import {
    Target,
    Zap,
    Globe,
    TrendingUp,
    BarChart,
    Users,
    Briefcase,
    Shield,
    Cpu,
    Lightbulb,
    Map,
    ChevronRight,
    Play,
    Settings,
    Star,
    AlertTriangle,
    CheckCircle,
    Clock,
    Activity,
    Network,
    Rocket,
    Crown,
    ArrowUp,
    Filter,
    Search,
    Calendar,
    DollarSign,
    Sparkles
} from 'lucide-react'

interface GlobalMetric {
    id: string
    name: string
    category: 'Revenue' | 'Operations' | 'Market' | 'Technology' | 'Team'
    current_value: number
    target_value: number
    growth_rate: number
    trend: 'up' | 'down' | 'stable'
    importance: 'Critical' | 'High' | 'Medium' | 'Low'
    last_updated: string
}

interface ExpansionOpportunity {
    id: string
    title: string
    description: string
    market: string
    estimated_revenue: number
    investment_required: number
    roi_projection: number
    timeline: string
    difficulty: 'Low' | 'Medium' | 'High' | 'Legendary'
    success_probability: number
    key_requirements: string[]
    competitive_advantage: string
}

interface ScalingStrategy {
    id: string
    name: string
    phase: number
    description: string
    target_markets: string[]
    key_objectives: string[]
    success_metrics: string[]
    estimated_timeline: string
    resource_requirements: {
        team_size: number
        technology_stack: string[]
        budget_range: string
    }
    risk_factors: string[]
    mitigation_strategies: string[]
}

export default function GlobalExpansionDashboard() {
    const [globalMetrics, setGlobalMetrics] = useState<GlobalMetric[]>([])
    const [expansionOpportunities, setExpansionOpportunities] = useState<ExpansionOpportunity[]>([])
    const [scalingStrategies, setScalingStrategies] = useState<ScalingStrategy[]>([])
    const [activeView, setActiveView] = useState<'overview' | 'opportunities' | 'strategies'>('overview')
    const [selectedMarket, setSelectedMarket] = useState<string>('all')
    const [isAnalyzing, setIsAnalyzing] = useState(false)
    const [timeframe, setTimeframe] = useState<'1M' | '3M' | '6M' | '1Y'>('3M')

    // Mock data initialization
    useEffect(() => {
        const initializeData = () => {
            setIsAnalyzing(true)

            setTimeout(() => {
                const mockMetrics: GlobalMetric[] = [
                    {
                        id: 'metric_revenue',
                        name: 'Global Revenue',
                        category: 'Revenue',
                        current_value: 2.3,
                        target_value: 10.0,
                        growth_rate: 0.34,
                        trend: 'up',
                        importance: 'Critical',
                        last_updated: '2025-08-04T12:00:00Z'
                    },
                    {
                        id: 'metric_markets',
                        name: 'Active Markets',
                        category: 'Market',
                        current_value: 5,
                        target_value: 25,
                        growth_rate: 0.28,
                        trend: 'up',
                        importance: 'High',
                        last_updated: '2025-08-04T11:45:00Z'
                    },
                    {
                        id: 'metric_team',
                        name: 'Global Team Size',
                        category: 'Team',
                        current_value: 47,
                        target_value: 200,
                        growth_rate: 0.22,
                        trend: 'up',
                        importance: 'High',
                        last_updated: '2025-08-04T11:30:00Z'
                    },
                    {
                        id: 'metric_operations',
                        name: 'Operational Efficiency',
                        category: 'Operations',
                        current_value: 0.87,
                        target_value: 0.95,
                        growth_rate: 0.08,
                        trend: 'up',
                        importance: 'Medium',
                        last_updated: '2025-08-04T11:15:00Z'
                    },
                    {
                        id: 'metric_tech',
                        name: 'Technology Adoption',
                        category: 'Technology',
                        current_value: 0.92,
                        target_value: 0.98,
                        growth_rate: 0.12,
                        trend: 'up',
                        importance: 'High',
                        last_updated: '2025-08-04T11:00:00Z'
                    }
                ]

                const mockOpportunities: ExpansionOpportunity[] = [
                    {
                        id: 'opp_apac',
                        title: 'Asia-Pacific Market Entry',
                        description: 'Strategic expansion into high-growth APAC markets with focus on fintech and AI solutions',
                        market: 'Asia-Pacific',
                        estimated_revenue: 15.7,
                        investment_required: 4.2,
                        roi_projection: 3.7,
                        timeline: '12-18 months',
                        difficulty: 'High',
                        success_probability: 0.78,
                        key_requirements: ['Local partnerships', 'Regulatory compliance', 'Localization', 'Cultural adaptation'],
                        competitive_advantage: 'First-mover advantage in AI-powered financial solutions'
                    },
                    {
                        id: 'opp_europe',
                        title: 'European Union Expansion',
                        description: 'Compliance-first approach to EU markets with emphasis on data privacy and GDPR alignment',
                        market: 'Europe',
                        estimated_revenue: 12.3,
                        investment_required: 3.8,
                        roi_projection: 3.2,
                        timeline: '8-12 months',
                        difficulty: 'Medium',
                        success_probability: 0.84,
                        key_requirements: ['GDPR compliance', 'Multi-language support', 'Regional partnerships', 'Legal framework'],
                        competitive_advantage: 'Privacy-first AI solutions aligned with EU regulations'
                    },
                    {
                        id: 'opp_latam',
                        title: 'Latin America Digital Transformation',
                        description: 'Capitalize on digital transformation wave across Latin American emerging markets',
                        market: 'Latin America',
                        estimated_revenue: 8.9,
                        investment_required: 2.1,
                        roi_projection: 4.2,
                        timeline: '6-10 months',
                        difficulty: 'Medium',
                        success_probability: 0.82,
                        key_requirements: ['Spanish/Portuguese localization', 'Mobile-first approach', 'Payment integration', 'Local talent'],
                        competitive_advantage: 'Cost-effective AI solutions for emerging market needs'
                    },
                    {
                        id: 'opp_vertical',
                        title: 'Vertical Market Specialization',
                        description: 'Deep penetration into healthcare, education, and manufacturing verticals with specialized AI solutions',
                        market: 'Global Verticals',
                        estimated_revenue: 18.4,
                        investment_required: 5.6,
                        roi_projection: 3.3,
                        timeline: '15-24 months',
                        difficulty: 'Legendary',
                        success_probability: 0.71,
                        key_requirements: ['Industry expertise', 'Compliance frameworks', 'Specialized partnerships', 'Custom solutions'],
                        competitive_advantage: 'Industry-specific AI optimization and domain knowledge'
                    }
                ]

                const mockStrategies: ScalingStrategy[] = [
                    {
                        id: 'strategy_phase1',
                        name: 'Foundation Scaling',
                        phase: 1,
                        description: 'Establish global infrastructure and operational foundation for worldwide expansion',
                        target_markets: ['North America', 'Western Europe', 'Australia'],
                        key_objectives: [
                            'Build scalable technology infrastructure',
                            'Establish international legal framework',
                            'Create global brand presence',
                            'Develop multi-currency payment systems'
                        ],
                        success_metrics: [
                            '10M+ global users',
                            '5 operational regions',
                            '98% uptime SLA',
                            '$50M ARR'
                        ],
                        estimated_timeline: '12-18 months',
                        resource_requirements: {
                            team_size: 75,
                            technology_stack: ['Global CDN', 'Multi-region deployment', 'Compliance automation'],
                            budget_range: '$8-12M'
                        },
                        risk_factors: ['Regulatory complexity', 'Cultural adaptation', 'Technical scaling challenges'],
                        mitigation_strategies: ['Legal partnership network', 'Cultural consultants', 'Gradual market entry']
                    },
                    {
                        id: 'strategy_phase2',
                        name: 'Market Penetration',
                        phase: 2,
                        description: 'Aggressive market penetration with localized solutions and strategic partnerships',
                        target_markets: ['Asia-Pacific', 'Latin America', 'Eastern Europe', 'Middle East'],
                        key_objectives: [
                            'Establish local partnerships',
                            'Develop region-specific features',
                            'Build local talent acquisition',
                            'Create market-specific pricing strategies'
                        ],
                        success_metrics: [
                            '50M+ global users',
                            '15 operational regions',
                            '25 strategic partnerships',
                            '$200M ARR'
                        ],
                        estimated_timeline: '18-30 months',
                        resource_requirements: {
                            team_size: 200,
                            technology_stack: ['Localization platform', 'Partnership APIs', 'Regional analytics'],
                            budget_range: '$25-40M'
                        },
                        risk_factors: ['Competition intensity', 'Local regulation changes', 'Partnership dependency'],
                        mitigation_strategies: ['Competitive intelligence', 'Regulatory monitoring', 'Partnership diversification']
                    },
                    {
                        id: 'strategy_phase3',
                        name: 'Global Dominance',
                        phase: 3,
                        description: 'Achieve market leadership position with innovative solutions and ecosystem expansion',
                        target_markets: ['Global Coverage', 'Emerging Markets', 'Niche Verticals'],
                        key_objectives: [
                            'Achieve market leadership in key regions',
                            'Launch innovative product categories',
                            'Build comprehensive ecosystem',
                            'Establish thought leadership'
                        ],
                        success_metrics: [
                            '200M+ global users',
                            '50+ countries active',
                            '100+ ecosystem partners',
                            '$1B+ ARR'
                        ],
                        estimated_timeline: '36-60 months',
                        resource_requirements: {
                            team_size: 500,
                            technology_stack: ['AI research platform', 'Ecosystem APIs', 'Innovation labs'],
                            budget_range: '$100-200M'
                        },
                        risk_factors: ['Market saturation', 'Technological disruption', 'Regulatory backlash'],
                        mitigation_strategies: ['Innovation investment', 'Regulatory engagement', 'Market diversification']
                    }
                ]

                setGlobalMetrics(mockMetrics)
                setExpansionOpportunities(mockOpportunities)
                setScalingStrategies(mockStrategies)
                setIsAnalyzing(false)
            }, 2000)
        }

        initializeData()
    }, [])

    const getCategoryColor = (category: string) => {
        const colors = {
            Revenue: 'from-green-400 to-green-600',
            Operations: 'from-blue-400 to-blue-600',
            Market: 'from-purple-400 to-purple-600',
            Technology: 'from-cyan-400 to-cyan-600',
            Team: 'from-yellow-400 to-yellow-600'
        }
        return colors[category as keyof typeof colors] || 'from-gray-400 to-gray-600'
    }

    const getTrendIcon = (trend: string) => {
        switch (trend) {
            case 'up': return ArrowUp
            case 'down': return <ArrowUp className="rotate-180" />
            case 'stable': return <ArrowUp className="rotate-90" />
            default: return ArrowUp
        }
    }

    const getDifficultyColor = (difficulty: string) => {
        const colors = {
            Low: 'from-green-400 to-green-500',
            Medium: 'from-yellow-400 to-yellow-500',
            High: 'from-orange-400 to-orange-500',
            Legendary: 'from-purple-400 to-pink-500'
        }
        return colors[difficulty as keyof typeof colors] || 'from-gray-400 to-gray-500'
    }

    const formatCurrency = (value: number) => {
        if (value >= 1) {
            return `$${value.toFixed(1)}M`
        } else {
            return `$${(value * 1000).toFixed(0)}K`
        }
    }

    const renderOverviewView = () => (
        <div className="space-y-6">
            {/* Global Metrics Dashboard */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 xl:grid-cols-5 gap-6">
                {globalMetrics.map((metric, idx) => {
                    const progress = (metric.current_value / metric.target_value) * 100
                    const TrendIcon = getTrendIcon(metric.trend)

                    return (
                        <motion.div
                            key={metric.id}
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: idx * 0.1 }}
                            className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600"
                        >
                            <div className="flex items-start justify-between mb-4">
                                <div className={`p-3 rounded-full bg-gradient-to-br ${getCategoryColor(metric.category)}`}>
                                    {metric.category === 'Revenue' && <DollarSign className="w-6 h-6 text-white" />}
                                    {metric.category === 'Operations' && <Settings className="w-6 h-6 text-white" />}
                                    {metric.category === 'Market' && <Globe className="w-6 h-6 text-white" />}
                                    {metric.category === 'Technology' && <Cpu className="w-6 h-6 text-white" />}
                                    {metric.category === 'Team' && <Users className="w-6 h-6 text-white" />}
                                </div>
                                <div className="text-right">
                                    <div className={`inline-flex items-center space-x-1 px-2 py-1 rounded text-xs font-semibold ${metric.importance === 'Critical' ? 'bg-red-500/20 text-red-300' :
                                            metric.importance === 'High' ? 'bg-orange-500/20 text-orange-300' :
                                                metric.importance === 'Medium' ? 'bg-yellow-500/20 text-yellow-300' :
                                                    'bg-green-500/20 text-green-300'
                                        }`}>
                                        {metric.importance}
                                    </div>
                                </div>
                            </div>

                            <h3 className="text-lg font-bold text-white mb-2">{metric.name}</h3>

                            <div className="mb-4">
                                <div className="flex items-center justify-between mb-2">
                                    <span className="text-2xl font-bold text-cyan-400">
                                        {metric.category === 'Revenue' ? formatCurrency(metric.current_value) :
                                            metric.category === 'Operations' || metric.category === 'Technology' ?
                                                `${(metric.current_value * 100).toFixed(0)}%` :
                                                metric.current_value.toLocaleString()}
                                    </span>
                                    <span className="text-sm text-gray-400">
                                        of {metric.category === 'Revenue' ? formatCurrency(metric.target_value) :
                                            metric.category === 'Operations' || metric.category === 'Technology' ?
                                                `${(metric.target_value * 100).toFixed(0)}%` :
                                                metric.target_value.toLocaleString()}
                                    </span>
                                </div>

                                <div className="w-full bg-slate-700 rounded-full h-2">
                                    <motion.div
                                        className={`h-2 rounded-full bg-gradient-to-r ${getCategoryColor(metric.category)}`}
                                        initial={{ width: 0 }}
                                        animate={{ width: `${Math.min(progress, 100)}%` }}
                                        transition={{ duration: 1, delay: idx * 0.1 }}
                                    />
                                </div>
                            </div>

                            <div className="flex items-center justify-between">
                                <div className="flex items-center space-x-2">
                                    {TrendIcon && <TrendIcon className="w-4 h-4 text-green-400" />}
                                    <span className="text-sm font-semibold text-green-400">
                                        +{(metric.growth_rate * 100).toFixed(0)}%
                                    </span>
                                </div>
                                <div className="text-xs text-gray-400">
                                    {timeframe} growth
                                </div>
                            </div>
                        </motion.div>
                    )
                })}
            </div>

            {/* Strategic Overview */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {/* Market Opportunities */}
                <motion.div
                    initial={{ opacity: 0, x: -20 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600"
                >
                    <div className="flex items-center space-x-3 mb-6">
                        <Target className="w-6 h-6 text-purple-400" />
                        <h3 className="text-xl font-bold text-white">High-Impact Opportunities</h3>
                    </div>

                    <div className="space-y-4">
                        {expansionOpportunities.slice(0, 3).map((opportunity, idx) => (
                            <motion.div
                                key={opportunity.id}
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: idx * 0.1 }}
                                className="bg-slate-700/30 rounded-lg p-4 border border-gray-600/50"
                            >
                                <div className="flex items-start justify-between mb-2">
                                    <h4 className="font-semibold text-white">{opportunity.title}</h4>
                                    <span className={`px-2 py-1 rounded text-xs font-semibold bg-gradient-to-r ${getDifficultyColor(opportunity.difficulty)} text-white`}>
                                        {opportunity.difficulty}
                                    </span>
                                </div>
                                <p className="text-sm text-gray-400 mb-3">{opportunity.description}</p>
                                <div className="grid grid-cols-3 gap-4">
                                    <div className="text-center">
                                        <div className="text-lg font-bold text-green-400">{formatCurrency(opportunity.estimated_revenue)}</div>
                                        <div className="text-xs text-gray-400">Revenue</div>
                                    </div>
                                    <div className="text-center">
                                        <div className="text-lg font-bold text-blue-400">{opportunity.roi_projection.toFixed(1)}x</div>
                                        <div className="text-xs text-gray-400">ROI</div>
                                    </div>
                                    <div className="text-center">
                                        <div className="text-lg font-bold text-purple-400">{(opportunity.success_probability * 100).toFixed(0)}%</div>
                                        <div className="text-xs text-gray-400">Success</div>
                                    </div>
                                </div>
                            </motion.div>
                        ))}
                    </div>

                    <motion.button
                        className="w-full mt-4 py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-lg font-semibold hover:from-purple-600 hover:to-pink-600 transition-all"
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        onClick={() => setActiveView('opportunities')}
                    >
                        View All Opportunities
                    </motion.button>
                </motion.div>

                {/* Scaling Strategies */}
                <motion.div
                    initial={{ opacity: 0, x: 20 }}
                    animate={{ opacity: 1, x: 0 }}
                    className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600"
                >
                    <div className="flex items-center space-x-3 mb-6">
                        <Rocket className="w-6 h-6 text-cyan-400" />
                        <h3 className="text-xl font-bold text-white">Scaling Roadmap</h3>
                    </div>

                    <div className="space-y-4">
                        {scalingStrategies.map((strategy, idx) => (
                            <motion.div
                                key={strategy.id}
                                initial={{ opacity: 0, y: 10 }}
                                animate={{ opacity: 1, y: 0 }}
                                transition={{ delay: idx * 0.1 }}
                                className="bg-slate-700/30 rounded-lg p-4 border border-gray-600/50"
                            >
                                <div className="flex items-center space-x-3 mb-2">
                                    <div className={`w-8 h-8 rounded-full bg-gradient-to-br ${strategy.phase === 1 ? 'from-green-400 to-green-600' :
                                            strategy.phase === 2 ? 'from-blue-400 to-blue-600' :
                                                'from-purple-400 to-purple-600'
                                        } flex items-center justify-center`}>
                                        <span className="text-sm font-bold text-white">{strategy.phase}</span>
                                    </div>
                                    <h4 className="font-semibold text-white flex-grow">{strategy.name}</h4>
                                    <span className="text-xs text-gray-400">{strategy.estimated_timeline}</span>
                                </div>
                                <p className="text-sm text-gray-400 mb-3">{strategy.description}</p>
                                <div className="flex items-center justify-between">
                                    <div className="text-sm text-cyan-400 font-semibold">
                                        {strategy.target_markets.length} markets • {strategy.resource_requirements.team_size} team size
                                    </div>
                                    <div className="text-sm text-green-400 font-semibold">
                                        {strategy.resource_requirements.budget_range}
                                    </div>
                                </div>
                            </motion.div>
                        ))}
                    </div>

                    <motion.button
                        className="w-full mt-4 py-3 bg-gradient-to-r from-cyan-500 to-blue-500 text-white rounded-lg font-semibold hover:from-cyan-600 hover:to-blue-600 transition-all"
                        whileHover={{ scale: 1.02 }}
                        whileTap={{ scale: 0.98 }}
                        onClick={() => setActiveView('strategies')}
                    >
                        Explore Strategies
                    </motion.button>
                </motion.div>
            </div>

            {/* Quick Actions */}
            <div className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600">
                <h3 className="text-xl font-bold text-white mb-6">⚡ Quick Launch Actions</h3>
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
                    {[
                        { icon: Crown, title: 'Launch Premium Tier', description: 'Deploy AI coaching premium services', color: 'from-yellow-400 to-yellow-600' },
                        { icon: Shield, title: 'Security Audit', description: 'Complete global security compliance', color: 'from-red-400 to-red-600' },
                        { icon: Network, title: 'Partnership Network', description: 'Activate strategic partnerships', color: 'from-blue-400 to-blue-600' },
                        { icon: Sparkles, title: 'Innovation Lab', description: 'Launch R&D innovation center', color: 'from-purple-400 to-purple-600' }
                    ].map((action, idx) => (
                        <motion.button
                            key={idx}
                            className="bg-slate-700/30 rounded-lg p-4 border border-gray-600/50 hover:border-gray-500/50 transition-all text-left"
                            whileHover={{ scale: 1.02, y: -2 }}
                            whileTap={{ scale: 0.98 }}
                        >
                            <div className={`p-3 rounded-lg bg-gradient-to-br ${action.color} mb-3 w-fit`}>
                                <action.icon className="w-6 h-6 text-white" />
                            </div>
                            <h4 className="font-semibold text-white mb-1">{action.title}</h4>
                            <p className="text-sm text-gray-400">{action.description}</p>
                        </motion.button>
                    ))}
                </div>
            </div>
        </div>
    )

    const renderOpportunitiesView = () => (
        <div className="space-y-6">
            {/* Opportunities Grid */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {expansionOpportunities.map((opportunity, idx) => (
                    <motion.div
                        key={opportunity.id}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: idx * 0.1 }}
                        className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600"
                    >
                        <div className="flex items-start justify-between mb-4">
                            <div>
                                <h3 className="text-xl font-bold text-white mb-2">{opportunity.title}</h3>
                                <p className="text-gray-400 text-sm mb-3">{opportunity.description}</p>
                                <div className="flex items-center space-x-2">
                                    <Globe className="w-4 h-4 text-blue-400" />
                                    <span className="text-sm text-blue-400 font-semibold">{opportunity.market}</span>
                                </div>
                            </div>
                            <span className={`px-3 py-1 rounded text-sm font-semibold bg-gradient-to-r ${getDifficultyColor(opportunity.difficulty)} text-white`}>
                                {opportunity.difficulty}
                            </span>
                        </div>

                        {/* Financial Metrics */}
                        <div className="grid grid-cols-3 gap-4 mb-6">
                            <div className="text-center">
                                <div className="text-2xl font-bold text-green-400">{formatCurrency(opportunity.estimated_revenue)}</div>
                                <div className="text-xs text-gray-400">Est. Revenue</div>
                            </div>
                            <div className="text-center">
                                <div className="text-2xl font-bold text-orange-400">{formatCurrency(opportunity.investment_required)}</div>
                                <div className="text-xs text-gray-400">Investment</div>
                            </div>
                            <div className="text-center">
                                <div className="text-2xl font-bold text-purple-400">{opportunity.roi_projection.toFixed(1)}x</div>
                                <div className="text-xs text-gray-400">ROI</div>
                            </div>
                        </div>

                        {/* Success Probability */}
                        <div className="mb-6">
                            <div className="flex items-center justify-between mb-2">
                                <span className="text-sm font-semibold text-white">Success Probability</span>
                                <span className="text-sm font-bold text-cyan-400">
                                    {(opportunity.success_probability * 100).toFixed(0)}%
                                </span>
                            </div>
                            <div className="w-full bg-slate-700 rounded-full h-2">
                                <motion.div
                                    className="h-2 rounded-full bg-gradient-to-r from-cyan-400 to-blue-500"
                                    initial={{ width: 0 }}
                                    animate={{ width: `${opportunity.success_probability * 100}%` }}
                                    transition={{ duration: 1, delay: idx * 0.1 }}
                                />
                            </div>
                        </div>

                        {/* Key Requirements */}
                        <div className="mb-6">
                            <h4 className="text-sm font-semibold text-white mb-2">Key Requirements</h4>
                            <div className="flex flex-wrap gap-2">
                                {opportunity.key_requirements.map((req, reqIdx) => (
                                    <span
                                        key={reqIdx}
                                        className="px-2 py-1 bg-slate-700/50 text-gray-300 text-xs rounded"
                                    >
                                        {req}
                                    </span>
                                ))}
                            </div>
                        </div>

                        {/* Competitive Advantage */}
                        <div className="mb-6">
                            <h4 className="text-sm font-semibold text-white mb-2">Competitive Advantage</h4>
                            <p className="text-sm text-green-400 bg-green-500/10 rounded-lg p-3 border border-green-500/20">
                                {opportunity.competitive_advantage}
                            </p>
                        </div>

                        {/* Timeline & Action */}
                        <div className="flex items-center justify-between">
                            <div className="flex items-center space-x-2">
                                <Clock className="w-4 h-4 text-gray-400" />
                                <span className="text-sm text-gray-400">{opportunity.timeline}</span>
                            </div>
                            <motion.button
                                className="px-4 py-2 bg-gradient-to-r from-green-500 to-blue-500 text-white rounded-lg font-semibold hover:from-green-600 hover:to-blue-600 transition-all"
                                whileHover={{ scale: 1.05 }}
                                whileTap={{ scale: 0.95 }}
                            >
                                Launch Initiative
                            </motion.button>
                        </div>
                    </motion.div>
                ))}
            </div>
        </div>
    )

    const renderStrategiesView = () => (
        <div className="space-y-6">
            {/* Strategies Timeline */}
            <div className="space-y-6">
                {scalingStrategies.map((strategy, idx) => (
                    <motion.div
                        key={strategy.id}
                        initial={{ opacity: 0, x: idx % 2 === 0 ? -20 : 20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: idx * 0.2 }}
                        className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600"
                    >
                        <div className="flex items-start space-x-4">
                            {/* Phase Indicator */}
                            <div className={`w-16 h-16 rounded-full bg-gradient-to-br ${strategy.phase === 1 ? 'from-green-400 to-green-600' :
                                    strategy.phase === 2 ? 'from-blue-400 to-blue-600' :
                                        'from-purple-400 to-purple-600'
                                } flex items-center justify-center flex-shrink-0`}>
                                <span className="text-2xl font-bold text-white">{strategy.phase}</span>
                            </div>

                            {/* Strategy Content */}
                            <div className="flex-grow">
                                <div className="flex items-start justify-between mb-4">
                                    <div>
                                        <h3 className="text-2xl font-bold text-white mb-2">{strategy.name}</h3>
                                        <p className="text-gray-400 mb-4">{strategy.description}</p>
                                    </div>
                                    <div className="text-right">
                                        <div className="text-lg font-bold text-cyan-400">{strategy.estimated_timeline}</div>
                                        <div className="text-sm text-gray-400">Timeline</div>
                                    </div>
                                </div>

                                {/* Target Markets */}
                                <div className="mb-6">
                                    <h4 className="text-sm font-semibold text-white mb-2">Target Markets</h4>
                                    <div className="flex flex-wrap gap-2">
                                        {strategy.target_markets.map((market, marketIdx) => (
                                            <span
                                                key={marketIdx}
                                                className="px-3 py-1 bg-blue-500/20 text-blue-300 text-sm rounded-full border border-blue-500/30"
                                            >
                                                {market}
                                            </span>
                                        ))}
                                    </div>
                                </div>

                                {/* Key Objectives and Success Metrics */}
                                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
                                    <div>
                                        <h4 className="text-sm font-semibold text-white mb-3">Key Objectives</h4>
                                        <div className="space-y-2">
                                            {strategy.key_objectives.map((objective, objIdx) => (
                                                <div key={objIdx} className="flex items-center space-x-2">
                                                    <CheckCircle className="w-4 h-4 text-green-400 flex-shrink-0" />
                                                    <span className="text-sm text-gray-300">{objective}</span>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                    <div>
                                        <h4 className="text-sm font-semibold text-white mb-3">Success Metrics</h4>
                                        <div className="space-y-2">
                                            {strategy.success_metrics.map((metric, metricIdx) => (
                                                <div key={metricIdx} className="flex items-center space-x-2">
                                                    <Target className="w-4 h-4 text-purple-400 flex-shrink-0" />
                                                    <span className="text-sm text-gray-300">{metric}</span>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                </div>

                                {/* Resource Requirements */}
                                <div className="bg-slate-700/30 rounded-lg p-4 mb-6">
                                    <h4 className="text-sm font-semibold text-white mb-3">Resource Requirements</h4>
                                    <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                                        <div className="text-center">
                                            <div className="text-lg font-bold text-yellow-400">{strategy.resource_requirements.team_size}</div>
                                            <div className="text-xs text-gray-400">Team Members</div>
                                        </div>
                                        <div className="text-center">
                                            <div className="text-lg font-bold text-green-400">{strategy.resource_requirements.budget_range}</div>
                                            <div className="text-xs text-gray-400">Budget Range</div>
                                        </div>
                                        <div className="text-center">
                                            <div className="text-lg font-bold text-cyan-400">{strategy.resource_requirements.technology_stack.length}</div>
                                            <div className="text-xs text-gray-400">Tech Components</div>
                                        </div>
                                    </div>
                                </div>

                                {/* Risk Factors and Mitigation */}
                                <div className="grid grid-cols-1 lg:grid-cols-2 gap-6 mb-6">
                                    <div>
                                        <h4 className="text-sm font-semibold text-white mb-3">Risk Factors</h4>
                                        <div className="space-y-2">
                                            {strategy.risk_factors.map((risk, riskIdx) => (
                                                <div key={riskIdx} className="flex items-center space-x-2">
                                                    <AlertTriangle className="w-4 h-4 text-orange-400 flex-shrink-0" />
                                                    <span className="text-sm text-gray-300">{risk}</span>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                    <div>
                                        <h4 className="text-sm font-semibold text-white mb-3">Mitigation Strategies</h4>
                                        <div className="space-y-2">
                                            {strategy.mitigation_strategies.map((mitigation, mitigationIdx) => (
                                                <div key={mitigationIdx} className="flex items-center space-x-2">
                                                    <Shield className="w-4 h-4 text-green-400 flex-shrink-0" />
                                                    <span className="text-sm text-gray-300">{mitigation}</span>
                                                </div>
                                            ))}
                                        </div>
                                    </div>
                                </div>

                                {/* Launch Button */}
                                <motion.button
                                    className={`w-full py-3 bg-gradient-to-r ${strategy.phase === 1 ? 'from-green-500 to-emerald-500' :
                                            strategy.phase === 2 ? 'from-blue-500 to-cyan-500' :
                                                'from-purple-500 to-pink-500'
                                        } text-white rounded-lg font-semibold hover:shadow-lg transition-all flex items-center justify-center space-x-2`}
                                    whileHover={{ scale: 1.02 }}
                                    whileTap={{ scale: 0.98 }}
                                >
                                    <Play className="w-5 h-5" />
                                    <span>Launch Phase {strategy.phase} Strategy</span>
                                </motion.button>
                            </div>
                        </div>
                    </motion.div>
                ))}
            </div>
        </div>
    )

    if (isAnalyzing) {
        return (
            <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 flex items-center justify-center">
                <motion.div
                    className="text-center"
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                >
                    <motion.div
                        className="relative mb-8"
                        animate={{ rotate: 360 }}
                        transition={{ duration: 3, repeat: Infinity, ease: "linear" }}
                    >
                        <Globe className="w-16 h-16 text-cyan-400 mx-auto" />
                        <motion.div
                            className="absolute inset-0 w-16 h-16 border-4 border-cyan-400/30 rounded-full mx-auto"
                            animate={{ scale: [1, 1.3, 1] }}
                            transition={{ duration: 2, repeat: Infinity }}
                        />
                    </motion.div>
                    <h2 className="text-2xl font-bold text-white mb-2">Analyzing Global Markets</h2>
                    <p className="text-gray-400">Evaluating expansion opportunities and scaling strategies...</p>
                </motion.div>
            </div>
        )
    }

    return (
        <div className="min-h-screen bg-gradient-to-br from-slate-900 via-purple-900 to-slate-900 p-6">
            {/* Header */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="mb-8"
            >
                <div className="flex items-center space-x-4 mb-4">
                    <motion.div
                        animate={{
                            scale: [1, 1.1, 1],
                            rotate: [0, 360, 0]
                        }}
                        transition={{
                            duration: 6,
                            repeat: Infinity
                        }}
                    >
                        <Globe className="w-10 h-10 text-cyan-400" />
                    </motion.div>
                    <div>
                        <h1 className="text-4xl font-bold text-white">
                            🌍⚡ Global Expansion Dashboard ⚡🌍
                        </h1>
                        <p className="text-gray-400">
                            Strategic Market Analysis • Expansion Opportunities • Scaling Roadmaps
                        </p>
                    </div>
                </div>
            </motion.div>

            {/* View Controls */}
            <div className="flex flex-wrap gap-2 mb-6">
                {[
                    { view: 'overview', icon: BarChart, label: 'Strategic Overview' },
                    { view: 'opportunities', icon: Target, label: 'Market Opportunities' },
                    { view: 'strategies', icon: Map, label: 'Scaling Strategies' }
                ].map(({ view, icon: Icon, label }) => (
                    <motion.button
                        key={view}
                        className={`flex items-center space-x-2 px-4 py-2 rounded-lg font-semibold transition-all ${activeView === view
                                ? 'bg-gradient-to-r from-cyan-500 to-blue-500 text-white'
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
                    {activeView === 'overview' && renderOverviewView()}
                    {activeView === 'opportunities' && renderOpportunitiesView()}
                    {activeView === 'strategies' && renderStrategiesView()}
                </motion.div>
            </AnimatePresence>
        </div>
    )
}
