// 🚀💎⚡ HYPERFOCUS ZONE Jest Configuration ⚡💎🚀
// ADHD-friendly testing setup for legendary development

module.exports = {
    testEnvironment: 'node',
    roots: ['<rootDir>'],
    testMatch: [
        '**/__tests__/**/*.js',
        '**/?(*.)+(spec|test).js'
    ],
    collectCoverageFrom: [
        '**/*.js',
        '!**/node_modules/**',
        '!**/dist/**',
        '!**/build/**',
        '!**/*.config.js',
        '!**/*.min.js'
    ],
    coverageDirectory: 'coverage',
    coverageReporters: ['text', 'lcov', 'html'],
    testTimeout: 10000,
    verbose: true,
    // 🧠 ADHD-Optimized: Clear, focused test output
    reporters: [
        'default',
        ['jest-html-reporters', {
            publicPath: './coverage',
            filename: 'test-report.html',
            pageTitle: '🏆 HYPERFOCUS ZONE Test Results'
        }]
    ],
    // 🎯 Allow tests to pass even if no test files exist
    passWithNoTests: true,
    // 🚀 Setup for future test files
    setupFilesAfterEnv: [],
    moduleFileExtensions: ['js', 'json', 'mjs'],
    transform: {},
    testPathIgnorePatterns: [
        '/node_modules/',
        '/dist/',
        '/build/',
        '\\.py$',
        '\\.md$',
        '\\.txt$'
    ]
};
