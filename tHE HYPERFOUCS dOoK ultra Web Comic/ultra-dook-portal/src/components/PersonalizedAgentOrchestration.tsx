'use client'

import React, { useState, useEffect } from 'react'
import { motion, AnimatePresence } from 'framer-motion'
import {
    Users,
    Brain,
    Zap,
    Target,
    Settings,
    Star,
    Shield,
    Briefcase,
    Cog,
    Lightbulb,
    Palette,
    Globe,
    ChevronRight,
    Play,
    Pause,
    RotateCcw,
    TrendingUp,
    Activity,
    Clock,
    CheckCircle,
    AlertCircle,
    Eye,
    Cpu,
    Network,
    Sparkles
} from 'lucide-react'

interface AgentProfile {
    id: string
    name: string
    category: 'Security' | 'Business' | 'Automation' | 'Intelligence' | 'Creative' | 'Web3'
    specialization: string
    capabilities: string[]
    performance_score: number
    efficiency_rating: number
    experience_level: 'Novice' | 'Intermediate' | 'Expert' | 'Legendary'
    current_status: 'available' | 'busy' | 'optimization' | 'learning'
    last_active: string
    preferred_tasks: string[]
    collaboration_rating: number
}

interface TeamComposition {
    id: string
    name: string
    description: string
    agents: AgentProfile[]
    estimated_completion: string
    success_probability: number
    synergy_score: number
    total_cost: number
    recommended_for: string[]
}

interface OrchestrationTask {
    id: string
    title: string
    description: string
    complexity: 'Low' | 'Medium' | 'High' | 'Legendary'
    estimated_duration: string
    required_skills: string[]
    priority: 'Low' | 'Medium' | 'High' | 'Critical'
    status: 'pending' | 'in_progress' | 'completed' | 'optimizing'
    assigned_team?: TeamComposition
}

