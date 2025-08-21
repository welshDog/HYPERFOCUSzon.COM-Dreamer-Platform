
import React from 'react';
import { LineChart, Line, ResponsiveContainer } from 'recharts';

interface StatCardProps {
    icon: React.ReactNode;
    title: string;
    value: string;
    subtitle?: string;
    trend?: number[];
    color?: 'cyan' | 'amber' | 'violet' | 'green'
}

const colorMap = {
    cyan: { text: 'text-cyan-400', line: '#22d3ee', bg: 'bg-cyan-900/20' },
    amber: { text: 'text-amber-400', line: '#fbb_a26', bg: 'bg-amber-900/20' },
    violet: { text: 'text-violet-400', line: '#a78bfa', bg: 'bg-violet-900/20' },
    green: { text: 'text-green-400', line: '#4ade80', bg: 'bg-green-900/20' },
};

const StatCard: React.FC<StatCardProps> = ({ icon, title, value, subtitle, trend, color = 'cyan' }) => {
    const theme = colorMap[color];
    const trendData = trend ? trend.map((val, index) => ({ name: index, value: val })) : [];

    return (
        <div className={`p-4 rounded-xl shadow-lg border border-gray-700 bg-gray-800/50 backdrop-blur-sm flex justify-between items-center ${theme.bg}`}>
            <div className="flex flex-col">
                <div className="flex items-center gap-3 mb-1">
                    <div className={`w-8 h-8 ${theme.text}`}>
                        {icon}
                    </div>
                    <span className="text-gray-400 font-medium">{title}</span>
                </div>
                <p className={`text-4xl font-bold ${theme.text}`}>{value}</p>
                {subtitle && <p className="text-sm text-gray-500 font-mono mt-1">{subtitle}</p>}
            </div>
            {trend && trend.length > 1 && (
                <div className="w-24 h-12 ml-4">
                    <ResponsiveContainer width="100%" height="100%">
                        <LineChart data={trendData}>
                            <Line type="monotone" dataKey="value" stroke={theme.line} strokeWidth={2} dot={false} />
                        </LineChart>
                    </ResponsiveContainer>
                </div>
            )}
        </div>
    );
};

export default StatCard;
