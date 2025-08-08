'use client';

import React, { useState, useEffect, useCallback, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
    Bot,
    Activity,
    Zap,
    Database,
    Shield,
    Briefcase,
    Palette,
    Brain,
    Users,
    Monitor,
    AlertCircle,
    CheckCircle,
    Clock,
    TrendingUp,
    Settings,
    Play,
    Pause
} from 'lucide-react';

// 🤖 Agent Categories with 677+ Distribution
const AGENT_CATEGORIES = {
    security: { count: 89, color: 'text-red-400', bg: 'bg-red-500/20', icon: Shield, name: 'Security' },
    business: { count: 112, color: 'text-green-400', bg: 'bg-green-500/20', icon: Briefcase, name: 'Business' },
    automation: { count: 156, color: 'text-blue-400', bg: 'bg-blue-500/20', icon: Zap, name: 'Automation' },
    intelligence: { count: 134, color: 'text-purple-400', bg: 'bg-purple-500/20', icon: Brain, name: 'Intelligence' },
    creative: { count: 98, color: 'text-pink-400', bg: 'bg-pink-500/20', icon: Palette, name: 'Creative' },
    web3: { count: 88, color: 'text-orange-400', bg: 'bg-orange-500/20', icon: Database, name: 'Web3' }
};

// 🔥 Real-time Agent Status Interface
interface AgentStatus {
    category: string;
    activeCount: number;
    totalCount: number;
    performance: number;
    tasks: string[];
    lastUpdate: Date;
    broSkiRewards: number;
}

// ⚡ Performance Metrics Interface
interface PerformanceMetrics {
    responseTime: number;
    throughput: number;
    errorRate: number;
    agentCoordination: number;
}

