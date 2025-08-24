// 🧠💎⚡ HYPERFOCUS ZONE DASHBOARD COMPONENTS ⚡💎🧠
// ADHD-Optimized UI Components for Neurodivergent Developers

class HyperFocusDashboard {
    constructor() {
        this.apiBase = window.location.hostname === 'localhost'
            ? 'http://localhost:3001/api'
            : '/api';
        this.projects = [];
        this.deployments = [];
        this.currentProject = null;
        this.refreshInterval = null;
        this.celebrationMode = false;
    }

    // 🎯 Initialize Dashboard
    async init() {
        console.log('🚀 Initializing HyperFocus Zone Dashboard...');
        this.createDashboardHTML();
        await this.loadProjects();
        this.startRealTimeUpdates();
        this.setupEventListeners();
        this.showWelcomeMessage();
    }

    // 🌟 Create Dashboard HTML Structure
    createDashboardHTML() {
        const dashboardHTML = `
            <div id="hyperfocus-dashboard" class="dashboard-container">
                <!-- Header Section -->
                <div class="dashboard-header">
                    <h1>🧠💎 HyperFocus Zone Command Center 💎🧠</h1>
                    <div class="status-indicator" id="connection-status">
                        <span class="status-dot connecting"></span>
                        <span>Connecting to AI...</span>
                    </div>
                </div>

                <!-- Quick Actions Bar -->
                <div class="quick-actions">
                    <button class="action-btn deploy-btn" onclick="dashboard.quickDeploy()">
                        🚀 Quick Deploy
                    </button>
                    <button class="action-btn refresh-btn" onclick="dashboard.refresh()">
                        🔄 Refresh All
                    </button>
                    <button class="action-btn focus-btn" onclick="dashboard.enterFocusMode()">
                        🎯 Focus Mode
                    </button>
                    <button class="action-btn celebration-btn" onclick="dashboard.celebrate()">
                        🎉 Celebrate Success
                    </button>
                </div>

                <!-- Projects Overview -->
                <div class="projects-section">
                    <h2>📋 Your Projects</h2>
                    <div id="projects-grid" class="projects-grid">
                        <div class="loading-card">⏳ Loading your amazing projects...</div>
                    </div>
                </div>

                <!-- Deployment Timeline -->
                <div class="timeline-section">
                    <h2>🚀 Recent Deployments</h2>
                    <div id="deployment-timeline" class="timeline">
                        <div class="loading-card">⏳ Loading deployment history...</div>
                    </div>
                </div>

                <!-- ADHD-Friendly Progress Tracker -->
                <div class="progress-section">
                    <h2>📊 Your Progress Today</h2>
                    <div class="progress-stats">
                        <div class="stat-card">
                            <div class="stat-emoji">🎯</div>
                            <div class="stat-number" id="deployments-today">0</div>
                            <div class="stat-label">Deployments</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-emoji">⚡</div>
                            <div class="stat-number" id="focus-score">95</div>
                            <div class="stat-label">Focus Score</div>
                        </div>
                        <div class="stat-card">
                            <div class="stat-emoji">🎉</div>
                            <div class="stat-number" id="success-streak">3</div>
                            <div class="stat-label">Success Streak</div>
                        </div>
                    </div>
                </div>

                <!-- AI Assistant Panel -->
                <div class="ai-assistant-panel">
                    <h3>🤖 Your ADHD-Friendly AI Assistant</h3>
                    <div id="ai-suggestions" class="ai-suggestions">
                        <div class="suggestion">
                            💡 <strong>Tip:</strong> Your deployment success rate is 94%!
                            Consider setting up automated testing for even better results.
                        </div>
                    </div>
                </div>
            </div>
        `;

        // Insert dashboard into portal page or create dedicated container
        const container = document.getElementById('dashboard-container') || document.body;
        const dashboardDiv = document.createElement('div');
        dashboardDiv.innerHTML = dashboardHTML;
        container.appendChild(dashboardDiv);
    }

