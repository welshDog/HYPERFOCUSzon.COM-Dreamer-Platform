
import React from 'react';
import { usePiData } from '../hooks/usePiData';
import StatCard from './StatCard';
import ChartCard from './ChartCard';
import ProcessList from './ProcessList';
import SystemInfoCard from './SystemInfoCard';
import GeminiAssistant from './GeminiAssistant';
import { CpuIcon } from './icons/CpuIcon';
import { MemoryIcon } from './icons/MemoryIcon';
import { DiskIcon } from './icons/DiskIcon';
import { ThermometerIcon } from './icons/ThermometerIcon';

interface DashboardProps {
    piAddress: string;
}

const Dashboard: React.FC<DashboardProps> = ({ piAddress }) => {
    const { stats, historicalData, isLoading, error } = usePiData(piAddress);

    if (isLoading && !stats) {
        return (
            <div className="flex items-center justify-center h-[60vh]">
                 <div className="animate-spin rounded-full h-32 w-32 border-t-2 border-b-2 border-pi-red"></div>
            </div>
        );
    }

    if (error) {
        return (
            <div className="text-center p-8 bg-red-900/50 border border-red-700 rounded-lg">
                <h2 className="text-2xl text-red-300 font-bold">Connection Error</h2>
                <p className="text-red-400 mt-2">{error}</p>
            </div>
        );
    }
    
    if (!stats) {
        return null;
    }

    const memoryUsage = (stats.memory.used / stats.memory.total) * 100;
    const diskUsage = (stats.disk.used / stats.disk.total) * 100;
    
    return (
        <div className="grid grid-cols-1 lg:grid-cols-3 xl:grid-cols-4 gap-6">
            {/* Column 1 */}
            <div className="lg:col-span-1 xl:col-span-1 flex flex-col gap-6">
                <SystemInfoCard info={stats.info} cpuModel={stats.cpu.model} />
                 <StatCard 
                    icon={<CpuIcon/>} 
                    title="CPU Usage" 
                    value={`${stats.cpu.usage}%`} 
                    trend={historicalData.map(d => d.cpuUsage)}
                    color="cyan"
                />
                 <StatCard 
                    icon={<ThermometerIcon/>} 
                    title="CPU Temp" 
                    value={`${stats.cpu.temperature}°C`} 
                    trend={historicalData.map(d => d.temperature)}
                    color="amber"
                />
            </div>

            {/* Column 2 */}
            <div className="lg:col-span-2 xl:col-span-2 flex flex-col gap-6">
                <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                     <StatCard 
                        icon={<MemoryIcon/>} 
                        title="Memory Usage" 
                        value={`${memoryUsage.toFixed(1)}%`} 
                        subtitle={`${stats.memory.used} / ${stats.memory.total} MB`}
                        color="violet"
                    />
                    <StatCard 
                        icon={<DiskIcon/>} 
                        title="Disk Usage" 
                        value={`${diskUsage.toFixed(1)}%`} 
                        subtitle={`${stats.disk.used} / ${stats.disk.total} GB`}
                        color="green"
                    />
                </div>
                <ChartCard 
                    title="Real-time CPU & Memory Usage" 
                    data={historicalData} 
                />
                <ProcessList piAddress={piAddress}/>
            </div>
            
            {/* Column 3 */}
            <div className="lg:col-span-3 xl:col-span-1 flex flex-col gap-6">
                <GeminiAssistant currentStats={stats} />
            </div>
        </div>
    );
};

export default Dashboard;
