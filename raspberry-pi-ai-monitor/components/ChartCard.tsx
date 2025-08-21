
import React from 'react';
import { ResponsiveContainer, LineChart, CartesianGrid, XAxis, YAxis, Tooltip, Legend, Line } from 'recharts';
import type { HistoricalDataPoint } from '../types';

interface ChartCardProps {
    title: string;
    data: HistoricalDataPoint[];
}

const ChartCard: React.FC<ChartCardProps> = ({ title, data }) => {
    return (
        <div className="p-4 rounded-xl shadow-lg border border-gray-700 bg-gray-800/50 backdrop-blur-sm h-80">
            <h3 className="text-lg font-semibold text-white mb-4">{title}</h3>
            <ResponsiveContainer width="100%" height="90%">
                <LineChart data={data} margin={{ top: 5, right: 20, left: -10, bottom: 5 }}>
                    <CartesianGrid strokeDasharray="3 3" stroke="#4a5568" />
                    <XAxis dataKey="time" stroke="#a0aec0" fontSize={12} />
                    <YAxis yAxisId="left" stroke="#a0aec0" fontSize={12} unit="%" domain={[0, 100]} />
                    <YAxis yAxisId="right" orientation="right" stroke="#a0aec0" fontSize={12} unit="°C" domain={[20, 90]}/>
                    <Tooltip
                        contentStyle={{
                            backgroundColor: '#1a202c',
                            border: '1px solid #4a5568',
                            borderRadius: '0.5rem',
                        }}
                        labelStyle={{ color: '#e2e8f0' }}
                    />
                    <Legend wrapperStyle={{ color: '#e2e8f0' }} />
                    <Line yAxisId="left" type="monotone" dataKey="cpuUsage" name="CPU" stroke="#22d3ee" strokeWidth={2} dot={false} />
                    <Line yAxisId="left" type="monotone" dataKey="memoryUsage" name="Memory" stroke="#a78bfa" strokeWidth={2} dot={false} />
                    <Line yAxisId="right" type="monotone" dataKey="temperature" name="Temp" stroke="#fbb_a26" strokeWidth={2} dot={false} />
                </LineChart>
            </ResponsiveContainer>
        </div>
    );
};

export default ChartCard;
