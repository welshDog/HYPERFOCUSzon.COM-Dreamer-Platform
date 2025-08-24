# 🌟💎⚡ Repository Creation Script ⚡💎🌟

"""
HYPERFOCUS ZONE NEURO SOCIAL DREAMER
GitHub Repository Creation and Setup Engine

This script creates the GitHub repository and sets up the complete
development environment for the neurodivergent-focused social platform.
"""

import json
import os
import subprocess


class GitHubRepositoryCreator:
    def __init__(self):
        self.repo_name = "HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER"
        self.github_username = "welshDog"
        self.local_path = f"h:\\{self.repo_name}"

    def create_repository_structure(self):
        """Create the complete directory structure for the repository"""
        print("🏗️ Creating repository directory structure...")

        # Main directories
        directories = [
            "frontend/mobile/src/components",
            "frontend/mobile/src/screens",
            "frontend/mobile/src/navigation",
            "frontend/mobile/src/accessibility",
            "frontend/mobile/src/utils",
            "frontend/mobile/ios",
            "frontend/mobile/android",
            "frontend/web/src/pages",
            "frontend/web/src/components",
            "frontend/web/src/styles",
            "frontend/web/src/utils",
            "frontend/web/public",
            "api-gateway/src/routes",
            "api-gateway/src/middleware",
            "api-gateway/src/services",
            "api-gateway/src/utils",
            "api-gateway/config",
            "docker/development",
            "docker/staging",
            "docker/production",
            "docs/accessibility",
            "docs/api",
            "docs/deployment",
            "tests/mobile",
            "tests/web",
            "tests/integration",
            ".github/workflows",
            ".github/ISSUE_TEMPLATE",
            ".github/PULL_REQUEST_TEMPLATE",
        ]

        # Create directories
        for dir_path in directories:
            os.makedirs(f"{self.local_path}/{dir_path}", exist_ok=True)
            print(f"✅ Created: {dir_path}")

    def create_essential_files(self):
        """Create essential configuration and documentation files"""
        print("📝 Creating essential files...")

        # Package.json for the root
        package_json = {
            "name": "hyperfocus-zone-neuro-social-dreamer",
            "version": "1.0.0",
            "description": "The world's first neurodivergent-focused social platform",
            "main": "index.js",
            "scripts": {
                "dev": "npm run dev:web",
                "dev:web": "cd frontend/web && npm run dev",
                "dev:mobile": "cd frontend/mobile && npx react-native start",
                "build": "npm run build:web && npm run build:mobile",
                "build:web": "cd frontend/web && npm run build",
                "build:mobile": "cd frontend/mobile && npx react-native bundle",
                "test": "npm run test:web && npm run test:mobile",
                "test:web": "cd frontend/web && npm test",
                "test:mobile": "cd frontend/mobile && npm test",
                "docker:dev": "docker-compose -f docker/development/docker-compose.yml up",
                "docker:staging": "docker-compose -f docker/staging/docker-compose.yml up",
                "docker:prod": "docker-compose -f docker/production/docker-compose.yml up",
            },
            "keywords": [
                "neurodivergent",
                "adhd",
                "social-platform",
                "accessibility",
                "react-native",
                "nextjs",
                "hyperfocus",
            ],
            "author": "HyperFocus Zone Community",
            "license": "MIT",
            "repository": {
                "type": "git",
                "url": f"https://github.com/{self.github_username}/{self.repo_name}.git",
            },
        }

        with open(f"{self.local_path}/package.json", "w") as f:
            json.dump(package_json, f, indent=2)
        print("✅ Created: package.json")

        # Docker Compose for development
        docker_compose = """version: '3.8'

services:
  api-gateway:
    build:
      context: ../../api-gateway
      dockerfile: Dockerfile.dev
    ports:
      - "3001:3001"
    environment:
      - NODE_ENV=development
      - DREAMER_API_PORT_5001=5001
      - DREAMER_API_PORT_5002=5002
      - DREAMER_API_PORT_5003=5003
      - AI_AGENTS_PORT=8888
      - MEMORY_CRYSTALS_PORT=9000
      - BROSKI_ECONOMY_PORT=7000
      - HEALTH_MONITOR_PORT=6000
    volumes:
      - ../../api-gateway:/app
      - /app/node_modules
    command: npm run dev

  web-app:
    build:
      context: ../../frontend/web
      dockerfile: Dockerfile.dev
    ports:
      - "3000:3000"
    environment:
      - NODE_ENV=development
      - NEXT_PUBLIC_API_URL=http://localhost:3001
    volumes:
      - ../../frontend/web:/app
      - /app/node_modules
      - /app/.next
    command: npm run dev

  postgres:
    image: postgres:15
    environment:
      - POSTGRES_DB=hyperfocus_zone_neuro
      - POSTGRES_USER=hyperfocus_user
      - POSTGRES_PASSWORD=secure_password_123
    ports:
      - "5432:5432"
    volumes:
      - postgres_data:/var/lib/postgresql/data

  redis:
    image: redis:7-alpine
    ports:
      - "6379:6379"
    command: redis-server --appendonly yes
    volumes:
      - redis_data:/data

volumes:
  postgres_data:
  redis_data:
"""

        with open(f"{self.local_path}/docker/development/docker-compose.yml", "w") as f:
            f.write(docker_compose)
        print("✅ Created: docker/development/docker-compose.yml")

        # GitHub Actions CI/CD
        github_workflow = """name: 🌟 HyperFocus Zone Neuro Social Dreamer CI/CD

on:
  push:
    branches: [ main, develop ]
  pull_request:
    branches: [ main ]

jobs:
  test-accessibility:
    name: 🧠 Accessibility Testing
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: |
          cd frontend/web
          npm ci

      - name: Run accessibility tests
        run: |
          cd frontend/web
          npm run test:a11y

      - name: Upload accessibility report
        uses: actions/upload-artifact@v3
        with:
          name: accessibility-report
          path: frontend/web/accessibility-report.html

  test-mobile:
    name: 📱 Mobile App Testing
    runs-on: macos-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: |
          cd frontend/mobile
          npm ci

      - name: Run tests
        run: |
          cd frontend/mobile
          npm test

  test-web:
    name: 🌐 Web App Testing
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: '18'
          cache: 'npm'

      - name: Install dependencies
        run: |
          cd frontend/web
          npm ci

      - name: Run tests
        run: |
          cd frontend/web
          npm test

      - name: Build application
        run: |
          cd frontend/web
          npm run build

  deploy-staging:
    name: 🚀 Deploy to Staging
    runs-on: ubuntu-latest
    needs: [test-accessibility, test-mobile, test-web]
    if: github.ref == 'refs/heads/develop'
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to staging
        run: echo "🌟 Deploying to staging environment..."
        # Add actual deployment steps here

  deploy-production:
    name: 🏆 Deploy to Production
    runs-on: ubuntu-latest
    needs: [test-accessibility, test-mobile, test-web]
    if: github.ref == 'refs/heads/main'
    steps:
      - uses: actions/checkout@v4
      - name: Deploy to production
        run: echo "🌟 Deploying to production environment..."
        # Add actual deployment steps here
"""

        with open(f"{self.local_path}/.github/workflows/ci-cd.yml", "w") as f:
            f.write(github_workflow)
        print("✅ Created: .github/workflows/ci-cd.yml")

        # Contributing guidelines
        contributing = """# 🤝 Contributing to HyperFocus Zone Neuro Social Dreamer

Welcome! We're thrilled you want to contribute to the world's first neurodivergent-focused social platform. This guide is designed with ADHD-friendly instructions and clear, actionable steps.

## 🧠 ADHD-Friendly Contribution Process

### ⚡ Quick Start (5 minutes)
1. **Fork the repository** (click the fork button)
2. **Clone your fork** to your local machine
3. **Create a branch** for your contribution
4. **Make your changes** in small, focused commits
5. **Submit a pull request** with a clear description

### 🎯 Focus Areas We Need Help With

#### 🔥 High Impact, Quick Wins
- **Accessibility improvements** (alt text, keyboard navigation, screen reader support)
- **ADHD-specific UX enhancements** (focus indicators, simplified navigation)
- **Bug fixes** with clear reproduction steps
- **Documentation improvements** (making guides clearer and more accessible)

#### 🌟 Deeper Contributions
- **New neurodivergent-friendly features** (hyperfocus timers, interest-based filtering)
- **Performance optimizations** (faster loading, smoother animations)
- **AI integration improvements** (better coaching algorithms, smarter notifications)
- **Community moderation tools** (safe space enforcement, conflict resolution)

## 🛠️ Development Setup

### Prerequisites
- Node.js 18+ (use [nvm](https://github.com/nvm-sh/nvm) for easy version management)
- Git (with proper SSH keys set up)
- A code editor with accessibility extensions (we recommend VS Code)

### Quick Environment Setup
```bash
# Clone your fork
git clone https://github.com/YOUR_USERNAME/HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER.git
cd HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER

# Install all dependencies
npm install

# Start development environment
npm run docker:dev

# In separate terminals:
npm run dev:web    # Web app at http://localhost:3000
npm run dev:mobile # Mobile app development server
```

## 🎨 Design Principles

When contributing, please keep these neurodivergent-focused principles in mind:

### 🧠 Cognitive Load Reduction
- **Simplify complex interfaces** - break down multi-step processes
- **Use clear, descriptive labels** - avoid jargon or unclear terminology
- **Provide consistent navigation** - same actions should work the same way everywhere
- **Minimize decision fatigue** - offer smart defaults and clear recommendations

### ⚡ Attention Management
- **Respect hyperfocus states** - avoid unnecessary interruptions
- **Support task switching** - make it easy to resume where someone left off
- **Use progressive disclosure** - show basic options first, advanced on request
- **Provide clear visual hierarchy** - most important things should stand out

### 🌈 Sensory Considerations
- **Support customization** - themes, font sizes, animation preferences
- **Avoid overwhelming visuals** - too many colors, animations, or elements
- **Test with screen readers** - all functionality should be accessible
- **Consider motion sensitivity** - provide reduced motion options

## 📝 Code Standards

### Accessibility Requirements
- **All interactive elements must be keyboard accessible**
- **Include proper ARIA labels and descriptions**
- **Maintain color contrast ratios of 4.5:1 minimum**
- **Test with screen readers** (we recommend NVDA, JAWS, or VoiceOver)

### Code Quality
- **Write self-documenting code** with clear variable and function names
- **Include inline comments** for complex logic or accessibility considerations
- **Write tests** for new features and accessibility compliance
- **Follow TypeScript strict mode** for better error catching

### Commit Guidelines
We use a simplified commit format that's ADHD-friendly:

```
🎯 Brief description of what you did

Longer explanation if needed:
- What problem this solves
- How you tested it
- Any accessibility considerations
```

Examples:
```
🐛 Fix keyboard navigation in focus mode selector

- Added proper focus management for tab navigation
- Tested with NVDA screen reader
- Fixes issue where users couldn't access focus modes with keyboard

✨ Add hyperfocus timer with gentle break reminders

- 25-minute timer with optional 5-minute break alerts
- Customizable reminder tone (or silent mode)
- Saves session history for progress tracking
- Tested with ADHD community beta users

🎨 Improve color contrast in dark mode

- Updated button colors to meet WCAG AA standards
- Tested with Color Oracle for color blindness simulation
- All contrast ratios now 4.5:1 or higher
```

## 🧪 Testing

### Before Submitting
- [ ] **Run accessibility tests**: `npm run test:a11y`
- [ ] **Test keyboard navigation**: Navigate entire feature with only keyboard
- [ ] **Test screen reader**: Use NVDA/VoiceOver to test all functionality
- [ ] **Test on mobile**: Ensure touch targets are large enough (44px minimum)
- [ ] **Run automated tests**: `npm test`

### Accessibility Testing Tools
- **axe-core**: Automated accessibility testing
- **Wave**: Browser extension for accessibility evaluation
- **Lighthouse**: Accessibility audit in Chrome DevTools
- **Color Oracle**: Color blindness simulation

## 💬 Getting Help

### ADHD-Friendly Support
- **Stuck?** Create a draft pull request and ask for help in the description
- **Need clarification?** Open a discussion with your question
- **Want to pair program?** Mention in Discord that you're looking for a coding buddy
- **Feeling overwhelmed?** Break your contribution into smaller pieces - we're here to help!

### Communication Channels
- **🐛 Bug Reports**: [GitHub Issues](https://github.com/welshDog/HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER/issues)
- **💡 Feature Ideas**: [GitHub Discussions](https://github.com/welshDog/HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER/discussions)
- **❓ Questions**: Discord community or GitHub discussions
- **🚨 Urgent Issues**: Email community@hyperfocuszone.com

## 🌟 Recognition

We believe in celebrating contributions! When you contribute:

- **Your name goes in our contributors list** with a link to your profile
- **Significant contributions** get featured in our monthly community newsletter
- **You earn BROski$ tokens** in our community economy system
- **First-time contributors** get a special welcome and mentorship offer

## 🎯 Contribution Ideas for Beginners

### 🟢 Good First Issues
- **Add alt text** to images missing accessibility descriptions
- **Fix typos** in documentation or user-facing text
- **Improve error messages** to be more helpful and less technical
- **Add keyboard shortcuts** to existing mouse-only interactions

### 🟡 Intermediate Contributions
- **Implement focus management** for modal dialogs and dynamic content
- **Add dark mode support** to components that don't have it yet
- **Create reusable accessibility components** (skip links, focus traps)
- **Optimize performance** for users with older devices or slower connections

### 🔴 Advanced Contributions
- **Design new AI coaching algorithms** for ADHD support
- **Build community moderation tools** for maintaining safe spaces
- **Create advanced accessibility features** (voice control, eye tracking)
- **Architect new neurodivergent-focused social features**

## 📜 Code of Conduct

Our community is built on **understanding, acceptance, and mutual support**. We have zero tolerance for:
- Ableism or discrimination against neurodivergent individuals
- Dismissing someone's needs or experiences
- Using language that stigmatizes mental health
- Making assumptions about someone's capabilities

Instead, we celebrate:
- **Different thinking styles** and problem-solving approaches
- **Questions and learning** - no question is too basic
- **Mistakes and iteration** - progress over perfection
- **Collaboration and mutual support** - we succeed together

## 🚀 Ready to Contribute?

1. **Check out our [good first issues](https://github.com/welshDog/HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER/labels/good%20first%20issue)**
2. **Join our Discord community** for real-time support and collaboration
3. **Read through our [accessibility guidelines](docs/accessibility/README.md)**
4. **Fork the repo and start coding!**

Remember: **Progress over perfection**. We're building this together, one contribution at a time. Your unique perspective as a neurodivergent developer (or ally) makes our platform better for everyone.

---

**🌟 Thank you for helping us build a more inclusive internet! 🌟**

*Every contribution, no matter how small, makes a difference in creating spaces where neurodivergent minds can thrive.*
"""

        with open(f"{self.local_path}/CONTRIBUTING.md", "w") as f:
            f.write(contributing)
        print("✅ Created: CONTRIBUTING.md")

        # Gitignore
        gitignore = """# Dependencies
node_modules/
*/node_modules/
npm-debug.log*
yarn-debug.log*
yarn-error.log*

# Production builds
build/
dist/
*/build/
*/dist/

# Environment variables
.env
.env.local
.env.development.local
.env.test.local
.env.production.local

# IDE and editor files
.vscode/
.idea/
*.swp
*.swo
*~

# OS generated files
.DS_Store
.DS_Store?
._*
.Spotlight-V100
.Trashes
ehthumbs.db
Thumbs.db

# React Native
# React Native CLI
frontend/mobile/ios/build/
frontend/mobile/android/app/build/
frontend/mobile/android/build/

# Expo
frontend/mobile/.expo/
frontend/mobile/dist/
frontend/mobile/npm-debug.*
frontend/mobile/*.jks
frontend/mobile/*.p8
frontend/mobile/*.p12
frontend/mobile/*.key
frontend/mobile/*.mobileprovision
frontend/mobile/*.orig.*

# Next.js
frontend/web/.next/
frontend/web/out/

# Docker
.docker/

# Logs
logs
*.log

# Runtime data
pids
*.pid
*.seed
*.pid.lock

# Testing
coverage/
.nyc_output/
.coverage/

# Accessibility reports
accessibility-report.html
lighthouse-report.html

# Temporary files
*.tmp
*.temp

# Database
*.db
*.sqlite
*.sqlite3

# Cache
.cache/
.parcel-cache/
"""

        with open(f"{self.local_path}/.gitignore", "w") as f:
            f.write(gitignore)
        print("✅ Created: .gitignore")

    def initialize_git_repository(self):
        """Initialize git repository and set up remote"""
        print("🔧 Initializing Git repository...")

        # Change to repository directory
        os.chdir(self.local_path)

        # Initialize git
        subprocess.run(["git", "init"], check=True)
        print("✅ Git repository initialized")

        # Add all files
        subprocess.run(["git", "add", "."], check=True)
        print("✅ Files staged for commit")

        # Initial commit
        commit_message = "🌟 Initial commit: HyperFocus Zone Neuro Social Dreamer platform foundation"
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print("✅ Initial commit created")

        # Set up remote (this will need manual creation on GitHub first)
        remote_url = f"https://github.com/{self.github_username}/{self.repo_name}.git"
        subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
        print(f"✅ Remote origin set to: {remote_url}")

    def create_development_environment_files(self):
        """Create essential development environment files"""
        print("🛠️ Creating development environment files...")

        # API Gateway Dockerfile
        api_dockerfile = """FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci --only=production

# Copy source code
COPY . .

# Expose port
EXPOSE 3001

# Health check
HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \\
  CMD curl -f http://localhost:3001/health || exit 1

# Start application
CMD ["npm", "start"]
"""

        with open(f"{self.local_path}/api-gateway/Dockerfile", "w") as f:
            f.write(api_dockerfile)
        print("✅ Created: api-gateway/Dockerfile")

        # Web app Dockerfile
        web_dockerfile = """FROM node:18-alpine

WORKDIR /app

# Install dependencies
COPY package*.json ./
RUN npm ci

# Copy source code
COPY . .

# Build application
RUN npm run build

# Expose port
EXPOSE 3000

# Start application
CMD ["npm", "start"]
"""

        with open(f"{self.local_path}/frontend/web/Dockerfile", "w") as f:
            f.write(web_dockerfile)
        print("✅ Created: frontend/web/Dockerfile")

        # Environment template
        env_template = """# HyperFocus Zone Neuro Social Dreamer Environment Configuration

# Database Configuration
DATABASE_URL=postgresql://hyperfocus_user:secure_password_123@localhost:5432/hyperfocus_zone_neuro

# Redis Configuration
REDIS_URL=redis://localhost:6379

# API Gateway Configuration
API_GATEWAY_PORT=3001
API_GATEWAY_HOST=localhost

# HyperFocus Zone Empire Backend Services
DREAMER_API_BASE_URL=http://localhost
DREAMER_API_PORT_5001=5001
DREAMER_API_PORT_5002=5002
DREAMER_API_PORT_5003=5003

# AI Agent Army Configuration
AI_AGENTS_BASE_URL=http://localhost:8888
AI_AGENTS_API_KEY=your_ai_agents_api_key_here

# Memory Crystal Network Configuration
MEMORY_CRYSTALS_BASE_URL=http://localhost:9000
MEMORY_CRYSTALS_API_KEY=your_memory_crystals_api_key_here

# BROski Economy Configuration
BROSKI_ECONOMY_BASE_URL=http://localhost:7000
BROSKI_ECONOMY_API_KEY=your_broski_economy_api_key_here

# Health Monitor Configuration
HEALTH_MONITOR_BASE_URL=http://localhost:6000

# Authentication Configuration
JWT_SECRET=your_super_secure_jwt_secret_here
JWT_EXPIRES_IN=7d

# External APIs
OPENAI_API_KEY=your_openai_api_key_here
GEMMA_API_KEY=your_gemma_api_key_here

# Security Configuration
CORS_ORIGIN=http://localhost:3000
RATE_LIMIT_WINDOW_MS=900000
RATE_LIMIT_MAX_REQUESTS=100

# Accessibility Configuration
ACCESSIBILITY_COMPLIANCE_LEVEL=AA
WCAG_VERSION=2.1

# Development Configuration
NODE_ENV=development
DEBUG=hyperfocus:*
LOG_LEVEL=debug

# Production Configuration (for deployment)
# NODE_ENV=production
# LOG_LEVEL=info
# DATABASE_SSL=true
"""

        with open(f"{self.local_path}/.env.template", "w") as f:
            f.write(env_template)
        print("✅ Created: .env.template")

    def display_next_steps(self):
        """Display next steps for the user"""
        print("\n" + "=" * 80)
        print("🎉 REPOSITORY STRUCTURE CREATED SUCCESSFULLY! 🎉")
        print("=" * 80)

        print(
            f"""
🌟 Your new repository is ready at: {self.local_path}

📋 NEXT STEPS TO COMPLETE SETUP:

1. 🌐 CREATE GITHUB REPOSITORY:
   - Go to https://github.com/new
   - Repository name: {self.repo_name}
   - Set to Public
   - Don't initialize with README (we already have one)
   - Click "Create repository"

2. 🔐 PUSH TO GITHUB:
   cd {self.local_path}
   git push -u origin main

3. 🛠️ DEVELOPMENT ENVIRONMENT:
   - Copy .env.template to .env and fill in your API keys
   - Run: npm install
   - Run: npm run docker:dev
   - Start coding! 🚀

4. 🤝 COMMUNITY SETUP:
   - Enable GitHub Discussions
   - Set up issue templates
   - Invite collaborators
   - Configure branch protection rules

📚 USEFUL COMMANDS:
   npm run dev:web          # Start web development server
   npm run dev:mobile       # Start mobile development server
   npm run docker:dev       # Start all backend services
   npm test                 # Run all tests
   npm run test:a11y        # Run accessibility tests

🌟 WHAT'S INCLUDED:
   ✅ Complete repository structure
   ✅ Docker development environment
   ✅ CI/CD pipeline with accessibility testing
   ✅ ADHD-friendly contributing guidelines
   ✅ Neurodivergent-focused documentation
   ✅ Integration points for existing empire services

🎯 READY TO BUILD THE FUTURE OF NEURODIVERGENT SOCIAL PLATFORMS!
"""
        )

    def run(self):
        """Execute the complete repository creation process"""
        print("🌟💎⚡ HYPERFOCUS ZONE NEURO SOCIAL DREAMER ⚡💎🌟")
        print("Starting repository creation process...\n")

        try:
            # Create directory structure
            self.create_repository_structure()
            print()

            # Create essential files
            self.create_essential_files()
            print()

            # Create development environment files
            self.create_development_environment_files()
            print()

            # Initialize git repository
            self.initialize_git_repository()
            print()

            # Display next steps
            self.display_next_steps()

        except Exception as e:
            print(f"❌ Error during repository creation: {e}")
            return False

        return True


if __name__ == "__main__":
    creator = GitHubRepositoryCreator()
    success = creator.run()

    if success:
        print("\n🎉 Repository creation completed successfully!")
        print("Ready to revolutionize social platforms for neurodivergent minds! 🧠💫")
    else:
        print("\n❌ Repository creation failed. Please check the errors above.")
