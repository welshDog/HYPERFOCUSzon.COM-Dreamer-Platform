// 🚀💎⚡ HYPERFOCUS ZONE ESLint Configuration ⚡💎🚀
// ADHD-friendly, non-overwhelming linting rules for legendary development

module.exports = {
    env: {
        browser: true,
        es2021: true,
        node: true,
        jest: true
    },
    extends: [
        'eslint:recommended'
    ],
    parserOptions: {
        ecmaVersion: 'latest',
        sourceType: 'module'
    },
    rules: {
        // 🧠 ADHD-Optimized Rules - Focused on what matters most
        'no-unused-vars': 'warn',           // Warn instead of error - less overwhelming
        'no-console': 'off',                // Allow console.log for debugging
        'no-undef': 'error',                // Catch undefined variables
        'semi': ['warn', 'always'],         // Consistent semicolons
        'quotes': ['warn', 'single'],       // Consistent quotes

        // 🎯 Focus on critical issues only
        'no-unreachable': 'error',          // Dead code detection
        'no-duplicate-case': 'error',       // Switch statement issues
        'no-redeclare': 'error',            // Variable redeclaration

        // 🚀 Allow flexibility for rapid prototyping
        'no-irregular-whitespace': 'off',   // Allow emoji and special chars
        'no-mixed-spaces-and-tabs': 'warn'  // Formatting but not blocking
    },
    ignorePatterns: [
        'node_modules/',
        'dist/',
        '*.min.js',
        'build/',
        'coverage/',
        '**/*.py',          // Ignore Python files
        '**/*.md',          // Ignore Markdown files
        '**/*.txt',         // Ignore text files
        '**/*.json',        // Ignore JSON files (handled separately)
        '**/*💎*',          // Ignore files with emoji names (our style!)
        '**/*⚡*',
        '**/*🚀*',
        '**/*🧠*',
        '**/*🏆*'
    ]
};
