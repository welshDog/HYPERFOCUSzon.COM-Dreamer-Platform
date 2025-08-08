'use client';

import React, { useState, useEffect, useCallback, useRef } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
    Code2,
    Bug,
    Search,
    Terminal,
    FileText,
    Eye,
    BarChart3,
    Layers,
    GitBranch,
    Cpu,
    Database,
    Network,
    AlertCircle,
    CheckCircle,
    XCircle,
    Info,
    Settings,
    Filter,
    Download,
    Play,
    Pause,
    RefreshCw,
    Zap,
    Brain,
    Target
} from 'lucide-react';

// 🔧 Debug Log Interface
interface DebugLog {
    id: string;
    timestamp: Date;
    level: 'error' | 'warn' | 'info' | 'debug';
    category: string;
    message: string;
    data?: any;
    source: string;
    performance?: {
        duration: number;
        memory: number;
    };
}

// 📊 Analytics Data Interface
interface AnalyticsData {
    pageViews: number;
    uniqueUsers: number;
    sessionDuration: number;
    bounceRate: number;
    dopamineInteractions: number;
    celebrationTriggers: number;
    energyModeChanges: number;
    memoryAccess: number;
    broSkiEarned: number;
}

// 🎯 Performance Profiler Interface
interface PerformanceProfile {
    componentName: string;
    renderTime: number;
    renderCount: number;
    memoryUsage: number;
    lastRender: Date;
    isOptimized: boolean;
}

