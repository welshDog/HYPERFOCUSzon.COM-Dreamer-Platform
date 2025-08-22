#!/usr/bin/env python3
"""
🧠💎⚡ NEURODIVERGENT AI - CLI CLIENT ⚡💎🧠
================================================================

HYPERFOCUS ZONE EMPIRE - Neurodivergent-First AI Demo Client
Ask questions and get empathy-driven, strengths-based responses!

Modes:
🟦 science  - Peer-reviewed research and clinical data
🟩 lived    - Community stories and lived experiences
🟨 balanced - Weighted blend of both perspectives

Usage:
python ask.py "Does ADHD improve creativity?"
python ask.py "What helps with sensory overload?" --mode lived
python ask.py "ADHD and autism overlap" --mode science

================================================================
"""

import argparse
import json
import sys
from datetime import datetime
from typing import Any, Dict

import requests


class NeurodivergentAIClient:
    """🧠 CLI Client for Neurodivergent-First AI System"""

    def __init__(self, base_url: str = "http://localhost:8000"):
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update(
            {
                "User-Agent": "NeurodivergentAI-CLI/1.0",
                "Content-Type": "application/json",
            }
        )

    def ask_question(
        self, question: str, mode: str = "balanced", user_id: str = "demo-user"
    ) -> Dict[str, Any]:
        """🎯 Ask a question to the neurodivergent AI system"""

        payload = {
            "question": question,
            "mode": mode,
            "user_id": user_id,
            "timestamp": datetime.now().isoformat(),
        }

        try:
            response = self.session.post(
                f"{self.base_url}/ask", json=payload, timeout=30
            )

            if response.status_code == 200:
                return response.json()
            elif response.status_code == 403:
                return {
                    "error": "Consent not granted for this scope",
                    "message": "Please check your consent settings",
                }
            else:
                return {
                    "error": f"HTTP {response.status_code}",
                    "message": response.text,
                }

        except requests.exceptions.ConnectionError:
            return {
                "error": "Connection failed",
                "message": "Could not connect to AI server. Is it running?",
                "suggestion": "Try starting the mock server: python mock_server/server.py",
            }
        except requests.exceptions.Timeout:
            return {
                "error": "Request timeout",
                "message": "The AI is thinking deeply... please try again",
            }
        except Exception as e:
            return {"error": "Unexpected error", "message": str(e)}

    def get_model_card(self) -> Dict[str, Any]:
        """📋 Get model transparency information"""

        try:
            response = self.session.get(f"{self.base_url}/modelcard", timeout=10)
            if response.status_code == 200:
                return response.json()
            else:
                return {"error": f"HTTP {response.status_code}"}
        except Exception as e:
            return {"error": str(e)}

    def format_response(self, result: Dict[str, Any], mode: str) -> str:
        """🎨 Format the AI response for beautiful CLI display"""

        if "error" in result:
            return f"""
❌ ERROR: {result['error']}
💡 {result.get('message', 'Unknown error occurred')}
{result.get('suggestion', '')}
"""

        # Mode emoji mapping
        mode_emoji = {"science": "🟦", "lived": "🟩", "balanced": "🟨"}

        verdict = result.get("verdict", "❓ Unknown")
        trust = result.get("trust", 0.0)
        sources = result.get("sources", [])
        answer = result.get("answer", {})

        # Trust score visualization
        trust_bar = "█" * int(trust * 10) + "░" * (10 - int(trust * 10))

        output = f"""
╔══════════════════════════════════════════════════════════════╗
║  🧠💎⚡ NEURODIVERGENT AI - RESPONSE ⚡💎🧠                ║
╚══════════════════════════════════════════════════════════════╝

{mode_emoji.get(mode, '🟨')} MODE: {mode.upper()}
{verdict}

📊 TRUST SCORE: {trust:.2f} [{trust_bar}] ({int(trust*100)}%)

🔍 SOURCES ({len(sources)}):"""

        for i, source in enumerate(sources[:5], 1):
            output += f"\n   {i}. {source}"

        if len(sources) > 5:
            output += f"\n   ... and {len(sources) - 5} more sources"

        if answer:
            output += f"""

💬 EXPLANATION:
{answer.get('explanation', 'No explanation provided')}

🏷️ DETECTED THEMES:"""

            tags = answer.get("tags", {})
            if tags.get("strengths"):
                output += f"\n   💪 Strengths: {', '.join(tags['strengths'])}"
            if tags.get("overlaps"):
                output += f"\n   🔗 Overlaps: {', '.join(tags['overlaps'])}"
            if tags.get("struggles"):
                output += f"\n   ⚠️ Challenges: {', '.join(tags['struggles'])}"

        output += f"""

🧠 NEURODIVERGENT-FIRST APPROACH:
✅ Strengths-based framing
✅ Lived experience valued
✅ Community-driven insights
✅ Ethical transparency

🌟 Thank you for using Neurodivergent AI! 🌟
"""

        return output

    def format_model_card(self, model_info: Dict[str, Any]) -> str:
        """📋 Format model card information"""

        if "error" in model_info:
            return f"❌ Could not retrieve model card: {model_info['error']}"

        return f"""
╔══════════════════════════════════════════════════════════════╗
║  📋 NEURODIVERGENT AI - MODEL CARD                          ║
╚══════════════════════════════════════════════════════════════╝

🏷️ NAME: {model_info.get('name', 'Unknown')}
🌐 MODES: {', '.join(model_info.get('modes', []))}
🛡️ CONSENT: {model_info.get('consent', 'Unknown')}
🔒 PII HANDLING: {model_info.get('pii', 'Unknown')}
⚠️ LIMITATIONS: {', '.join(model_info.get('limits', []))}

🧠 DESIGNED FOR NEURODIVERGENT EXCELLENCE
"""


def main():
    """🚀 Main CLI application"""

    parser = argparse.ArgumentParser(
        description="🧠💎⚡ Neurodivergent AI CLI Client",
        epilog="Examples:\n"
        '  python ask.py "Does ADHD improve creativity?"\n'
        '  python ask.py "What helps with sensory overload?" --mode lived\n'
        '  python ask.py "ADHD and autism overlap" --mode science',
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument("question", help="Question to ask the neurodivergent AI")

    parser.add_argument(
        "--mode",
        "-m",
        choices=["science", "lived", "balanced"],
        default="balanced",
        help="AI mode: science (research), lived (community), balanced (both)",
    )

    parser.add_argument(
        "--server",
        "-s",
        default="http://localhost:8000",
        help="AI server URL (default: http://localhost:8000)",
    )

    parser.add_argument(
        "--user-id",
        "-u",
        default="demo-user",
        help="User ID for consent tracking (default: demo-user)",
    )

    parser.add_argument(
        "--model-card", action="store_true", help="Show model card information and exit"
    )

    parser.add_argument("--json", action="store_true", help="Output raw JSON response")

    args = parser.parse_args()

    # Initialize client
    client = NeurodivergentAIClient(args.server)

    # Handle model card request
    if args.model_card:
        model_info = client.get_model_card()
        print(client.format_model_card(model_info))
        return

    # Ask the question
    print(f'🧠 Asking neurodivergent AI: "{args.question}"')
    print(f"🎯 Mode: {args.mode}")
    print("⏳ Thinking...")

    result = client.ask_question(args.question, args.mode, args.user_id)

    if args.json:
        print(json.dumps(result, indent=2))
    else:
        print(client.format_response(result, args.mode))


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n🌟 Thank you for using Neurodivergent AI! 🌟")
        sys.exit(0)
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
        sys.exit(1)
