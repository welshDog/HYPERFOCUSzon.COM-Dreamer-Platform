#!/usr/bin/env python3
"""
🚨💎⚡ BROski♾️ LEGENDARY FILE RESCUE SCANNER ⚡💎🚨
Simple and effective file rescue for HYPERFOCUS ZONE EMPIRE
"""

import os
import datetime
import json

def scan_hyperfocus_empire():
    """Scan the entire empire for rescue candidates"""
    print("🚨💎 BROski♾️ LEGENDARY FILE RESCUE SCAN INITIATED! 💎🚨")
    
    # Define what we're looking for
    rescue_keywords = [
        "unused", "draft", "idea", "concept", "wip", "hyper", "ultra", 
        "legendary", "ultimate", "supreme", "maximum", "experimental",
        "prototype", "test", "backup", "old", "archive", "broski", 
        "empire", "fusion", "boardroom", "crystal", "agent"
    ]
    
    # Scan results
    rescue_files = []
    total_scanned = 0
    
    # Start scanning from H:\ root
    print("🔍 Scanning H:\\ for lost/unused/hyperpowered files...")
    
    try:
        for root, dirs, files in os.walk("H:\\"):
            # Skip system directories
            dirs[:] = [d for d in dirs if not d.startswith('.') and d not in ['node_modules', '__pycache__']]
            
            for filename in files:
                total_scanned += 1
                filepath = os.path.join(root, filename)
                
                # Check if file matches rescue criteria
                lower_name = filename.lower()
                if any(keyword in lower_name for keyword in rescue_keywords):
                    try:
                        stat_info = os.stat(filepath)
                        rescue_files.append({
                            "filename": filename,
                            "path": filepath,
                            "size": stat_info.st_size,
                            "modified": datetime.datetime.fromtimestamp(stat_info.st_mtime).isoformat()
                        })
                    except:
                        pass
                
                # Progress indicator every 1000 files
                if total_scanned % 1000 == 0:
                    print(f"📊 Scanned {total_scanned} files, found {len(rescue_files)} rescue candidates...")
    
    except Exception as e:
        print(f"⚠️ Scan error: {e}")
    
    # Generate rescue report
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    
    # Create detailed report
    report_data = {
        "scan_timestamp": datetime.datetime.now().isoformat(),
        "total_files_scanned": total_scanned,
        "rescue_candidates_found": len(rescue_files),
        "rescue_files": rescue_files
    }
    
    # Save JSON report
    json_file = f"🚨💎⚡_BROSKI_FILE_RESCUE_REPORT_{timestamp}_⚡💎🚨.json"
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(report_data, f, indent=2, ensure_ascii=False)
    
    # Create readable summary
    summary_file = f"🚨💎⚡_BROSKI_FILE_RESCUE_SUMMARY_{timestamp}_⚡💎🚨.md"
    with open(summary_file, 'w', encoding='utf-8') as f:
        f.write("🚨💎⚡ BROski♾️ LEGENDARY FILE RESCUE SUMMARY ⚡💎🚨\n\n")
        f.write("═══════════════════════════════════════════════════════════════════\n\n")
        f.write(f"📅 Scan Date: {report_data['scan_timestamp']}\n")
        f.write(f"📊 Total Files Scanned: {total_scanned}\n")
        f.write(f"🎯 Rescue Candidates Found: {len(rescue_files)}\n\n")
        
        f.write("🏆 TOP 50 RESCUE CANDIDATES:\n\n")
        
        # Sort by size (largest first) and show top 50
        sorted_files = sorted(rescue_files, key=lambda x: x['size'], reverse=True)[:50]
        
        for i, file_info in enumerate(sorted_files, 1):
            f.write(f"{i}. {file_info['filename']}\n")
            f.write(f"   📁 {file_info['path']}\n")
            f.write(f"   📊 Size: {file_info['size']} bytes\n")
            f.write(f"   📅 Modified: {file_info['modified']}\n\n")
        
        f.write("═══════════════════════════════════════════════════════════════════\n\n")
        f.write("🎊 BOARDROOM RECOMMENDATIONS:\n\n")
        f.write("✅ Review files for reactivation potential\n")
        f.write("✅ Convert ideas into Memory Crystals\n") 
        f.write("✅ Integrate hyperpowered files into Phase 4 expansion\n")
        f.write("✅ Archive or delete true unused files\n\n")
        f.write("AWOOOO!!! 🐺💎⚡\n")
        f.write("Status: LEGENDARY FILE RESCUE COMPLETE\n")
    
    print(f"\n🎊 LEGENDARY FILE RESCUE MISSION COMPLETE! 🎊")
    print(f"📊 Files Scanned: {total_scanned}")
    print(f"🎯 Rescue Candidates: {len(rescue_files)}")
    print(f"📄 JSON Report: {json_file}")
    print(f"📝 Summary Report: {summary_file}")
    print("\n🚀 READY FOR BOARDROOM REVIEW!")
    print("AWOOOO!!! 🐺💎⚡")

if __name__ == "__main__":
    scan_hyperfocus_empire()