export default function DeveloperToolsSuite() {
    const [debugLogs, setDebugLogs] = useState<DebugLog[]>([]);
    const [analytics, setAnalytics] = useState<AnalyticsData>({
        pageViews: 1247,
        uniqueUsers: 389,
        sessionDuration: 345,
        bounceRate: 23.5,
        dopamineInteractions: 2158,
        celebrationTriggers: 567,
        energyModeChanges: 89,
        memoryAccess: 445,
        broSkiEarned: 15750
    });
    const [performanceProfiles, setPerformanceProfiles] = useState<PerformanceProfile[]>([]);
    const [isDebuggerActive, setIsDebuggerActive] = useState(true);
    const [filterLevel, setFilterLevel] = useState<string>('all');
    const [selectedCategory, setSelectedCategory] = useState<string>('all');
    const intervalRef = useRef<NodeJS.Timeout>();
    const logContainerRef = useRef<HTMLDivElement>(null);

    // 🎨 Log Level Colors
    const logColors = {
        error: 'text-red-400 bg-red-500/10 border-red-500/30',
        warn: 'text-yellow-400 bg-yellow-500/10 border-yellow-500/30',
        info: 'text-blue-400 bg-blue-500/10 border-blue-500/30',
        debug: 'text-gray-400 bg-gray-500/10 border-gray-500/30'
    };

    const logIcons = {
        error: XCircle,
        warn: AlertCircle,
        info: Info,
        debug: Code2
    };

    // 🔄 Generate Mock Debug Logs
    const generateMockLog = useCallback((): DebugLog => {
        const levels: ('error' | 'warn' | 'info' | 'debug')[] = ['error', 'warn', 'info', 'debug'];
        const categories = ['dopamine', 'performance', 'agent-integration', 'ui-interaction', 'memory-crystal', 'celebration'];
        const sources = ['AgentIntegrationHub', 'DopamineArchitecture', 'MemoryCrystal', 'CelebrationSystem', 'PerformanceOptimizer'];

        const messages = {
            dopamine: [
                'Dopamine level increased to 85%',
                'Focus streak milestone reached: 5x multiplier',
                'Energy mode switched to hyperfocus',
                'Celebration trigger activated'
            ],
            performance: [
                'Component rendered in 12ms',
                'Bundle optimization complete: -150KB',
                'Cache hit rate: 94.5%',
                'Frame rate stabilized at 60fps'
            ],
            'agent-integration': [
                'Security agents: 89/89 active',
                'Agent coordination at 98.7%',
                'Real-time sync successful',
                'BROski$ rewards distributed: +250'
            ],
            'ui-interaction': [
                'Memory crystal hover detected',
                'Tag click interaction processed',
                'Smooth scroll animation complete',
                'Accessibility focus ring applied'
            ],
            'memory-crystal': [
                'Memory crystal data loaded',
                'Emotion mapping updated',
                'Crystal animation sequence started',
                'Metadata extraction complete'
            ],
            celebration: [
                'Epic celebration triggered',
                'Particle system initialized',
                'Achievement unlocked notification',
                'Celebration cascade complete'
            ]
        };

        const level = levels[Math.floor(Math.random() * levels.length)];
        const category = categories[Math.floor(Math.random() * categories.length)];
        const source = sources[Math.floor(Math.random() * sources.length)];
        const categoryMessages = messages[category as keyof typeof messages];
        const message = categoryMessages[Math.floor(Math.random() * categoryMessages.length)];

        return {
            id: `log-${Date.now()}-${Math.random().toString(36).substr(2, 9)}`,
            timestamp: new Date(),
            level,
            category,
            message,
            source,
            data: level === 'error' ? { stack: 'MockStackTrace', code: 'ERR_MOCK' } : undefined,
            performance: {
                duration: Math.random() * 50,
                memory: Math.random() * 10
            }
        };
    }, []);

    // 🚀 Start Debug Logging
    useEffect(() => {
        if (isDebuggerActive) {
            intervalRef.current = setInterval(() => {
                const newLog = generateMockLog();
                setDebugLogs(prev => {
                    const updated = [newLog, ...prev];
                    return updated.length > 100 ? updated.slice(0, 100) : updated;
                });

                // Update analytics
                setAnalytics(prev => ({
                    ...prev,
                    dopamineInteractions: prev.dopamineInteractions + Math.floor(Math.random() * 3),
                    celebrationTriggers: prev.celebrationTriggers + (Math.random() > 0.8 ? 1 : 0),
                    broSkiEarned: prev.broSkiEarned + Math.floor(Math.random() * 25)
                }));

                // Update performance profiles
                setPerformanceProfiles(prev => {
                    const components = ['DopamineArchitecture', 'AgentIntegrationHub', 'MemoryCrystal', 'CelebrationSystem'];
                    const randomComponent = components[Math.floor(Math.random() * components.length)];

                    const existingIndex = prev.findIndex(p => p.componentName === randomComponent);
                    if (existingIndex >= 0) {
                        const updated = [...prev];
                        updated[existingIndex] = {
                            ...updated[existingIndex],
                            renderTime: Math.random() * 20,
                            renderCount: updated[existingIndex].renderCount + 1,
                            memoryUsage: Math.random() * 5,
                            lastRender: new Date()
                        };
                        return updated;
                    } else {
                        return [...prev, {
                            componentName: randomComponent,
                            renderTime: Math.random() * 20,
                            renderCount: 1,
                            memoryUsage: Math.random() * 5,
                            lastRender: new Date(),
                            isOptimized: Math.random() > 0.3
                        }];
                    }
                });
            }, 1500);
        }

        return () => {
            if (intervalRef.current) {
                clearInterval(intervalRef.current);
            }
        };
    }, [isDebuggerActive, generateMockLog]);

    // 📊 Filter Logs
    const filteredLogs = debugLogs.filter(log => {
        if (filterLevel !== 'all' && log.level !== filterLevel) return false;
        if (selectedCategory !== 'all' && log.category !== selectedCategory) return false;
        return true;
    });

    // 🎯 Analytics Summary
    const getAnalyticsSummary = () => {
        return [
            { label: 'Page Views', value: analytics.pageViews.toLocaleString(), change: '+12%', color: 'text-blue-400' },
            { label: 'Unique Users', value: analytics.uniqueUsers.toLocaleString(), change: '+8%', color: 'text-green-400' },
            { label: 'Avg Session', value: `${Math.floor(analytics.sessionDuration / 60)}m ${analytics.sessionDuration % 60}s`, change: '+15%', color: 'text-purple-400' },
            { label: 'Bounce Rate', value: `${analytics.bounceRate.toFixed(1)}%`, change: '-5%', color: 'text-yellow-400' }
        ];
    };

    // 🔧 Developer Actions
    const clearLogs = () => setDebugLogs([]);
    const exportLogs = () => {
        const dataStr = JSON.stringify(debugLogs, null, 2);
        const dataUri = 'data:application/json;charset=utf-8,' + encodeURIComponent(dataStr);
        const exportFileDefaultName = `debug-logs-${new Date().toISOString().split('T')[0]}.json`;

        const linkElement = document.createElement('a');
        linkElement.setAttribute('href', dataUri);
        linkElement.setAttribute('download', exportFileDefaultName);
        linkElement.click();
    };

    return (
        <div className="space-y-6">
            {/* 🔧 Developer Tools Header */}
            <motion.div
                initial={{ opacity: 0, y: -20 }}
                animate={{ opacity: 1, y: 0 }}
                className="relative overflow-hidden rounded-2xl bg-gradient-to-r from-green-600/20 via-blue-600/20 to-purple-600/20 border border-green-500/30 p-6"
            >
                <div className="flex items-center justify-between">
                    <div className="space-y-2">
                        <h2 className="text-2xl font-bold text-white flex items-center gap-3">
                            <Terminal className="w-8 h-8 text-green-400" />
                            🔧 DEVELOPER TOOLS SUITE
                            <span className="text-green-400">({filteredLogs.length} logs)</span>
                        </h2>
                        <p className="text-green-200">
                            Advanced debugging, analytics & performance profiling for ADHD-optimized development
                        </p>
                    </div>

                    <div className="flex gap-2">
                        <motion.button
                            whileHover={{ scale: 1.05 }}
                            whileTap={{ scale: 0.95 }}
                            onClick={() => setIsDebuggerActive(!isDebuggerActive)}
                            className={`flex items-center gap-2 px-4 py-2 rounded-xl font-semibold transition-colors ${isDebuggerActive
                                    ? 'bg-green-500/20 text-green-400 border border-green-500/30'
                                    : 'bg-gray-500/20 text-gray-400 border border-gray-500/30'
                                }`}
                        >
                            {isDebuggerActive ? <Pause className="w-4 h-4" /> : <Play className="w-4 h-4" />}
                            {isDebuggerActive ? 'ACTIVE' : 'PAUSED'}
                        </motion.button>

                        <motion.button
                            whileHover={{ scale: 1.05 }}
                            whileTap={{ scale: 0.95 }}
                            onClick={exportLogs}
                            className="flex items-center gap-2 px-4 py-2 rounded-xl font-semibold bg-blue-500/20 text-blue-400 border border-blue-500/30 hover:bg-blue-500/30 transition-colors"
                        >
                            <Download className="w-4 h-4" />
                            EXPORT
                        </motion.button>
                    </div>
                </div>

                {/* Activity Indicator */}
                {isDebuggerActive && (
                    <motion.div
                        className="absolute bottom-0 left-0 right-0 h-1 bg-gradient-to-r from-green-500 via-blue-500 to-purple-500"
                        animate={{
                            scaleX: [0, 1, 0],
                            opacity: [0.3, 1, 0.3]
                        }}
                        transition={{
                            duration: 2,
                            repeat: Infinity,
                            ease: "easeInOut"
                        }}
                        style={{ transformOrigin: 'left' }}
                    />
                )}
            </motion.div>

            {/* 📊 Analytics Dashboard */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.1 }}
            >
                <h3 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
                    <BarChart3 className="w-5 h-5 text-blue-400" />
                    Real-time Analytics
                </h3>

                <div className="grid grid-cols-2 md:grid-cols-4 gap-4 mb-6">
                    {getAnalyticsSummary().map((metric, index) => (
                        <motion.div
                            key={metric.label}
                            initial={{ opacity: 0, scale: 0.9 }}
                            animate={{ opacity: 1, scale: 1 }}
                            transition={{ delay: 0.2 + index * 0.1 }}
                            className="bg-gradient-to-br from-gray-800/50 to-gray-900/50 border border-gray-700 rounded-xl p-4"
                        >
                            <div className="text-sm text-gray-400 mb-1">{metric.label}</div>
                            <div className={`text-xl font-bold ${metric.color} mb-1`}>{metric.value}</div>
                            <div className="text-xs text-green-400">{metric.change} vs last hour</div>
                        </motion.div>
                    ))}
                </div>

                {/* ADHD-Specific Metrics */}
                <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
                    <div className="bg-gradient-to-br from-purple-500/10 to-pink-500/10 border border-purple-500/20 rounded-xl p-4">
                        <div className="flex items-center gap-2 mb-2">
                            <Brain className="w-5 h-5 text-purple-400" />
                            <span className="text-purple-400 font-semibold">Dopamine Interactions</span>
                        </div>
                        <div className="text-2xl font-bold text-white">{analytics.dopamineInteractions.toLocaleString()}</div>
                        <div className="text-sm text-purple-300">+{Math.floor(Math.random() * 50)} this hour</div>
                    </div>

                    <div className="bg-gradient-to-br from-yellow-500/10 to-orange-500/10 border border-yellow-500/20 rounded-xl p-4">
                        <div className="flex items-center gap-2 mb-2">
                            <Zap className="w-5 h-5 text-yellow-400" />
                            <span className="text-yellow-400 font-semibold">Celebration Triggers</span>
                        </div>
                        <div className="text-2xl font-bold text-white">{analytics.celebrationTriggers.toLocaleString()}</div>
                        <div className="text-sm text-yellow-300">Epic: {Math.floor(analytics.celebrationTriggers * 0.3)}</div>
                    </div>

                    <div className="bg-gradient-to-br from-green-500/10 to-emerald-500/10 border border-green-500/20 rounded-xl p-4">
                        <div className="flex items-center gap-2 mb-2">
                            <Target className="w-5 h-5 text-green-400" />
                            <span className="text-green-400 font-semibold">BROski$ Earned</span>
                        </div>
                        <div className="text-2xl font-bold text-white">{analytics.broSkiEarned.toLocaleString()}</div>
                        <div className="text-sm text-green-300">Avg: {Math.floor(analytics.broSkiEarned / analytics.uniqueUsers)} per user</div>
                    </div>
                </div>
            </motion.div>

            {/* 🔍 Debug Log Filters */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.3 }}
                className="flex flex-wrap gap-4 items-center justify-between bg-gray-800/30 border border-gray-700 rounded-xl p-4"
            >
                <div className="flex items-center gap-4">
                    <div className="flex items-center gap-2">
                        <Filter className="w-4 h-4 text-gray-400" />
                        <span className="text-sm text-gray-400">Filter by level:</span>
                        <select
                            value={filterLevel}
                            onChange={(e) => setFilterLevel(e.target.value)}
                            className="bg-gray-700 border border-gray-600 rounded-lg px-3 py-1 text-sm text-white focus:border-blue-500 focus:outline-none"
                            aria-label="Filter debug logs by level"
                        >
                            <option value="all">All Levels</option>
                            <option value="error">Errors</option>
                            <option value="warn">Warnings</option>
                            <option value="info">Info</option>
                            <option value="debug">Debug</option>
                        </select>
                    </div>

                    <div className="flex items-center gap-2">
                        <span className="text-sm text-gray-400">Category:</span>
                        <select
                            value={selectedCategory}
                            onChange={(e) => setSelectedCategory(e.target.value)}
                            className="bg-gray-700 border border-gray-600 rounded-lg px-3 py-1 text-sm text-white focus:border-blue-500 focus:outline-none"
                            aria-label="Filter debug logs by category"
                        >
                            <option value="all">All Categories</option>
                            <option value="dopamine">Dopamine</option>
                            <option value="performance">Performance</option>
                            <option value="agent-integration">Agent Integration</option>
                            <option value="ui-interaction">UI Interaction</option>
                            <option value="memory-crystal">Memory Crystal</option>
                            <option value="celebration">Celebration</option>
                        </select>
                    </div>
                </div>

                <motion.button
                    whileHover={{ scale: 1.05 }}
                    whileTap={{ scale: 0.95 }}
                    onClick={clearLogs}
                    className="flex items-center gap-2 px-3 py-1 rounded-lg bg-red-500/20 text-red-400 border border-red-500/30 hover:bg-red-500/30 transition-colors text-sm"
                >
                    <RefreshCw className="w-4 h-4" />
                    Clear Logs
                </motion.button>
            </motion.div>

            {/* 📝 Debug Log Console */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.4 }}
                className="bg-gray-900/50 border border-gray-700 rounded-xl p-4"
            >
                <h3 className="text-lg font-bold text-white mb-4 flex items-center gap-2">
                    <Bug className="w-5 h-5 text-red-400" />
                    Debug Console ({filteredLogs.length} entries)
                </h3>

                <div
                    ref={logContainerRef}
                    className="max-h-96 overflow-y-auto space-y-2 font-mono text-sm"
                >
                    <AnimatePresence>
                        {filteredLogs.map((log, index) => {
                            const IconComponent = logIcons[log.level];
                            return (
                                <motion.div
                                    key={log.id}
                                    initial={{ opacity: 0, x: -20 }}
                                    animate={{ opacity: 1, x: 0 }}
                                    exit={{ opacity: 0, x: 20 }}
                                    transition={{ delay: index * 0.02 }}
                                    className={`flex items-start gap-3 p-3 rounded-lg border ${logColors[log.level]}`}
                                >
                                    <IconComponent className="w-4 h-4 mt-0.5 flex-shrink-0" />

                                    <div className="flex-1 min-w-0">
                                        <div className="flex items-center gap-2 mb-1">
                                            <span className="font-semibold">[{log.source}]</span>
                                            <span className="text-xs text-gray-500">
                                                {log.timestamp.toLocaleTimeString()}
                                            </span>
                                            <span className="text-xs bg-gray-700 px-2 py-0.5 rounded">
                                                {log.category}
                                            </span>
                                        </div>

                                        <div className="text-white mb-1">{log.message}</div>

                                        {log.performance && (
                                            <div className="text-xs text-gray-400">
                                                Duration: {log.performance.duration.toFixed(2)}ms |
                                                Memory: {log.performance.memory.toFixed(2)}MB
                                            </div>
                                        )}

                                        {log.data && (
                                            <details className="mt-2">
                                                <summary className="text-xs text-gray-400 cursor-pointer hover:text-gray-300">
                                                    Show Details
                                                </summary>
                                                <pre className="mt-1 text-xs text-gray-500 bg-gray-800 p-2 rounded overflow-x-auto">
                                                    {JSON.stringify(log.data, null, 2)}
                                                </pre>
                                            </details>
                                        )}
                                    </div>
                                </motion.div>
                            );
                        })}
                    </AnimatePresence>
                </div>
            </motion.div>

            {/* 🏆 Performance Profiler */}
            <motion.div
                initial={{ opacity: 0, y: 20 }}
                animate={{ opacity: 1, y: 0 }}
                transition={{ delay: 0.6 }}
                className="bg-gradient-to-br from-blue-500/10 to-purple-500/10 border border-blue-500/20 rounded-2xl p-6"
            >
                <h3 className="text-xl font-bold text-blue-400 mb-4 flex items-center gap-2">
                    <Cpu className="w-6 h-6" />
                    Component Performance Profiler
                </h3>

                <div className="space-y-3">
                    {performanceProfiles.map((profile, index) => (
                        <motion.div
                            key={profile.componentName}
                            initial={{ opacity: 0, x: -20 }}
                            animate={{ opacity: 1, x: 0 }}
                            transition={{ delay: 0.7 + index * 0.1 }}
                            className="flex items-center justify-between bg-gray-800/50 border border-gray-700 rounded-lg p-4"
                        >
                            <div className="flex items-center gap-4">
                                <div className={`w-3 h-3 rounded-full ${profile.isOptimized ? 'bg-green-400' : 'bg-yellow-400'}`} />
                                <div>
                                    <div className="font-semibold text-white">{profile.componentName}</div>
                                    <div className="text-sm text-gray-400">
                                        Rendered {profile.renderCount} times |
                                        Last: {profile.lastRender.toLocaleTimeString()}
                                    </div>
                                </div>
                            </div>

                            <div className="text-right">
                                <div className="text-sm text-blue-400">
                                    {profile.renderTime.toFixed(2)}ms render
                                </div>
                                <div className="text-xs text-gray-400">
                                    {profile.memoryUsage.toFixed(2)}MB memory
                                </div>
                            </div>
                        </motion.div>
                    ))}
                </div>
            </motion.div>
        </div>
    );
}
