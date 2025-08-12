#!/usr/bin/env python3
"""
EXECUTE THE COMPLETE PORTAL TESTING ADVENTURES SYSTEM WITH USER JOURNEY VALIDATION
"""

# Import the complete system
import sys
import os

def main():
    print("🚀⚡💎 PORTAL TESTING ADVENTURES - LEGENDARY EXECUTION STARTING! 💎⚡🚀")
    print("🪄 MERGE APPROACH: Technical Testing + User Journey Validation ACTIVATED!")
    print("=" * 85)

    try:
        # Change to correct directory
        os.chdir("h:\\")

        # Execute the complete system directly
        exec(open('🚀⚡💎_PORTAL_TESTING_ADVENTURES_COMPLETE_💎⚡🚀.py', encoding='utf-8').read())

        print("\n🎊 PORTAL TESTING ADVENTURES WITH USER JOURNEY VALIDATION COMPLETE! 🎊")
        print("✅ MERGE APPROACH SUCCESSFUL - ULTIMATE USER EXPERIENCE VALIDATION ACHIEVED! ✅")

    except Exception as e:
        print(f"❌ Error executing portal testing system: {e}")
        print("🔧 Let's diagnose and fix the issue...")
        import traceback
        traceback.print_exc()

        # Alternative execution method
        try:
            print("\n🔄 Trying alternative execution method...")

            # Import and run directly
            sys.path.insert(0, 'h:\\')

            # Read and execute the file content
            with open('🚀⚡💎_PORTAL_TESTING_ADVENTURES_COMPLETE_💎⚡🚀.py', 'r', encoding='utf-8') as f:
                code = f.read()
                exec(code)

            print("✅ Alternative execution successful!")

        except Exception as e2:
            print(f"❌ Alternative execution also failed: {e2}")
            traceback.print_exc()

if __name__ == "__main__":
    main()

        if result.stderr:
            print("\nSTDERR:")
            print(result.stderr)

        print(f"\nReturn code: {result.returncode}")

        if result.returncode == 0:
            print("\n🎊 EXECUTION SUCCESSFUL!")
        else:
            print("\n⚠️ Execution completed with warnings/errors")

    except Exception as e:
        print(f"❌ Execution error: {e}")

if __name__ == "__main__":
    execute_portal_system()
