# 🧠💎⚡ Neurodivergent AI - Demo Clients

**Built BY and FOR the neurodivergent community**

This repository contains demo clients for the revolutionary Neurodivergent-First AI System:

* **🖥️ CLI Client** - Fast command-line interface for developers and power users
* **🌐 Web Interface** - Beautiful, accessible web app with real-time interactions
* **🧪 Mock Server** - Realistic API server for demonstrations and testing
* **🛡️ Ethics Dashboard** - Transparency and governance interface (coming next)

---

## 🚀 **Vision**

Neurodivergent AI is building the world's first AI system that truly **understands neurodivergence** — ADHD, autism, dyslexia, and their overlaps — using both:

* **🔬 Science Data** - Peer-reviewed research, clinical studies, validated knowledge
* **💬 Lived Data** - Community stories, forum discussions, advocacy voices

The demo clients prove our **pipeline works end-to-end** and set us up for community testing and stakeholder confidence.

---

## 📂 **Structure**

```
neurodivergent-ai-demo/
├── cli/                   # Python CLI client
│   └── ask.py            # Main CLI application
├── web/                   # Web interface
│   └── index.html        # Interactive web client
├── mock_server/           # Mock API server
│   └── server.py         # FastAPI mock implementation
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

---

## 🖥️ **CLI Client Usage**

### **Quick Start**
```bash
# Install dependencies
pip install -r requirements.txt

# Ask a question
python cli/ask.py "Does ADHD improve creativity?"

# Specify mode
python cli/ask.py "What helps with sensory overload?" --mode lived
python cli/ask.py "ADHD and autism overlap" --mode science
```

### **Example Output**
```
╔══════════════════════════════════════════════════════════════╗
║  🧠💎⚡ NEURODIVERGENT AI - RESPONSE ⚡💎🧠                ║
╚══════════════════════════════════════════════════════════════╝

🟨 MODE: BALANCED
✅ Likely True

📊 TRUST SCORE: 0.87 [████████░░] (87%)

🔍 SOURCES (3):
   1. https://pubmed.ncbi.nlm.nih.gov/creativity-adhd-2023
   2. https://neuropsychology.org/adhd-creative-cognition
   3. https://additudemag.com/creative-adhd-minds

💬 EXPLANATION:
Research shows that ADHD individuals often demonstrate enhanced creativity
through divergent thinking, cognitive flexibility, and novel connections...

🏷️ DETECTED THEMES:
   💪 Strengths: creativity, divergent thinking, cognitive flexibility
   🔗 Overlaps: ADHD+creativity
```

---

## 🌐 **Web Interface Usage**

### **Quick Start**
```bash
# Start mock server
python mock_server/server.py

# Open web interface
cd web
python -m http.server 8080

# Open in browser
http://localhost:8080
```

### **Features**
* **🎨 Mode Toggles** - Switch between science, lived, and balanced perspectives
* **📊 Trust Visualization** - Real-time trust score with animated progress bars
* **🔍 Source Attribution** - Clickable links to research and community sources
* **♿ Accessibility** - Designed for neurodivergent users with screen reader support
* **🌈 Neurodivergent-Friendly** - High contrast, clear typography, sensory considerations

---

## 🧪 **Mock Server**

If you don't have the full AI system running yet, use our realistic mock server:

```bash
# Start mock server
cd mock_server
python server.py

