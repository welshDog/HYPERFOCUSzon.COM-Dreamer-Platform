/*
 * App.jsx
 * -------
 * Simple React front end for the BROski auto–business portal system.  It
 * fetches the list of available portals from the backend and
 * implements an "Agent Chooser" that asks the user what they need and
 * recommends the appropriate portal based on keyword matching.
 *
 * To integrate this into a full application, create a new React
 * project (e.g. with Create React App or Vite), copy this component
 * into ``src/App.jsx``, and ensure that requests to `/api/*` are
 * proxied to your FastAPI backend during development.
 */

import React, { useState, useEffect } from 'react';

const keywordMapping = {
  shop: 'Creator Portal Showcase',
  creator: 'Creator Portal Showcase',
  coaching: 'Creator Portal Showcase',
  course: 'Creator Portal Showcase',
  showcase: 'Showcase Portal Demo',
  project: 'Showcase Portal Demo',
  admin: 'Admin Portal Showcase',
  dashboard: 'Admin Portal Showcase',
};

function AgentChooser({ portals }) {
  const [question, setQuestion] = useState('');
  const [recommendation, setRecommendation] = useState(null);

  const handleSubmit = (e) => {
    e.preventDefault();
    const lower = question.toLowerCase();
    let matchedPortal = null;
    Object.keys(keywordMapping).forEach((keyword) => {
      if (lower.includes(keyword)) {
        matchedPortal = keywordMapping[keyword];
      }
    });
    setRecommendation(matchedPortal);
  };

  return (
    <div className="agent-chooser">
      <h2>What do you need today?</h2>
      <form onSubmit={handleSubmit} style={{ display: 'flex', gap: '8px' }}>
        <input
          type="text"
          value={question}
          placeholder="Type your request (e.g. shop, coaching, admin)"
          onChange={(e) => setQuestion(e.target.value)}
        />
        <button type="submit">Find Portal</button>
      </form>
      {recommendation && (
        <div style={{ marginTop: '1rem' }}>
          <p>
            Recommended Portal: <strong>{recommendation}</strong>
          </p>
          {portals
            .filter((p) => p.name === recommendation)
            .map((p) => (
              <a key={p.path} href={`/${p.path}`} target="_blank" rel="noopener noreferrer">
                Visit {p.name}
              </a>
            ))}
        </div>
      )}
    </div>
  );
}

export default function App() {
  const [portals, setPortals] = useState([]);

  useEffect(() => {
    async function fetchPortals() {
      try {
        const res = await fetch('/api/portals');
        const data = await res.json();
        setPortals(data);
      } catch (err) {
        console.error('Failed to fetch portals', err);
      }
    }
    fetchPortals();
  }, []);

  return (
    <div style={{ padding: '2rem', fontFamily: 'Arial, sans-serif' }}>
      <h1>HYPERFOCUS ZONE Master Directory</h1>
      <p>Welcome to the Hyperfocus Zone! Select a service or ask the agent for guidance.</p>
      <AgentChooser portals={portals} />
      <hr style={{ margin: '2rem 0' }} />
      <h2>Available Portals</h2>
      <ul>
        {portals.map((portal) => (
          <li key={portal.path}>
            <a href={`/${portal.path}`} target="_blank" rel="noopener noreferrer">
              {portal.name}
            </a>
          </li>
        ))}
      </ul>
    </div>
  );
}