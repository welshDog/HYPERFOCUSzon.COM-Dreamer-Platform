
import React, { useState } from 'react';
import { WifiIcon } from './icons/WifiIcon';

interface ConnectScreenProps {
    onConnect: (address: string) => void;
}

const ConnectScreen: React.FC<ConnectScreenProps> = ({ onConnect }) => {
    const [address, setAddress] = useState<string>('192.168.1.10');

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        if (address.trim()) {
            onConnect(address.trim());
        }
    };

    return (
        <div className="flex flex-col items-center justify-center h-[60vh]">
            <div className="w-full max-w-md p-8 bg-gray-800/50 backdrop-blur-sm border border-gray-700 rounded-2xl shadow-xl text-center">
                <WifiIcon className="w-16 h-16 text-pi-green mx-auto mb-4" />
                <h2 className="text-3xl font-bold text-white mb-2">Connect to your Pi</h2>
                <p className="text-gray-400 mb-6">Enter the IP address of your Raspberry Pi on the local network.</p>
                <form onSubmit={handleSubmit} className="flex flex-col gap-4">
                    <input
                        type="text"
                        value={address}
                        onChange={(e) => setAddress(e.target.value)}
                        placeholder="e.g., 192.168.1.10"
                        className="w-full px-4 py-3 bg-gray-900 border-2 border-gray-700 rounded-lg text-center text-lg font-mono text-pi-green focus:outline-none focus:ring-2 focus:ring-pi-red focus:border-pi-red transition-all"
                    />
                    <button
                        type="submit"
                        className="w-full py-3 bg-pi-red text-white font-bold text-lg rounded-lg hover:bg-red-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-900 focus:ring-pi-red transition-all duration-300"
                    >
                        Connect
                    </button>
                </form>
            </div>
             <p className="text-gray-600 mt-6 text-sm">
                Note: This app uses a mock data service for demonstration. Any valid IP format will work.
            </p>
        </div>
    );
};

export default ConnectScreen;
