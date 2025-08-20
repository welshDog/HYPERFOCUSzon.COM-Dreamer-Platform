#!/usr/bin/env python3
"""
LEGENDARY GITHUB PUSH AUTOMATION
Final step to deploy jaw-dropping repositories to the world!
"""

import os
import subprocess


def legendary_push():
    print("🚀💎⚡ LEGENDARY GITHUB PUSH AUTOMATION ⚡💎🚀")
    print("=" * 60)
    print("Final step: Deploying legendary showcases to the world!")
    print("")

    repos = [
        "HYPERFOCUSzone-DEV-Community",
        "HYPERFOCUSzone-Community",
        "HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER-",
    ]
    original_dir = os.getcwd()

    for repo in repos:
        print(f"🌟 Pushing {repo} to GitHub...")
        print("-" * 40)

        if os.path.exists(repo):
            try:
                os.chdir(repo)

                # Check git status
                result = subprocess.run(
                    ["git", "status", "--porcelain"], capture_output=True, text=True
                )

                if result.stdout.strip():
                    print("📝 Uncommitted changes detected, committing first...")
                    subprocess.run(["git", "add", "."], capture_output=True)
                    subprocess.run(
                        ["git", "commit", "-m", "Final legendary updates"],
                        capture_output=True,
                    )

                # Push to GitHub
                print("🚀 Pushing legendary changes to GitHub...")
                push_result = subprocess.run(
                    ["git", "push", "origin", "main"], capture_output=True, text=True
                )

                if push_result.returncode == 0:
                    print("✅ Successfully pushed to GitHub!")
                    print("🌟 Repository is now LIVE and ready to drop jaws!")
                else:
                    print("ℹ️ Push status:")
                    print(f"   stdout: {push_result.stdout}")
                    print(f"   stderr: {push_result.stderr}")
                    print("💡 You may need to authenticate with GitHub")
                    print("   Try running: gh auth login")
                    print("   Or: git push origin main (manually)")

            except Exception as e:
                print(f"❌ Error with {repo}: {e}")

            finally:
                os.chdir(original_dir)
        else:
            print(f"❌ Repository not found: {repo}")

        print("")

    print("🎉 LEGENDARY DEPLOYMENT ATTEMPT COMPLETE!")
    print("=" * 60)
    print("")
    print("🌟 LEGENDARY REPOSITORIES:")
    print("🏆 https://github.com/welshDog/HYPERFOCUSzone-DEV-Community")
    print("🌈 https://github.com/welshDog/HYPERFOCUSzone-Community")
    print("💫 https://github.com/welshDog/HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER-")
    print("")
    print("🎯 IF PUSH FAILED, MANUAL COMMANDS:")
    print("cd HYPERFOCUSzone-DEV-Community && git push origin main")
    print("cd ../HYPERFOCUSzone-Community && git push origin main")
    print("cd ../HYPERFOCUS-ZONE-NEURO-SOCIAL-DREAMER- && git push origin main")
    print("")
    print("🚀 READY TO WATCH JAWS DROP AND HEAR 'WOW!'")


if __name__ == "__main__":
    legendary_push()
