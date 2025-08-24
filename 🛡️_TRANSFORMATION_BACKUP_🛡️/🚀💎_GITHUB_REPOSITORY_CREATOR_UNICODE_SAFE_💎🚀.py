# HYPERFOCUS ZONE NEURO SOCIAL DREAMER - Repository Setup Script

"""
HYPERFOCUS ZONE NEURO SOCIAL DREAMER
GitHub Repository Creation and Setup Engine (Unicode-Safe Version)

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
        print("Creating repository directory structure...")

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
            full_path = os.path.join(self.local_path, dir_path)
            os.makedirs(full_path, exist_ok=True)
            print(f"Created: {dir_path}")

    def create_essential_files(self):
        """Create essential configuration and documentation files"""
        print("Creating essential files...")

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

        package_path = os.path.join(self.local_path, "package.json")
        with open(package_path, "w", encoding="utf-8") as f:
            json.dump(package_json, f, indent=2)
        print("Created: package.json")

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

        docker_path = os.path.join(
            self.local_path, "docker", "development", "docker-compose.yml"
        )
        with open(docker_path, "w", encoding="utf-8") as f:
            f.write(docker_compose)
        print("Created: docker/development/docker-compose.yml")

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

        gitignore_path = os.path.join(self.local_path, ".gitignore")
        with open(gitignore_path, "w", encoding="utf-8") as f:
            f.write(gitignore)
        print("Created: .gitignore")

    def initialize_git_repository(self):
        """Initialize git repository and set up remote"""
        print("Initializing Git repository...")

        # Change to repository directory
        os.chdir(self.local_path)

        # Initialize git
        subprocess.run(["git", "init"], check=True)
        print("Git repository initialized")

        # Add all files
        subprocess.run(["git", "add", "."], check=True)
        print("Files staged for commit")

        # Initial commit
        commit_message = (
            "Initial commit: HyperFocus Zone Neuro Social Dreamer platform foundation"
        )
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print("Initial commit created")

        # Set up remote (this will need manual creation on GitHub first)
        remote_url = f"https://github.com/{self.github_username}/{self.repo_name}.git"
        subprocess.run(["git", "remote", "add", "origin", remote_url], check=True)
        print(f"Remote origin set to: {remote_url}")

    def create_development_files(self):
        """Create additional development files"""
        print("Creating development files...")

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
"""

        env_path = os.path.join(self.local_path, ".env.template")
        with open(env_path, "w", encoding="utf-8") as f:
            f.write(env_template)
        print("Created: .env.template")

    def display_next_steps(self):
        """Display next steps for the user"""
        print("\n" + "=" * 60)
        print("REPOSITORY STRUCTURE CREATED SUCCESSFULLY!")
        print("=" * 60)

        print(
            f"""
Your new repository is ready at: {self.local_path}

NEXT STEPS TO COMPLETE SETUP:

1. CREATE GITHUB REPOSITORY:
   - Go to https://github.com/new
   - Repository name: {self.repo_name}
   - Set to Public
   - Don't initialize with README (we already have one)
   - Click "Create repository"

2. PUSH TO GITHUB:
   cd {self.local_path}
   git push -u origin main

3. DEVELOPMENT ENVIRONMENT:
   - Copy .env.template to .env and fill in your API keys
   - Run: npm install
   - Run: npm run docker:dev
   - Start coding!

USEFUL COMMANDS:
   npm run dev:web          # Start web development server
   npm run dev:mobile       # Start mobile development server
   npm run docker:dev       # Start all backend services
   npm test                 # Run all tests

WHAT'S INCLUDED:
   - Complete repository structure
   - Docker development environment
   - Integration points for existing empire services
   - Neurodivergent-focused documentation

READY TO BUILD THE FUTURE OF NEURODIVERGENT SOCIAL PLATFORMS!
"""
        )

    def run(self):
        """Execute the complete repository creation process"""
        print("HYPERFOCUS ZONE NEURO SOCIAL DREAMER")
        print("Starting repository creation process...")

        try:
            # Create directory structure
            self.create_repository_structure()
            print()

            # Create essential files
            self.create_essential_files()
            print()

            # Create development files
            self.create_development_files()
            print()

            # Initialize git repository
            self.initialize_git_repository()
            print()

            # Display next steps
            self.display_next_steps()

        except Exception as e:
            print(f"Error during repository creation: {e}")
            return False

        return True


if __name__ == "__main__":
    creator = GitHubRepositoryCreator()
    success = creator.run()

    if success:
        print("\nRepository creation completed successfully!")
        print("Ready to revolutionize social platforms for neurodivergent minds!")
    else:
        print("\nRepository creation failed. Please check the errors above.")
