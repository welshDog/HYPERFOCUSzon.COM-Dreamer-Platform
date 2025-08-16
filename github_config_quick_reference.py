#!/usr/bin/env python3
"""
🎯 QUICK GITHUB CONFIGURATION REFERENCE 🎯
==========================================
Copy-paste ready commands and configurations
For rapid GitHub interface setup
==========================================
"""

print("🎯⚡ QUICK GITHUB CONFIGURATION REFERENCE ⚡🎯")
print("=" * 55)
print()

# DIRECT LINKS FOR IMMEDIATE ACCESS
print("🔗 DIRECT CONFIGURATION LINKS:")
print("-" * 35)
repo_base = "https://github.com/welshDog/HYPERFOCUSzone-Community"

direct_links = [
    ("🛡️ Security Settings", f"{repo_base}/settings/security_analysis"),
    ("🏷️ Label Management", f"{repo_base}/labels"),
    ("🌿 Branch Protection", f"{repo_base}/settings/branches"),
    ("⚙️ General Settings", f"{repo_base}/settings"),
    ("🚀 GitHub Actions", f"{repo_base}/actions"),
]

for name, url in direct_links:
    print(f"{name}")
    print(f"   📍 {url}")
    print()

# SECURITY CONFIGURATION CHECKLIST
print("🛡️ SECURITY CONFIGURATION QUICK CHECKLIST:")
print("-" * 45)

security_items = [
    "✅ Dependabot alerts → Click 'Enable'",
    "✅ Dependabot security updates → Click 'Enable'",
    "✅ Dependabot version updates → Click 'Enable'",
    "✅ Secret scanning → Click 'Enable'",
    "✅ Push protection → Click 'Enable'",
    "✅ Code scanning → Click 'Set up' → Choose CodeQL",
]

for i, item in enumerate(security_items, 1):
    print(f"{i}. {item}")
print()

# LABEL CREATION QUICK REFERENCE
print("🏷️ LABEL CREATION QUICK REFERENCE:")
print("-" * 40)
print("Copy these exact values when creating labels:")
print()

label_data = [
    ("good first issue", "#7057ff", "Great for newcomers"),
    ("help wanted", "#008672", "Extra attention needed"),
    ("documentation", "#0075ca", "Improvements needed"),
    ("enhancement", "#a2eeef", "New feature request"),
    ("bug", "#d73a4a", "Something isn't working"),
    ("question", "#d876e3", "Further information needed"),
    ("empire-core", "#ff6b6b", "Core empire functionality"),
    ("ai-parliament", "#4ecdc4", "AI coordination system"),
    ("hyperfocus", "#45b7d1", "ADHD/focus optimization"),
    ("neurodivergent", "#96ceb4", "Accessibility features"),
    ("performance", "#feca57", "Speed optimization"),
    ("security", "#ff9ff3", "Security improvements"),
    ("devops", "#54a0ff", "Infrastructure changes"),
    ("community", "#5f27cd", "Community building"),
]

print("📋 ESSENTIAL LABELS (Copy-paste ready):")
for name, color, desc in label_data:
    print(f"Name: {name}")
    print(f"Color: {color}")
    print(f"Description: {desc}")
    print("---")

# BRANCH PROTECTION QUICK SETUP
print("\n🌿 BRANCH PROTECTION QUICK SETUP:")
print("-" * 40)

protection_settings = [
    "✅ Require pull request reviews before merging",
    "✅ Required number of reviewers: 1",
    "✅ Require status checks to pass before merging",
    "✅ Require branches to be up to date before merging",
    "✅ Include administrators",
    "✅ Allow force pushes: ❌ (Keep disabled)",
    "✅ Allow deletions: ❌ (Keep disabled)",
]

for setting in protection_settings:
    print(f"   {setting}")

print()
print("🎯 PRIORITY ORDER:")
print("1️⃣ Security settings (5 minutes)")
print("2️⃣ Essential labels (10 minutes)")
print("3️⃣ Branch protection (3 minutes)")
print()
print("⏱️ Total estimated time: 18 minutes")
print("🏆 Result: Enterprise-grade repository ready for community! ⚡💎")

# SUCCESS INDICATORS
print("\n✅ SUCCESS INDICATORS:")
print("-" * 25)

success_checks = [
    "🔒 Green security badge in repository",
    "🏷️ 14+ labels visible in Issues tab",
    "🌿 'Protected' badge on main branch",
    "🤖 Dependabot PRs start appearing",
    "🔍 CodeQL workflow in Actions tab",
]

for check in success_checks:
    print(f"   {check}")

print(f"\n🚀 READY TO CONFIGURE!")
print("Use these direct links and copy-paste values for rapid setup! ❤️‍🔥")
