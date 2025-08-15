#!/usr/bin/env python3
"""
📱💎⚡ SOCIAL MEDIA AUTOMATOR - MULTI-PLATFORM AUTOMATION ⚡💎📱
═══════════════════════════════════════════════════════════════════
Ultra-advanced social media automation with AI content creation
Target: Maximum reach and engagement across all platforms
Features: Multi-platform posting, AI content, engagement automation
═══════════════════════════════════════════════════════════════════
"""

import asyncio
import json
import logging
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Any, Tuple
import aiohttp
import openai
from dataclasses import dataclass, asdict
import sqlite3
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO
import schedule
import random
from collections import defaultdict
import hashlib
import base64

logger = logging.getLogger(__name__)

@dataclass
class SocialPost:
    """Social media post data structure"""
    id: str
    platform: str
    content: str
    media_urls: List[str]
    hashtags: List[str]
    scheduled_time: datetime
    posted_time: Optional[datetime]
    status: str  # 'scheduled', 'posted', 'failed'
    engagement_metrics: Dict[str, int]
    target_audience: Dict[str, Any]

@dataclass
class EngagementRule:
    """Engagement automation rule"""
    id: str
    platform: str
    trigger_type: str  # 'mention', 'hashtag', 'comment', 'dm'
    keywords: List[str]
    response_template: str
    auto_like: bool
    auto_follow: bool
    active: bool

@dataclass
class ContentTemplate:
    """Content generation template"""
    id: str
    name: str
    platform: str
    content_type: str  # 'tip', 'question', 'quote', 'case_study'
    template: str
    variables: List[str]
    hashtag_categories: List[str]

