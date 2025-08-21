
import React, { useState, useRef, useEffect } from 'react';
import type { SystemStats, GeminiMessage } from '../types';
import { getPiHealthSuggestion } from '../services/geminiService';
import { SparklesIcon } from './icons/SparklesIcon';
import { PaperAirplaneIcon } from './icons/PaperAirplaneIcon';

interface GeminiAssistantProps {
    currentStats: SystemStats;
}

const GeminiAssistant: React.FC<GeminiAssistantProps> = ({ currentStats }) => {
    const [messages, setMessages] = useState<GeminiMessage[]>([
        { sender: 'ai', text: "Hello! I'm your Pi assistant. Ask me anything about your system's current stats." }
    ]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const messagesEndRef = useRef<HTMLDivElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(scrollToBottom, [messages]);

    const handleSend = async () => {
        if (!input.trim() || isLoading) return;

        const userMessage: GeminiMessage = { sender: 'user', text: input };
        setMessages(prev => [...prev, userMessage, { sender: 'ai', text: '', isLoading: true }]);
        setInput('');
        setIsLoading(true);

        const aiResponseText = await getPiHealthSuggestion(currentStats, input);
        
        const aiMessage: GeminiMessage = { sender: 'ai', text: aiResponseText };
        setMessages(prev => {
            const newMessages = [...prev];
            newMessages[newMessages.length - 1] = aiMessage;
            return newMessages;
        });
        setIsLoading(false);
    };
    
    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSend();
        }
    };
    
    return (
        <div className="flex flex-col h-[40rem] p-4 rounded-xl shadow-lg border border-gray-700 bg-gray-800/50 backdrop-blur-sm">
            <div className="flex items-center gap-2 mb-4">
                <SparklesIcon className="w-6 h-6 text-pi-red" />
                <h3 className="text-lg font-semibold text-white">Gemini AI Assistant</h3>
            </div>
            <div className="flex-grow overflow-y-auto mb-4 pr-2 space-y-4">
                {messages.map((msg, index) => (
                    <div key={index} className={`flex ${msg.sender === 'user' ? 'justify-end' : 'justify-start'}`}>
                        <div className={`max-w-xs md:max-w-sm rounded-lg px-4 py-2 ${
                            msg.sender === 'user' 
                                ? 'bg-pi-red text-white' 
                                : 'bg-gray-700 text-gray-200'
                        }`}>
                            {msg.isLoading ? (
                                <div className="flex items-center justify-center space-x-1">
                                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-pulse [animation-delay:-0.3s]"></div>
                                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-pulse [animation-delay:-0.15s]"></div>
                                    <div className="w-2 h-2 bg-gray-400 rounded-full animate-pulse"></div>
                                </div>
                            ) : (
                                <p className="text-sm whitespace-pre-wrap">{msg.text}</p>
                            )}
                        </div>
                    </div>
                ))}
                <div ref={messagesEndRef} />
            </div>
            <div className="flex items-center gap-2 border-t border-gray-700 pt-4">
                <input
                    type="text"
                    value={input}
                    onChange={(e) => setInput(e.target.value)}
                    onKeyPress={handleKeyPress}
                    placeholder="Why is CPU usage high?"
                    className="flex-grow bg-gray-900 border-2 border-gray-700 rounded-lg px-3 py-2 focus:outline-none focus:ring-2 focus:ring-pi-red focus:border-pi-red transition-all"
                    disabled={isLoading}
                />
                <button
                    onClick={handleSend}
                    disabled={isLoading}
                    className="bg-pi-red text-white p-2 rounded-lg disabled:bg-gray-600 hover:bg-red-700 transition-colors"
                >
                    <PaperAirplaneIcon className="w-5 h-5"/>
                </button>
            </div>
        </div>
    );
};

export default GeminiAssistant;
