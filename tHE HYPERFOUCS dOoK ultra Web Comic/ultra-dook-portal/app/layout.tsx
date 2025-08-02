import './globals.css'
import { Inter, JetBrains_Mono } from 'next/font/google'

const inter = Inter({
    subsets: ['latin'],
    variable: '--font-adhd',
})

const jetbrainsMono = JetBrains_Mono({
    subsets: ['latin'],
    variable: '--font-dook',
})

export const metadata = {
    title: '🧠⚡💎 Ultra dOoK Portal',
    description: 'ADHD-Optimized Memory Crystal System - Transform your experiences into wisdom',
    keywords: 'ADHD, neurodivergent, hyperfocus, memory crystals, gamification, BROski',
    authors: [{ name: 'BROski♾️ & The Hyperfocus Zone Empire' }],
    viewport: 'width=device-width, initial-scale=1',
    themeColor: '#3b82f6',
}

export default function RootLayout({
    children,
}: {
    children: React.ReactNode
}) {
    return (
        <html lang="en" className={`${inter.variable} ${jetbrainsMono.variable}`}>
            <head>
                <link rel="icon" href="/favicon.ico" />
                <meta name="apple-mobile-web-app-capable" content="yes" />
                <meta name="apple-mobile-web-app-status-bar-style" content="default" />
                <meta name="apple-mobile-web-app-title" content="Ultra dOoK" />
                <meta name="format-detection" content="telephone=no" />
                <meta name="mobile-web-app-capable" content="yes" />
                <meta name="theme-color" content="#3b82f6" />
            </head>
            <body className="min-h-screen antialiased">
                <div id="portal-root">
                    {children}
                </div>
                <div id="celebration-portal" />
            </body>
        </html>
    )
}
