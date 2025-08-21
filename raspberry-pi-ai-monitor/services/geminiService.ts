
import { GoogleGenAI } from "@google/genai";
import type { SystemStats } from '../types';

const API_KEY = process.env.API_KEY;

if (!API_KEY) {
    console.warn("API_KEY environment variable not set. Gemini AI features will be disabled.");
}

const ai = new GoogleGenAI({ apiKey: API_KEY! });

export const getPiHealthSuggestion = async (stats: SystemStats, question: string): Promise<string> => {
    if (!API_KEY) {
        return Promise.resolve("Gemini AI is not configured. Please set the API_KEY environment variable.");
    }
    
    const model = 'gemini-2.5-flash';
    const statsString = JSON.stringify(stats, null, 2);

    const prompt = `
        You are an expert system administrator specializing in Raspberry Pi and Linux systems.
        Analyze the following system statistics from a Raspberry Pi and answer the user's question.
        Provide a clear, concise explanation and, if relevant, suggest a helpful linux command the user could run in their terminal to investigate further.
        Format your response in simple markdown.

        System Statistics:
        \`\`\`json
        ${statsString}
        \`\`\`

        User's Question: "${question}"
    `;

    try {
        const response = await ai.models.generateContent({
            model: model,
            contents: prompt,
        });
        
        return response.text;
    } catch (error) {
        console.error("Error calling Gemini API:", error);
        return "Sorry, I encountered an error while trying to get an answer. Please check the console for details.";
    }
};
