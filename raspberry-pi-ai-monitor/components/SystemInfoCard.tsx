
import React from 'react';
import type { SystemInfo } from '../types';

interface SystemInfoCardProps {
    info: SystemInfo;
    cpuModel: string;
}

const InfoRow: React.FC<{ label: string; value: React.ReactNode }> = ({ label, value }) => (
    <div className="flex justify-between items-baseline py-2 border-b border-gray-700/50">
        <span className="text-sm text-gray-400">{label}</span>
        <span className="text-sm text-right font-mono text-pi-green">{value}</span>
    </div>
);

const SystemInfoCard: React.FC<SystemInfoCardProps> = ({ info, cpuModel }) => {
    return (
        <div className="p-4 rounded-xl shadow-lg border border-gray-700 bg-gray-800/50 backdrop-blur-sm">
            <h3 className="text-lg font-semibold text-white mb-2">System Information</h3>
            <div className="flex flex-col gap-1">
                <InfoRow label="Hostname" value={info.hostname} />
                <InfoRow label="OS" value={info.os} />
                <InfoRow label="Kernel" value={info.kernel} />
                <InfoRow label="Uptime" value={info.uptime} />
                <InfoRow label="CPU Model" value={cpuModel} />
            </div>
        </div>
    );
};

export default SystemInfoCard;
