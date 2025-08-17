# 🚀💎 BROSKI Auto‑Business Portal System 💎🚀

Welcome to the **BROSKI Auto‑Business Portal System**, a practical starter
kit that ties together the ideas showcased in the HYPERFOCUS Zone
repository and turns them into a living system.  This package includes a
simple backend, a React front‑end and a set of pluggable **agents**
designed to automate revenue collection, marketing, customer success,
analytics and security.  The goal is to help you build a business that
**runs itself**, delights customers and celebrates every sale.

## ✨ Inspiration

The Hyperfocus Zone repository describes a **Three‑Portal Network** – the
Admin Portal for operations management, the Creator Portal for content
creation, and the Showcase Portal for live demos【968767661064778†L34-L38】.  It also highlights an
**AI integration layer** including the BROski♾️ Automatic COO, ARIA
intelligence and an agent army【968767661064778†L39-L43】.  This project takes those ideas and
turns them into runnable code so you can start automating your own
empire.

## 🧱 Architecture

The system consists of two main components:

1. **Backend (FastAPI)** – provides JSON endpoints for discovering
   available portals, processing payments, handling user questions and
   recording analytics events.  It lives in `backend/app.py` and
   relies on helper modules:
   - `portal_scanner.py` – scans a folder of HTML files and returns
     human‑friendly portal descriptors.  It enables the “Master
     Directory” by enumerating all portals dynamically.
   - `agents.py` – defines stubs for **Revenue**, **Marketing**,
     **Customer Success**, **Analytics** and **Security** agents.  These
     classes centralise integrations with services like Stripe or
     Discord while keeping your business logic clean.
2. **Front‑End (React)** – implements a simple **Agent Chooser** that
   asks the visitor what they need and recommends a portal based on
   keyword matching.  It also lists all portals discovered by the
   backend and links to their HTML files.

The default folder layout looks like this:

```
auto_business_portal/
├── backend/
│   ├── app.py           # FastAPI application exposing /api endpoints
│   ├── portal_scanner.py# Scan HTML portals in the portals/ folder
│   └── agents.py        # Stub implementations of the BROSKI agent army
└── frontend/
    └── App.jsx         # React component for the master directory & agent chooser
```

## ⚙️ Setup

### Prerequisites

- **Python 3.10+** and **Node 18+** installed on your system.
- A folder called `portals` in your project root containing your
  portal HTML files.  You can start by copying the showcase HTML from
  the HYPERFOCUS Zone repository (e.g. `portals/admin-portal-showcase.html`,
  `portals/creator-portal-showcase.html`, `portals/showcase-portal-demo.html`).

### Backend installation

1. Create a virtual environment and install dependencies:

   ```bash
   cd auto_business_portal/backend
   python -m venv .venv
   source .venv/bin/activate
   pip install fastapi uvicorn
   ```

2. Run the development server:

   ```bash
   uvicorn app:app --reload --port 8000
   ```

   The API will be available at `http://localhost:8000/api/portals`.

### Front‑end installation

This project does not include a full React build toolchain.  To try
the front‑end component you can integrate the `App.jsx` into an
existing React application (created with [Create React App](https://create-react-app.dev/) or Vite).  For example:

1. Copy `frontend/App.jsx` into your React project’s `src` folder.

2. Import it in your `index.js` and render it.

3. During development configure a proxy so that requests to `/api/*`
   are forwarded to your FastAPI backend running on port 8000.  In
   Create React App you can add a `proxy` field in `package.json`:

   ```json
   {
     "proxy": "http://localhost:8000"
   }
   ```

4. Start your React app and open it in a browser.  You should see the
   master directory listing your portals and the agent chooser.

## 🤖 Agents explained

The agent army is inspired by the AI integration layer described in
the original repository【968767661064778†L39-L43】.  Each agent class in `agents.py` encapsulates
responsibility for a particular domain:

- **RevenueAgent** – handles payments through Stripe, Patreon, TikTok
  shop or Etsy.  In the stub implementation it logs the payment and
  returns success.  Extend this class with real API calls when you
  connect your accounts.
- **MarketingAgent** – launches campaigns on channels such as Discord,
  TikTok or email.  Use this to announce new products or sales.
- **CustomerSuccessAgent** – responds to customer queries and can be
  upgraded to use language models for AI‑driven support.
- **AnalyticsAgent** – records events like purchases or support
  interactions.  Wire this to an analytics backend for deeper insights.
- **SecurityAgent** – validates users and monitors transactions for
  fraud.  Expand this with calls to your identity provider or risk
  engine.

These agents demonstrate how you might connect **real payment flows**,
**auto‑marketing**, **customer success**, **analytics** and **security** into
a seamless pipeline.  By centralising this logic you make it easy to
swap providers and track state across the system.

## 🛣️ Workflow

The end‑to‑end customer journey in this system mirrors the **auto
business flow** described in the blueprint:

1. **User visits master directory.**  They see all available services and
   can either click directly or type what they need into the agent
   chooser.
2. **Agent Chooser routes the user.**  Based on simple keyword
   matching the front‑end suggests the best portal (e.g. shopping
   requests open the creator portal).  You can extend this logic to use
   natural language processing or a chatbot.
3. **Instant payment & onboarding.**  When the user initiates a
   purchase, the back‑end calls the revenue agent to process the
   payment.  Upon success you can use the marketing and customer
   success agents to send onboarding messages via Discord or email.
4. **Follow up & upsell.**  Use the analytics and marketing agents to
   track engagement and trigger follow‑up offers (coaching, VIP
   memberships, etc.).

## 📈 Extending this project

This starter kit is meant to be hacked on.  Here are some ideas for
next steps:

- **Parse portal metadata**: Instead of inferring portal names from file
  names, read titles or config objects embedded in each HTML file.
- **Real payment providers**: Use Stripe’s Python SDK to implement
  actual charging in `RevenueAgent.process_payment`.
- **AI‑powered routing**: Replace the keyword mapping in `App.jsx`
  with a call to a language model that interprets user intent.
- **Gamification**: Integrate a points system and Discord bot to award
  BROski$ or badges whenever a user completes an action, mirroring
  the ADHD‑friendly rewards described in the showcase【968767661064778†L137-L149】.

By following the **LOOK‑THEN‑BUILD** methodology【968767661064778†L85-L95】 you can incrementally
improve the system without duplicating work: scout existing features,
report findings, get approval, then build.  Happy hacking!