export default function PersonalizedAgentOrchestration() {
    const [availableAgents, setAvailableAgents] = useState<AgentProfile[]>([])
    const [customTeams, setCustomTeams] = useState<TeamComposition[]>([])
    const [activeTasks, setActiveTasks] = useState<OrchestrationTask[]>([])
    const [selectedAgents, setSelectedAgents] = useState<string[]>([])
    const [activeView, setActiveView] = useState<'agents' | 'teams' | 'orchestration'>('agents')
    const [isAnalyzing, setIsAnalyzing] = useState(false)
    const [orchestrationMode, setOrchestrationMode] = useState<'manual' | 'ai_assisted' | 'fully_automated'>('ai_assisted')

    // Mock data initialization
    useEffect(() => {
        const initializeData = () => {
            setIsAnalyzing(true)

            setTimeout(() => {
                const mockAgents: AgentProfile[] = [
                    {
                        id: 'agent_sec_001',
                        name: 'Fortress Guardian',
                        category: 'Security',
                        specialization: 'Vulnerability Assessment & Gap Analysis',
                        capabilities: ['Risk Assessment', 'Compliance Auditing', 'Threat Detection', 'Security Architecture'],
                        performance_score: 0.94,
                        efficiency_rating: 0.91,
                        experience_level: 'Legendary',
                        current_status: 'available',
                        last_active: '2025-08-04T11:45:00Z',
                        preferred_tasks: ['security audits', 'risk analysis', 'compliance checks'],
                        collaboration_rating: 0.89
                    },
                    {
                        id: 'agent_bus_001',
                        name: 'Revenue Maximizer',
                        category: 'Business',
                        specialization: 'Sales Optimization & Strategy',
                        capabilities: ['Market Analysis', 'Sales Funnels', 'Customer Acquisition', 'Revenue Modeling'],
                        performance_score: 0.92,
                        efficiency_rating: 0.88,
                        experience_level: 'Expert',
                        current_status: 'busy',
                        last_active: '2025-08-04T10:30:00Z',
                        preferred_tasks: ['sales strategy', 'market research', 'customer analysis'],
                        collaboration_rating: 0.93
                    },
                    {
                        id: 'agent_auto_001',
                        name: 'Process Streamliner',
                        category: 'Automation',
                        specialization: 'Workflow Automation & Optimization',
                        capabilities: ['Process Design', 'Automation Scripts', 'Integration Systems', 'Quality Assurance'],
                        performance_score: 0.96,
                        efficiency_rating: 0.94,
                        experience_level: 'Legendary',
                        current_status: 'available',
                        last_active: '2025-08-04T11:30:00Z',
                        preferred_tasks: ['process automation', 'system integration', 'workflow design'],
                        collaboration_rating: 0.87
                    },
                    {
                        id: 'agent_intel_001',
                        name: 'Strategic Analyzer',
                        category: 'Intelligence',
                        specialization: 'Data Analysis & Strategic Planning',
                        capabilities: ['Data Mining', 'Predictive Analytics', 'Strategic Planning', 'Market Intelligence'],
                        performance_score: 0.90,
                        efficiency_rating: 0.92,
                        experience_level: 'Expert',
                        current_status: 'optimization',
                        last_active: '2025-08-04T11:15:00Z',
                        preferred_tasks: ['data analysis', 'strategic planning', 'market intelligence'],
                        collaboration_rating: 0.91
                    },
                    {
                        id: 'agent_creative_001',
                        name: 'Brand Amplifier',
                        category: 'Creative',
                        specialization: 'Marketing & Content Creation',
                        capabilities: ['Content Strategy', 'Brand Development', 'Social Media', 'Creative Campaigns'],
                        performance_score: 0.88,
                        efficiency_rating: 0.86,
                        experience_level: 'Expert',
                        current_status: 'available',
                        last_active: '2025-08-04T11:00:00Z',
                        preferred_tasks: ['content creation', 'brand strategy', 'marketing campaigns'],
                        collaboration_rating: 0.95
                    },
                    {
                        id: 'agent_web3_001',
                        name: 'Blockchain Architect',
                        category: 'Web3',
                        specialization: 'DeFi & Smart Contract Security',
                        capabilities: ['Smart Contracts', 'DeFi Protocols', 'Blockchain Security', 'Token Economics'],
                        performance_score: 0.93,
                        efficiency_rating: 0.89,
                        experience_level: 'Legendary',
                        current_status: 'learning',
                        last_active: '2025-08-04T09:45:00Z',
                        preferred_tasks: ['smart contract audits', 'defi analysis', 'blockchain security'],
                        collaboration_rating: 0.84
                    }
                ]

                const mockTeams: TeamComposition[] = [
                    {
                        id: 'team_legendary_001',
                        name: 'Legendary Enhancement Squad',
                        description: 'Elite team for complex multi-system integrations and breakthrough implementations',
                        agents: [mockAgents[0], mockAgents[2], mockAgents[3]],
                        estimated_completion: '1-2 weeks',
                        success_probability: 0.95,
                        synergy_score: 0.92,
                        total_cost: 15000,
                        recommended_for: ['System Integration', 'Complex Enhancements', 'Security Implementations']
                    },
                    {
                        id: 'team_growth_001',
                        name: 'Revenue Acceleration Team',
                        description: 'Specialized team for business growth, marketing, and customer acquisition',
                        agents: [mockAgents[1], mockAgents[4], mockAgents[3]],
                        estimated_completion: '2-3 weeks',
                        success_probability: 0.89,
                        synergy_score: 0.88,
                        total_cost: 12000,
                        recommended_for: ['Market Expansion', 'Sales Optimization', 'Brand Development']
                    },
                    {
                        id: 'team_innovation_001',
                        name: 'Innovation Lab Squad',
                        description: 'Cutting-edge team for blockchain, AI, and next-generation technology development',
                        agents: [mockAgents[5], mockAgents[2], mockAgents[3]],
                        estimated_completion: '3-4 weeks',
                        success_probability: 0.87,
                        synergy_score: 0.90,
                        total_cost: 18000,
                        recommended_for: ['Blockchain Development', 'AI Innovation', 'Future Technologies']
                    }
                ]

                const mockTasks: OrchestrationTask[] = [
                    {
                        id: 'task_001',
                        title: 'Phase 4 Global Expansion Implementation',
                        description: 'Deploy comprehensive global expansion strategy with multi-regional coordination',
                        complexity: 'Legendary',
                        estimated_duration: '2-3 weeks',
                        required_skills: ['Global Strategy', 'System Integration', 'Multi-team Coordination'],
                        priority: 'Critical',
                        status: 'pending',
                        assigned_team: mockTeams[0]
                    },
                    {
                        id: 'task_002',
                        title: 'Advanced Quantum Memory Crystal Network',
                        description: 'Implement next-generation memory crystal system with AI-powered connections',
                        complexity: 'High',
                        estimated_duration: '1-2 weeks',
                        required_skills: ['AI Systems', 'Data Architecture', 'User Experience'],
                        priority: 'High',
                        status: 'in_progress',
                        assigned_team: mockTeams[2]
                    },
                    {
                        id: 'task_003',
                        title: 'Premium Service Tier Launch',
                        description: 'Develop and launch premium AI coaching service tier with exclusive features',
                        complexity: 'Medium',
                        estimated_duration: '1-2 weeks',
                        required_skills: ['Business Strategy', 'Service Design', 'Marketing'],
                        priority: 'Medium',
                        status: 'pending',
                        assigned_team: mockTeams[1]
                    }
                ]

                setAvailableAgents(mockAgents)
                setCustomTeams(mockTeams)
                setActiveTasks(mockTasks)
                setIsAnalyzing(false)
            }, 1500)
        }

        initializeData()
    }, [])

    const getCategoryColor = (category: string) => {
        const colors = {
            Security: 'from-red-400 to-red-600',
            Business: 'from-green-400 to-green-600',
            Automation: 'from-blue-400 to-blue-600',
            Intelligence: 'from-purple-400 to-purple-600',
            Creative: 'from-pink-400 to-pink-600',
            Web3: 'from-yellow-400 to-yellow-600'
        }
        return colors[category as keyof typeof colors] || 'from-gray-400 to-gray-600'
    }

    const getCategoryIcon = (category: string) => {
        const icons = {
            Security: Shield,
            Business: Briefcase,
            Automation: Cog,
            Intelligence: Brain,
            Creative: Palette,
            Web3: Globe
        }
        return icons[category as keyof typeof icons] || Users
    }

    const getStatusColor = (status: string) => {
        const colors = {
            available: 'text-green-400',
            busy: 'text-yellow-400',
            optimization: 'text-blue-400',
            learning: 'text-purple-400'
        }
        return colors[status as keyof typeof colors] || 'text-gray-400'
    }

    const getComplexityColor = (complexity: string) => {
        const colors = {
            Low: 'from-green-400 to-green-500',
            Medium: 'from-yellow-400 to-yellow-500',
            High: 'from-orange-400 to-orange-500',
            Legendary: 'from-purple-400 to-pink-500'
        }
        return colors[complexity as keyof typeof colors] || 'from-gray-400 to-gray-500'
    }

    const toggleAgentSelection = (agentId: string) => {
        setSelectedAgents(prev =>
            prev.includes(agentId)
                ? prev.filter(id => id !== agentId)
                : [...prev, agentId]
        )
    }

    const renderAgentsView = () => (
        <div className="space-y-6">
            {/* Agent Controls */}
            <div className="flex flex-wrap gap-4 items-center justify-between">
                <div className="flex flex-wrap gap-2">
                    {['All', 'Security', 'Business', 'Automation', 'Intelligence', 'Creative', 'Web3'].map((filter) => (
                        <motion.button
                            key={filter}
                            className="px-3 py-1 rounded-full text-sm font-medium bg-slate-700/50 text-gray-400 hover:text-white hover:bg-slate-600/50 transition-all"
                            whileHover={{ scale: 1.05 }}
                            whileTap={{ scale: 0.95 }}
                        >
                            {filter}
                        </motion.button>
                    ))}
                </div>

                <div className="flex items-center space-x-4">
                    <span className="text-sm text-gray-400">
                        {selectedAgents.length} selected
                    </span>
                    {selectedAgents.length > 0 && (
                        <motion.button
                            className="px-4 py-2 bg-gradient-to-r from-cyan-500 to-blue-500 text-white rounded-lg font-semibold"
                            whileHover={{ scale: 1.05 }}
                            whileTap={{ scale: 0.95 }}
                        >
                            Create Team
                        </motion.button>
                    )}
                </div>
            </div>

            {/* Agents Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {availableAgents.map((agent) => {
                    const CategoryIcon = getCategoryIcon(agent.category)
                    const isSelected = selectedAgents.includes(agent.id)

                    return (
                        <motion.div
                            key={agent.id}
                            className={`bg-gradient-to-br from-slate-800/80 to-slate-900/80 backdrop-blur-sm 
                         border-2 rounded-xl p-6 cursor-pointer transition-all duration-300
                         hover:scale-105 hover:shadow-2xl ${isSelected
                                    ? 'border-cyan-400 shadow-cyan-400/25'
                                    : 'border-gray-600 hover:border-gray-500'
                                }`}
                            onClick={() => toggleAgentSelection(agent.id)}
                            whileHover={{ y: -5 }}
                            whileTap={{ scale: 0.95 }}
                            layoutId={agent.id}
                        >
                            {/* Agent Header */}
                            <div className="flex items-start justify-between mb-4">
                                <div className="flex items-center space-x-3">
                                    <motion.div
                                        className={`p-3 rounded-full bg-gradient-to-br ${getCategoryColor(agent.category)}`}
                                        whileHover={{ rotate: 360 }}
                                        transition={{ duration: 0.5 }}
                                    >
                                        <CategoryIcon className="w-6 h-6 text-white" />
                                    </motion.div>
                                    <div>
                                        <h3 className="text-lg font-bold text-white">{agent.name}</h3>
                                        <p className="text-sm text-gray-400">{agent.category}</p>
                                    </div>
                                </div>
                                <div className="text-right">
                                    <div className={`text-sm font-semibold ${getStatusColor(agent.current_status)} capitalize`}>
                                        {agent.current_status}
                                    </div>
                                    <div className="text-xs text-gray-500">
                                        {agent.experience_level}
                                    </div>
                                </div>
                            </div>

                            {/* Specialization */}
                            <div className="mb-4">
                                <p className="text-sm text-gray-300 font-medium mb-2">{agent.specialization}</p>
                                <div className="flex flex-wrap gap-1">
                                    {agent.capabilities.slice(0, 3).map((capability, idx) => (
                                        <span
                                            key={idx}
                                            className="px-2 py-1 bg-slate-700/50 text-gray-400 text-xs rounded"
                                        >
                                            {capability}
                                        </span>
                                    ))}
                                    {agent.capabilities.length > 3 && (
                                        <span className="px-2 py-1 bg-slate-700/50 text-gray-400 text-xs rounded">
                                            +{agent.capabilities.length - 3} more
                                        </span>
                                    )}
                                </div>
                            </div>

                            {/* Performance Metrics */}
                            <div className="grid grid-cols-3 gap-4 mb-4">
                                <div className="text-center">
                                    <div className="text-lg font-bold text-cyan-400">
                                        {(agent.performance_score * 100).toFixed(0)}%
                                    </div>
                                    <div className="text-xs text-gray-400">Performance</div>
                                </div>
                                <div className="text-center">
                                    <div className="text-lg font-bold text-green-400">
                                        {(agent.efficiency_rating * 100).toFixed(0)}%
                                    </div>
                                    <div className="text-xs text-gray-400">Efficiency</div>
                                </div>
                                <div className="text-center">
                                    <div className="text-lg font-bold text-purple-400">
                                        {(agent.collaboration_rating * 100).toFixed(0)}%
                                    </div>
                                    <div className="text-xs text-gray-400">Teamwork</div>
                                </div>
                            </div>

                            {/* Selection Indicator */}
                            <AnimatePresence>
                                {isSelected && (
                                    <motion.div
                                        initial={{ opacity: 0, scale: 0 }}
                                        animate={{ opacity: 1, scale: 1 }}
                                        exit={{ opacity: 0, scale: 0 }}
                                        className="absolute top-4 right-4 w-6 h-6 bg-cyan-400 rounded-full flex items-center justify-center"
                                    >
                                        <CheckCircle className="w-4 h-4 text-white" />
                                    </motion.div>
                                )}
                            </AnimatePresence>
                        </motion.div>
                    )
                })}
            </div>
        </div>
    )

    const renderTeamsView = () => (
        <div className="space-y-6">
            {/* Team Creation */}
            <div className="bg-gradient-to-br from-purple-900/30 to-blue-900/30 border border-purple-500/30 rounded-xl p-6">
                <div className="flex items-center space-x-3 mb-4">
                    <Users className="w-6 h-6 text-purple-400" />
                    <h3 className="text-xl font-bold text-white">AI-Powered Team Composition</h3>
                </div>
                <p className="text-gray-400 mb-6">
                    Let our AI analyze your requirements and create the optimal team composition with perfect synergy.
                </p>

                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div className="bg-slate-800/50 rounded-lg p-4">
                        <Target className="w-8 h-8 text-blue-400 mb-3" />
                        <h4 className="font-semibold text-white mb-2">Goal-Oriented Assembly</h4>
                        <p className="text-sm text-gray-400">Teams assembled based on specific objectives and success metrics</p>
                    </div>
                    <div className="bg-slate-800/50 rounded-lg p-4">
                        <Brain className="w-8 h-8 text-green-400 mb-3" />
                        <h4 className="font-semibold text-white mb-2">Synergy Optimization</h4>
                        <p className="text-sm text-gray-400">AI calculates collaboration scores and skill complementarity</p>
                    </div>
                    <div className="bg-slate-800/50 rounded-lg p-4">
                        <TrendingUp className="w-8 h-8 text-yellow-400 mb-3" />
                        <h4 className="font-semibold text-white mb-2">Performance Prediction</h4>
                        <p className="text-sm text-gray-400">Predictive modeling for success probability and timeline</p>
                    </div>
                </div>
            </div>

            {/* Existing Teams */}
            <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">
                {customTeams.map((team, idx) => (
                    <motion.div
                        key={team.id}
                        initial={{ opacity: 0, y: 20 }}
                        animate={{ opacity: 1, y: 0 }}
                        transition={{ delay: idx * 0.1 }}
                        className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600"
                    >
                        <div className="flex items-start justify-between mb-4">
                            <div>
                                <h3 className="text-xl font-bold text-white mb-2">{team.name}</h3>
                                <p className="text-gray-400 text-sm mb-3">{team.description}</p>
                            </div>
                            <div className="text-right">
                                <div className="text-lg font-bold text-green-400">
                                    {(team.success_probability * 100).toFixed(0)}%
                                </div>
                                <div className="text-xs text-gray-400">Success Rate</div>
                            </div>
                        </div>

                        {/* Team Metrics */}
                        <div className="grid grid-cols-3 gap-4 mb-4">
                            <div className="text-center">
                                <div className="text-sm font-semibold text-cyan-400">
                                    {(team.synergy_score * 100).toFixed(0)}%
                                </div>
                                <div className="text-xs text-gray-400">Synergy</div>
                            </div>
                            <div className="text-center">
                                <div className="text-sm font-semibold text-purple-400">
                                    {team.estimated_completion}
                                </div>
                                <div className="text-xs text-gray-400">Timeline</div>
                            </div>
                            <div className="text-center">
                                <div className="text-sm font-semibold text-yellow-400">
                                    ${team.total_cost.toLocaleString()}
                                </div>
                                <div className="text-xs text-gray-400">Cost</div>
                            </div>
                        </div>

                        {/* Team Members */}
                        <div className="mb-4">
                            <h4 className="text-sm font-semibold text-white mb-2">Team Members ({team.agents.length})</h4>
                            <div className="flex -space-x-2">
                                {team.agents.map((agent, agentIdx) => {
                                    const CategoryIcon = getCategoryIcon(agent.category)
                                    return (
                                        <motion.div
                                            key={agent.id}
                                            className={`w-10 h-10 rounded-full bg-gradient-to-br ${getCategoryColor(agent.category)} 
                                 flex items-center justify-center border-2 border-slate-800`}
                                            whileHover={{ scale: 1.2, zIndex: 10 }}
                                            title={`${agent.name} - ${agent.specialization}`}
                                        >
                                            <CategoryIcon className="w-5 h-5 text-white" />
                                        </motion.div>
                                    )
                                })}
                            </div>
                        </div>

                        {/* Recommended For */}
                        <div className="mb-4">
                            <h4 className="text-sm font-semibold text-white mb-2">Recommended For:</h4>
                            <div className="flex flex-wrap gap-1">
                                {team.recommended_for.map((use, useIdx) => (
                                    <span
                                        key={useIdx}
                                        className="px-2 py-1 bg-blue-500/20 text-blue-300 text-xs rounded"
                                    >
                                        {use}
                                    </span>
                                ))}
                            </div>
                        </div>

                        {/* Deploy Button */}
                        <motion.button
                            className="w-full py-3 bg-gradient-to-r from-purple-500 to-pink-500 text-white rounded-lg font-semibold 
                         hover:from-purple-600 hover:to-pink-600 transition-all flex items-center justify-center space-x-2"
                            whileHover={{ scale: 1.02 }}
                            whileTap={{ scale: 0.98 }}
                        >
                            <Play className="w-4 h-4" />
                            <span>Deploy Team</span>
                        </motion.button>
                    </motion.div>
                ))}
            </div>
        </div>
    )

    const renderOrchestrationView = () => (
        <div className="space-y-6">
            {/* Orchestration Controls */}
            <div className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600">
                <div className="flex items-center justify-between mb-6">
                    <div className="flex items-center space-x-3">
                        <Settings className="w-6 h-6 text-cyan-400" />
                        <h3 className="text-xl font-bold text-white">Orchestration Control Center</h3>
                    </div>
                    <div className="flex items-center space-x-4">
                        <span className="text-sm text-gray-400">Mode:</span>
                        <select
                            value={orchestrationMode}
                            onChange={(e) => setOrchestrationMode(e.target.value as any)}
                            title="Select orchestration mode"
                            className="bg-slate-700 text-white rounded-lg px-3 py-1 text-sm border border-gray-600"
                        >
                            <option value="manual">Manual Control</option>
                            <option value="ai_assisted">AI Assisted</option>
                            <option value="fully_automated">Fully Automated</option>
                        </select>
                    </div>
                </div>

                <div className="grid grid-cols-1 md:grid-cols-4 gap-4">
                    <div className="bg-slate-700/50 rounded-lg p-4 text-center">
                        <Activity className="w-6 h-6 text-green-400 mx-auto mb-2" />
                        <div className="text-lg font-bold text-white">{activeTasks.length}</div>
                        <div className="text-sm text-gray-400">Active Tasks</div>
                    </div>
                    <div className="bg-slate-700/50 rounded-lg p-4 text-center">
                        <Users className="w-6 h-6 text-blue-400 mx-auto mb-2" />
                        <div className="text-lg font-bold text-white">
                            {availableAgents.filter(a => a.current_status === 'available').length}
                        </div>
                        <div className="text-sm text-gray-400">Available Agents</div>
                    </div>
                    <div className="bg-slate-700/50 rounded-lg p-4 text-center">
                        <TrendingUp className="w-6 h-6 text-purple-400 mx-auto mb-2" />
                        <div className="text-lg font-bold text-white">94%</div>
                        <div className="text-sm text-gray-400">Success Rate</div>
                    </div>
                    <div className="bg-slate-700/50 rounded-lg p-4 text-center">
                        <Clock className="w-6 h-6 text-yellow-400 mx-auto mb-2" />
                        <div className="text-lg font-bold text-white">2.3 days</div>
                        <div className="text-sm text-gray-400">Avg. Completion</div>
                    </div>
                </div>
            </div>

            {/* Active Tasks */}
            <div className="space-y-4">
                <h3 className="text-xl font-bold text-white">Active Orchestration Tasks</h3>
                {activeTasks.map((task, idx) => (
                    <motion.div
                        key={task.id}
                        initial={{ opacity: 0, x: -20 }}
                        animate={{ opacity: 1, x: 0 }}
                        transition={{ delay: idx * 0.1 }}
                        className="bg-gradient-to-br from-slate-800/80 to-slate-900/80 rounded-xl p-6 border border-gray-600"
                    >
                        <div className="flex items-start justify-between mb-4">
                            <div className="flex-grow">
                                <div className="flex items-center space-x-3 mb-2">
                                    <h4 className="text-lg font-bold text-white">{task.title}</h4>
                                    <span className={`px-2 py-1 rounded text-xs font-semibold bg-gradient-to-r ${getComplexityColor(task.complexity)} text-white`}>
                                        {task.complexity}
                                    </span>
                                    <span className={`px-2 py-1 rounded text-xs font-semibold ${task.priority === 'Critical' ? 'bg-red-500/20 text-red-300' :
                                            task.priority === 'High' ? 'bg-orange-500/20 text-orange-300' :
                                                task.priority === 'Medium' ? 'bg-yellow-500/20 text-yellow-300' :
                                                    'bg-green-500/20 text-green-300'
                                        }`}>
                                        {task.priority} Priority
                                    </span>
                                </div>
                                <p className="text-gray-400 text-sm mb-3">{task.description}</p>
                            </div>
                            <div className="text-right ml-4">
                                <div className={`inline-flex items-center space-x-1 px-2 py-1 rounded text-xs font-semibold ${task.status === 'completed' ? 'bg-green-500/20 text-green-300' :
                                        task.status === 'in_progress' ? 'bg-blue-500/20 text-blue-300' :
                                            task.status === 'optimizing' ? 'bg-purple-500/20 text-purple-300' :
                                                'bg-gray-500/20 text-gray-300'
                                    }`}>
                                    {task.status === 'completed' && <CheckCircle className="w-3 h-3" />}
                                    {task.status === 'in_progress' && <Activity className="w-3 h-3" />}
                                    {task.status === 'optimizing' && <Settings className="w-3 h-3" />}
                                    {task.status === 'pending' && <Clock className="w-3 h-3" />}
                                    <span className="capitalize">{task.status.replace('_', ' ')}</span>
                                </div>
                            </div>
                        </div>

                        {/* Task Details */}
                        <div className="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
                            <div>
                                <div className="text-xs text-gray-400 mb-1">Estimated Duration</div>
                                <div className="text-sm font-semibold text-cyan-400">{task.estimated_duration}</div>
                            </div>
                            <div>
                                <div className="text-xs text-gray-400 mb-1">Required Skills</div>
                                <div className="flex flex-wrap gap-1">
                                    {task.required_skills.slice(0, 2).map((skill, skillIdx) => (
                                        <span key={skillIdx} className="px-1 py-0.5 bg-slate-700 text-gray-300 text-xs rounded">
                                            {skill}
                                        </span>
                                    ))}
                                    {task.required_skills.length > 2 && (
                                        <span className="px-1 py-0.5 bg-slate-700 text-gray-300 text-xs rounded">
                                            +{task.required_skills.length - 2}
                                        </span>
                                    )}
                                </div>
                            </div>
                            <div>
                                <div className="text-xs text-gray-400 mb-1">Assigned Team</div>
                                <div className="text-sm font-semibold text-purple-400">
                                    {task.assigned_team?.name || 'Unassigned'}
                                </div>
                            </div>
                        </div>

                        {/* Assigned Team Preview */}
                        {task.assigned_team && (
                            <div className="bg-slate-700/30 rounded-lg p-4">
                                <div className="flex items-center justify-between">
                                    <div className="flex items-center space-x-3">
                                        <div className="flex -space-x-2">
                                            {task.assigned_team.agents.slice(0, 3).map((agent, agentIdx) => {
                                                const CategoryIcon = getCategoryIcon(agent.category)
                                                return (
                                                    <div
                                                        key={agent.id}
                                                        className={`w-8 h-8 rounded-full bg-gradient-to-br ${getCategoryColor(agent.category)} 
                                       flex items-center justify-center border-2 border-slate-800`}
                                                        title={agent.name}
                                                    >
                                                        <CategoryIcon className="w-4 h-4 text-white" />
                                                    </div>
                                                )
                                            })}
                                            {task.assigned_team.agents.length > 3 && (
                                                <div className="w-8 h-8 rounded-full bg-gray-600 flex items-center justify-center border-2 border-slate-800">
                                                    <span className="text-xs text-white">+{task.assigned_team.agents.length - 3}</span>
                                                </div>
                                            )}
                                        </div>
                                        <div>
                                            <div className="text-sm font-semibold text-white">{task.assigned_team.name}</div>
                                            <div className="text-xs text-gray-400">
                                                Success Rate: {(task.assigned_team.success_probability * 100).toFixed(0)}%
                                            </div>
                                        </div>
                                    </div>
                                    <div className="flex space-x-2">
                                        <motion.button
                                            className="p-2 bg-blue-500/20 text-blue-300 rounded-lg hover:bg-blue-500/30 transition-colors"
                                            whileHover={{ scale: 1.05 }}
                                            whileTap={{ scale: 0.95 }}
                                            title="Monitor Progress"
                                        >
                                            <Eye className="w-4 h-4" />
                                        </motion.button>
                                        <motion.button
                                            className="p-2 bg-green-500/20 text-green-300 rounded-lg hover:bg-green-500/30 transition-colors"
                                            whileHover={{ scale: 1.05 }}
                                            whileTap={{ scale: 0.95 }}
                                            title="Optimize Performance"
                                        >
                                            <Settings className="w-4 h-4" />
                                        </motion.button>
                                    </div>
                                </div>
                            </div>
                        )}
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
                        <Users className="w-16 h-16 text-purple-400 mx-auto" />
                        <motion.div
                            className="absolute inset-0 w-16 h-16 border-4 border-purple-400/30 rounded-full mx-auto"
                            animate={{ scale: [1, 1.3, 1] }}
                            transition={{ duration: 2, repeat: Infinity }}
                        />
                    </motion.div>
                    <h2 className="text-2xl font-bold text-white mb-2">Analyzing Agent Network</h2>
                    <p className="text-gray-400">Optimizing team compositions and orchestration strategies...</p>
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
                            rotate: [0, 5, -5, 0]
                        }}
                        transition={{
                            duration: 4,
                            repeat: Infinity
                        }}
                    >
                        <Users className="w-10 h-10 text-purple-400" />
                    </motion.div>
                    <div>
                        <h1 className="text-4xl font-bold text-white">
                            🎯⚡ Personalized Agent Orchestration ⚡🎯
                        </h1>
                        <p className="text-gray-400">
                            AI-Powered Team Assembly • Custom Agent Selection • Intelligent Task Coordination
                        </p>
                    </div>
                </div>
            </motion.div>

            {/* View Controls */}
            <div className="flex flex-wrap gap-2 mb-6">
                {[
                    { view: 'agents', icon: Users, label: 'Agent Profiles' },
                    { view: 'teams', icon: Network, label: 'Team Composition' },
                    { view: 'orchestration', icon: Settings, label: 'Task Orchestration' }
                ].map(({ view, icon: Icon, label }) => (
                    <motion.button
                        key={view}
                        className={`flex items-center space-x-2 px-4 py-2 rounded-lg font-semibold transition-all ${activeView === view
                                ? 'bg-gradient-to-r from-purple-500 to-pink-500 text-white'
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
                    {activeView === 'agents' && renderAgentsView()}
                    {activeView === 'teams' && renderTeamsView()}
                    {activeView === 'orchestration' && renderOrchestrationView()}
                </motion.div>
            </AnimatePresence>
        </div>
    )
}
