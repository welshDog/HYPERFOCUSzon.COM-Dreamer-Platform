'use client';

import { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import {
    Brain,
    Zap,
    Gem,
    BookOpen,
    Trophy,
    Heart,
    Sparkles,
    MessageCircle,
    Search,
    Filter,
    Star
} from 'lucide-react';

interface MemoryCrystal {
    id: string;
    title: string;
    category: string;
    broskiValue: number;
    date: string;
    emoji: string;
    preview: string;
    tags: string[];
}

export default function UltraDookPortal() {
    const [selectedCategory, setSelectedCategory] = useState('all');
    const [searchQuery, setSearchQuery] = useState('');
    const [broskiScore, setBroskiScore] = useState(43000);
    const [celebrationActive, setCelebrationActive] = useState(false);
    const [hyperfocusMode, setHyperfocusMode] = useState(false);

    // Mock Memory Crystals data
    const memoryCrystals: MemoryCrystal[] = [
        {
            id: '1',
            title: 'The BROski$ Economy Breakthrough',
            category: 'creative_explosions',
            broskiValue: 4000,
            date: '2025-07-05',
            emoji: '💰',
            preview: 'Gamifying ADHD motivation with a revolutionary reward system...',
            tags: ['economy', 'gamification', 'adhd', 'breakthrough']
        },
        {
            id: '2',
            title: 'The Family Empire Command Center',
            category: 'empire_building',
            broskiValue: 4000,
            date: '2025-07-06',
            emoji: '🏰',
            preview: 'Real-time ADHD-optimized business management dashboard...',
            tags: ['command center', 'family', 'business', 'dashboard']
        },
        {
            id: '3',
            title: 'The 4-Hour Hyperfocus Code Marathon',
            category: 'hyperfocus_sessions',
            broskiValue: 5000,
            date: '2025-07-06',
            emoji: '⚡',
            preview: 'Epic coding session that built the entire Agent Army...',
            tags: ['hyperfocus', 'coding', 'agent army', 'marathon']
        }
    ];

    const categories = [
        { id: 'all', name: 'All Crystals', emoji: '💎', count: memoryCrystals.length },
        { id: 'hyperfocus_sessions', name: 'Hyperfocus Sessions', emoji: '⚡', count: 1 },
        { id: 'automation_victories', name: 'Automation Victories', emoji: '🤖', count: 0 },
        { id: 'creative_explosions', name: 'Creative Explosions', emoji: '💡', count: 1 },
        { id: 'empire_building', name: 'Empire Building', emoji: '🏰', count: 1 },
        { id: 'technical_breakthroughs', name: 'Tech Breakthroughs', emoji: '💻', count: 0 },
    ];

    const triggerCelebration = () => {
        setCelebrationActive(true);
        setBroskiScore(prev => prev + 100);
        setTimeout(() => setCelebrationActive(false), 2000);
    };

    const filteredCrystals = memoryCrystals.filter(crystal => {
        const matchesCategory = selectedCategory === 'all' || crystal.category === selectedCategory;
        const matchesSearch = crystal.title.toLowerCase().includes(searchQuery.toLowerCase()) ||
            crystal.preview.toLowerCase().includes(searchQuery.toLowerCase()) ||
            crystal.tags.some(tag => tag.toLowerCase().includes(searchQuery.toLowerCase()));
        return matchesCategory && matchesSearch;
    });

    return (
        <div className={`min-h-screen transition-all duration-500 ${hyperfocusMode
                ? 'bg-gradient-to-br from-hyperfocus-900 via-hyperfocus-800 to-broski-900'
                : 'bg-gradient-to-br from-broski-50 via-hyperfocus-50 to-crystal-50'
            }`}>

            {/* Celebration Overlay */}
            <AnimatePresence>
                {celebrationActive && (
                    <motion.div
                        initial={{ opacity: 0, scale: 0 }}
                        animate={{ opacity: 1, scale: 1 }}
                        exit={{ opacity: 0, scale: 0 }}
                        className="fixed inset-0 flex items-center justify-center z-50 pointer-events-none"
                    >
                        <div className="text-6xl">🎊✨💎🚀⚡</div>
                    </motion.div>
                )}
            </AnimatePresence>

            {/* Header */}
            <header className={`sticky top-0 z-40 backdrop-blur-md border-b transition-all ${hyperfocusMode
                    ? 'bg-hyperfocus-900/80 border-hyperfocus-700 text-white'
                    : 'bg-white/80 border-broski-200'
                }`}>
                <div className="max-w-7xl mx-auto px-4 py-4">
                    <div className="flex items-center justify-between">

                        {/* Logo & Title */}
                        <motion.div
                            className="flex items-center space-x-3"
                            whileHover={{ scale: 1.05 }}
                            onClick={triggerCelebration}
                        >
                            <div className="relative">
                                <Brain className={`w-8 h-8 ${hyperfocusMode ? 'text-hyperfocus-400' : 'text-broski-600'}`} />
                                <Zap className="w-4 h-4 text-celebration-500 absolute -top-1 -right-1" />
                            </div>
                            <div>
                                <h1 className={`text-2xl font-bold ${hyperfocusMode ? 'text-white' : 'text-broski-900'}`}>
                                    🧠⚡💎 Ultra dOoK Portal
                                </h1>
                                <p className={`text-sm ${hyperfocusMode ? 'text-hyperfocus-300' : 'text-broski-600'}`}>
                                    ADHD-Optimized Memory Crystal System
                                </p>
                            </div>
                        </motion.div>

                        {/* Controls */}
                        <div className="flex items-center space-x-4">
                            <div className={`flex items-center space-x-2 px-3 py-2 rounded-xl ${hyperfocusMode ? 'bg-hyperfocus-800' : 'bg-broski-100'
                                }`}>
                                <Gem className="w-5 h-5 text-celebration-500" />
                                <span className={`font-bold ${hyperfocusMode ? 'text-white' : 'text-broski-900'}`}>
                                    {broskiScore.toLocaleString()} BROski$
                                </span>
                            </div>

                            <motion.button
                                whileHover={{ scale: 1.05 }}
                                whileTap={{ scale: 0.95 }}
                                onClick={() => setHyperfocusMode(!hyperfocusMode)}
                                className={`px-4 py-2 rounded-xl font-medium transition-all ${hyperfocusMode
                                        ? 'bg-hyperfocus-600 text-white hover:bg-hyperfocus-500'
                                        : 'bg-hyperfocus-500 text-white hover:bg-hyperfocus-600'
                                    } ${hyperfocusMode ? 'animate-hyperfocus' : ''}`}
                            >
                                {hyperfocusMode ? '🧠 HYPER MODE' : '⚡ ACTIVATE HYPER'}
                            </motion.button>
                        </div>
                    </div>
                </div>
            </header>

            <div className="max-w-7xl mx-auto px-4 py-8">

                {/* Search & Filter Bar */}
                <div className="mb-8">
                    <div className="flex flex-col md:flex-row md:items-center space-y-4 md:space-y-0 md:space-x-4">
                        <div className="relative flex-1">
                            <Search className={`w-5 h-5 absolute left-3 top-1/2 transform -translate-y-1/2 ${hyperfocusMode ? 'text-hyperfocus-400' : 'text-broski-400'
                                }`} />
                            <input
                                type="text"
                                placeholder="Search your memory crystals..."
                                value={searchQuery}
                                onChange={(e) => setSearchQuery(e.target.value)}
                                className={`w-full pl-10 pr-4 py-3 rounded-xl border-2 transition-all focus:outline-none focus:ring-2 ${hyperfocusMode
                                        ? 'bg-hyperfocus-800 border-hyperfocus-600 text-white placeholder-hyperfocus-400 focus:ring-hyperfocus-400'
                                        : 'bg-white border-broski-200 focus:ring-broski-400 focus:border-broski-400'
                                    }`}
                            />
                        </div>

                        <div className="relative">
                            <Filter className={`w-5 h-5 absolute left-3 top-1/2 transform -translate-y-1/2 ${hyperfocusMode ? 'text-hyperfocus-400' : 'text-broski-400'
                                }`} />
                            <select
                                value={selectedCategory}
                                onChange={(e) => setSelectedCategory(e.target.value)}
                                className={`pl-10 pr-8 py-3 rounded-xl border-2 transition-all focus:outline-none focus:ring-2 ${hyperfocusMode
                                        ? 'bg-hyperfocus-800 border-hyperfocus-600 text-white focus:ring-hyperfocus-400'
                                        : 'bg-white border-broski-200 focus:ring-broski-400 focus:border-broski-400'
                                    }`}
                            >
                                {categories.map(category => (
                                    <option key={category.id} value={category.id}>
                                        {category.emoji} {category.name} ({category.count})
                                    </option>
                                ))}
                            </select>
                        </div>
                    </div>
                </div>

                {/* Memory Crystals Grid */}
                <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
                    <AnimatePresence>
                        {filteredCrystals.map((crystal, index) => (
                            <motion.div
                                key={crystal.id}
                                initial={{ opacity: 0, y: 20 }}
                                animate={{ opacity: 1, y: 0 }}
                                exit={{ opacity: 0, y: -20 }}
                                transition={{ delay: index * 0.1 }}
                                whileHover={{
                                    scale: 1.03,
                                    boxShadow: hyperfocusMode
                                        ? '0 20px 40px rgba(168, 85, 247, 0.3)'
                                        : '0 20px 40px rgba(59, 130, 246, 0.2)'
                                }}
                                className={`p-6 rounded-2xl border-2 cursor-pointer transition-all ${hyperfocusMode
                                        ? 'bg-hyperfocus-800/50 border-hyperfocus-600 hover:border-hyperfocus-400'
                                        : 'bg-white border-broski-200 hover:border-broski-400'
                                    }`}
                                onClick={triggerCelebration}
                            >
                                <div className="flex items-start justify-between mb-4">
                                    <div className="text-3xl">{crystal.emoji}</div>
                                    <div className={`flex items-center space-x-1 px-2 py-1 rounded-lg text-xs font-medium ${hyperfocusMode
                                            ? 'bg-celebration-800 text-celebration-200'
                                            : 'bg-celebration-100 text-celebration-800'
                                        }`}>
                                        <Star className="w-3 h-3" />
                                        <span>{crystal.broskiValue.toLocaleString()}</span>
                                    </div>
                                </div>

                                <h3 className={`text-lg font-bold mb-2 line-clamp-2 ${hyperfocusMode ? 'text-white' : 'text-broski-900'
                                    }`}>
                                    {crystal.title}
                                </h3>

                                <p className={`text-sm mb-4 line-clamp-3 ${hyperfocusMode ? 'text-hyperfocus-300' : 'text-broski-600'
                                    }`}>
                                    {crystal.preview}
                                </p>

                                <div className="flex flex-wrap gap-2 mb-4">
                                    {crystal.tags.slice(0, 3).map(tag => (
                                        <span
                                            key={tag}
                                            className={`px-2 py-1 rounded-lg text-xs font-medium ${hyperfocusMode
                                                    ? 'bg-hyperfocus-700 text-hyperfocus-200'
                                                    : 'bg-broski-100 text-broski-700'
                                                }`}
                                        >
                                            #{tag}
                                        </span>
                                    ))}
                                </div>

                                <div className={`flex items-center justify-between text-xs ${hyperfocusMode ? 'text-hyperfocus-400' : 'text-broski-500'
                                    }`}>
                                    <span>{crystal.date}</span>
                                    <div className="flex items-center space-x-1">
                                        <Heart className="w-3 h-3" />
                                        <MessageCircle className="w-3 h-3" />
                                        <BookOpen className="w-3 h-3" />
                                    </div>
                                </div>
                            </motion.div>
                        ))}
                    </AnimatePresence>
                </div>

                {/* Empty State */}
                {filteredCrystals.length === 0 && (
                    <motion.div
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        className="text-center py-12"
                    >
                        <div className="text-6xl mb-4">🔍</div>
                        <h3 className={`text-xl font-bold mb-2 ${hyperfocusMode ? 'text-white' : 'text-broski-900'}`}>
                            No Memory Crystals Found
                        </h3>
                        <p className={`${hyperfocusMode ? 'text-hyperfocus-300' : 'text-broski-600'}`}>
                            Try adjusting your search or category filter
                        </p>
                    </motion.div>
                )}
            </div>

            {/* Footer */}
            <footer className={`mt-16 py-8 border-t ${hyperfocusMode
                    ? 'border-hyperfocus-700 bg-hyperfocus-900/50'
                    : 'border-broski-200 bg-white/50'
                }`}>
                <div className="max-w-7xl mx-auto px-4 text-center">
                    <p className={`text-sm ${hyperfocusMode ? 'text-hyperfocus-300' : 'text-broski-600'}`}>
                        🚀 Ultra dOoK Portal v1.0 | Built with 💎 by BROski♾️ & The Hyperfocus Zone Empire
                    </p>
                    <div className="mt-2">
                        <span className={`text-xs ${hyperfocusMode ? 'text-hyperfocus-400' : 'text-broski-500'}`}>
                            ADHD-Optimized • Neurodivergent-Friendly • Dopamine-Maximized
                        </span>
                    </div>
                </div>
            </footer>
        </div>
    );
}
