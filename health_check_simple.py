import os
import platform
import sys
from datetime import datetime


def main():
    print("HYPERFOCUS ZONE SUPER POWER TECH HEALTH CHECK")
    print("=" * 50)

    results = {
        "timestamp": datetime.now().isoformat(),
        "python_version": platform.python_version(),
        "os": platform.system(),
        "architecture": platform.architecture()[0],
        "status": "RUNNING",
    }

    print(f"Python Version: {results['python_version']}")
    print(f"Operating System: {results['os']}")
    print(f"Architecture: {results['architecture']}")
    print(f"Timestamp: {results['timestamp']}")

    # Check current directory
    current_dir = os.getcwd()
    print(f"Current Directory: {current_dir}")

    # List some files in the directory
    files = os.listdir(".")
    health_files = [f for f in files if "health" in f.lower() or "check" in f.lower()]
    print(f"Health/Check related files found: {len(health_files)}")

    for file in health_files[:5]:  # Show first 5
        print(f"  - {file}")

    results["health_files_count"] = len(health_files)
    results["current_directory"] = current_dir
    results["status"] = "COMPLETED"

    print("\nHEALTH CHECK COMPLETED SUCCESSFULLY!")
    print(f"Total health-related files: {len(health_files)}")

    return results


if __name__ == "__main__":
    try:
        results = main()
        print("\nSUCCESS: Health check completed!")
    except Exception as e:
        print(f"ERROR: {str(e)}")
        sys.exit(1)
