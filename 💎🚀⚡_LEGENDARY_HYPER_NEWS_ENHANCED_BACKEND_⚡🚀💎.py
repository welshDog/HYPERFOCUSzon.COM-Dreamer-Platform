#!/usr/bin/env python3
"""
💎🚀⚡ LEGENDARY HYPER NEWS WEB3 ENHANCED BACKEND ⚡🚀💎
Next-Generation Web3 News Portal with DeFi, NFT, AI & Gamification
Fully Integrated Enhancement Engine for Supreme User Experience
"""

import asyncio
import json
import time
import datetime
import feedparser
import requests
from flask import Flask, render_template, jsonify, request
from flask_cors import CORS
from threading import Thread
import webbrowser
from dataclasses import dataclass, asdict
from typing import List, Dict, Any, Optional
import logging
import openai
import os
import sqlite3
import hashlib
from dotenv import load_dotenv
import aiohttp
from concurrent.futures import ThreadPoolExecutor

# Load environment variables
load_dotenv('empire.env')

# Import tech blog extension
from hyper_news_tech_blog_extension_engine import TechBlogEngine, create_tech_blog_blueprint

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - 🚀 %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

@dataclass
class NewsItem:
    """Enhanced News item structure"""
    title: str
    content: str
    timestamp: datetime.datetime
    source: str
    tags: List[str]
    sentiment: str = "neutral"
    importance: int = 1
    web3_relevance: float = 0.0
    ai_analysis: Optional[str] = None
    user_engagement: int = 0

