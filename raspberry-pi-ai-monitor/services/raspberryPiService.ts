
import type { SystemStats, Process, HistoricalDataPoint } from '../types';

// --- Mock Data Store ---
// This simulates the state of the Raspberry Pi over time.
let mockState = {
    cpuUsage: 25,
    temperature: 45,
    memoryUsed: 1024, // MB
    diskUsed: 15, // GB
    uptimeSeconds: 3600 * 24 * 2, // 2 days
};

// --- Mock Data Generators ---

const generateStats = (): SystemStats => {
    // Fluctuate CPU usage
    mockState.cpuUsage += (Math.random() - 0.5) * 5;
    mockState.cpuUsage = Math.max(5, Math.min(95, mockState.cpuUsage));

    // Fluctuate temperature based on CPU
    mockState.temperature = 40 + (mockState.cpuUsage / 100) * 25 + (Math.random() - 0.5) * 2;
    mockState.temperature = Math.max(35, Math.min(80, mockState.temperature));
    
    // Slowly change memory and disk usage
    mockState.memoryUsed += (Math.random() - 0.45) * 10;
    mockState.memoryUsed = Math.max(512, Math.min(3800, mockState.memoryUsed));
    
    mockState.uptimeSeconds += 2; // Polling interval is 2s

    const formatUptime = (totalSeconds: number) => {
        const days = Math.floor(totalSeconds / (3600 * 24));
        const hours = Math.floor((totalSeconds % (3600 * 24)) / 3600);
        const minutes = Math.floor((totalSeconds % 3600) / 60);
        return `${days}d ${hours}h ${minutes}m`;
    };

    return {
        info: {
            hostname: 'raspberrypi',
            os: 'Debian GNU/Linux 11 (bullseye)',
            kernel: 'Linux 5.15.32-v7l+',
            uptime: formatUptime(mockState.uptimeSeconds),
        },
        cpu: {
            usage: parseFloat(mockState.cpuUsage.toFixed(1)),
            temperature: parseFloat(mockState.temperature.toFixed(1)),
            cores: 4,
            model: 'ARMv7 Processor rev 3 (v7l)',
        },
        memory: {
            total: 4096, // 4GB
            used: Math.round(mockState.memoryUsed),
            free: 4096 - Math.round(mockState.memoryUsed),
        },
        disk: {
            total: 64, // 64GB
            used: parseFloat(mockState.diskUsed.toFixed(2)),
            free: 64 - parseFloat(mockState.diskUsed.toFixed(2)),
        },
    };
};

const mockProcesses: Omit<Process, 'pid' | 'cpu' | 'mem'>[] = [
    { user: 'root', command: 'systemd' },
    { user: 'pi', command: 'sshd: pi@pts/0' },
    { user: 'pi', command: 'bash' },
    { user: 'www-data', command: 'nginx: worker process' },
    { user: 'root', command: 'kthreadd' },
    { user: 'pi', command: 'python3 /home/pi/myscript.py' },
    { user: 'root', command: 'rsyslogd' },
    { user: 'pi', command: 'node /home/pi/server.js' },
    { user: 'root', command: 'cron' },
    { user: 'message+', command: 'dbus-daemon --system --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only'},
];

const generateProcesses = (): Process[] => {
    return mockProcesses.map((p, i) => ({
        ...p,
        pid: 1000 + i * 20 + Math.floor(Math.random() * 10),
        cpu: (Math.random() * (p.command.includes('python') || p.command.includes('node') ? 15 : 2)).toFixed(1),
        mem: (Math.random() * 5).toFixed(1),
    })).sort((a, b) => parseFloat(b.cpu) - parseFloat(a.cpu));
};


// --- Mock API Functions ---

// We accept address but ignore it, as we have one mock source of truth.
export const fetchSystemStats = (address: string): Promise<SystemStats> => {
    console.log(`Fetching system stats from mock service for ${address}...`);
    return new Promise(resolve => {
        setTimeout(() => resolve(generateStats()), 300);
    });
};

export const fetchProcessList = (address: string): Promise<Process[]> => {
    console.log(`Fetching process list from mock service for ${address}...`);
    return new Promise(resolve => {
        setTimeout(() => resolve(generateProcesses()), 500);
    });
};
