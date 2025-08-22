import { Head, Html, Main, NextScript } from 'next/document';

// 🌐 Custom Document for HYPERFOCUS ZONE with Accessibility Optimization
export default function Document() {
    return (
        <Html lang="en" className="scroll-smooth">
            <Head>
                {/* 🧠 Neurodivergent-friendly meta tags */}
                <meta charSet="utf-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover" />
                <meta name="theme-color" content="#0066CC" />
                <meta name="color-scheme" content="light dark" />

                {/* 🎯 ADHD-friendly no-flash script */}
                <script
                    dangerouslySetInnerHTML={{
                        __html: `
              // Prevent flash of unstyled content for ADHD users
              try {
                const settings = JSON.parse(localStorage.getItem('hyperfocus-accessibility-settings') || '{}');
                if (settings.colorScheme === 'dark' || (settings.colorScheme === 'auto' && window.matchMedia('(prefers-color-scheme: dark)').matches)) {
                  document.documentElement.classList.add('dark');
                }
                if (settings.reducedMotion) {
                  document.documentElement.style.setProperty('--motion-duration', '0.01ms');
                }
              } catch (e) {}
            `,
                    }}
                />

                {/* 🔤 Dyslexic-friendly fonts */}
                <link rel="preconnect" href="https://fonts.googleapis.com" />
                <link rel="preconnect" href="https://fonts.gstatic.com" crossOrigin="anonymous" />
                <link
                    href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@400;500&display=swap"
                    rel="stylesheet"
                />

                {/* 🌈 Accessibility enhancements */}
                <meta name="description" content="HYPERFOCUS ZONE - Revolutionary productivity platform designed for 1.1 billion neurodivergent individuals. ADHD-friendly, autism-optimized, accessible to all." />
                <meta name="keywords" content="ADHD, autism, neurodivergent, productivity, accessibility, hyperfocus, executive function" />

                {/* 📱 PWA manifest */}
                <link rel="manifest" href="/manifest.json" />
                <link rel="apple-touch-icon" href="/icon-192.png" />

                {/* 🎨 Favicon */}
                <link rel="icon" href="/favicon.ico" />
            </Head>
            <body className="antialiased bg-white dark:bg-gray-900 text-gray-900 dark:text-white">
                {/* 🧠 Screen reader announcements */}
                <div id="announcements" aria-live="polite" aria-atomic="true" className="sr-only"></div>

                <Main />
                <NextScript />

                {/* 🎯 Focus management for ADHD users */}
                <div id="focus-guard-start" tabIndex={0}></div>
                <div id="focus-guard-end" tabIndex={0}></div>
            </body>
        </Html>
    );
}