    // 📊 Load Projects from MCP API
    async loadProjects() {
        try {
            this.updateConnectionStatus('loading', 'Loading projects...');

            const response = await fetch(`${this.apiBase}/mcp/projects`);
            const result = await response.json();

            this.projects = result.data;
            this.renderProjects();

            // Load deployments for first project
            if (this.projects.length > 0) {
                await this.loadDeployments(this.projects[0].id);
            }

            this.updateConnectionStatus('connected', 'AI Connected ✨');
        } catch (error) {
            console.error('Failed to load projects:', error);
            this.updateConnectionStatus('error', 'Connection failed ❌');
            this.showErrorMessage('Failed to load projects. Check your connection.');
        }
    }

    // 🚀 Load Deployments for Project
    async loadDeployments(projectId) {
        try {
            const response = await fetch(`${this.apiBase}/mcp/deployments/${projectId}`);
            const result = await response.json();

            this.deployments = result.data;
            this.renderDeploymentTimeline();
            this.updateProgressStats();
        } catch (error) {
            console.error('Failed to load deployments:', error);
        }
    }

    // 🎨 Render Projects Grid
    renderProjects() {
        const grid = document.getElementById('projects-grid');
        if (!grid) return;

        grid.innerHTML = this.projects.map(project => `
            <div class="project-card ${project.status}" onclick="dashboard.selectProject('${project.id}')">
                <div class="project-header">
                    <h3>${project.name}</h3>
                    <div class="health-score">
                        <span class="score-number">${project.healthScore}</span>
                        <span class="score-label">Health</span>
                    </div>
                </div>

                <div class="project-status">
                    <span class="status-indicator ${project.status}">
                        ${this.getStatusEmoji(project.status)} ${project.status.toUpperCase()}
                    </span>
                </div>

                <div class="project-stats">
                    <div class="stat">
                        <span class="stat-label">Deployments:</span>
                        <span class="stat-value">${project.deploymentCount}</span>
                    </div>
                    <div class="stat">
                        <span class="stat-label">Framework:</span>
                        <span class="stat-value">${project.framework}</span>
                    </div>
                </div>

                <div class="project-actions">
                    <a href="${project.url}" target="_blank" class="btn-link">🌐 View Live</a>
                    <button onclick="dashboard.deployProject('${project.id}')" class="btn-deploy">🚀 Deploy</button>
                </div>
            </div>
        `).join('');
    }

    // ⏰ Render Deployment Timeline
    renderDeploymentTimeline() {
        const timeline = document.getElementById('deployment-timeline');
        if (!timeline) return;

        timeline.innerHTML = this.deployments.map(deployment => `
            <div class="timeline-item ${deployment.success ? 'success' : 'error'}">
                <div class="timeline-marker">
                    ${deployment.success ? '✅' : '❌'}
                </div>
                <div class="timeline-content">
                    <div class="timeline-header">
                        <span class="deployment-id">${deployment.id.substring(0, 8)}...</span>
                        <span class="deployment-time">${this.formatTime(deployment.createdAt)}</span>
                    </div>
                    <div class="timeline-details">
                        <div class="detail">🎯 Target: ${deployment.target}</div>
                        <div class="detail">⏱️ Duration: ${deployment.duration}</div>
                        ${deployment.error ?
                `<div class="detail error">❌ Error: ${deployment.error}</div>` :
                `<div class="detail">🌍 Regions: ${deployment.regions.join(', ')}</div>`
            }
                    </div>
                </div>
            </div>
        `).join('');
    }

    // 📊 Update Progress Statistics
    updateProgressStats() {
        const todayDeployments = this.deployments.filter(d => {
            const deployDate = new Date(d.createdAt);
            const today = new Date();
            return deployDate.toDateString() === today.toDateString();
        });

        const successCount = this.deployments.filter(d => d.success).length;
        const successRate = this.deployments.length > 0 ?
            Math.round((successCount / this.deployments.length) * 100) : 0;

        document.getElementById('deployments-today').textContent = todayDeployments.length;
        document.getElementById('focus-score').textContent = successRate;

        // Calculate success streak
        let streak = 0;
        for (let i = 0; i < this.deployments.length; i++) {
            if (this.deployments[i].success) {
                streak++;
            } else {
                break;
            }
        }
        document.getElementById('success-streak').textContent = streak;
    }

