
import React, { useState, useEffect, useCallback } from 'react';
import { fetchProcessList } from '../services/raspberryPiService';
import type { Process } from '../types';

interface ProcessListProps {
    piAddress: string;
}

const ProcessList: React.FC<ProcessListProps> = ({ piAddress }) => {
    const [processes, setProcesses] = useState<Process[]>([]);
    const [isLoading, setIsLoading] = useState(true);

    const loadProcesses = useCallback(async () => {
        setIsLoading(true);
        const data = await fetchProcessList(piAddress);
        setProcesses(data);
        setIsLoading(false);
    }, [piAddress]);

    useEffect(() => {
        loadProcesses();
        const interval = setInterval(loadProcesses, 5000); // Refresh every 5 seconds
        return () => clearInterval(interval);
    }, [loadProcesses]);

    return (
        <div className="p-4 rounded-xl shadow-lg border border-gray-700 bg-gray-800/50 backdrop-blur-sm">
            <h3 className="text-lg font-semibold text-white mb-4">Running Processes</h3>
            <div className="h-96 overflow-y-auto pr-2">
                <table className="w-full text-left text-sm font-mono">
                    <thead className="sticky top-0 bg-gray-800/80 backdrop-blur-sm">
                        <tr>
                            <th className="p-2 text-pi-green">PID</th>
                            <th className="p-2 text-pi-green">User</th>
                            <th className="p-2 text-pi-green">%CPU</th>
                            <th className="p-2 text-pi-green">%MEM</th>
                            <th className="p-2 text-pi-green">Command</th>
                        </tr>
                    </thead>
                    <tbody className="divide-y divide-gray-700">
                        {processes.map((p) => (
                            <tr key={p.pid} className="hover:bg-gray-700/50">
                                <td className="p-2 text-gray-400">{p.pid}</td>
                                <td className="p-2 text-gray-300">{p.user}</td>
                                <td className="p-2 text-cyan-400">{p.cpu}</td>
                                <td className="p-2 text-violet-400">{p.mem}</td>
                                <td className="p-2 text-gray-300 truncate" title={p.command}>{p.command}</td>
                            </tr>
                        ))}
                    </tbody>
                </table>
                 {isLoading && processes.length === 0 && <p className="text-center p-4 text-gray-500">Loading processes...</p>}
            </div>
        </div>
    );
};

export default ProcessList;