export default function AgentIntegrationHub() {
    const [agentStatuses, setAgentStatuses] = useState<AgentStatus[]>([]);
    const [performance, setPerformance] = useState<PerformanceMetrics>({
        responseTime: 0.3,
        throughput: 1247,
        errorRate: 0.02,
        agentCoordination: 98.7
    });
    const [isSystemActive, setIsSystemActive] = useState(true);
    const [totalBroSkiRewards, setTotalBroSkiRewards] = useState(125750);
    const [coordinationLevel, setCoordinationLevel] = useState(0);
    const intervalRef = useRef<NodeJS.Timeout>();

    // 🚀 Initialize Agent System
    useEffect(() => {
        initializeAgentSystem();
        startRealTimeUpdates();

        return () => {
            if (intervalRef.current) {
                clearInterval(intervalRef.current);
            }
        };
    }, []);

    const initializeAgentSystem = useCallback(() => {
        const initialStatuses: AgentStatus[] = Object.entries(AGENT_CATEGORIES).map(([key, config]) => ({
            category: key,
            activeCount: Math.floor(config.count * (0.85 + Math.random() * 0.15)),
            totalCount: config.count,
            performance: 85 + Math.random() * 15,
            tasks: generateRandomTasks(key),
            lastUpdate: new Date(),
            broSkiRewards: Math.floor(config.count * (50 + Math.random() * 100))
        }));

        setAgentStatuses(initialStatuses);
    }, []);

    const generateRandomTasks = (category: string): string[] => {
        const taskTemplates = {
            security: [
                'Security gap analysis in progress',
                'Vulnerability scanning active',
                'Client system monitoring',
                'Threat assessment complete',
                'Security proposal generated'
            ],
            business: [
                'Lead qualification processing',
                'Revenue optimization active',
                'Client acquisition campaign',
                'Sales pipeline analysis',
                'Conversion tracking update'
            ],
            automation: [
                'Client onboarding sequence',
                'Workflow optimization running',
                'Process automation active',
                'System integration complete',
                'Efficiency analysis update'
            ],
            intelligence: [
                'Data analysis in progress',
                'Strategic insights generation',
                'Market research active',
                'Performance metrics update',
                'Intelligence report ready'
            ],
            creative: [
                'Content creation active',
                'Design optimization running',
                'Campaign material generation',
                'Brand asset creation',
                'Creative strategy update'
            ],
            web3: [
                'Blockchain analysis active',
                'Smart contract audit',
                'DeFi security assessment',
                'Web3 integration testing',
                'Crypto security monitoring'
            ]
        };

        const templates = taskTemplates[category as keyof typeof taskTemplates] || [];
        return templates.slice(0, 2 + Math.floor(Math.random() * 3));
    };

    const startRealTimeUpdates = useCallback(() => {
        intervalRef.current = setInterval(() => {
            if (isSystemActive) {
                // Update agent statuses
                setAgentStatuses(prev => prev.map(status => ({
                    ...status,
                    activeCount: Math.min(status.totalCount, status.activeCount + Math.floor(Math.random() * 3) - 1),
                    performance: Math.max(75, Math.min(100, status.performance + (Math.random() - 0.4) * 5)),
                    lastUpdate: new Date(),
                    broSkiRewards: status.broSkiRewards + Math.floor(Math.random() * 10)
                })));

                // Update performance metrics
                setPerformance(prev => ({
                    responseTime: Math.max(0.1, Math.min(1.0, prev.responseTime + (Math.random() - 0.5) * 0.1)),
                    throughput: Math.max(500, prev.throughput + Math.floor((Math.random() - 0.5) * 100)),
                    errorRate: Math.max(0, Math.min(5, prev.errorRate + (Math.random() - 0.7) * 0.5)),
                    agentCoordination: Math.max(90, Math.min(100, prev.agentCoordination + (Math.random() - 0.3) * 2))
                }));

                // Update coordination level animation
                setCoordinationLevel(prev => (prev + 1) % 100);

                // Update total rewards
                setTotalBroSkiRewards(prev => prev + Math.floor(Math.random() * 25));
            }
        }, 2000);
    }, [isSystemActive]);

    const toggleSystemStatus = () => {
        setIsSystemActive(!isSystemActive);
    };

    const getTotalActiveAgents = () => {
        return agentStatuses.reduce((sum, status) => sum + status.activeCount, 0);
    };

    const getTotalAgents = () => {
        return agentStatuses.reduce((sum, status) => sum + status.totalCount, 0);
    };

    const getOverallPerformance = () => {
        if (agentStatuses.length === 0) return 0;
        return agentStatuses.reduce((sum, status) => sum + status.performance, 0) / agentStatuses.length;
    };

    return (
        <div className="space-y-6">
            {/* 🏛️ Agent System Header */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-blue-600/20 via-purple-600/20 to-green-600/20 border border-blue-500/30 p-6"
            >
                <div className="flex items-center justify-between">
                    <div className="space-y-2">
                        <h2 className="text-2xl font-bold text-white flex items-center gap-3">
                            <Bot className="w-8 h-8 text-blue-400" />
                            🤖 AGENT INTEGRATION HUB
                            <span className="text-green-400">({getTotalActiveAgents()}/{getTotalAgents()})</span>
                        </h2>
                        <p className="text-blue-200">
                            Real-time coordination of 677+ AI agents across security, business & automation operations
                        </p>
                    </div>

                    <motion.button
                        whileHover={{ scale: 1.05 }}
                        whileTap={{ scale: 0.95 }}
                        onClick={toggleSystemStatus}
                        className={`flex items-center gap-2 px-4 py-2 rounded-xl font-semibold transition-colors ${isSystemActive
                                ? 'bg-green-500/20 text-green-400 border border-green-500/30'
                                : 'bg-red-500/20 text-red-400 border border-red-500/30'
                            }`}
                    >
                        {isSystemActive ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
                        {isSystemActive ? 'ACTIVE' : 'PAUSED'}
                    </motion.button>
                </div>

                {/* 🌊 Coordination Wave Animation */}
                <motion.div
                    className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-blue-500 via-purple-500 to-green-500"
                    initial={{ scaleX: 0 }}
                    animate={{
                        scaleX: isSystemActive ? [0, 1, 0] : 0,
                        opacity: isSystemActive ? [0.3, 1, 0.3] : 0
                    }}
                    transition={{
                        duration: 3,
                        repeat: Infinity,
                        ease: "easeInOut"
                    }}
                    style={{ transformOrigin: 'left' }}
                />
            </motion.div>

            {/* 📊 Performance Dashboard */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.1 }}
                className="grid grid-cols-2 md:grid-cols-4 gap-4"
            >
                <div className="bg-gradient-to-br from-green-500/10 to-green-600/5 border border-green-500/20 rounded-xl p-4">
                    <div className="flex items-center gap-2 mb-2">
                        <Clock className="w-5 h-5 text-green-400" />
                        <span className="text-green-400 font-semibold">Response Time</span>
                    </div>
                    <div className="text-2xl font-bold text-white">{performance.responseTime.toFixed(2)}s</div>
                    <div className="text-sm text-green-300">Target: &lt;1.0s</div>
                </div>

                <div className="bg-gradient-to-br from-blue-500/10 to-blue-600/5 border border-blue-500/20 rounded-xl p-4">
                    <div className="flex items-center gap-2 mb-2">
                        <TrendingUp className="w-5 h-5 text-blue-400" />
                        <span className="text-blue-400 font-semibold">Throughput</span>
                    </div>
                    <div className="text-2xl font-bold text-white">{performance.throughput.toLocaleString()}</div>
                    <div className="text-sm text-blue-300">ops/min</div>
                </div>

                <div className="bg-gradient-to-br from-purple-500/10 to-purple-600/5 border border-purple-500/20 rounded-xl p-4">
                    <div className="flex items-center gap-2 mb-2">
                        <AlertCircle className="w-5 h-5 text-purple-400" />
                        <span className="text-purple-400 font-semibold">Error Rate</span>
                    </div>
                    <div className="text-2xl font-bold text-white">{performance.errorRate.toFixed(2)}%</div>
                    <div className="text-sm text-purple-300">Target: &lt;1%</div>
                </div>

                <div className="bg-gradient-to-br from-yellow-500/10 to-yellow-600/5 border border-yellow-500/20 rounded-xl p-4">
                    <div className="flex items-center gap-2 mb-2">
                        <Users className="w-5 h-5 text-yellow-400" />
                        <span className="text-yellow-400 font-semibold">Coordination</span>
                    </div>
                    <div className="text-2xl font-bold text-white">{performance.agentCoordination.toFixed(1)}%</div>
                    <div className="text-sm text-yellow-300">Agent sync</div>
                </div>
            </motion.div>

            {/* 🤖 Agent Category Grid */}
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                {agentStatuses.map((status, index) => {
                    const config = AGENT_CATEGORIES[status.category as keyof typeof AGENT_CATEGORIES];
                    const IconComponent = config.icon;
                    const utilizationRate = (status.activeCount / status.totalCount) * 100;

                    return (
                        <motion.div
                            key={status.category}
                            initial={{ opacity: 0, y: 20 }}
                            animate={{ opacity: 1, y: 0 }}
                            transition={{ delay: 0.2 + index * 0.1 }}
                            className={`relative overflow-hidden rounded-xl ${config.bg} border border-opacity-30 p-6 hover:border-opacity-60 transition-all duration-300`}
                            whileHover={{ scale: 1.02, y: -2 }}
                        >
                            {/* Agent Category Header */}
                            <div className="flex items-center justify-between mb-4">
                                <div className="flex items-center gap-3">
                                    <div className={`p-2 rounded-lg ${config.bg} ${config.color}`}>
                                        <IconComponent className="w-6 h-6" />
                                    </div>
                                    <div>
                                        <h3 className={`font-bold text-lg ${config.color}`}>
                                            {config.name} Agents
                                        </h3>
                                        <p className="text-sm text-gray-400">
                                            {status.activeCount}/{status.totalCount} active
                                        </p>
                                    </div>
                                </div>

                                <div className="text-right">
                                    <div className={`text-2xl font-bold ${config.color}`}>
                                        {utilizationRate.toFixed(0)}%
                                    </div>
                                    <div className="text-xs text-gray-400">utilization</div>
                                </div>
                            </div>

                            {/* Performance Bar */}
                            <div className="mb-4">
                                <div className="flex items-center justify-between text-sm mb-1">
                                    <span className="text-gray-300">Performance</span>
                                    <span className={config.color}>{status.performance.toFixed(1)}%</span>
                                </div>
                                <div className="w-full bg-gray-700 rounded-full h-2">
                                    <motion.div
                                        className={`h-2 rounded-full bg-gradient-to-r ${config.color.replace('text-', 'from-').replace('-400', '-500')} to-opacity-60`}
                                        initial={{ width: 0 }}
                                        animate={{ width: `${status.performance}%` }}
                                        transition={{ delay: 0.5 + index * 0.1, duration: 1 }}
                                    />
                                </div>
                            </div>

                            {/* Active Tasks */}
                            <div className="space-y-2 mb-4">
                                <h4 className="text-sm font-semibold text-gray-300">Current Tasks:</h4>
                                {status.tasks.slice(0, 2).map((task, taskIndex) => (
                                    <motion.div
                                        key={taskIndex}
                                        initial={{ opacity: 0, x: -10 }}
                                        animate={{ opacity: 1, x: 0 }}
                                        transition={{ delay: 0.7 + index * 0.1 + taskIndex * 0.1 }}
                                        className="flex items-center gap-2 text-xs text-gray-400"
                                    >
                                        <CheckCircle className="w-3 h-3 text-green-400" />
                                        {task}
                                    </motion.div>
                                ))}
                            </div>

                            {/* BROski$ Rewards */}
                            <div className="flex items-center justify-between pt-3 border-t border-gray-700">
                                <span className="text-sm text-gray-400">BROski$ Earned</span>
                                <span className="font-bold text-yellow-400">
                                    {status.broSkiRewards.toLocaleString()}
                                </span>
                            </div>

                            {/* Activity Pulse */}
                            {isSystemActive && (
                                <motion.div
                                    className={`absolute top-4 right-4 w-3 h-3 rounded-full ${config.color.replace('text-', 'bg-')}`}
                                    animate={{
                                        scale: [1, 1.5, 1],
                                        opacity: [0.7, 1, 0.7]
                                    }}
                                    transition={{
                                        duration: 2,
                                        repeat: Infinity,
                                        delay: index * 0.3
                                    }}
                                />
                            )}
                        </motion.div>
                    );
                })}
            </div>

            {/* 🏆 System Summary */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 1 }}
                className="bg-gradient-to-r from-yellow-500/10 via-orange-500/10 to-red-500/10 border border-yellow-500/30 rounded-2xl p-6"
            >
                <div className="flex items-center justify-between">
                    <div>
                        <h3 className="text-xl font-bold text-yellow-400 mb-2">
                            🏆 LEGENDARY AGENT EMPIRE STATUS
                        </h3>
                        <div className="space-y-1 text-sm">
                            <div className="text-gray-300">
                                <span className="text-green-400 font-semibold">{getTotalActiveAgents()}</span> agents active out of <span className="text-blue-400 font-semibold">{getTotalAgents()}</span> total
                            </div>
                            <div className="text-gray-300">
                                Overall performance: <span className="text-purple-400 font-semibold">{getOverallPerformance().toFixed(1)}%</span>
                            </div>
                            <div className="text-gray-300">
                                Total BROski$ rewards: <span className="text-yellow-400 font-semibold">{totalBroSkiRewards.toLocaleString()}</span>
                            </div>
                        </div>
                    </div>

                    <div className="text-center">
                        <motion.div
                            className="w-20 h-20 rounded-full border-4 border-yellow-400 flex items-center justify-center mb-2"
                            animate={{ rotate: isSystemActive ? 360 : 0 }}
                            transition={{ duration: 10, repeat: Infinity, ease: "linear" }}
                        >
                            <Activity className="w-8 h-8 text-yellow-400" />
                        </motion.div>
                        <div className="text-xs text-yellow-300">COORDINATION</div>
                    </div>
                </div>
            </motion.div>
        </div>
    );
}
