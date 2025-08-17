"""
🎯⚡💎 BROski♾️ GENIUS DETECTION & RADAR CHART GENERATOR 💎⚡🎯

This system generates visual intelligence radar charts, manages genius detection,
and creates beautiful visual representations of intelligence profiles.
"""

import json
import math
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import Circle
import datetime
from pathlib import Path
from typing import Dict, List, Tuple


class BROskiGeniusVisualizationEngine:
    """🎯 Visual intelligence profiling and genius detection system"""

    def __init__(self):
        self.intelligence_colors = {
            'linguistic': '#FF6B6B',          # Red - Communication
            'logical_math': '#4ECDC4',        # Teal - Logic
            'spatial': '#45B7D1',            # Blue - Spatial
            'musical': '#96CEB4',             # Green - Musical
            'bodily_kinesthetic': '#FFEAA7',  # Yellow - Physical
            'interpersonal': '#DDA0DD',       # Plum - Social
            'intrapersonal': '#98D8E8',       # Light Blue - Self
            'naturalistic': '#6AB04C',        # Dark Green - Nature
            'creative': '#FF9FF3',            # Pink - Creative
            'emotional': '#F9CA24',           # Orange - Emotional
            'practical': '#6C5CE7'            # Purple - Practical
        }

        self.genius_thresholds = {
            'genius': 0.85,
            'high_potential': 0.70,
            'developing': 0.50,
            'emerging': 0.30
        }

        print("🎯⚡💎 BROski♾️ GENIUS VISUALIZATION ENGINE ACTIVATED 💎⚡🎯")

    def create_intelligence_radar_chart(self, skill_vector: Dict, user_name: str = "User",
                                      save_path: str = None, show_genius_zone: bool = True) -> str:
        """Create a beautiful radar chart of intelligence scores"""

        # Extract intelligence types and scores
        intelligences = list(self.intelligence_colors.keys())
        scores = [skill_vector.get(intel, {}).get('value', 0) for intel in intelligences]
        confidence = [skill_vector.get(intel, {}).get('confidence', 0) for intel in intelligences]

        # Create the radar chart
        fig, ax = plt.subplots(figsize=(12, 10), subplot_kw=dict(projection='polar'))
        fig.patch.set_facecolor('#0F0F23')  # Dark background
        ax.set_facecolor('#1E1E3F')

        # Calculate angles for each intelligence type
        angles = np.linspace(0, 2 * np.pi, len(intelligences), endpoint=False).tolist()
        scores += scores[:1]  # Complete the circle
        angles += angles[:1]

        # Plot the main intelligence profile
        ax.plot(angles, scores, 'o-', linewidth=3, color='#00F5FF',
                markersize=8, markerfacecolor='#00F5FF', markeredgecolor='white',
                markeredgewidth=2, label='Intelligence Profile')
        ax.fill(angles, scores, alpha=0.25, color='#00F5FF')

        # Add genius zone if requested
        if show_genius_zone:
            genius_line = [self.genius_thresholds['genius']] * len(angles)
            ax.plot(angles, genius_line, '--', linewidth=2, color='#FFD700',
                   alpha=0.8, label='Genius Zone (0.85+)')
            ax.fill_between(angles, genius_line, [1.0] * len(angles),
                           alpha=0.1, color='#FFD700')

        # Customize the chart
        ax.set_ylim(0, 1.0)
        ax.set_yticks([0.2, 0.4, 0.6, 0.8, 1.0])
        ax.set_yticklabels(['0.2', '0.4', '0.6', '0.8', '1.0'],
                          color='white', fontsize=10)

        # Set intelligence type labels
        ax.set_xticks(angles[:-1])
        intelligence_labels = [intel.replace('_', ' ').title() for intel in intelligences]
        ax.set_xticklabels(intelligence_labels, color='white', fontsize=11,
                          fontweight='bold')

        # Add title and styling
        plt.title(f'🧠⚡ {user_name} - Intelligence Radar Map ⚡🧠',
                 fontsize=16, fontweight='bold', color='#00F5FF', pad=30)

        # Add legend
        ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1),
                 facecolor='#1E1E3F', edgecolor='white', labelcolor='white')

        # Add genius detection annotations
        avg_score = np.mean(scores[:-1])
        max_score = max(scores[:-1])
        top_intelligence = intelligences[scores[:-1].index(max_score)]

        genius_status = self._determine_genius_status(avg_score, max_score)

        # Add text annotations
        fig.text(0.02, 0.95, f'🏆 Genius Status: {genius_status["title"]}',
                fontsize=14, fontweight='bold', color=genius_status["color"],
                transform=fig.transFigure)

        fig.text(0.02, 0.90, f'🎯 Top Strength: {top_intelligence.replace("_", " ").title()} ({max_score:.2f})',
                fontsize=12, color='#00F5FF', transform=fig.transFigure)

        fig.text(0.02, 0.85, f'⭐ Average Score: {avg_score:.2f}',
                fontsize=12, color='white', transform=fig.transFigure)

        # Add BROski branding
        fig.text(0.98, 0.02, 'BROski♾️ Ultra Intelligence System',
                fontsize=10, color='#888888', ha='right', transform=fig.transFigure)

        # Save the chart
        if not save_path:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            save_path = f"h:/🧠⚡_INTELLIGENCE_RADAR_{user_name.replace(' ', '_')}_{timestamp}.png"

        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight',
                   facecolor='#0F0F23', edgecolor='none', transparent=False)
        plt.close()

        print(f"🎯 Radar chart generated: {save_path}")
        return save_path

    def _determine_genius_status(self, avg_score: float, max_score: float) -> Dict:
        """Determine genius status based on scores"""
        if avg_score >= 0.85 or max_score >= 0.95:
            return {"title": "GENIUS LEVEL 🔥", "color": "#FFD700"}
        elif avg_score >= 0.70 or max_score >= 0.85:
            return {"title": "HIGH POTENTIAL 🚀", "color": "#00F5FF"}
        elif avg_score >= 0.50:
            return {"title": "DEVELOPING 📈", "color": "#96CEB4"}
        else:
            return {"title": "EMERGING 🌱", "color": "#FFEAA7"}

    def create_genius_progression_chart(self, user_assessments: List[Dict], save_path: str = None) -> str:
        """Create a progression chart showing genius development over time"""

        if len(user_assessments) < 2:
            print("⚠️ Need at least 2 assessments to show progression")
            return None

        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(14, 10))
        fig.patch.set_facecolor('#0F0F23')

        # Extract data
        dates = [datetime.datetime.fromisoformat(a['timestamp']) for a in user_assessments]
        composite_scores = [a.get('composite_genius_score', 0) for a in user_assessments]

        # Plot 1: Composite Genius Score Over Time
        ax1.set_facecolor('#1E1E3F')
        ax1.plot(dates, composite_scores, 'o-', linewidth=3, color='#00F5FF',
                markersize=8, markerfacecolor='#FFD700', markeredgecolor='white',
                markeredgewidth=2)

        # Add genius threshold line
        ax1.axhline(y=0.85, color='#FFD700', linestyle='--', linewidth=2,
                   alpha=0.8, label='Genius Threshold')
        ax1.fill_between(dates, [0.85] * len(dates), [1.0] * len(dates),
                        alpha=0.1, color='#FFD700', label='Genius Zone')

        ax1.set_title('🧠⚡ Genius Development Progression ⚡🧠',
                     fontsize=16, fontweight='bold', color='#00F5FF', pad=20)
        ax1.set_ylabel('Composite Genius Score', color='white', fontweight='bold')
        ax1.tick_params(colors='white')
        ax1.legend(facecolor='#1E1E3F', edgecolor='white', labelcolor='white')
        ax1.grid(True, alpha=0.3, color='white')
        ax1.set_ylim(0, 1.0)

        # Plot 2: Top 3 Intelligence Areas Over Time
        ax2.set_facecolor('#1E1E3F')

        # Get top 3 intelligences from latest assessment
        latest_assessment = user_assessments[-1]
        if 'skill_vector' in latest_assessment:
            skill_vector = latest_assessment['skill_vector']
            top_3 = sorted(skill_vector.items(), key=lambda x: x[1].get('value', 0), reverse=True)[:3]

            for i, (intel_type, _) in enumerate(top_3):
                intel_scores = []
                for assessment in user_assessments:
                    if 'skill_vector' in assessment and intel_type in assessment['skill_vector']:
                        intel_scores.append(assessment['skill_vector'][intel_type].get('value', 0))
                    else:
                        intel_scores.append(0)

                color = self.intelligence_colors.get(intel_type, '#FFFFFF')
                label = intel_type.replace('_', ' ').title()
                ax2.plot(dates, intel_scores, 'o-', linewidth=2, color=color,
                        markersize=6, markerfacecolor=color, markeredgecolor='white',
                        markeredgewidth=1, label=label, alpha=0.8)

        ax2.set_title('🎯 Top 3 Intelligence Areas Development 🎯',
                     fontsize=14, fontweight='bold', color='#00F5FF', pad=15)
        ax2.set_ylabel('Intelligence Score', color='white', fontweight='bold')
        ax2.set_xlabel('Assessment Date', color='white', fontweight='bold')
        ax2.tick_params(colors='white')
        ax2.legend(facecolor='#1E1E3F', edgecolor='white', labelcolor='white')
        ax2.grid(True, alpha=0.3, color='white')
        ax2.set_ylim(0, 1.0)

        # Add BROski branding
        fig.text(0.98, 0.02, 'BROski♾️ Ultra Intelligence System - Progression Analytics',
                fontsize=10, color='#888888', ha='right', transform=fig.transFigure)

        # Save the chart
        if not save_path:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            save_path = f"h:/🧠⚡_GENIUS_PROGRESSION_{timestamp}.png"

        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight',
                   facecolor='#0F0F23', edgecolor='none', transparent=False)
        plt.close()

        print(f"🎯 Progression chart generated: {save_path}")
        return save_path

    def create_team_intelligence_map(self, team_profiles: List[Dict], save_path: str = None) -> str:
        """Create a team intelligence coordination map"""

        if len(team_profiles) < 2:
            print("⚠️ Need at least 2 team members to create team map")
            return None

        fig, ax = plt.subplots(figsize=(16, 12))
        fig.patch.set_facecolor('#0F0F23')
        ax.set_facecolor('#1E1E3F')

        # Create scatter plot where x = composite score, y = top intelligence score
        x_coords = []
        y_coords = []
        colors = []
        names = []

        for profile in team_profiles:
            composite = profile.get('composite_genius_score', 0)
            skill_vector = profile.get('skill_vector', {})

            if skill_vector:
                top_score = max([data.get('value', 0) for data in skill_vector.values()])
                top_intelligence = max(skill_vector.items(),
                                     key=lambda x: x[1].get('value', 0))[0]
                color = self.intelligence_colors.get(top_intelligence, '#FFFFFF')
            else:
                top_score = 0
                color = '#FFFFFF'

            x_coords.append(composite)
            y_coords.append(top_score)
            colors.append(color)
            names.append(profile.get('display_name', 'Unknown'))

        # Create scatter plot
        scatter = ax.scatter(x_coords, y_coords, c=colors, s=200, alpha=0.8,
                           edgecolors='white', linewidth=2)

        # Add names as annotations
        for i, name in enumerate(names):
            ax.annotate(name, (x_coords[i], y_coords[i]),
                       xytext=(5, 5), textcoords='offset points',
                       fontsize=11, fontweight='bold', color='white',
                       bbox=dict(boxstyle='round,pad=0.3', facecolor='black', alpha=0.7))

        # Add genius zones
        ax.axvline(x=0.85, color='#FFD700', linestyle='--', linewidth=2,
                  alpha=0.8, label='Genius Zone (Composite)')
        ax.axhline(y=0.85, color='#FF6B6B', linestyle='--', linewidth=2,
                  alpha=0.8, label='Genius Zone (Individual)')

        # Fill genius quadrant
        ax.fill([0.85, 1.0, 1.0, 0.85], [0.85, 0.85, 1.0, 1.0],
               alpha=0.1, color='#FFD700', label='Ultra Genius Zone')

        ax.set_xlabel('Composite Genius Score', fontsize=14, fontweight='bold', color='white')
        ax.set_ylabel('Top Intelligence Score', fontsize=14, fontweight='bold', color='white')
        ax.set_title('🏛️⚡ Team Intelligence Coordination Map ⚡🏛️',
                    fontsize=18, fontweight='bold', color='#00F5FF', pad=30)

        ax.tick_params(colors='white')
        ax.legend(facecolor='#1E1E3F', edgecolor='white', labelcolor='white')
        ax.grid(True, alpha=0.3, color='white')
        ax.set_xlim(0, 1.0)
        ax.set_ylim(0, 1.0)

        # Add team stats
        avg_composite = np.mean(x_coords)
        avg_top = np.mean(y_coords)
        genius_count = sum(1 for x, y in zip(x_coords, y_coords) if x >= 0.85 or y >= 0.85)

        stats_text = f"""
🎯 Team Intelligence Stats:
• Team Size: {len(team_profiles)} members
• Avg Composite Score: {avg_composite:.2f}
• Avg Top Intelligence: {avg_top:.2f}
• Genius-Level Members: {genius_count}
• Team Coordination Potential: {"LEGENDARY" if avg_composite > 0.7 else "HIGH" if avg_composite > 0.5 else "DEVELOPING"}
        """.strip()

        ax.text(0.02, 0.98, stats_text, transform=ax.transAxes,
               fontsize=12, color='white', verticalalignment='top',
               bbox=dict(boxstyle='round,pad=0.5', facecolor='#1E1E3F', alpha=0.8))

        # Add BROski branding
        fig.text(0.98, 0.02, 'BROski♾️ Ultra Intelligence System - Team Analytics',
                fontsize=10, color='#888888', ha='right', transform=fig.transFigure)

        # Save the chart
        if not save_path:
            timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
            save_path = f"h:/🏛️⚡_TEAM_INTELLIGENCE_MAP_{timestamp}.png"

        plt.tight_layout()
        plt.savefig(save_path, dpi=300, bbox_inches='tight',
                   facecolor='#0F0F23', edgecolor='none', transparent=False)
        plt.close()

        print(f"🏛️ Team intelligence map generated: {save_path}")
        return save_path

    def generate_intelligence_card_export(self, profile: Dict, card_type: str = "full") -> Dict:
        """Generate exportable intelligence card data"""

        # Create radar chart
        radar_path = self.create_intelligence_radar_chart(
            profile['skill_vector'],
            profile['display_name']
        )

        # Determine genius status
        composite = profile.get('composite_genius_score', 0)
        genius_status = self._determine_genius_status(composite, composite)

        # Create card data
        card_data = {
            "user_info": {
                "name": profile['display_name'],
                "user_id": profile['user_id'],
                "assessment_date": profile.get('last_assessed', ''),
                "genius_status": genius_status['title']
            },
            "intelligence_summary": {
                "composite_genius_score": composite,
                "top_strengths": profile.get('top_strengths', []),
                "genius_flags": profile.get('genius_flags', []),
                "broski_points": profile.get('broski_points', 0)
            },
            "visual_assets": {
                "radar_chart": radar_path,
                "color_scheme": "BROski Ultra Dark",
                "brand": "BROski♾️ Ultra Intelligence System"
            },
            "export_formats": {
                "pdf_ready": True,
                "png_ready": True,
                "discord_embed_ready": True,
                "print_friendly": True
            },
            "recommendations": self._generate_development_recommendations(profile),
            "timestamp": datetime.datetime.now().isoformat()
        }

        return card_data

    def _generate_development_recommendations(self, profile: Dict) -> List[Dict]:
        """Generate personalized development recommendations"""
        recommendations = []
        skill_vector = profile.get('skill_vector', {})

        # Find top 3 and bottom 2 intelligences
        sorted_skills = sorted(skill_vector.items(),
                             key=lambda x: x[1].get('value', 0), reverse=True)

        if len(sorted_skills) >= 3:
            # Strengths to amplify
            top_3 = sorted_skills[:3]
            for intel, data in top_3:
                if data.get('value', 0) >= 0.7:
                    recommendations.append({
                        "type": "amplify_strength",
                        "intelligence": intel,
                        "title": f"Amplify Your {intel.replace('_', ' ').title()} Genius",
                        "description": f"Your {intel.replace('_', ' ')} score of {data.get('value', 0):.2f} shows real potential. Consider mentoring others or taking on advanced challenges in this area.",
                        "priority": "high",
                        "time_investment": "15-30 minutes daily"
                    })

        if len(sorted_skills) >= 2:
            # Areas for growth
            bottom_2 = sorted_skills[-2:]
            for intel, data in bottom_2:
                if data.get('value', 0) < 0.5:
                    recommendations.append({
                        "type": "growth_opportunity",
                        "intelligence": intel,
                        "title": f"Develop Your {intel.replace('_', ' ').title()} Skills",
                        "description": f"Your {intel.replace('_', ' ')} area has room for growth. Small, consistent practice can make a big difference.",
                        "priority": "medium",
                        "time_investment": "10-15 minutes weekly"
                    })

        # Neurodivergent-specific recommendations
        if profile.get('genius_flags'):
            recommendations.append({
                "type": "neurodivergent_optimization",
                "intelligence": "meta",
                "title": "ADHD Superpower Activation",
                "description": "Your genius-level abilities suggest strong neurodivergent traits. Use hyperfocus sessions, creative breaks, and dopamine rewards to maximize your potential.",
                "priority": "high",
                "time_investment": "Integrate into daily routine"
            })

        return recommendations[:5]  # Return top 5 recommendations


