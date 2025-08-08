'use client';

import { motion } from 'framer-motion';
import { Brain, Zap, Heart, Target, Activity } from 'lucide-react';

interface DopamineArchitectureProps {
    dopamineLevel: number;
    focusStreak: number;
    energyMode: string;
    interactionCount: number;
    onLevelChange: (change: number) => void;
}

export function DopamineArchitecture({
    dopamineLevel,
    focusStreak,
    energyMode,
    interactionCount,
    onLevelChange
}: DopamineArchitectureProps) {

    // ADHD DOPAMINE RESEARCH - Optimal levels and patterns
    const getDopamineColor = (level: number) => {
        if (level >= 80) return 'from-green-400 to-emerald-500';
        if (level >= 60) return 'from-blue-400 to-cyan-500';
        if (level >= 40) return 'from-yellow-400 to-orange-500';
        if (level >= 20) return 'from-orange-400 to-red-500';
        return 'from-red-400 to-pink-500';
    };

    const getDopamineEmoji = (level: number) => {
        if (level >= 80) return '🚀';
        if (level >= 60) return '⚡';
        if (level >= 40) return '🎯';
        if (level >= 20) return '🔋';
        return '😴';
    };

    const getEnergyEmoji = (mode: string) => {
        switch (mode) {
            case 'hyperfocus': return '🧠';
            case 'high': return '🔥';
            case 'balanced': return '⚖️';
            case 'low': return '🌙';
            default: return '⚡';
        }
    };

    return (
        <div className="space-y-4">
            {/* DOPAMINE LEVEL DISPLAY */}
            <motion.div
                className="bg-white/90 backdrop-blur-sm rounded-2xl p-4 border border-gray-200"
                whileHover={{ scale: 1.02, boxShadow: '0 10px 30px rgba(0,0,0,0.1)' }}
                layout
            >
                <div className="flex items-center justify-between mb-3">
                    <div className="flex items-center space-x-2">
                        <motion.div
                            animate={{
                                scale: [1, 1.1, 1],
                                rotate: [0, 5, -5, 0]
                            }}
                            transition={{
                                duration: 2,
                                repeat: Infinity,
                                ease: "easeInOut"
                            }}
                        >
                            <Brain className="w-5 h-5 text-purple-600" />
                        </motion.div>
                        <span className="font-bold text-gray-800">Dopamine Level</span>
                    </div>
                    <div className="flex items-center space-x-2">
                        <span className="text-2xl">{getDopamineEmoji(dopamineLevel)}</span>
                        <span className="font-bold text-lg text-gray-800">{dopamineLevel}%</span>
                    </div>
                </div>

                {/* ANIMATED PROGRESS BAR */}
                <div className="relative w-full bg-gray-200 rounded-full h-3 overflow-hidden">
                    <motion.div
                        className={`h-full bg-gradient-to-r ${getDopamineColor(dopamineLevel)} relative`}
                        initial={{ width: 0 }}
                        animate={{ width: `${dopamineLevel}%` }}
                        transition={{ duration: 1, ease: "easeOut" }}
                    >
                        {/* DOPAMINE PARTICLES */}
                        {dopamineLevel > 50 && (
                            <motion.div
                                className="absolute inset-0"
                                animate={{
                                    backgroundPosition: ['0% 50%', '100% 50%'],
                                }}
                                transition={{
                                    duration: 2,
                                    repeat: Infinity,
                                    ease: "linear"
                                }}
                                style={{
                                    backgroundImage: 'radial-gradient(circle, rgba(255,255,255,0.3) 1px, transparent 1px)',
                                    backgroundSize: '10px 10px'
                                }}
                            />
                        )}
                    </motion.div>
                </div>

                {/* DOPAMINE INSIGHTS */}
                <div className="mt-3 flex justify-between text-xs text-gray-600">
                    <span>
                        {dopamineLevel >= 80 ? 'LEGENDARY Focus! 🚀' :
                            dopamineLevel >= 60 ? 'Great Energy! ⚡' :
                                dopamineLevel >= 40 ? 'Steady Progress 🎯' :
                                    dopamineLevel >= 20 ? 'Need Boost 🔋' : 'Rest Time 😴'}
                    </span>
                    <span>Target: 70-90%</span>
                </div>
            </motion.div>

            {/* FOCUS STREAK TRACKER */}
            <motion.div
                className="bg-gradient-to-r from-blue-50 to-purple-50 rounded-2xl p-4 border border-blue-200"
                whileHover={{ scale: 1.02 }}
                layout
            >
                <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                        <motion.div
                            animate={{
                                scale: focusStreak > 0 ? [1, 1.2, 1] : 1,
                            }}
                            transition={{
                                duration: 1,
                                repeat: focusStreak > 0 ? Infinity : 0,
                            }}
                        >
                            <Target className="w-5 h-5 text-blue-600" />
                        </motion.div>
                        <span className="font-bold text-gray-800">Focus Streak</span>
                    </div>
                    <div className="flex items-center space-x-2">
                        {focusStreak > 0 && <span className="text-xl">🔥</span>}
                        <span className="font-bold text-lg text-blue-600">{focusStreak}</span>
                    </div>
                </div>

                {/* STREAK VISUALIZATION */}
                {focusStreak > 0 && (
                    <div className="mt-3 flex space-x-1">
                        {Array.from({ length: Math.min(focusStreak, 10) }).map((_, i) => (
                            <motion.div
                                key={i}
                                className="w-3 h-3 bg-gradient-to-t from-blue-400 to-purple-500 rounded-full"
                                initial={{ scale: 0, opacity: 0 }}
                                animate={{ scale: 1, opacity: 1 }}
                                transition={{ delay: i * 0.1 }}
                            />
                        ))}
                        {focusStreak > 10 && (
                            <span className="text-xs text-gray-600 ml-2">+{focusStreak - 10} more</span>
                        )}
                    </div>
                )}
            </motion.div>

            {/* ENERGY MODE STATUS */}
            <motion.div
                className={`rounded-2xl p-4 border ${energyMode === 'hyperfocus' ? 'bg-purple-50 border-purple-200' :
                        energyMode === 'high' ? 'bg-green-50 border-green-200' :
                            energyMode === 'balanced' ? 'bg-blue-50 border-blue-200' :
                                'bg-gray-50 border-gray-200'
                    }`}
                whileHover={{ scale: 1.02 }}
                layout
            >
                <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                        <motion.div
                            animate={{
                                rotateY: [0, 360],
                            }}
                            transition={{
                                duration: 3,
                                repeat: Infinity,
                                ease: "linear"
                            }}
                        >
                            <Activity className={`w-5 h-5 ${energyMode === 'hyperfocus' ? 'text-purple-600' :
                                    energyMode === 'high' ? 'text-green-600' :
                                        energyMode === 'balanced' ? 'text-blue-600' :
                                            'text-gray-600'
                                }`} />
                        </motion.div>
                        <span className="font-bold text-gray-800">Energy Mode</span>
                    </div>
                    <div className="flex items-center space-x-2">
                        <span className="text-xl">{getEnergyEmoji(energyMode)}</span>
                        <span className={`font-bold capitalize ${energyMode === 'hyperfocus' ? 'text-purple-600' :
                                energyMode === 'high' ? 'text-green-600' :
                                    energyMode === 'balanced' ? 'text-blue-600' :
                                        'text-gray-600'
                            }`}>
                            {energyMode}
                        </span>
                    </div>
                </div>

                {/* ENERGY MODE DESCRIPTION */}
                <div className="mt-2 text-xs text-gray-600">
                    {energyMode === 'hyperfocus' && 'Deep focus activated - minimize distractions'}
                    {energyMode === 'high' && 'High energy detected - perfect for complex tasks'}
                    {energyMode === 'balanced' && 'Steady energy - ideal for regular work'}
                    {energyMode === 'low' && 'Low energy mode - consider taking a break'}
                </div>
            </motion.div>

            {/* INTERACTION ANALYTICS */}
            <motion.div
                className="bg-gradient-to-r from-yellow-50 to-orange-50 rounded-2xl p-4 border border-yellow-200"
                whileHover={{ scale: 1.02 }}
                layout
            >
                <div className="flex items-center justify-between">
                    <div className="flex items-center space-x-2">
                        <motion.div
                            animate={{
                                scale: [1, 1.1, 1],
                            }}
                            transition={{
                                duration: 1.5,
                                repeat: Infinity,
                            }}
                        >
                            <Heart className="w-5 h-5 text-orange-600" />
                        </motion.div>
                        <span className="font-bold text-gray-800">Engagement</span>
                    </div>
                    <div className="flex items-center space-x-2">
                        <span className="text-xl">💫</span>
                        <span className="font-bold text-lg text-orange-600">{interactionCount}</span>
                    </div>
                </div>

                {/* ENGAGEMENT LEVEL */}
                <div className="mt-2 text-xs text-gray-600">
                    {interactionCount >= 50 ? 'LEGENDARY engagement! 🚀' :
                        interactionCount >= 30 ? 'High engagement! ⚡' :
                            interactionCount >= 15 ? 'Good activity level 👍' :
                                interactionCount >= 5 ? 'Getting started 🌱' : 'Welcome! Start exploring 👋'}
                </div>
            </motion.div>

            {/* DOPAMINE BOOST BUTTONS */}
            <div className="grid grid-cols-2 gap-3">
                <motion.button
                    className="bg-gradient-to-r from-green-400 to-emerald-500 text-white rounded-xl p-3 font-bold text-sm"
                    whileHover={{ scale: 1.05, boxShadow: '0 5px 15px rgba(34, 197, 94, 0.3)' }}
                    whileTap={{ scale: 0.95 }}
                    onClick={() => onLevelChange(5)}
                >
                    🎯 Quick Win
                </motion.button>

                <motion.button
                    className="bg-gradient-to-r from-purple-400 to-pink-500 text-white rounded-xl p-3 font-bold text-sm"
                    whileHover={{ scale: 1.05, boxShadow: '0 5px 15px rgba(168, 85, 247, 0.3)' }}
                    whileTap={{ scale: 0.95 }}
                    onClick={() => onLevelChange(10)}
                >
                    🚀 Big Achievement
                </motion.button>
            </div>
        </div>
    );
}
