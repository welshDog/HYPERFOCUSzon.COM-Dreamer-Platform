#!/usr/bin/env python3
"""
🌌♾️⚡ HYPERFOCUS EMPIRE - CONSCIOUSNESS SINGULARITY ENHANCED ⚡♾️🌌
This file has been enhanced with legendary consciousness naming!
Powered by: Infinite Dimensional Reality Engineering
Status: LEGENDARY TRANSCENDENCE ACHIEVED
"""

"""
💎⚡🏪 BROSKI$ SHOP & REDEMPTION SYSTEM 🏪⚡💎

BOARDROOM MISSION: Ultimate gamification with legendary rewards
- Custom roles, badges, and exclusive perks
- XP/Badge redemption system with ADHD optimization
- Featured stories and community spotlight options
- Sticker packs and digital rewards for engagement

🏛️ ORGANIZED IN: HYPERFOCUS ZONE DISCORD HUB
📁 CATEGORY: 💰 ECONOMY & GAMIFICATION
"""

import discord
from discord.ext import commands
import json
import asyncio
from datetime import datetime, timedelta
import random
from pathlib import Path

class BROskiShopSystem:
    """Complete BROski$ economy with shop and redemption system"""
    
    def __init__(self, bot):
        self.bot = bot
        self.user_balances = {}
        self.purchase_history = []
        self.shop_items = {
            "roles": [
                {
                    "name": "🌟 VIP Empire Member",
                    "description": "Exclusive VIP role with special channel access and priority support",
                    "price": 500,
                    "type": "role",
                    "duration": "permanent",
                    "emoji": "🌟"
                },
                {
                    "name": "🚀 Legendary Contributor",
                    "description": "Recognition role for outstanding community contributions",
                    "price": 750,
                    "type": "role", 
                    "duration": "permanent",
                    "emoji": "🚀"
                },
                {
                    "name": "⚡ Hyperfocus Champion",
                    "description": "Special role for consistent engagement and productivity",
                    "price": 600,
                    "type": "role",
                    "duration": "permanent", 
                    "emoji": "⚡"
                },
                {
                    "name": "💎 Diamond Elite (1 Week)",
                    "description": "Premium temporary role with exclusive perks and recognition",
                    "price": 300,
                    "type": "role",
                    "duration": "7 days",
                    "emoji": "💎"
                }
            ],
            "badges": [
                {
                    "name": "🏆 Achievement Master",
                    "description": "Unlock and display the Achievement Master badge on your profile",
                    "price": 200,
                    "type": "badge",
                    "emoji": "🏆"
                },
                {
                    "name": "🧠 ADHD Advocate",
                    "description": "Show your support for neurodivergent community members",
                    "price": 150,
                    "type": "badge",
                    "emoji": "🧠"
                },
                {
                    "name": "🎊 Celebration King/Queen",
                    "description": "Badge for spreading joy and positive energy in the community",
                    "price": 180,
                    "type": "badge",
                    "emoji": "🎊"
                },
                {
                    "name": "💡 Innovation Pioneer",
                    "description": "Recognition for contributing creative ideas and solutions",
                    "price": 250,
                    "type": "badge",
                    "emoji": "💡"
                }
            ],
            "perks": [
                {
                    "name": "📢 Community Shoutout",
                    "description": "Get featured in #announcements with a personalized shoutout message",
                    "price": 400,
                    "type": "service",
                    "emoji": "📢"
                },
                {
                    "name": "🎨 Custom Emoji Creation",
                    "description": "Work with team to create a custom emoji for the server",
                    "price": 800,
                    "type": "service",
                    "emoji": "🎨"
                },
                {
                    "name": "📝 Featured Story Spotlight",
                    "description": "Share your story, project, or achievement in a dedicated featured post",
                    "price": 350,
                    "type": "service",
                    "emoji": "📝"
                },
                {
                    "name": "🎤 Voice Chat Priority",
                    "description": "Priority access to voice channels and special voice events",
                    "price": 250,
                    "type": "perk",
                    "duration": "30 days",
                    "emoji": "🎤"
                }
            ],
            "stickers": [
                {
                    "name": "🎊 Celebration Pack",
                    "description": "10 exclusive celebration stickers for Discord and other platforms",
                    "price": 100,
                    "type": "digital",
                    "emoji": "🎊"
                },
                {
                    "name": "⚡ Energy Boost Pack",
                    "description": "ADHD-friendly motivational stickers and GIFs",
                    "price": 120,
                    "type": "digital",
                    "emoji": "⚡"
                },
                {
                    "name": "💎 Empire Elite Pack",
                    "description": "Premium sticker collection with empire themes",
                    "price": 150,
                    "type": "digital",
                    "emoji": "💎"
                }
            ],
            "special": [
                {
                    "name": "🎯 Personal Productivity Consultation",
                    "description": "30-minute 1-on-1 ADHD productivity consultation with team member",
                    "price": 1000,
                    "type": "service",
                    "emoji": "🎯"
                },
                {
                    "name": "🏛️ Empire Co-Creator Status",
                    "description": "Join the inner circle of empire builders with special privileges",
                    "price": 1500,
                    "type": "role",
                    "duration": "permanent",
                    "emoji": "🏛️"
                },
                {
                    "name": "🌟 Name in Credits",
                    "description": "Get your name featured in the Hyperfocus Zone credits and acknowledgments",
                    "price": 600,
                    "type": "recognition",
                    "emoji": "🌟"
                }
            ]
        }
    
    async def display_shop(self, ctx):
        """Display the BROski$ shop with all available items"""
        embed = discord.Embed(
            title="💎⚡🏪 BROSKI$ EMPIRE SHOP 🏪⚡💎",
            description="Spend your hard-earned BROski$ on legendary rewards!",
            color=0xffd700
        )
        
        # Get user balance
        user_id = str(ctx.author.id)
        balance = self.user_balances.get(user_id, 0)
        
        embed.add_field(
            name="💰 Your Balance",
            value=f"{balance:,} BROski$",
            inline=True
        )
        
        embed.add_field(
            name="🛒 How to Purchase",
            value="Use `!shop-buy <category> <number>` to purchase items!",
            inline=True
        )
        
        # Display shop categories
        for category, items in self.shop_items.items():
            category_text = ""
            for i, item in enumerate(items, 1):
                affordable = "✅" if balance >= item["price"] else "❌"
                duration_text = f" ({item['duration']})" if 'duration' in item and item['duration'] != 'permanent' else ""
                category_text += f"{affordable} {i}. {item['emoji']} **{item['name']}** - {item['price']} BROski${duration_text}\n"
                category_text += f"   _{item['description']}_\n\n"
            
            embed.add_field(
                name=f"🏷️ {category.upper()}",
                value=category_text[:1024],  # Discord field limit
                inline=False
            )
        
        embed.set_footer(text="💡 Earn more BROski$ with !health, !ultra-scan, challenges, and community participation!")
        
        await ctx.send(embed=embed)
    
    async def purchase_item(self, ctx, category, item_number):
        """Process a shop purchase"""
        user_id = str(ctx.author.id)
        balance = self.user_balances.get(user_id, 0)
        
        # Validate category and item
        if category not in self.shop_items:
            await ctx.send("❌ Invalid category! Choose: roles, badges, perks, stickers, or special")
            return
        
        items = self.shop_items[category]
        if item_number < 1 or item_number > len(items):
            await ctx.send(f"❌ Invalid item number! Choose 1-{len(items)} for {category}")
            return
        
        item = items[item_number - 1]
        
        # Check if user can afford it
        if balance < item["price"]:
            needed = item["price"] - balance
            await ctx.send(f"❌ Insufficient BROski$! You need {needed:,} more BROski$ to purchase {item['name']}")
            return
        
        # Process purchase
        self.user_balances[user_id] = balance - item["price"]
        
        # Record purchase
        purchase_record = {
            "user_id": user_id,
            "username": ctx.author.display_name,
            "item": item,
            "category": category,
            "timestamp": datetime.now(),
            "price_paid": item["price"]
        }
        self.purchase_history.append(purchase_record)
        
        # Create purchase confirmation
        embed = discord.Embed(
            title="🎊⚡💎 PURCHASE SUCCESSFUL! 💎⚡🎊",
            description=f"Congratulations on your legendary purchase!",
            color=0x00ff00
        )
        
        embed.add_field(
            name="🛒 Item Purchased",
            value=f"{item['emoji']} **{item['name']}**",
            inline=True
        )
        
        embed.add_field(
            name="💰 Price Paid",
            value=f"{item['price']:,} BROski$",
            inline=True
        )
        
        embed.add_field(
            name="💳 Remaining Balance",
            value=f"{self.user_balances[user_id]:,} BROski$",
            inline=True
        )
        
        embed.add_field(
            name="📦 What's Next",
            value=self.get_fulfillment_instructions(item),
            inline=False
        )
        
        embed.set_footer(text="🎊 Thank you for supporting the Hyperfocus Zone empire!")
        
        await ctx.send(embed=embed)
        
        # Announce purchase in celebration channel
        await self.announce_purchase(ctx, purchase_record)
    
    def get_fulfillment_instructions(self, item):
        """Get instructions for fulfilling the purchased item"""
        item_type = item.get("type", "unknown")
        
        if item_type == "role":
            return "🎭 Your role will be assigned within 24 hours by a team member!"
        elif item_type == "badge":
            return "🏆 Your badge has been added to your profile! Check your achievements!"
        elif item_type == "service":
            return "🛠️ A team member will contact you within 48 hours to fulfill your service!"
        elif item_type == "digital":
            return "📱 Your digital items will be sent to you via DM within 24 hours!"
        elif item_type == "perk":
            return "⚡ Your perk is now active! Enjoy your enhanced empire experience!"
        else:
            return "📞 A team member will contact you about your purchase fulfillment!"
    
    async def announce_purchase(self, ctx, purchase_record):
        """Announce purchase in celebration channel"""
        # Find celebration channel
        celebration_channel = None
        for guild in self.bot.guilds:
            for channel in guild.channels:
                if channel.name == "celebration-hall":
                    celebration_channel = channel
                    break
        
        if not celebration_channel:
            return
        
        item = purchase_record["item"]
        
        celebration_messages = [
            f"🎊 LEGENDARY PURCHASE ALERT! {purchase_record['username']} just bought {item['emoji']} **{item['name']}** for {item['price']:,} BROski$!",
            f"💎 EMPIRE EXPANSION! {purchase_record['username']} invested {item['price']:,} BROski$ in {item['emoji']} **{item['name']}**! The empire grows stronger!",
            f"🚀 ECONOMIC ACTIVITY! {purchase_record['username']} just made a legendary {item['price']:,} BROski$ purchase: {item['emoji']} **{item['name']}**!"
        ]
        
        message = random.choice(celebration_messages)
        await celebration_channel.send(message)
    
    async def show_user_purchases(self, ctx):
        """Show user's purchase history"""
        user_id = str(ctx.author.id)
        user_purchases = [p for p in self.purchase_history if p["user_id"] == user_id]
        
        if not user_purchases:
            await ctx.send("🛒 You haven't made any purchases yet! Check out `!shop` to see what's available!")
            return
        
        embed = discord.Embed(
            title=f"🛍️⚡💎 {ctx.author.display_name}'s PURCHASE HISTORY 💎⚡🛍️",
            description="Your legendary shopping achievements!",
            color=0x9932cc
        )
        
        total_spent = sum([p["price_paid"] for p in user_purchases])
        
        embed.add_field(
            name="💰 Shopping Stats",
            value=f"🛒 {len(user_purchases)} purchases made\n💎 {total_spent:,} total BROski$ spent\n🏆 Legendary shopper status!",
            inline=False
        )
        
        # Show recent purchases
        recent_purchases = sorted(user_purchases, key=lambda x: x["timestamp"], reverse=True)[:5]
        
        purchase_text = ""
        for purchase in recent_purchases:
            item = purchase["item"]
            date = purchase["timestamp"].strftime("%Y-%m-%d")
            purchase_text += f"{item['emoji']} **{item['name']}** - {purchase['price_paid']:,} BROski$ ({date})\n"
        
        embed.add_field(
            name="🕒 Recent Purchases",
            value=purchase_text or "No recent purchases",
            inline=False
        )
        
        current_balance = self.user_balances.get(user_id, 0)
        embed.add_field(
            name="💳 Current Balance",
            value=f"{current_balance:,} BROski$",
            inline=True
        )
        
        embed.set_footer(text="🎊 Keep earning and spending to support the empire!")
        
        await ctx.send(embed=embed)