def main():
    """Demo the visualization engine"""
    print("🎯" * 30)
    print("🧠⚡💎 BROski♾️ GENIUS VISUALIZATION DEMO 💎⚡🧠")
    print("🎯" * 30)

    # Sample data for demo
    demo_skill_vector = {
        'linguistic': {'value': 0.72, 'confidence': 0.88},
        'logical_math': {'value': 0.95, 'confidence': 0.92},
        'spatial': {'value': 0.40, 'confidence': 0.70},
        'musical': {'value': 0.10, 'confidence': 0.60},
        'bodily_kinesthetic': {'value': 0.78, 'confidence': 0.85},
        'interpersonal': {'value': 0.85, 'confidence': 0.90},
        'intrapersonal': {'value': 0.60, 'confidence': 0.80},
        'naturalistic': {'value': 0.30, 'confidence': 0.65},
        'creative': {'value': 0.92, 'confidence': 0.95},
        'emotional': {'value': 0.75, 'confidence': 0.82},
        'practical': {'value': 0.81, 'confidence': 0.87}
    }

    engine = BROskiGeniusVisualizationEngine()

    # Generate radar chart
    print("\n🎯 Generating intelligence radar chart...")
    radar_path = engine.create_intelligence_radar_chart(demo_skill_vector, "Chief Lyndz")

    # Create sample profile for card export
    demo_profile = {
        'user_id': 'demo_chief_lyndz',
        'display_name': 'Chief Lyndz',
        'skill_vector': demo_skill_vector,
        'composite_genius_score': 0.88,
        'genius_flags': ['creative_outlier', 'problem_solver_pro'],
        'broski_points': 2500,
        'top_strengths': [('logical_math', 0.95), ('creative', 0.92), ('interpersonal', 0.85)],
        'last_assessed': datetime.datetime.now().isoformat()
    }

    # Generate exportable card
    print("\n💎 Generating intelligence card export...")
    card_data = engine.generate_intelligence_card_export(demo_profile)

    # Save card data
    card_file = f"h:/🎯⚡_INTELLIGENCE_CARD_EXPORT_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(card_file, 'w', encoding='utf-8') as f:
        json.dump(card_data, f, indent=2, ensure_ascii=False)

    print(f"\n🎊 Demo Complete!")
    print(f"📊 Radar chart: {radar_path}")
    print(f"💎 Intelligence card: {card_file}")
    print("\n🚀 Ready for legendary intelligence visualization!")


if __name__ == "__main__":
    main()
