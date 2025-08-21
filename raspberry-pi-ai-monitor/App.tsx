
import React, { useState, useCallback } from 'react';
import ConnectScreen from './components/ConnectScreen';
import Dashboard from './components/Dashboard';
import { RaspberryPiIcon } from './components/icons/RaspberryPiIcon';

const App: React.FC = () => {
    const [piAddress, setPiAddress] = useState<string | null>(null);

    const handleConnect = useCallback((address: string) => {
        // In a real app, you might validate the address here
        setPiAddress(address);
    }, []);

    const handleDisconnect = useCallback(() => {
        setPiAddress(null);
    }, []);

    return (
        <main className="min-h-screen bg-gray-900 text-gray-200 font-sans p-4 sm:p-6 lg:p-8">
            <div className="max-w-7xl mx-auto">
                <header className="flex justify-between items-center mb-6">
                    <div className="flex items-center gap-3">
                        <RaspberryPiIcon className="w-10 h-10 text-pi-red" />
                        <h1 className="text-2xl font-bold text-white">
                            Raspberry Pi <span className="text-pi-red">AI</span> Monitor
                        </h1>
                    </div>
                    {piAddress && (
                         <div className="flex items-center gap-4">
                            <div className="text-right">
                                <span className="text-sm text-gray-400 block">Connected to</span>
                                <span className="font-mono text-pi-green">{piAddress}</span>
                            </div>
                            <button
                                onClick={handleDisconnect}
                                className="px-4 py-2 bg-pi-red text-white font-semibold rounded-lg hover:bg-red-700 transition-colors duration-300"
                            >
                                Disconnect
                            </button>
                        </div>
                    )}
                </header>
                
                {piAddress ? (
                    <Dashboard piAddress={piAddress} />
                ) : (
                    <ConnectScreen onConnect={handleConnect} />
                )}

                <footer className="text-center mt-8 text-gray-500 text-sm">
                    <p>Powered by Gemini AI. Designed for modern Raspberry Pi monitoring.</p>
                </footer>
            </div>
        </main>
    );
};

export default App;