    // 🔄 Start Real-time Updates
    startRealTimeUpdates() {
        // Update every 30 seconds
        this.refreshInterval = setInterval(() => {
            this.loadProjects();
        }, 30000);
    }

    // 🎯 ADHD-Friendly Helper Methods
    getStatusEmoji(status) {
        const emojis = {
            'active': '🟢',
            'building': '🟡',
            'error': '🔴',
            'paused': '⏸️'
        };
        return emojis[status] || '⚪';
    }

    formatTime(timestamp) {
        const date = new Date(timestamp);
        const now = new Date();
        const diff = now - date;

        if (diff < 3600000) { // Less than 1 hour
            return `${Math.round(diff / 60000)}m ago`;
        } else if (diff < 86400000) { // Less than 1 day
            return `${Math.round(diff / 3600000)}h ago`;
        } else {
            return date.toLocaleDateString();
        }
    }

    updateConnectionStatus(type, message) {
        const statusEl = document.getElementById('connection-status');
        if (!statusEl) return;

        const dot = statusEl.querySelector('.status-dot');
        const text = statusEl.querySelector('span:last-child');

        dot.className = `status-dot ${type}`;
        text.textContent = message;
    }

    // 🎉 Celebration Mode for ADHD Dopamine Boost
    celebrate() {
        this.celebrationMode = true;
        document.body.classList.add('celebration-mode');

        // Create celebration overlay
        const celebration = document.createElement('div');
        celebration.className = 'celebration-overlay';
        celebration.innerHTML = `
            <div class="celebration-content">
                <h1>🎉 LEGENDARY SUCCESS! 🎉</h1>
                <p>Your deployment skills are absolutely amazing!</p>
                <div class="celebration-emojis">
                    🚀 💎 ⚡ 🧠 🎯 🌟 ❤️‍🔥 🔥
                </div>
                <button onclick="dashboard.stopCelebration()" class="btn-continue">
                    Continue Conquering! 💪
                </button>
            </div>
        `;

        document.body.appendChild(celebration);

        // Auto-remove after 5 seconds
        setTimeout(() => {
            if (this.celebrationMode) {
                this.stopCelebration();
            }
        }, 5000);
    }

    stopCelebration() {
        this.celebrationMode = false;
        document.body.classList.remove('celebration-mode');
        const overlay = document.querySelector('.celebration-overlay');
        if (overlay) {
            overlay.remove();
        }
    }

    // 🔄 Refresh All Data
    async refresh() {
        await this.loadProjects();
        this.showSuccessMessage('✅ Dashboard refreshed successfully!');
    }

    // 🎯 Enter Focus Mode
    enterFocusMode() {
        document.body.classList.add('focus-mode');
        this.showInfoMessage('🎯 Focus Mode activated! Distractions minimized.');

        // Auto-exit focus mode after 25 minutes (Pomodoro technique)
        setTimeout(() => {
            document.body.classList.remove('focus-mode');
            this.showSuccessMessage('⏰ Focus session complete! Time for a break.');
        }, 25 * 60 * 1000);
    }

    // 📱 Show Messages
    showSuccessMessage(message) {
        this.showMessage(message, 'success');
    }

    showErrorMessage(message) {
        this.showMessage(message, 'error');
    }

    showInfoMessage(message) {
        this.showMessage(message, 'info');
    }

    showMessage(message, type) {
        const messageEl = document.createElement('div');
        messageEl.className = `message-toast ${type}`;
        messageEl.textContent = message;

        document.body.appendChild(messageEl);

        setTimeout(() => {
            messageEl.classList.add('show');
        }, 100);

        setTimeout(() => {
            messageEl.remove();
        }, 4000);
    }

    showWelcomeMessage() {
        this.showSuccessMessage('🚀 Welcome to HyperFocus Zone! Your AI-powered neurodivergent platform is ready!');
    }
}

// Initialize dashboard when DOM is ready
document.addEventListener('DOMContentLoaded', () => {
    window.dashboard = new HyperFocusDashboard();
    dashboard.init();
});

// Export for use in other modules
if (typeof module !== 'undefined' && module.exports) {
    module.exports = HyperFocusDashboard;
}
