import { useState, useEffect, useCallback, useRef } from 'react';
import { fetchSystemStats } from '../services/raspberryPiService';
import type { SystemStats, HistoricalDataPoint } from '../types';

const POLLING_INTERVAL = 2000; // 2 seconds
const MAX_HISTORY_LENGTH = 30; // Keep 30 data points (1 minute of data)

export const usePiData = (piAddress: string | null) => {
    const [stats, setStats] = useState<SystemStats | null>(null);
    const [historicalData, setHistoricalData] = useState<HistoricalDataPoint[]>([]);
    const [isLoading, setIsLoading] = useState<boolean>(true);
    const [error, setError] = useState<string | null>(null);
    
    // Use a ref for the interval ID to avoid issues with stale closures
    const intervalIdRef = useRef<number | null>(null);

    const fetchData = useCallback(async () => {
        if (!piAddress) return;
        
        try {
            const currentStats = await fetchSystemStats(piAddress);
            setStats(currentStats);
            
            setHistoricalData(prevData => {
                const now = new Date();
                const newPoint: HistoricalDataPoint = {
                    time: `${now.getHours().toString().padStart(2, '0')}:${now.getMinutes().toString().padStart(2, '0')}:${now.getSeconds().toString().padStart(2, '0')}`,
                    cpuUsage: currentStats.cpu.usage,
                    memoryUsage: (currentStats.memory.used / currentStats.memory.total) * 100,
                    temperature: currentStats.cpu.temperature,
                };
                
                const updatedData = [...prevData, newPoint];
                if (updatedData.length > MAX_HISTORY_LENGTH) {
                    return updatedData.slice(updatedData.length - MAX_HISTORY_LENGTH);
                }
                return updatedData;
            });
            setError(null);
        } catch (e) {
            console.error("Failed to fetch Raspberry Pi data:", e);
            setError("Could not connect to the Raspberry Pi. Check the address and network connection.");
            if (intervalIdRef.current) {
                clearInterval(intervalIdRef.current);
            }
        } finally {
            setIsLoading(false);
        }
    }, [piAddress]);

    useEffect(() => {
        if (piAddress) {
            setIsLoading(true);
            setHistoricalData([]); // Reset history on new connection
            fetchData(); // Fetch immediately on connect

            // Clear any existing interval before setting a new one
            if (intervalIdRef.current) {
                clearInterval(intervalIdRef.current);
            }

            intervalIdRef.current = setInterval(fetchData, POLLING_INTERVAL);

            // Cleanup function to clear interval on component unmount or address change
            return () => {
                if (intervalIdRef.current) {
                    clearInterval(intervalIdRef.current);
                }
            };
        }
    }, [piAddress, fetchData]); // Rerun effect when piAddress or fetchData changes

    return { stats, historicalData, isLoading, error };
};
