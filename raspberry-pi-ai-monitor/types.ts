
export interface SystemInfo {
    hostname: string;
    os: string;
    kernel: string;
    uptime: string;
}

export interface CpuStats {
    usage: number; // percentage
    temperature: number; // celsius
    cores: number;
    model: string;
}

export interface MemoryStats {
    total: number; // MB
    used: number; // MB
    free: number; // MB
}

export interface DiskStats {
    total: number; // GB
    used: number; // GB
    free: number; // GB
}

export interface SystemStats {
    info: SystemInfo;
    cpu: CpuStats;
    memory: MemoryStats;
    disk: DiskStats;
}

export interface HistoricalDataPoint {
    time: string;
    cpuUsage: number;
    memoryUsage: number;
    temperature: number;
}

export interface Process {
    pid: number;
    user: string;
    cpu: string;
    mem: string;
    command: string;
}

export interface GeminiMessage {
    sender: 'user' | 'ai';
    text: string;
    isLoading?: boolean;
}