# Server runs at: http://localhost:8000
# API endpoints:
#   POST /ask       - Ask questions
#   GET /modelcard  - Model transparency
#   GET /health     - Health check
```

The mock server provides realistic responses with:
- ✅ Multiple response categories (creativity, sensory, overlap)
- ✅ Mode-specific answers (science vs lived vs balanced)
- ✅ Trust scoring and source attribution
- ✅ Neurodivergent strengths and challenges detection

---

## 🛡️ **Modes & Safety**

### **🎯 Query Modes**
- **🟦 Science Mode** - Peer-reviewed research and clinical data only
- **🟩 Lived Mode** - Community experiences and advocacy voices
- **🟨 Balanced Mode** - Weighted blend of research and lived experience

### **🛡️ Safety Defaults**
- **Consent Enforced** - All interactions respect user consent settings
- **PII Scrubbed** - Personal information automatically removed
- **Bias Monitoring** - Real-time fairness and representation checks
- **Transparency** - Full source attribution and trust scoring

---

## 🎯 **Demo Questions**

Try these example questions to see the AI in action:

### **🧠 ADHD Questions**
- "Does ADHD improve creativity?"
- "What are ADHD strengths in the workplace?"
- "How does hyperfocus work?"

### **🌈 Autism Questions**
- "What helps with sensory overload?"
- "What are autism strengths?"
- "How do autistic people communicate?"

### **🔗 Overlap Questions**
- "How do ADHD and autism overlap?"
- "Can you have both ADHD and dyslexia?"
- "What are neurodivergent superpowers?"

### **🏢 Workplace Questions**
- "What accommodations help neurodivergent employees?"
- "How to create inclusive teams?"
- "Neurodivergent leadership strengths?"

---

## 🚀 **Next: Ethics Dashboard**

Coming next - an interactive React dashboard showing:

- **📊 Trust Histogram** - Distribution of claim trust scores
- **🛡️ Consent Integrity** - Percentage of usable data by consent scope
- **🌈 Bias Gap Chart** - Fairness metrics across neurodivergent segments
- **🔍 Flag Queue** - Open issues, SLA timers, community resolutions
- **📋 Model Card** - Version info, data mix, known limitations

---

## 🗂️ **Development Setup**

### **Requirements**
- Python 3.8+
- FastAPI for mock server
- Modern web browser for interface

### **Installation**
```bash
# Clone the repo
git clone <repo-url>
cd neurodivergent-ai-demo

# Install Python dependencies
pip install -r requirements.txt

# Test CLI client
python cli/ask.py "Test question"

# Start mock server
python mock_server/server.py

# Test web interface
cd web && python -m http.server 8080
```

### **Testing**
```bash
# Test CLI with different modes
python cli/ask.py "Creativity test" --mode science
python cli/ask.py "Sensory test" --mode lived
python cli/ask.py "Overlap test" --mode balanced

# Test API directly
curl -X POST "http://localhost:8000/ask" \
     -H "Content-Type: application/json" \
     -d '{"question": "Test", "mode": "balanced"}'

# Get model card
curl "http://localhost:8000/modelcard"
```

---

## 🤝 **Community Principles**

### **🧠 Neurodivergent-First Design**
- **Strengths-Based** - Amplify creativity, hyperfocus, empathy, pattern recognition
- **Lived Experience** - Community stories valued equally with research
- **Nothing About Us Without Us** - Community governance and feedback loops
- **Accessible by Default** - Built for diverse cognitive and sensory needs

### **🛡️ Ethical Foundations**
- **Consent-Driven** - Full transparency and user control
- **Bias-Aware** - Continuous fairness monitoring and correction
- **Privacy-First** - Data protection and anonymization by design
- **Community-Governed** - Democratic oversight and policy revision

---

## 📜 **License & Ethics**

This project follows **neurodivergent-first ethical guidelines**:

- ✅ **Strengths-based framing** - Focus on abilities, not deficits
- ✅ **Consent-aware data handling** - Transparent, revocable permissions
- ✅ **Transparent trust scoring** - Explainable AI with source attribution
- ✅ **Community feedback loops** - Democratic governance and continuous improvement

---

## 🧨 **Roadmap**

### **✅ Now: Demo Clients**
- CLI client with full mode support
- Interactive web interface
- Mock server for demonstrations
- Comprehensive documentation

### **🚧 Next: Ethics Dashboard**
- Real-time transparency metrics
- Community governance interface
- Bias detection and reporting
- Model card and audit trails

### **🔮 Later: Full Integration**
- Connection to production AI system
- Advanced neurodivergent reasoning
- Truth graph knowledge representation
- Global community platform

---

## 🌟 **Get Involved**

This is **your** neurodivergent AI system. Ways to contribute:

- **🧪 Test the demos** - Try the CLI and web interface
- **💬 Share feedback** - Tell us what works and what doesn't
- **🏷️ Suggest features** - What would make this more useful?
- **🌍 Spread the word** - Share with neurodivergent communities
- **🔧 Contribute code** - Help build the future of inclusive AI

---

**🪄 BROSKI Protocol: Build fast, verify truth, celebrate progress! 🚀**

Built with ❤️ for the neurodivergent community