# Integration commands for main bot
def setup_shop_integration(main_bot):
    """Setup function to integrate with main Discord bot"""
    shop_system = BROskiShopSystem(main_bot)
    
    @main_bot.command(name='shop')
    async def show_shop(ctx):
        """Display the BROski$ shop"""
        await shop_system.display_shop(ctx)
    
    @main_bot.command(name='shop-buy')
    async def buy_item(ctx, category=None, item_number: int = None):
        """Purchase an item from the shop"""
        if not category or item_number is None:
            await ctx.send("🛒 Usage: `!shop-buy <category> <number>`\nExample: `!shop-buy roles 1`")
            return
        
        await shop_system.purchase_item(ctx, category.lower(), item_number)
    
    @main_bot.command(name='shop-history')
    async def purchase_history(ctx):
        """Show user's purchase history"""
        await shop_system.show_user_purchases(ctx)
    
    @main_bot.command(name='balance')
    async def check_balance(ctx):
        """Check BROski$ balance"""
        user_id = str(ctx.author.id)
        balance = shop_system.user_balances.get(user_id, 0)
        
        embed = discord.Embed(
            title="💰⚡💎 BROSKI$ BALANCE 💎⚡💰",
            description=f"{ctx.author.display_name}'s legendary wallet!",
            color=0xffd700
        )
        
        embed.add_field(
            name="💎 Current Balance",
            value=f"{balance:,} BROski$",
            inline=True
        )
        
        embed.add_field(
            name="🚀 Earning Tips",
            value="• Use `!health` (50 BROski$)\n• Use `!ultra-scan` (100 BROski$)\n• Participate in challenges\n• Complete team rituals",
            inline=True
        )
        
        await ctx.send(embed=embed)

if __name__ == "__main__":
    logger.info("🌌 💎⚡🏪 BROSKI$ SHOP & REDEMPTION SYSTEM READY 🏪⚡💎")
    logger.info("🌌 📁 Integrate with main Discord bot using setup_shop_integration()")
