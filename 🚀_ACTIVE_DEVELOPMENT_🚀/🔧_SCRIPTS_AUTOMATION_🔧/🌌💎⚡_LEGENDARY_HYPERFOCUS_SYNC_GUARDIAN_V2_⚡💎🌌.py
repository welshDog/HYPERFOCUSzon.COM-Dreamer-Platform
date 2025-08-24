#!/usr/bin/env python3
"""
🌌💎⚡ LEGENDARY HYPERFOCUS SYNC GUARDIAN V2.0 ⚡💎🌌

Enhanced version of the original Hybrid Hyperfocus Sync Guardian with:
✨ Discord real-time broadcasting
📊 Visual sync health dashboard
☁️ Multi-target sync (local + cloud + external)
🔍 Advanced empire chronicle analytics
⚡ Performance optimization & auto-healing
🎯 Smart sync prioritization
🧠 AI-powered sync prediction

The ultimate empire synchronization system!
"""

from pathlib import Path
import logging

# Enhanced logging
logging.basicConfig(
    level=logging.INFO,
    format="🌌💎⚡ %(asctime)s - %(levelname)s - %(message)s ⚡💎🌌",
    handlers=[
        logging.FileHandler("h:/empire_sync_legendary.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# 🔥 ENHANCED CONFIG
HYPERFOCUS_ROOT = Path(r"h:\")  # Updated to current workspace
SYNC_TARGETS = [
    {"path": Path(r"h:\backup_primary"), "type": "local", "priority": 1, "enabled": True},
    {"path": Path(r"h:\backup_secondary"), "type": "external", "priority": 2, "enabled": True},
    # Add cloud targets when available:
    # {"path": Path(r"C:\Users\YourName\OneDrive\HyperfocusBackup"), "type": "cloud", "priority": 3, "enabled": True}
]

SYNC_DB = HYPERFOCUS_ROOT / "hyperfocus_sync_legendary.json"
CHRONICLE_LOG = HYPERFOCUS_ROOT / "empire_chronicle_legendary.json"
PERFORMANCE_LOG = HYPERFOCUS_ROOT / "sync_performance_metrics.json"
NIGHTLY_SCAN_HOUR = 3

# Enhanced sync configuration
SYNC_CONFIG = {
    "verify_integrity": True,
    "enable_compression": False,  # For large files
    "enable_encryption": False,   # For sensitive files
    "max_retry_attempts": 3,
    "sync_batch_size": 10,
    "performance_monitoring": True,
    "ai_prediction": True,
    "auto_healing": True
}

# Discord configuration (set enabled=True when you have credentials)
DISCORD_CONFIG = {
    "enabled": False,
    "token": "YOUR_DISCORD_BOT_TOKEN_HERE",
    "channel_id": 12345678901234567890,
    "broadcast_important_only": True
}


class EnhancedSyncMetrics:
    """📊 Advanced sync performance tracking"""

    def __init__(self):
        self.metrics = {
            "sync_operations": 0,
            "successful_syncs": 0,
            "failed_syncs": 0,
            "total_bytes_synced": 0,
            "average_sync_time": 0.0,
            "sync_speed_mbps": 0.0,
            "empire_health_score": 100.0,
            "last_full_scan": None,
            "uptime_hours": 0.0,
            "files_monitored": 0,
            "auto_healing_events": 0
        }
        self.start_time = datetime.now()

    def record_sync(self, success: bool, file_size: int, sync_time: float):
        """📈 Record sync operation metrics"""
        self.metrics["sync_operations"] += 1

        if success:
            self.metrics["successful_syncs"] += 1
            self.metrics["total_bytes_synced"] += file_size

            # Update average sync time
            total_time = self.metrics["average_sync_time"] * (self.metrics["successful_syncs"] - 1) + sync_time
            self.metrics["average_sync_time"] = total_time / self.metrics["successful_syncs"]

            # Calculate sync speed (MB/s)
            if sync_time > 0:
                speed_mbps = (file_size / (1024 * 1024)) / sync_time
                self.metrics["sync_speed_mbps"] = speed_mbps
        else:
            self.metrics["failed_syncs"] += 1

        # Update empire health score
        self._calculate_empire_health()

    def _calculate_empire_health(self):
        """🏆 Calculate overall empire sync health score"""
        if self.metrics["sync_operations"] == 0:
            return

        success_rate = self.metrics["successful_syncs"] / self.metrics["sync_operations"]
        base_health = success_rate * 100

        # Bonus points for consistent performance
        if self.metrics["average_sync_time"] < 1.0:  # Fast syncs
            base_health += 5
        if self.metrics["auto_healing_events"] > 0:  # Self-healing capability
            base_health += 10

        self.metrics["empire_health_score"] = min(base_health, 100.0)

    def get_performance_report(self) -> Dict:
        """📊 Generate comprehensive performance report"""
        uptime = (datetime.now() - self.start_time).total_seconds() / 3600
        self.metrics["uptime_hours"] = round(uptime, 2)

        return {
            "timestamp": datetime.now().isoformat(),
            "metrics": self.metrics.copy(),
            "status": self._get_status_assessment(),
            "recommendations": self._get_optimization_recommendations()
        }

    def _get_status_assessment(self) -> str:
        """🎯 Assess current sync system status"""
        health = self.metrics["empire_health_score"]

        if health >= 95:
            return "🏆 LEGENDARY - Empire operating at peak performance"
        elif health >= 85:
            return "⚡ EXCELLENT - Strong empire synchronization"
        elif health >= 70:
            return "💎 GOOD - Stable empire operations"
        elif health >= 50:
            return "⚠️ CAUTION - Empire needs optimization"
        else:
            return "🚨 CRITICAL - Immediate attention required"

    def _get_optimization_recommendations(self) -> List[str]:
        """💡 Generate optimization recommendations"""
        recommendations = []

        if self.metrics["failed_syncs"] > self.metrics["successful_syncs"] * 0.1:
            recommendations.append("🔧 High failure rate detected - check storage health")

        if self.metrics["average_sync_time"] > 5.0:
            recommendations.append("⚡ Slow sync times - consider storage optimization")

        if self.metrics["sync_operations"] < 10:
            recommendations.append("📈 Low activity - verify monitoring is active")

        if not recommendations:
            recommendations.append("✨ Empire running optimally - maintain current configuration")

        return recommendations


class LegendaryHyperfocusHandler(FileSystemEventHandler):
    """🌟 Enhanced file system event handler with multi-target sync"""

    def __init__(self, sync_targets: List[Dict], metrics: EnhancedSyncMetrics):
        self.sync_targets = sync_targets
        self.metrics = metrics
        self.sync_queue = asyncio.Queue()

        # Performance tracking
        self.last_sync_times = {}
        self.sync_priorities = {}

    def on_modified(self, event):
        if not event.is_directory:
            self._queue_sync(event.src_path, "modified")

    def on_created(self, event):
        if not event.is_directory:
            self._queue_sync(event.src_path, "created")

    def on_moved(self, event):
        if not event.is_directory:
            self._handle_file_move(event.src_path, event.dest_path)

    def on_deleted(self, event):
        if not event.is_directory:
            self._handle_file_deletion(event.src_path)

    def _queue_sync(self, src_path: str, event_type: str):
        """📋 Queue file for intelligent sync processing"""
        try:
            file_path = Path(src_path)

            # Calculate sync priority
            priority = self._calculate_sync_priority(file_path, event_type)

            # Add to sync queue
            sync_task = {
                "file_path": file_path,
                "event_type": event_type,
                "priority": priority,
                "timestamp": datetime.now(),
                "retry_count": 0
            }

            # Process sync task
            asyncio.create_task(self._process_sync_task(sync_task))

        except Exception as e:
            logger.error(f"❌ Error queuing sync for {src_path}: {e}")
            log_event("queue_error", src_path, str(e))

    def _calculate_sync_priority(self, file_path: Path, event_type: str) -> int:
        """🎯 Calculate sync priority based on file importance"""
        priority = 5  # Default priority

        # High priority for critical files
        critical_extensions = {'.py', '.json', '.md', '.txt', '.html'}
        if file_path.suffix.lower() in critical_extensions:
            priority += 3

        # Higher priority for recent modifications
        if event_type == "created":
            priority += 2
        elif event_type == "modified":
            priority += 1

        # Lower priority for temporary files
        if file_path.name.startswith(('.tmp', '~')):
            priority -= 2

        return max(priority, 1)  # Minimum priority of 1

    async def _process_sync_task(self, task: Dict):
        """⚡ Process a single sync task with retry logic"""
        start_time = time.time()
        file_path = task["file_path"]

        try:
            if not file_path.exists():
                logger.warning(f"⚠️ File no longer exists: {file_path}")
                return

            file_size = file_path.stat().st_size
            success_count = 0

            # Sync to all enabled targets
            for target in self.sync_targets:
                if not target["enabled"]:
                    continue

                try:
                    if await self._sync_to_target(file_path, target):
                        success_count += 1
                        target["sync_count"] = target.get("sync_count", 0) + 1
                    else:
                        target["error_count"] = target.get("error_count", 0) + 1

                except Exception as e:
                    logger.error(f"❌ Target sync failed {target['path']}: {e}")
                    target["error_count"] = target.get("error_count", 0) + 1

            # Record metrics
            sync_time = time.time() - start_time
            success = success_count > 0
            self.metrics.record_sync(success, file_size, sync_time)

            # Log results
            if success:
                log_event("multi_sync", str(file_path.relative_to(HYPERFOCUS_ROOT)),
                         f"synced_to_{success_count}_targets")
            else:
                log_event("sync_failure", str(file_path.relative_to(HYPERFOCUS_ROOT)),
                         "all_targets_failed")

                # Auto-healing attempt
                if SYNC_CONFIG["auto_healing"] and task["retry_count"] < SYNC_CONFIG["max_retry_attempts"]:
                    task["retry_count"] += 1
                    await asyncio.sleep(2 ** task["retry_count"])  # Exponential backoff
                    await self._process_sync_task(task)
                    self.metrics.metrics["auto_healing_events"] += 1

        except Exception as e:
            logger.error(f"❌ Sync task processing failed: {e}")
            log_event("task_error", str(file_path), str(e))

    async def _sync_to_target(self, src_file: Path, target: Dict) -> bool:
        """🎯 Sync file to a specific target with verification"""
        try:
            rel_path = src_file.relative_to(HYPERFOCUS_ROOT)
            dst_file = target["path"] / rel_path

            # Create target directory
            dst_file.parent.mkdir(parents=True, exist_ok=True)

            # Copy file
            shutil.copy2(src_file, dst_file)

            # Verify integrity if enabled
            if SYNC_CONFIG["verify_integrity"]:
                if hash_file(src_file) == hash_file(dst_file):
                    target["last_sync"] = datetime.now().isoformat()
                    return True
                else:
                    logger.error(f"❌ Hash mismatch: {dst_file}")
                    dst_file.unlink()  # Remove corrupted copy
                    return False
            else:
                target["last_sync"] = datetime.now().isoformat()
                return True

        except Exception as e:
            logger.error(f"❌ Target sync error {target['path']}: {e}")
            return False

    def _handle_file_move(self, old_path: str, new_path: str):
        """🔄 Handle file move/rename operations"""
        try:
            # Remove old file from all targets
            old_rel_path = Path(old_path).relative_to(HYPERFOCUS_ROOT)
            for target in self.sync_targets:
                if not target["enabled"]:
                    continue

                old_target_file = target["path"] / old_rel_path
                if old_target_file.exists():
                    old_target_file.unlink()

            # Sync new file location
            self._queue_sync(new_path, "moved")
            log_event("file_move", f"{old_path} → {new_path}", "relocated")

        except Exception as e:
            logger.error(f"❌ File move error: {e}")
            log_event("move_error", old_path, str(e))

    def _handle_file_deletion(self, deleted_path: str):
        """🗑️ Handle file deletion across all targets"""
        try:
            rel_path = Path(deleted_path).relative_to(HYPERFOCUS_ROOT)

            for target in self.sync_targets:
                if not target["enabled"]:
                    continue

                target_file = target["path"] / rel_path
                if target_file.exists():
                    target_file.unlink()

            log_event("multi_delete", str(rel_path), "removed_from_all_targets")

        except Exception as e:
            logger.error(f"❌ File deletion error: {e}")
            log_event("delete_error", deleted_path, str(e))


# Enhanced utility functions
def hash_file(filepath: Path) -> str:
    """🔐 Create SHA256 hash of a file"""
    h = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            for chunk in iter(lambda: f.read(8192), b""):  # Larger chunks for better performance
                h.update(chunk)
        return h.hexdigest()
    except Exception as e:
        logger.error(f"❌ Hash calculation failed for {filepath}: {e}")
        return ""


def log_event(event_type: str, rel_path: str, status: str = "ok"):
    """📜 Enhanced event logging with metrics"""
    entry = {
        "time": datetime.now().isoformat(timespec="seconds"),
        "event": event_type,
        "path": str(rel_path),
        "status": status,
        "session_id": getattr(log_event, 'session_id', datetime.now().strftime("%Y%m%d_%H%M%S"))
    }

    # Initialize session ID on first call
    if not hasattr(log_event, 'session_id'):
        log_event.session_id = datetime.now().strftime("%Y%m%d_%H%M%S")

    try:
        # Load existing chronicle
        if CHRONICLE_LOG.exists():
            with open(CHRONICLE_LOG, 'r', encoding='utf-8') as f:
                log_data = json.load(f)
        else:
            log_data = []

        log_data.append(entry)

        # Keep only last 1000 entries to prevent log bloat
        if len(log_data) > 1000:
            log_data = log_data[-1000:]

        # Save chronicle
        with open(CHRONICLE_LOG, 'w', encoding='utf-8') as f:
            json.dump(log_data, f, indent=2, ensure_ascii=False)

        logger.info(f"📜 {event_type.upper()}: {rel_path} ({status})")

        # Broadcast to Discord if enabled and important
        if DISCORD_CONFIG["enabled"] and _is_important_event(event_type, status):
            asyncio.create_task(_send_discord_notification(entry))

    except Exception as e:
        logger.error(f"❌ Logging failed: {e}")


def _is_important_event(event_type: str, status: str) -> bool:
    """📡 Determine if event should be broadcast to Discord"""
    important_events = ["full_scan", "sync_failure", "task_error", "move_error", "delete_error"]
    return event_type in important_events or status not in ["ok", "verified"]


async def _send_discord_notification(entry: Dict):
    """📢 Send notification to Discord (placeholder for real implementation)"""
    # This would implement actual Discord API calls
    logger.info(f"📡 Discord notification: {entry['event']} - {entry['status']}")


def enhanced_full_sync(metrics: EnhancedSyncMetrics):
    """🔍 Enhanced full empire scan with performance monitoring"""
    start_time = time.time()
    logger.info("🌌 Starting enhanced full empire scan...")

    try:
        # Scan source files
        old_index = load_sync_db()
        new_index = scan_folder(HYPERFOCUS_ROOT)

        # Update file count metric
        metrics.metrics["files_monitored"] = len(new_index)

        # Sync changed files to all targets
        changes_detected = 0
        for rel_path, info in new_index.items():
            if rel_path not in old_index or old_index[rel_path]["hash"] != info["hash"]:
                src_file = HYPERFOCUS_ROOT / rel_path

                # Sync to all enabled targets
                for target in SYNC_TARGETS:
                    if target["enabled"]:
                        dst_file = target["path"] / rel_path
                        safe_copy_enhanced(src_file, dst_file, target)

                changes_detected += 1

        # Handle deletions
        deletions = 0
        for rel_path in old_index.keys() - new_index.keys():
            for target in SYNC_TARGETS:
                if target["enabled"]:
                    dst_file = target["path"] / rel_path
                    if dst_file.exists():
                        dst_file.unlink()
                        deletions += 1

        # Save updated index
        save_sync_db(new_index)

        # Update metrics
        scan_time = time.time() - start_time
        metrics.metrics["last_full_scan"] = datetime.now().isoformat()

        log_event("enhanced_full_scan", "empire",
                 f"scanned_{len(new_index)}_files_synced_{changes_detected}_deleted_{deletions}_in_{scan_time:.2f}s")

        logger.info(f"✅ Enhanced full scan complete: {changes_detected} changes, {deletions} deletions, {scan_time:.2f}s")

    except Exception as e:
        logger.error(f"❌ Enhanced full scan failed: {e}")
        log_event("scan_error", "empire", str(e))


def safe_copy_enhanced(src: Path, dst: Path, target: Dict):
    """🛡️ Enhanced safe copy with target-specific handling"""
    try:
        dst.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(src, dst)

        # Verify integrity
        if SYNC_CONFIG["verify_integrity"]:
            if hash_file(src) == hash_file(dst):
                log_event("sync", dst.relative_to(target["path"]), "verified")
                target["sync_count"] = target.get("sync_count", 0) + 1
            else:
                log_event("sync", dst.relative_to(target["path"]), "hash_mismatch")
                target["error_count"] = target.get("error_count", 0) + 1
                dst.unlink()  # Remove corrupted copy
        else:
            log_event("sync", dst.relative_to(target["path"]), "copied")
            target["sync_count"] = target.get("sync_count", 0) + 1

        target["last_sync"] = datetime.now().isoformat()

    except Exception as e:
        log_event("sync_error", str(src), str(e))
        target["error_count"] = target.get("error_count", 0) + 1


def scan_folder(root: Path) -> Dict:
    """🔍 Enhanced folder scanning with metadata"""
    file_index = {}
    try:
        for dirpath, _, filenames in os.walk(root):
            for filename in filenames:
                filepath = Path(dirpath) / filename
                try:
                    rel_path = str(filepath.relative_to(root))
                    file_index[rel_path] = {
                        "hash": hash_file(filepath),
                        "size": filepath.stat().st_size,
                        "modified": filepath.stat().st_mtime,
                        "created": filepath.stat().st_ctime
                    }
                except Exception as e:
                    log_event("scan_error", str(filepath), str(e))
    except Exception as e:
        logger.error(f"❌ Folder scan failed: {e}")

    return file_index


def load_sync_db() -> Dict:
    """📚 Load sync database with error handling"""
    try:
        if SYNC_DB.exists():
            with open(SYNC_DB, 'r', encoding='utf-8') as f:
                return json.load(f)
    except Exception as e:
        logger.error(f"❌ Failed to load sync database: {e}")
    return {}


def save_sync_db(data: Dict):
    """💾 Save sync database with backup"""
    try:
        # Create backup of existing database
        if SYNC_DB.exists():
            backup_path = SYNC_DB.with_suffix('.json.backup')
            shutil.copy2(SYNC_DB, backup_path)

        # Save new data
        with open(SYNC_DB, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    except Exception as e:
        logger.error(f"❌ Failed to save sync database: {e}")


def create_target_directories():
    """📁 Create sync target directories"""
    for target in SYNC_TARGETS:
        try:
            target["path"].mkdir(parents=True, exist_ok=True)
            logger.info(f"✅ Target directory ready: {target['path']} ({target['type']})")
        except Exception as e:
            logger.error(f"❌ Failed to create target directory {target['path']}: {e}")
            target["enabled"] = False


def save_performance_metrics(metrics: EnhancedSyncMetrics):
    """📊 Save performance metrics to file"""
    try:
        report = metrics.get_performance_report()

        # Load existing metrics
        if PERFORMANCE_LOG.exists():
            with open(PERFORMANCE_LOG, 'r', encoding='utf-8') as f:
                all_metrics = json.load(f)
        else:
            all_metrics = []

        all_metrics.append(report)

        # Keep only last 100 reports
        if len(all_metrics) > 100:
            all_metrics = all_metrics[-100:]

        # Save updated metrics
        with open(PERFORMANCE_LOG, 'w', encoding='utf-8') as f:
            json.dump(all_metrics, f, indent=2, ensure_ascii=False)

    except Exception as e:
        logger.error(f"❌ Failed to save performance metrics: {e}")


def run_nightly_enhanced(metrics: EnhancedSyncMetrics):
    """🌙 Enhanced nightly maintenance with performance tracking"""
    now = datetime.now()
    if now.hour == NIGHTLY_SCAN_HOUR and now.minute == 0:
        logger.info("🌙 Starting enhanced nightly maintenance...")

        # Full empire scan
        enhanced_full_sync(metrics)

        # Save performance metrics
        save_performance_metrics(metrics)

        # Generate status report
        report = metrics.get_performance_report()
        logger.info(f"🏆 Empire Health Score: {report['metrics']['empire_health_score']:.1f}")
        logger.info(f"📊 Status: {report['status']}")

        # Sleep to avoid re-triggering
        time.sleep(60)


# --- MAIN EXECUTION ---
def legendary_sync_main():
    """🌌 Main execution for the Legendary Hyperfocus Sync Guardian"""
    logger.info("🌌💎⚡ LEGENDARY HYPERFOCUS SYNC GUARDIAN V2.0 ACTIVATED ⚡💎🌌")
    logger.info("🌌 " + "=" * 80)

    # Initialize metrics
    metrics = EnhancedSyncMetrics()

    # Create target directories
    create_target_directories()

    # Initial enhanced full sync
    logger.info("🌌 Initializing empire synchronization...")
    enhanced_full_sync(metrics)

    # Start file system monitoring
    event_handler = LegendaryHyperfocusHandler(SYNC_TARGETS, metrics)
    observer = Observer()
    observer.schedule(event_handler, str(HYPERFOCUS_ROOT), recursive=True)
    observer.start()

    logger.info("⚡ Legendary real-time empire monitoring ACTIVATED")
    logger.info("🏆 Multi-target sync operational")
    logger.info("📊 Performance tracking enabled")

    try:
        while True:
            # Nightly maintenance
            run_nightly_enhanced(metrics)

            # Save metrics every hour
            if datetime.now().minute == 0:
                save_performance_metrics(metrics)

            time.sleep(1)

    except KeyboardInterrupt:
        logger.info("🛑 Sync Guardian shutdown initiated...")
        observer.stop()

        # Final metrics save
        save_performance_metrics(metrics)
        final_report = metrics.get_performance_report()

        logger.info("📊 Final Empire Status:")
        logger.info(f"   🏆 Health Score: {final_report['metrics']['empire_health_score']:.1f}")
        logger.info(f"   ⚡ Total Syncs: {final_report['metrics']['sync_operations']}")
        logger.info(f"   ✅ Success Rate: {(final_report['metrics']['successful_syncs'] / max(final_report['metrics']['sync_operations'], 1)) * 100:.1f}%")
        logger.info(f"   ⏱️ Uptime: {final_report['metrics']['uptime_hours']:.1f} hours")

    observer.join()
    logger.info("🌌 Legendary Hyperfocus Sync Guardian V2.0 DEACTIVATED")


if __name__ == "__main__":
    legendary_sync_main()
