import json
import sqlite3
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

class AnalyticsDashboardHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            
            # Get analytics data
            analytics_data = self.get_analytics_data()
            
            html_content = f"""
            <!DOCTYPE html>
            <html>
            <head>
                <title>V2 Analytics Dashboard</title>
                <style>
                    body {{ font-family: Arial, sans-serif; background: #1a1a1a; color: #fff; margin: 0; padding: 20px; }}
                    .header {{ text-align: center; margin-bottom: 30px; }}
                    .metrics {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(300px, 1fr)); gap: 20px; }}
                    .metric-card {{ background: #2a2a2a; border-radius: 10px; padding: 20px; border: 2px solid #444; }}
                    .metric-title {{ font-size: 18px; font-weight: bold; margin-bottom: 10px; color: #00ff88; }}
                    .metric-value {{ font-size: 24px; font-weight: bold; color: #fff; }}
                    .metric-subtitle {{ font-size: 14px; color: #ccc; margin-top: 5px; }}
                    .status {{ color: #00ff88; font-weight: bold; }}
                </style>
            </head>
            <body>
                <div class="header">
                    <h1>DOPAMINE GUARDIAN V2 ANALYTICS</h1>
                    <p class="status">System Status: OPERATIONAL</p>
                    <p>Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}</p>
                </div>
                
                <div class="metrics">
                    <div class="metric-card">
                        <div class="metric-title">Total Mood Check-ins</div>
                        <div class="metric-value">{analytics_data['total_checkins']}</div>
                        <div class="metric-subtitle">Recorded mood entries</div>
                    </div>
                    
                    <div class="metric-card">
                        <div class="metric-title">Total Wins</div>
                        <div class="metric-value">{analytics_data['total_wins']}</div>
                        <div class="metric-subtitle">Achievements logged</div>
                    </div>
                    
                    <div class="metric-card">
                        <div class="metric-title">Average Mood</div>
                        <div class="metric-value">{analytics_data['avg_mood']:.1f}/10</div>
                        <div class="metric-subtitle">Overall mood trend</div>
                    </div>
                    
                    <div class="metric-card">
                        <div class="metric-title">Average Energy</div>
                        <div class="metric-value">{analytics_data['avg_energy']:.1f}/10</div>
                        <div class="metric-subtitle">Energy levels</div>
                    </div>
                    
                    <div class="metric-card">
                        <div class="metric-title">Average Focus</div>
                        <div class="metric-value">{analytics_data['avg_focus']:.1f}/10</div>
                        <div class="metric-subtitle">Focus performance</div>
                    </div>
                    
                    <div class="metric-card">
                        <div class="metric-title">System Health</div>
                        <div class="metric-value">OPERATIONAL</div>
                        <div class="metric-subtitle">V2 components active</div>
                    </div>
                </div>
                
                <div style="text-align: center; margin-top: 40px; color: #666;">
                    <p>V2 Deployment Emergency Fix Complete</p>
                    <p>Analytics Dashboard Running on Port 9999</p>
                </div>
            </body>
            </html>
            """
            
            self.wfile.write(html_content.encode())
            
        elif self.path == '/api/health':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            health_data = {
                "status": "healthy",
                "timestamp": datetime.now().isoformat(),
                "uptime": "operational",
                "version": "2.0"
            }
            
            self.wfile.write(json.dumps(health_data).encode())
            
        else:
            self.send_error(404)
    
    def get_analytics_data(self):
        try:
            conn = sqlite3.connect('dopamine_guardian.db')
            cursor = conn.cursor()
            
            # Get analytics data
            cursor.execute("SELECT COUNT(*) FROM mood_checkins")
            total_checkins = cursor.fetchone()[0]
            
            cursor.execute("SELECT COUNT(*) FROM wins")
            total_wins = cursor.fetchone()[0]
            
            cursor.execute("SELECT AVG(mood_score), AVG(energy_level), AVG(focus_level) FROM mood_checkins")
            averages = cursor.fetchone()
            
            conn.close()
            
            return {
                'total_checkins': total_checkins,
                'total_wins': total_wins,
                'avg_mood': averages[0] or 0,
                'avg_energy': averages[1] or 0,
                'avg_focus': averages[2] or 0
            }
        except:
            return {
                'total_checkins': 0,
                'total_wins': 0,
                'avg_mood': 0,
                'avg_energy': 0,
                'avg_focus': 0
            }

def start_dashboard():
    server = HTTPServer(('localhost', 9999), AnalyticsDashboardHandler)
    print("Analytics Dashboard started on http://localhost:9999")
    server.serve_forever()

if __name__ == "__main__":
    start_dashboard()
