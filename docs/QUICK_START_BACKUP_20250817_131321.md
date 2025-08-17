# QUICK START GUIDE

Get your HYPERFOCUS Zone Empire running in under 5 minutes! ⚡

## 🚀 **Prerequisites**

- **Node.js** 18+ ([Download](https://nodejs.org/))
- **Python** 3.10+ ([Download](https://python.org/))
- **Git** ([Download](https://git-scm.com/))
- **Docker** (optional) ([Download](https://docker.com/))

## ⚡ **One-Command Setup**

### Option 1: Node.js (Recommended)
```bash
git clone https://github.com/welshDog/HYPERFOCUSzon.COM-V10.git
cd HYPERFOCUSzon.COM-V10
npm install
npm start
```

### Option 2: Python Empire
```bash
git clone https://github.com/welshDog/HYPERFOCUSzon.COM-V10.git
cd HYPERFOCUSzon.COM-V10
pip install -r requirements.txt
python empire_ai/main.py
```

### Option 3: Docker (Full Stack)
```bash
git clone https://github.com/welshDog/HYPERFOCUSzon.COM-V10.git
cd HYPERFOCUSzon.COM-V10
docker-compose up --build
```

## 🎯 **Verify Setup**

After starting, check these endpoints:

- **Main App**: http://localhost:3000
- **Health Check**: http://localhost:3000/health
- **AI Parliament**: http://localhost:3000/ai-parliament
- **Empire Dashboard**: http://localhost:3000/empire

## 🔧 **Configuration**

1. Copy environment template:
```bash
cp .env.example .env
```

2. Edit `.env` with your settings:
```bash
# Discord Bot Token (optional)
DISCORD_TOKEN=your_token_here

# Database URL (optional - defaults to SQLite)
DATABASE_URL=sqlite:./empire.db

# API Keys (optional)
OPENAI_API_KEY=your_key_here
```

## 🧪 **Run Tests**

```bash
# JavaScript tests
npm test

# Python tests
pytest

# Full test suite
npm run test:all
```

## 🎉 **What's Running?**

Once started, you'll have:

- ✅ **AI Parliament** (100+ agents coordinating)
- ✅ **Memory Crystals** (strategic intelligence)
- ✅ **Health Monitoring** (real-time empire status)
- ✅ **Discord Integration** (community connection)
- ✅ **Automation Engines** (background tasks)
- ✅ **BROski Economy** (reward system)

## 🆘 **Troubleshooting**

### Common Issues:

**Port 3000 already in use:**
```bash
# Change port in package.json or:
PORT=3001 npm start
```

**Python dependencies issues:**
```bash
# Create virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

**Docker issues:**
```bash
# Clean and rebuild:
docker-compose down
docker-compose up --build --force-recreate
```

## 🚀 **Next Steps**

1. 📖 [Explore Empire Systems](../docs/EMPIRE_SYSTEMS.md)
2. 🤖 [Configure AI Parliament](../docs/AI_PARLIAMENT.md)
3. 💬 [Join Discord Community](https://discord.gg/hyperfocus-zone)
4. 🛠️ [Start Contributing](../CONTRIBUTING.md)

## 💡 **Need Help?**

- 🐛 [Report Issues](https://github.com/welshDog/HYPERFOCUSzon.COM-V10/issues)
- 💬 [Discord Support](https://discord.gg/hyperfocus-zone)
- 📧 [Email Support](mailto:lyndzwills@gmail.com)

---

**Welcome to your GOD-TIER empire! ❤️‍🔥**

Ready to experience neurodivergent-optimized productivity? Let's build something legendary together! 🚀✨