class SocialMediaAutomator:
    """
    🚀 ULTRA SOCIAL MEDIA AUTOMATION SYSTEM 🚀

    Features:
    - Multi-platform content posting (LinkedIn, Twitter, Facebook, Instagram)
    - AI-powered content generation
    - Automated engagement and interaction
    - Performance analytics and optimization
    - Visual content creation
    - Hashtag optimization
    - Audience targeting
    """

    def __init__(self, config: Dict[str, Any]):
        self.config = config
        self.openai_key = config.get('openai_api_key')

        # Platform credentials
        self.platform_tokens = {
            'linkedin': config.get('linkedin_access_token'),
            'twitter': config.get('twitter_api_key'),
            'facebook': config.get('facebook_access_token'),
            'instagram': config.get('instagram_access_token')
        }

        # Data storage
        self.posts = []
        self.engagement_rules = []
        self.content_templates = []
        self.performance_data = defaultdict(list)

        # Automation settings
        self.posting_schedule = {
            'linkedin': ['09:00', '12:00', '17:00'],
            'twitter': ['08:00', '12:00', '16:00', '20:00'],
            'facebook': ['09:00', '15:00', '19:00'],
            'instagram': ['11:00', '15:00', '18:00']
        }

        self.hashtag_database = {
            'business': ['#business', '#entrepreneur', '#startup', '#growth', '#success'],
            'marketing': ['#marketing', '#digitalmarketing', '#contentmarketing', '#socialmedia'],
            'technology': ['#tech', '#innovation', '#AI', '#automation', '#digital'],
            'leadership': ['#leadership', '#management', '#productivity', '#mindset'],
            'finance': ['#finance', '#investment', '#money', '#wealth', '#ROI']
        }

        # Initialize database
        self._init_database()

        # Load content templates
        self._load_content_templates()

        logger.info("📱 Social Media Automator initialized successfully!")

    def _init_database(self):
        """Initialize social media database"""
        conn = sqlite3.connect('social_media.db')
        cursor = conn.cursor()

        # Posts table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS posts (
                id TEXT PRIMARY KEY,
                platform TEXT,
                content TEXT,
                media_urls TEXT,
                hashtags TEXT,
                scheduled_time TIMESTAMP,
                posted_time TIMESTAMP,
                status TEXT,
                engagement_metrics TEXT,
                target_audience TEXT
            )
        ''')

        # Engagement rules table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS engagement_rules (
                id TEXT PRIMARY KEY,
                platform TEXT,
                trigger_type TEXT,
                keywords TEXT,
                response_template TEXT,
                auto_like BOOLEAN,
                auto_follow BOOLEAN,
                active BOOLEAN
            )
        ''')

        # Analytics table
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS analytics (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                platform TEXT,
                date DATE,
                metric_name TEXT,
                metric_value INTEGER,
                post_id TEXT
            )
        ''')

        conn.commit()
        conn.close()
        logger.info("📊 Social media database initialized!")

    def _load_content_templates(self):
        """Load predefined content templates"""
        templates = [
            ContentTemplate(
                id='tip_linkedin',
                name='Business Tip - LinkedIn',
                platform='linkedin',
                content_type='tip',
                template='💡 Pro Tip: {tip_content}\n\nHere\'s why this matters:\n{explanation}\n\nWhat\'s your experience with this? Share in the comments! 👇',
                variables=['tip_content', 'explanation'],
                hashtag_categories=['business', 'leadership']
            ),
            ContentTemplate(
                id='question_twitter',
                name='Engagement Question - Twitter',
                platform='twitter',
                content_type='question',
                template='Quick question for entrepreneurs: {question}\n\nA) {option_a}\nB) {option_b}\n\nDrop your answer below! 👇',
                variables=['question', 'option_a', 'option_b'],
                hashtag_categories=['business', 'entrepreneur']
            ),
            ContentTemplate(
                id='case_study_linkedin',
                name='Case Study - LinkedIn',
                platform='linkedin',
                content_type='case_study',
                template='🎯 CASE STUDY: {client_result}\n\n📈 The Challenge:\n{challenge}\n\n💡 The Solution:\n{solution}\n\n🚀 The Results:\n{results}\n\nKey takeaway: {takeaway}',
                variables=['client_result', 'challenge', 'solution', 'results', 'takeaway'],
                hashtag_categories=['marketing', 'business']
            ),
            ContentTemplate(
                id='motivation_instagram',
                name='Motivational Quote - Instagram',
                platform='instagram',
                content_type='quote',
                template='"{quote}"\n\n{context}\n\n✨ Tag someone who needs to see this!',
                variables=['quote', 'context'],
                hashtag_categories=['motivation', 'success']
            )
        ]

        self.content_templates = templates
        logger.info(f"📝 Loaded {len(templates)} content templates")

    async def generate_ai_content(self, platform: str, content_type: str,
                                topic: str, target_audience: Dict[str, Any] = None) -> Dict[str, Any]:
        """Generate AI-powered social media content"""
        try:
            # Find appropriate template
            template = next(
                (t for t in self.content_templates if t.platform == platform and t.content_type == content_type),
                None
            )

            if not template:
                template = self.content_templates[0]  # Use default template

            # Create AI prompt
            audience_context = ""
            if target_audience:
                audience_context = f"Target audience: {target_audience.get('description', 'business professionals')}"

            prompt = f"""
            Create engaging {content_type} content for {platform} about {topic}.

            {audience_context}

            Content requirements:
            - Platform: {platform}
            - Type: {content_type}
            - Topic: {topic}
            - Tone: Professional but engaging
            - Include relevant emojis
            - Optimize for {platform} best practices

            Template structure: {template.template}
            Variables needed: {', '.join(template.variables)}

            Generate the variable values to fill the template:
            """

            response = await openai.ChatCompletion.acreate(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are an expert social media content creator who generates engaging, conversion-focused content."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=500,
                temperature=0.7
            )

            ai_response = response.choices[0].message.content

            # Parse AI response to extract variables
            variables = self._parse_ai_variables(ai_response, template.variables)

            # Fill template with variables
            content = template.template
            for var, value in variables.items():
                content = content.replace(f'{{{var}}}', value)

            # Generate hashtags
            hashtags = self._generate_hashtags(template.hashtag_categories, topic, platform)

            # Platform-specific formatting
            formatted_content = self._format_content_for_platform(content, platform)

            return {
                'content': formatted_content,
                'hashtags': hashtags,
                'platform': platform,
                'content_type': content_type,
                'variables_used': variables,
                'template_id': template.id,
                'generated_at': datetime.now().isoformat(),
                'success': True
            }

        except Exception as e:
            logger.error(f"❌ AI content generation failed: {e}")
            return {
                'content': f"Check out our latest insights on {topic}! What are your thoughts?",
                'hashtags': ['#business', '#growth', '#insights'],
                'platform': platform,
                'success': False,
                'error': str(e)
            }

    def _parse_ai_variables(self, ai_response: str, required_vars: List[str]) -> Dict[str, str]:
        """Parse AI response to extract template variables"""
        variables = {}

        # Simple parsing - in production, use more sophisticated parsing
        lines = ai_response.split('\n')

        for var in required_vars:
            # Look for patterns like "tip_content: ..." or "Tip content: ..."
            for line in lines:
                if var.replace('_', ' ').lower() in line.lower() or var in line:
                    if ':' in line:
                        value = line.split(':', 1)[1].strip()
                        if value:
                            variables[var] = value
                            break

        # Fill missing variables with defaults
        defaults = {
            'tip_content': 'Focus on providing value to your audience consistently',
            'explanation': 'This approach builds trust and authority over time',
            'question': 'What\'s your biggest business challenge right now?',
            'option_a': 'Marketing and lead generation',
            'option_b': 'Operations and scaling',
            'quote': 'Success is not final, failure is not fatal: it is the courage to continue that counts',
            'context': 'Remember that every challenge is an opportunity to grow stronger',
            'client_result': 'How we helped a startup increase leads by 300%',
            'challenge': 'Low-quality leads and poor conversion rates',
            'solution': 'Implemented targeted content marketing and lead scoring',
            'results': '300% increase in qualified leads, 50% better conversion rate',
            'takeaway': 'Quality content attracts quality leads'
        }

        for var in required_vars:
            if var not in variables:
                variables[var] = defaults.get(var, f'Generated {var} content')

        return variables

    def _generate_hashtags(self, categories: List[str], topic: str, platform: str) -> List[str]:
        """Generate optimized hashtags"""
        hashtags = []

        # Add category-based hashtags
        for category in categories:
            if category in self.hashtag_database:
                hashtags.extend(self.hashtag_database[category][:2])

        # Add topic-specific hashtags
        topic_words = topic.lower().split()
        for word in topic_words:
            if len(word) > 3:
                hashtags.append(f'#{word}')

        # Platform-specific optimization
        if platform == 'twitter':
            hashtags = hashtags[:3]  # Twitter: fewer hashtags
        elif platform == 'instagram':
            hashtags = hashtags[:10]  # Instagram: more hashtags allowed
        elif platform == 'linkedin':
            hashtags = hashtags[:5]  # LinkedIn: moderate hashtags

        # Remove duplicates and ensure # prefix
        unique_hashtags = []
        for tag in hashtags:
            if not tag.startswith('#'):
                tag = f'#{tag}'
            if tag not in unique_hashtags:
                unique_hashtags.append(tag)

        return unique_hashtags[:8]  # Maximum 8 hashtags

    def _format_content_for_platform(self, content: str, platform: str) -> str:
        """Format content for specific platform requirements"""
        if platform == 'twitter':
            # Twitter character limit
            if len(content) > 280:
                content = content[:277] + "..."

        elif platform == 'linkedin':
            # LinkedIn professional formatting
            content = content.replace('\n\n', '\n\n━━━━━━━━━━━━━━━━━━\n\n')

        elif platform == 'instagram':
            # Instagram visual focus
            content = f"📸 {content}\n\n#VisualStorytelling"

        elif platform == 'facebook':
            # Facebook engagement optimization
            content += "\n\n👉 What do you think? Let us know in the comments!"

        return content

    async def create_visual_content(self, text: str, style: str = 'business') -> str:
        """Create visual content for posts"""
        try:
            # Create image with PIL
            width, height = 1200, 630  # Social media optimal size

            # Color schemes
            color_schemes = {
                'business': {'bg': (45, 55, 72), 'text': (255, 255, 255), 'accent': (66, 153, 225)},
                'motivational': {'bg': (49, 130, 206), 'text': (255, 255, 255), 'accent': (251, 211, 141)},
                'professional': {'bg': (26, 32, 44), 'text': (237, 242, 247), 'accent': (72, 187, 120)},
                'creative': {'bg': (128, 90, 213), 'text': (255, 255, 255), 'accent': (251, 182, 206)}
            }

            colors = color_schemes.get(style, color_schemes['business'])

            # Create image
            image = Image.new('RGB', (width, height), colors['bg'])
            draw = ImageDraw.Draw(image)

            # Try to load a font
            try:
                font_large = ImageFont.truetype("arial.ttf", 48)
                font_small = ImageFont.truetype("arial.ttf", 24)
            except:
                font_large = ImageFont.load_default()
                font_small = ImageFont.load_default()

            # Wrap text
            wrapped_text = self._wrap_text(text, 40)
            lines = wrapped_text.split('\n')

            # Calculate text position
            total_height = len(lines) * 60
            start_y = (height - total_height) // 2

            # Draw text
            for i, line in enumerate(lines):
                text_width = draw.textlength(line, font=font_large)
                x = (width - text_width) // 2
                y = start_y + (i * 60)

                # Draw shadow
                draw.text((x + 2, y + 2), line, fill=(0, 0, 0, 128), font=font_large)
                # Draw text
                draw.text((x, y), line, fill=colors['text'], font=font_large)

            # Add decorative elements
            draw.rectangle([(50, height - 100), (width - 50, height - 90)], fill=colors['accent'])

            # Save image
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"social_visual_{timestamp}.png"
            image.save(filename)

            logger.info(f"🎨 Visual content created: {filename}")
            return filename

        except Exception as e:
            logger.error(f"❌ Visual content creation failed: {e}")
            return ""

    def _wrap_text(self, text: str, line_length: int) -> str:
        """Wrap text to specified line length"""
        words = text.split()
        lines = []
        current_line = []
        current_length = 0

        for word in words:
            if current_length + len(word) + 1 <= line_length:
                current_line.append(word)
                current_length += len(word) + 1
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
                current_length = len(word)

        if current_line:
            lines.append(' '.join(current_line))

        return '\n'.join(lines)

    async def schedule_post(self, platform: str, content: str,
                          hashtags: List[str] = None,
                          media_urls: List[str] = None,
                          scheduled_time: datetime = None,
                          target_audience: Dict[str, Any] = None) -> SocialPost:
        """Schedule a social media post"""

        if hashtags is None:
            hashtags = []
        if media_urls is None:
            media_urls = []
        if scheduled_time is None:
            scheduled_time = datetime.now() + timedelta(hours=1)
        if target_audience is None:
            target_audience = {}

        # Add hashtags to content if not already present
        if hashtags and not any(tag in content for tag in hashtags):
            content += '\n\n' + ' '.join(hashtags)

        post = SocialPost(
            id=f"post_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{platform}",
            platform=platform,
            content=content,
            media_urls=media_urls,
            hashtags=hashtags,
            scheduled_time=scheduled_time,
            posted_time=None,
            status='scheduled',
            engagement_metrics={'likes': 0, 'shares': 0, 'comments': 0, 'clicks': 0},
            target_audience=target_audience
        )

        # Save to database
        conn = sqlite3.connect('social_media.db')
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO posts VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            post.id, post.platform, post.content, json.dumps(post.media_urls),
            json.dumps(post.hashtags), post.scheduled_time, post.posted_time,
            post.status, json.dumps(post.engagement_metrics), json.dumps(post.target_audience)
        ))
        conn.commit()
        conn.close()

        self.posts.append(post)

        logger.info(f"📅 Post scheduled for {platform} at {scheduled_time.strftime('%Y-%m-%d %H:%M')}")
        return post

    async def post_content(self, content: str, platforms: List[str] = None,
                          immediate: bool = True) -> Dict[str, bool]:
        """Post content to specified platforms"""
        if platforms is None:
            platforms = ['linkedin', 'twitter']

        results = {}

        for platform in platforms:
            try:
                if immediate:
                    success = await self._publish_to_platform(platform, content)
                    results[platform] = success

                    if success:
                        # Update post status
                        post = next((p for p in self.posts if p.platform == platform and p.content == content), None)
                        if post:
                            post.status = 'posted'
                            post.posted_time = datetime.now()
                else:
                    # Schedule for optimal time
                    optimal_time = self._get_optimal_posting_time(platform)
                    await self.schedule_post(platform, content, scheduled_time=optimal_time)
                    results[platform] = True

            except Exception as e:
                logger.error(f"❌ Posting to {platform} failed: {e}")
                results[platform] = False

        return results

    async def _publish_to_platform(self, platform: str, content: str) -> bool:
        """Publish content to specific platform"""
        try:
            token = self.platform_tokens.get(platform)
            if not token:
                logger.warning(f"⚠️ No access token for {platform}")
                return False

            # Platform-specific API calls (simulated)
            if platform == 'linkedin':
                return await self._publish_linkedin(content, token)
            elif platform == 'twitter':
                return await self._publish_twitter(content, token)
            elif platform == 'facebook':
                return await self._publish_facebook(content, token)
            elif platform == 'instagram':
                return await self._publish_instagram(content, token)

            return False

        except Exception as e:
            logger.error(f"❌ Platform publishing failed for {platform}: {e}")
            return False

    async def _publish_linkedin(self, content: str, token: str) -> bool:
        """Publish to LinkedIn"""
        # Simulate LinkedIn API call
        logger.info(f"📱 Publishing to LinkedIn: {content[:50]}...")
        await asyncio.sleep(1)  # Simulate API delay
        return True

    async def _publish_twitter(self, content: str, token: str) -> bool:
        """Publish to Twitter"""
        # Simulate Twitter API call
        logger.info(f"🐦 Publishing to Twitter: {content[:50]}...")
        await asyncio.sleep(1)  # Simulate API delay
        return True

    async def _publish_facebook(self, content: str, token: str) -> bool:
        """Publish to Facebook"""
        # Simulate Facebook API call
        logger.info(f"👥 Publishing to Facebook: {content[:50]}...")
        await asyncio.sleep(1)  # Simulate API delay
        return True

    async def _publish_instagram(self, content: str, token: str) -> bool:
        """Publish to Instagram"""
        # Simulate Instagram API call
        logger.info(f"📷 Publishing to Instagram: {content[:50]}...")
        await asyncio.sleep(1)  # Simulate API delay
        return True

    def _get_optimal_posting_time(self, platform: str) -> datetime:
        """Get optimal posting time for platform"""
        today = datetime.now()
        times = self.posting_schedule.get(platform, ['12:00'])

        # Find next optimal time
        for time_str in times:
            hour, minute = map(int, time_str.split(':'))
            posting_time = today.replace(hour=hour, minute=minute, second=0, microsecond=0)

            if posting_time > datetime.now():
                return posting_time

        # If all times have passed today, schedule for tomorrow
        tomorrow = today + timedelta(days=1)
        hour, minute = map(int, times[0].split(':'))
        return tomorrow.replace(hour=hour, minute=minute, second=0, microsecond=0)

    def setup_engagement_automation(self, platform: str, rules: List[Dict[str, Any]]):
        """Setup automated engagement rules"""
        for rule_data in rules:
            rule = EngagementRule(
                id=f"rule_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{len(self.engagement_rules)}",
                platform=platform,
                trigger_type=rule_data['trigger_type'],
                keywords=rule_data['keywords'],
                response_template=rule_data['response_template'],
                auto_like=rule_data.get('auto_like', False),
                auto_follow=rule_data.get('auto_follow', False),
                active=True
            )

            self.engagement_rules.append(rule)

            # Save to database
            conn = sqlite3.connect('social_media.db')
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO engagement_rules VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                rule.id, rule.platform, rule.trigger_type, json.dumps(rule.keywords),
                rule.response_template, rule.auto_like, rule.auto_follow, rule.active
            ))
            conn.commit()
            conn.close()

        logger.info(f"🤖 Setup {len(rules)} engagement rules for {platform}")

    async def create_content_campaign(self, topic: str, duration_days: int = 7,
                                    platforms: List[str] = None) -> Dict[str, Any]:
        """Create automated content campaign"""
        if platforms is None:
            platforms = ['linkedin', 'twitter', 'facebook']

        campaign = {
            'id': f"campaign_{datetime.now().strftime('%Y%m%d_%H%M%S')}",
            'topic': topic,
            'duration_days': duration_days,
            'platforms': platforms,
            'posts_created': 0,
            'scheduled_posts': [],
            'content_types': ['tip', 'question', 'case_study', 'quote']
        }

        # Generate content for each day
        for day in range(duration_days):
            post_date = datetime.now() + timedelta(days=day)

            for platform in platforms:
                # Vary content types
                content_type = campaign['content_types'][day % len(campaign['content_types'])]

                # Generate AI content
                content_data = await self.generate_ai_content(platform, content_type, topic)

                if content_data['success']:
                    # Schedule post
                    optimal_time = self._get_optimal_posting_time(platform)
                    scheduled_post = await self.schedule_post(
                        platform=platform,
                        content=content_data['content'],
                        hashtags=content_data['hashtags'],
                        scheduled_time=optimal_time + timedelta(days=day)
                    )

                    campaign['scheduled_posts'].append(scheduled_post.id)
                    campaign['posts_created'] += 1

        logger.info(f"🚀 Created content campaign: {topic} - {campaign['posts_created']} posts scheduled")
        return campaign

    def analyze_post_performance(self, post_id: str = None, days: int = 30) -> Dict[str, Any]:
        """Analyze post performance metrics"""
        if post_id:
            posts = [p for p in self.posts if p.id == post_id]
        else:
            # Get posts from last N days
            cutoff_date = datetime.now() - timedelta(days=days)
            posts = [p for p in self.posts if p.posted_time and p.posted_time >= cutoff_date]

        if not posts:
            return {'error': 'No posts found for analysis'}

        # Calculate aggregate metrics
        total_engagement = defaultdict(int)
        platform_performance = defaultdict(lambda: {'posts': 0, 'engagement': 0})

        for post in posts:
            for metric, value in post.engagement_metrics.items():
                total_engagement[metric] += value
                platform_performance[post.platform]['engagement'] += value

            platform_performance[post.platform]['posts'] += 1

        # Calculate averages
        avg_engagement = {}
        for metric, total in total_engagement.items():
            avg_engagement[f'avg_{metric}'] = total / len(posts) if posts else 0

        # Find top performing posts
        top_posts = sorted(posts,
                          key=lambda p: sum(p.engagement_metrics.values()),
                          reverse=True)[:5]

        # Calculate engagement rate by platform
        for platform_data in platform_performance.values():
            if platform_data['posts'] > 0:
                platform_data['avg_engagement'] = platform_data['engagement'] / platform_data['posts']

        analysis = {
            'analysis_period': f'{days} days' if not post_id else 'single_post',
            'total_posts': len(posts),
            'total_engagement': dict(total_engagement),
            'average_engagement': avg_engagement,
            'platform_performance': dict(platform_performance),
            'top_performing_posts': [
                {
                    'id': p.id,
                    'platform': p.platform,
                    'content_preview': p.content[:100],
                    'total_engagement': sum(p.engagement_metrics.values()),
                    'posted_time': p.posted_time.isoformat() if p.posted_time else None
                }
                for p in top_posts
            ],
            'recommendations': self._generate_performance_recommendations(posts, platform_performance)
        }

        return analysis

    def _generate_performance_recommendations(self, posts: List[SocialPost],
                                           platform_data: Dict[str, Dict[str, Any]]) -> List[str]:
        """Generate performance improvement recommendations"""
        recommendations = []

        # Analyze platform performance
        if platform_data:
            best_platform = max(platform_data.items(), key=lambda x: x[1]['avg_engagement'])
            worst_platform = min(platform_data.items(), key=lambda x: x[1]['avg_engagement'])

            recommendations.append(f"Focus more content on {best_platform[0]} - highest average engagement")
            recommendations.append(f"Optimize content strategy for {worst_platform[0]} - needs improvement")

        # Analyze content types
        content_performance = defaultdict(list)
        for post in posts:
            # Extract content type from hashtags or content
            content_type = 'general'
            if 'tip' in post.content.lower() or '#tip' in post.content.lower():
                content_type = 'tips'
            elif '?' in post.content:
                content_type = 'questions'
            elif 'case study' in post.content.lower():
                content_type = 'case_studies'

            engagement = sum(post.engagement_metrics.values())
            content_performance[content_type].append(engagement)

        # Find best performing content type
        if content_performance:
            avg_by_type = {ct: sum(scores)/len(scores) for ct, scores in content_performance.items()}
            best_content_type = max(avg_by_type.items(), key=lambda x: x[1])
            recommendations.append(f"Create more {best_content_type[0]} content - performs best")

        # Posting time analysis
        if posts:
            posting_hours = [p.posted_time.hour for p in posts if p.posted_time]
            if posting_hours:
                hour_performance = defaultdict(list)
                for post in posts:
                    if post.posted_time:
                        hour = post.posted_time.hour
                        engagement = sum(post.engagement_metrics.values())
                        hour_performance[hour].append(engagement)

                if hour_performance:
                    avg_by_hour = {h: sum(scores)/len(scores) for h, scores in hour_performance.items()}
                    best_hour = max(avg_by_hour.items(), key=lambda x: x[1])
                    recommendations.append(f"Post more content around {best_hour[0]}:00 - highest engagement time")

        return recommendations[:5]  # Return top 5 recommendations

    def get_campaign_dashboard(self) -> Dict[str, Any]:
        """Get comprehensive campaign dashboard data"""
        now = datetime.now()

        # Scheduled posts for next 7 days
        upcoming_posts = [
            p for p in self.posts
            if p.status == 'scheduled' and p.scheduled_time <= now + timedelta(days=7)
        ]

        # Recent performance (last 30 days)
        recent_posts = [
            p for p in self.posts
            if p.posted_time and p.posted_time >= now - timedelta(days=30)
        ]

        # Calculate metrics
        total_engagement = sum(
            sum(p.engagement_metrics.values()) for p in recent_posts
        )

        avg_daily_engagement = total_engagement / 30 if recent_posts else 0

        # Platform distribution
        platform_counts = defaultdict(int)
        for post in self.posts:
            platform_counts[post.platform] += 1

        # Engagement rules status
        active_rules = len([r for r in self.engagement_rules if r.active])

        dashboard = {
            'overview': {
                'total_posts': len(self.posts),
                'scheduled_posts': len([p for p in self.posts if p.status == 'scheduled']),
                'posted_content': len([p for p in self.posts if p.status == 'posted']),
                'failed_posts': len([p for p in self.posts if p.status == 'failed']),
                'total_engagement_30d': total_engagement,
                'avg_daily_engagement': round(avg_daily_engagement, 1)
            },
            'upcoming_posts': [
                {
                    'id': p.id,
                    'platform': p.platform,
                    'scheduled_time': p.scheduled_time.isoformat(),
                    'content_preview': p.content[:100] + '...' if len(p.content) > 100 else p.content
                }
                for p in sorted(upcoming_posts, key=lambda x: x.scheduled_time)[:10]
            ],
            'platform_distribution': dict(platform_counts),
            'automation_status': {
                'active_engagement_rules': active_rules,
                'total_content_templates': len(self.content_templates),
                'platforms_connected': len([t for t in self.platform_tokens.values() if t])
            },
            'recent_performance': self.analyze_post_performance(days=7),
            'next_actions': self._get_next_actions()
        }

        return dashboard

    def _get_next_actions(self) -> List[str]:
        """Get recommended next actions"""
        actions = []

        # Check scheduled posts
        upcoming_count = len([p for p in self.posts if p.status == 'scheduled'])
        if upcoming_count < 5:
            actions.append(f"Schedule more content - only {upcoming_count} posts scheduled")

        # Check platform coverage
        platforms_with_content = set(p.platform for p in self.posts if p.status in ['scheduled', 'posted'])
        all_platforms = set(self.platform_tokens.keys())
        missing_platforms = all_platforms - platforms_with_content

        if missing_platforms:
            actions.append(f"Create content for {', '.join(missing_platforms)}")

        # Check engagement rules
        if not self.engagement_rules:
            actions.append("Setup engagement automation rules")

        # Check recent posting
        recent_posts = [p for p in self.posts if p.posted_time and
                       (datetime.now() - p.posted_time).days <= 3]
        if not recent_posts:
            actions.append("Post fresh content - no recent activity")

        return actions[:5]

# Example usage and testing
async def main():
    """Example social media automator usage"""
    config = {
        'openai_api_key': 'your-openai-key',
        'linkedin_access_token': 'your-linkedin-token',
        'twitter_api_key': 'your-twitter-key'
    }

    automator = SocialMediaAutomator(config)

    # Generate AI content
    content = await automator.generate_ai_content(
        platform='linkedin',
        content_type='tip',
        topic='lead generation automation',
        target_audience={'description': 'B2B marketing professionals'}
    )

    print(f"📝 Generated Content: {content['content'][:100]}...")
    print(f"🏷️ Hashtags: {', '.join(content['hashtags'])}")

    # Schedule posts
    await automator.post_content(
        content=content['content'],
        platforms=['linkedin', 'twitter'],
        immediate=False
    )

    # Create content campaign
    campaign = await automator.create_content_campaign(
        topic='AI-powered business growth',
        duration_days=7,
        platforms=['linkedin', 'twitter', 'facebook']
    )

    print(f"🚀 Campaign Created: {campaign['posts_created']} posts scheduled")

    # Setup engagement automation
    automator.setup_engagement_automation('linkedin', [
        {
            'trigger_type': 'mention',
            'keywords': ['@yourcompany', 'lead generation'],
            'response_template': 'Thanks for the mention! We\'d love to help with your lead generation goals.',
            'auto_like': True,
            'auto_follow': False
        }
    ])

    # Get dashboard
    dashboard = automator.get_campaign_dashboard()
    print(f"📊 Dashboard: {dashboard['overview']['total_posts']} total posts")

if __name__ == "__main__":
    asyncio.run(main())