class LegendaryWeb3NewsPortal:
    """🚀 LEGENDARY Web3 News Portal with Enhancement Engine"""
    
    def __init__(self):
        self.app = Flask(__name__)
        CORS(self.app)
        
        self.news_items: List[NewsItem] = []
        self.db_path = 'legendary_web3_portal.db'
        
        # Initialize databases
        self.init_databases()
        
        # Initialize Tech Blog Extension
        self.tech_blog_engine = TechBlogEngine(self.db_path)
        tech_blog_bp = create_tech_blog_blueprint(self.tech_blog_engine)
        self.app.register_blueprint(tech_blog_bp)
        
        # API Configuration
        self.openai_api_key = os.getenv('OPENAI_API_KEY')
        self.defi_llama_api = "https://api.llama.fi"
        self.opensea_api = "https://api.opensea.io/api/v1"
        
        # News Sources
        self.sources = {
            'coindesk': 'https://www.coindesk.com/arc/outboundfeeds/rss/',
            'cointelegraph': 'https://cointelegraph.com/rss',
            'theblock': 'https://www.theblock.co/rss.xml',
            'decrypt': 'https://decrypt.co/feed',
            'ethereum_blog': 'https://blog.ethereum.org/feed.xml',
            'polygon_blog': 'https://blog.polygon.technology/feed'
        }
        
        # Gamification Settings
        self.rewards = {
            'read_article': 10,
            'defi_read': 25,
            'nft_read': 20,
            'ai_summary': 50,
            'daily_visit': 100,
            'weekly_streak': 500
        }
        
        self.setup_routes()
        logger.info("🚀💎 LEGENDARY Web3 Portal Initialized! 💎🚀")
    
    def init_databases(self):
        """Initialize all required databases"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # News table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS news_items (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT NOT NULL,
                    content TEXT,
                    timestamp DATETIME,
                    source TEXT,
                    tags TEXT,
                    sentiment TEXT DEFAULT 'neutral',
                    ai_analysis TEXT,
                    user_engagement INTEGER DEFAULT 0
                )
            ''')
            
            # DeFi Protocols table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS defi_protocols (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    protocol TEXT NOT NULL,
                    tvl REAL,
                    volume_24h REAL,
                    yield_percentage REAL,
                    risk_score INTEGER,
                    last_updated DATETIME
                )
            ''')
            
            # NFT Collections table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS nft_collections (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    floor_price REAL,
                    volume_24h REAL,
                    change_24h REAL,
                    trending_score INTEGER,
                    last_updated DATETIME
                )
            ''')
            
            # User Statistics table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_stats (
                    user_id TEXT PRIMARY KEY,
                    broskie_balance INTEGER DEFAULT 0,
                    articles_read INTEGER DEFAULT 0,
                    level INTEGER DEFAULT 1,
                    streak_days INTEGER DEFAULT 0,
                    last_visit DATETIME,
                    total_achievements INTEGER DEFAULT 0,
                    preferences TEXT DEFAULT '{}'
                )
            ''')
            
            # User Achievements table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS user_achievements (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    user_id TEXT NOT NULL,
                    achievement_name TEXT NOT NULL,
                    achievement_description TEXT,
                    earned_at DATETIME,
                    UNIQUE(user_id, achievement_name)
                )
            ''')
            
            # AI Analysis Cache table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS ai_analysis_cache (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    content_hash TEXT UNIQUE,
                    analysis TEXT,
                    sentiment TEXT,
                    model_used TEXT,
                    token_usage INTEGER,
                    created_at DATETIME
                )
            ''')
            
            conn.commit()
            conn.close()
            logger.info("✅ Databases initialized successfully!")
            
        except Exception as e:
            logger.error(f"❌ Database initialization error: {e}")
    
    def setup_routes(self):
        """Setup all API routes"""
        
        @self.app.route('/')
        def index():
            """Serve the legendary portal"""
            return render_template('💎🚀⚡_LEGENDARY_HYPER_NEWS_WEB3_PORTAL_⚡🚀💎.html')
        
        @self.app.route('/api/news')
        def get_news():
            """Get latest news with enhanced features"""
            return jsonify({
                'news': [asdict(item) for item in self.news_items[:20]],
                'status': 'legendary_active',
                'total_items': len(self.news_items)
            })
        
        @self.app.route('/api/enhanced/personalized_feed', methods=['POST'])
        def get_personalized_feed():
            """Get personalized news feed based on user preferences"""
            try:
                data = request.json
                user_id = data.get('user_id', 'default_user')
                
                # Get user preferences
                preferences = self.get_user_preferences(user_id)
                
                # Filter and rank news based on preferences
                personalized_news = self.personalize_news(preferences)
                
                return jsonify({
                    'news': [asdict(item) for item in personalized_news[:15]],
                    'user_id': user_id,
                    'preferences_applied': True
                })
                
            except Exception as e:
                logger.error(f"❌ Personalization error: {e}")
                return jsonify({'error': str(e)}), 500
        
        @self.app.route('/api/enhanced/defi_data')
        def get_defi_data():
            """Get latest DeFi protocol data"""
            try:
                protocols = self.fetch_defi_protocols()
                return jsonify({
                    'defi_protocols': protocols,
                    'last_updated': datetime.datetime.now().isoformat()
                })
            except Exception as e:
                logger.error(f"❌ DeFi data error: {e}")
                return jsonify({'error': str(e)}), 500
        
        @self.app.route('/api/enhanced/nft_collections')
        def get_nft_data():
            """Get latest NFT collection data"""
            try:
                collections = self.fetch_nft_collections()
                return jsonify({
                    'nft_collections': collections,
                    'last_updated': datetime.datetime.now().isoformat()
                })
            except Exception as e:
                logger.error(f"❌ NFT data error: {e}")
                return jsonify({'error': str(e)}), 500
        
        @self.app.route('/api/enhanced/user_stats', methods=['POST'])
        def update_user_stats():
            """Update user statistics and handle gamification"""
            try:
                data = request.json
                user_id = data.get('user_id', 'default_user')
                action = data.get('action', 'portal_visit')
                
                stats = self.update_user_gamification(user_id, action)
                return jsonify(stats)
                
            except Exception as e:
                logger.error(f"❌ User stats error: {e}")
                return jsonify({'error': str(e)}), 500
        
        @self.app.route('/api/enhanced/ai_analysis', methods=['POST'])
        def generate_ai_analysis():
            """Generate AI-powered market analysis"""
            try:
                data = request.json
                user_id = data.get('user_id', 'default_user')
                analysis_type = data.get('analysis_type', 'trend_prediction')
                
                analysis = self.generate_market_analysis(analysis_type)
                
                # Update user stats for AI usage
                self.update_user_gamification(user_id, 'ai_summary')
                
                return jsonify(analysis)
                
            except Exception as e:
                logger.error(f"❌ AI analysis error: {e}")
                return jsonify({'error': str(e)}), 500
    
    def fetch_defi_protocols(self):
        """Fetch latest DeFi protocol data"""
        try:
            # Check database cache first
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('''
                SELECT * FROM defi_protocols 
                WHERE last_updated > datetime('now', '-1 hour')
                ORDER BY tvl DESC LIMIT 10
            ''')
            
            cached_data = cursor.fetchall()
            
            if cached_data:
                protocols = []
                for row in cached_data:
                    protocols.append({
                        'protocol': row[1],
                        'tvl': row[2],
                        'volume_24h': row[3],
                        'yield_percentage': row[4],
                        'risk_score': row[5]
                    })
                conn.close()
                return protocols
            
            # Fetch fresh data from DeFi Llama
            protocols_url = f"{self.defi_llama_api}/protocols"
            response = requests.get(protocols_url, timeout=10)
            
            if response.status_code == 200:
                data = response.json()
                protocols = []
                
                for protocol in data[:10]:  # Top 10 protocols
                    protocol_data = {
                        'protocol': protocol.get('name', 'Unknown'),
                        'tvl': protocol.get('tvl', 0),
                        'volume_24h': protocol.get('volume_24h', 0),
                        'yield_percentage': self.calculate_yield(protocol),
                        'risk_score': self.calculate_risk_score(protocol)
                    }
                    
                    protocols.append(protocol_data)
                    
                    # Cache in database
                    cursor.execute('''
                        INSERT OR REPLACE INTO defi_protocols 
                        (protocol, tvl, volume_24h, yield_percentage, risk_score, last_updated)
                        VALUES (?, ?, ?, ?, ?, ?)
                    ''', (
                        protocol_data['protocol'],
                        protocol_data['tvl'],
                        protocol_data['volume_24h'],
                        protocol_data['yield_percentage'],
                        protocol_data['risk_score'],
                        datetime.datetime.now()
                    ))
                
                conn.commit()
                conn.close()
                return protocols
            
            conn.close()
            return []
            
        except Exception as e:
            logger.error(f"❌ DeFi fetch error: {e}")
            return []
    
    def fetch_nft_collections(self):
        """Fetch NFT collection data from multiple sources"""
        try:
            # Mock data for now (replace with actual API calls)
            collections = [
                {
                    'name': 'Bored Ape Yacht Club',
                    'floor_price': 45.2,
                    'volume_24h': 234.5,
                    'change_24h': 5.2,
                    'trending_score': 8
                },
                {
                    'name': 'Art Blocks',
                    'floor_price': 1.2,
                    'volume_24h': 67.3,
                    'change_24h': 12.1,
                    'trending_score': 7
                },
                {
                    'name': 'Azuki',
                    'floor_price': 8.9,
                    'volume_24h': 123.4,
                    'change_24h': -2.3,
                    'trending_score': 6
                }
            ]
            
            # Cache in database
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            for collection in collections:
                cursor.execute('''
                    INSERT OR REPLACE INTO nft_collections 
                    (name, floor_price, volume_24h, change_24h, trending_score, last_updated)
                    VALUES (?, ?, ?, ?, ?, ?)
                ''', (
                    collection['name'],
                    collection['floor_price'],
                    collection['volume_24h'],
                    collection['change_24h'],
                    collection['trending_score'],
                    datetime.datetime.now()
                ))
            
            conn.commit()
            conn.close()
            
            return collections
            
        except Exception as e:
            logger.error(f"❌ NFT fetch error: {e}")
            return []
    
    def calculate_yield(self, protocol):
        """Calculate estimated yield for protocol"""
        # Simplified yield calculation
        tvl = protocol.get('tvl', 0)
        if tvl > 1000000000:  # > 1B TVL
            return round(5 + (tvl / 10000000000), 1)  # Lower yield for high TVL
        return round(8 + (1000000000 - tvl) / 100000000, 1)
    
    def calculate_risk_score(self, protocol):
        """Calculate risk score (1-10, 1 = lowest risk)"""
        tvl = protocol.get('tvl', 0)
        age_days = protocol.get('age_days', 365)
        
        # Lower risk for higher TVL and older protocols
        risk = 10
        if tvl > 1000000000:
            risk -= 3
        if age_days > 365:
            risk -= 2
        if protocol.get('audited', False):
            risk -= 2
            
        return max(1, min(10, risk))
    
    def update_user_gamification(self, user_id, action):
        """Update user stats and handle gamification"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            # Get current user stats
            cursor.execute('SELECT * FROM user_stats WHERE user_id = ?', (user_id,))
            user_data = cursor.fetchone()
            
            if not user_data:
                # Create new user
                cursor.execute('''
                    INSERT INTO user_stats (user_id, broskie_balance, articles_read, level, streak_days, last_visit, total_achievements)
                    VALUES (?, 100, 0, 1, 0, ?, 0)
                ''', (user_id, datetime.datetime.now()))
                conn.commit()
                
                # Get the newly created user
                cursor.execute('SELECT * FROM user_stats WHERE user_id = ?', (user_id,))
                user_data = cursor.fetchone()
            
            # Unpack user data
            _, broskie_balance, articles_read, level, streak_days, last_visit, total_achievements, preferences = user_data
            
            # Calculate rewards
            rewards_earned = 0
            new_achievements = []
            
            if action in self.rewards:
                rewards_earned = self.rewards[action]
                broskie_balance += rewards_earned
                
                if action == 'read_article' or action == 'defi_read':
                    articles_read += 1
                    
                    # Check for reading achievements
                    if articles_read == 1:
                        new_achievements.append(('📖 First Steps', 'Read your first Web3 article'))
                    elif articles_read == 10:
                        new_achievements.append(('📚 Bookworm', 'Read 10 articles'))
                    elif articles_read == 50:
                        new_achievements.append(('🧠 Knowledge Seeker', 'Read 50 articles'))
            
            # Update streak
            if last_visit:
                last_visit_date = datetime.datetime.fromisoformat(last_visit)
                today = datetime.datetime.now().date()
                last_date = last_visit_date.date()
                
                if (today - last_date).days == 1:
                    streak_days += 1
                    if streak_days == 7:
                        new_achievements.append(('🔥 Week Warrior', '7-day reading streak'))
                        rewards_earned += self.rewards['weekly_streak']
                        broskie_balance += self.rewards['weekly_streak']
                elif (today - last_date).days > 1:
                    streak_days = 1
            else:
                streak_days = 1
            
            # Calculate new level
            new_level = min(10, 1 + (articles_read // 10))
            if new_level > level:
                new_achievements.append((f'⬆️ Level {new_level}', f'Reached level {new_level}'))
                level = new_level
            
            # Update user stats
            cursor.execute('''
                UPDATE user_stats 
                SET broskie_balance = ?, articles_read = ?, level = ?, streak_days = ?, 
                    last_visit = ?, total_achievements = ?
                WHERE user_id = ?
            ''', (
                broskie_balance, articles_read, level, streak_days,
                datetime.datetime.now(), total_achievements + len(new_achievements), user_id
            ))
            
            # Add new achievements
            for name, description in new_achievements:
                cursor.execute('''
                    INSERT OR IGNORE INTO user_achievements 
                    (user_id, achievement_name, achievement_description, earned_at)
                    VALUES (?, ?, ?, ?)
                ''', (user_id, name, description, datetime.datetime.now()))
            
            conn.commit()
            conn.close()
            
            return {
                'broskie_balance': broskie_balance,
                'articles_read': articles_read,
                'level': level,
                'streak_days': streak_days,
                'total_achievements': total_achievements + len(new_achievements),
                'rewards_earned': rewards_earned,
                'new_achievements': [{'name': name, 'description': desc} for name, desc in new_achievements]
            }
            
        except Exception as e:
            logger.error(f"❌ Gamification error: {e}")
            return {}
    
    def get_user_preferences(self, user_id):
        """Get user preferences for personalization"""
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()
            
            cursor.execute('SELECT preferences FROM user_stats WHERE user_id = ?', (user_id,))
            result = cursor.fetchone()
            
            if result and result[0]:
                preferences = json.loads(result[0])
            else:
                preferences = {
                    'preferred_tags': ['DeFi', 'NFT', 'Web3'],
                    'sentiment_preference': 'all',
                    'importance_threshold': 1
                }
            
            conn.close()
            return preferences
            
        except Exception as e:
            logger.error(f"❌ Preferences error: {e}")
            return {}
    
    def personalize_news(self, preferences):
        """Personalize news feed based on user preferences"""
        try:
            preferred_tags = preferences.get('preferred_tags', [])
            importance_threshold = preferences.get('importance_threshold', 1)
            
            # Score and filter news items
            scored_news = []
            for item in self.news_items:
                score = item.importance
                
                # Boost score for preferred tags
                for tag in item.tags:
                    if tag in preferred_tags:
                        score += 2
                
                # Filter by importance threshold
                if item.importance >= importance_threshold:
                    scored_news.append((score, item))
            
            # Sort by score and return top items
            scored_news.sort(key=lambda x: x[0], reverse=True)
            return [item for score, item in scored_news[:15]]
            
        except Exception as e:
            logger.error(f"❌ Personalization error: {e}")
            return self.news_items[:15]
    
    def generate_market_analysis(self, analysis_type='trend_prediction'):
        """Generate AI-powered market analysis"""
        try:
            if not self.openai_api_key:
                return {
                    'analysis': 'AI analysis requires OpenAI API key configuration.',
                    'sentiment': 'neutral',
                    'model': 'unavailable'
                }
            
            # Prepare market data context
            recent_news = [item.title for item in self.news_items[:5]]
            defi_data = self.fetch_defi_protocols()
            
            prompt = f"""
            Analyze the current Web3/DeFi market based on:
            
            Recent News Headlines:
            {chr(10).join(recent_news)}
            
            Top DeFi Protocols:
            {json.dumps(defi_data[:3], indent=2)}
            
            Provide a concise market analysis focusing on:
            1. Overall market sentiment (bullish/bearish/neutral)
            2. Key trends and opportunities
            3. Risk factors to watch
            
            Keep response under 200 words and include specific insights.
            """
            
            # Create OpenAI client
            client = openai.OpenAI(api_key=self.openai_api_key)
            
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a Web3/DeFi market analyst providing concise, actionable insights."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=300,
                temperature=0.7
            )
            
            analysis_text = response.choices[0].message.content
            
            # Determine sentiment from analysis
            sentiment = 'neutral'
            if any(word in analysis_text.lower() for word in ['bullish', 'positive', 'growth', 'opportunity']):
                sentiment = 'bullish'
            elif any(word in analysis_text.lower() for word in ['bearish', 'negative', 'risk', 'decline']):
                sentiment = 'bearish'
            
            return {
                'analysis': analysis_text,
                'sentiment': sentiment,
                'model': 'gpt-4',
                'token_usage': response.usage.total_tokens,
                'generated_at': datetime.datetime.now().isoformat()
            }
            
        except Exception as e:
            logger.error(f"❌ AI analysis error: {e}")
            return {
                'analysis': f'Analysis temporarily unavailable: {str(e)}',
                'sentiment': 'neutral',
                'model': 'error'
            }
    
    def fetch_news(self):
        """Fetch news from all sources"""
        try:
            logger.info("🔍 Fetching Web3 news from sources...")
            new_items = []
            
            for source_name, source_url in self.sources.items():
                try:
                    feed = feedparser.parse(source_url)
                    
                    for entry in feed.entries[:5]:  # Top 5 from each source
                        # Extract content
                        content = getattr(entry, 'summary', '')
                        if hasattr(entry, 'content') and entry.content:
                            content = entry.content[0].value
                        
                        # Clean HTML
                        content = self.clean_html(content)
                        
                        # Create news item
                        item = NewsItem(
                            title=entry.title,
                            content=content[:500],  # Limit content
                            timestamp=datetime.datetime.now(),
                            source=source_name,
                            tags=self.extract_tags(entry.title + ' ' + content),
                            sentiment=self.analyze_sentiment(entry.title),
                            importance=self.calculate_importance(entry.title, content),
                            web3_relevance=self.calculate_web3_relevance(entry.title, content)
                        )
                        
                        new_items.append(item)
                        
                except Exception as e:
                    logger.error(f"❌ Error fetching from {source_name}: {e}")
            
            # Add new items to the collection
            self.news_items = new_items + self.news_items
            self.news_items = self.news_items[:100]  # Keep latest 100 items
            
            logger.info(f"✅ Fetched {len(new_items)} new articles")
            return len(new_items)
            
        except Exception as e:
            logger.error(f"❌ News fetch error: {e}")
            return 0
    
    def clean_html(self, html_content):
        """Clean HTML tags from content"""
        try:
            from bs4 import BeautifulSoup
            soup = BeautifulSoup(html_content, 'html.parser')
            return soup.get_text().strip()
        except:
            return html_content
    
    def extract_tags(self, text):
        """Extract relevant tags from text"""
        web3_keywords = {
            'defi': 'DeFi',
            'nft': 'NFT',
            'ethereum': 'Ethereum',
            'bitcoin': 'Bitcoin',
            'crypto': 'Crypto',
            'blockchain': 'Blockchain',
            'dao': 'DAO',
            'dex': 'DEX',
            'yield': 'Yield',
            'staking': 'Staking',
            'bridge': 'Bridge',
            'layer 2': 'Layer2',
            'metaverse': 'Metaverse',
            'web3': 'Web3'
        }
        
        tags = []
        text_lower = text.lower()
        
        for keyword, tag in web3_keywords.items():
            if keyword in text_lower:
                tags.append(tag)
        
        return list(set(tags))  # Remove duplicates
    
    def analyze_sentiment(self, title):
        """Simple sentiment analysis"""
        positive_words = ['surge', 'rise', 'gain', 'bull', 'up', 'high', 'record', 'success']
        negative_words = ['crash', 'fall', 'bear', 'down', 'low', 'drop', 'decline', 'loss']
        
        title_lower = title.lower()
        
        positive_count = sum(1 for word in positive_words if word in title_lower)
        negative_count = sum(1 for word in negative_words if word in title_lower)
        
        if positive_count > negative_count:
            return 'bullish'
        elif negative_count > positive_count:
            return 'bearish'
        else:
            return 'neutral'
    
    def calculate_importance(self, title, content):
        """Calculate article importance (1-5)"""
        important_keywords = ['billion', 'million', 'hack', 'launch', 'partnership', 'regulation']
        text = (title + ' ' + content).lower()
        
        importance = 1
        for keyword in important_keywords:
            if keyword in text:
                importance += 1
        
        return min(5, importance)
    
    def calculate_web3_relevance(self, title, content):
        """Calculate Web3 relevance score (0.0-1.0)"""
        web3_terms = ['web3', 'defi', 'nft', 'blockchain', 'crypto', 'ethereum', 'dao', 'dex']
        text = (title + ' ' + content).lower()
        
        relevance = 0.0
        for term in web3_terms:
            if term in text:
                relevance += 0.15
        
        return min(1.0, relevance)
    
    def start_background_tasks(self):
        """Start background news fetching"""
        def fetch_loop():
            while True:
                try:
                    self.fetch_news()
                    time.sleep(300)  # Fetch every 5 minutes
                except Exception as e:
                    logger.error(f"❌ Background fetch error: {e}")
                    time.sleep(60)
        
        fetch_thread = Thread(target=fetch_loop, daemon=True)
        fetch_thread.start()
        logger.info("🔄 Background news fetching started")
    
    def run(self, host='127.0.0.1', port=5001, debug=False):
        """Run the legendary portal"""
        try:
            # Initial news fetch
            self.fetch_news()
            
            # Start background tasks
            self.start_background_tasks()
            
            logger.info(f"🚀💎 LEGENDARY Web3 Portal starting at http://{host}:{port} 💎🚀")
            
            # Auto-open browser
            if not debug:
                webbrowser.open(f'http://{host}:{port}')
            
            self.app.run(host=host, port=port, debug=debug)
            
        except Exception as e:
            logger.error(f"❌ Portal startup error: {e}")

def main():
    """Main execution function"""
    print("🚀💎⚡ LEGENDARY HYPER NEWS WEB3 PORTAL ⚡💎🚀")
    print("Enhanced with DeFi Data, NFT Integration, AI Analysis & Gamification")
    print("=" * 60)
    
    portal = LegendaryWeb3NewsPortal()
    portal.run(debug=False)

if __name__ == "__main__":
    main()
