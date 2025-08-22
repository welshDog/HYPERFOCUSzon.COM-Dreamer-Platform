import type { AppProps } from 'next/app';
import { AccessibilityProvider, FocusManager } from '../components/AccessibilityProvider';
import '../styles/globals.css';

// 🚀 HYPERFOCUS ZONE Next.js App with Neurodivergent Optimization
function MyApp({ Component, pageProps }: AppProps) {
    return (
        <AccessibilityProvider>
            <FocusManager>
                {/* 🎯 Skip link for keyboard navigation */}
                <a
                    href="#main-content"
                    className="skip-link sr-only focus:not-sr-only focus:absolute focus:top-2 focus:left-2 focus:z-50 bg-hyperfocus-blue text-white px-4 py-2 rounded-md font-semibold"
                >
                    Skip to main content
                </a>

                {/* 📱 Main application */}
                <div id="app-root" className="min-h-screen bg-white dark:bg-gray-900">
                    <Component {...pageProps} />
                </div>
            </FocusManager>
        </AccessibilityProvider>
    );
}

export default MyApp;
