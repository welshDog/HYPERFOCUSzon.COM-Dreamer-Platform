BEGIN TRANSACTION;
CREATE TABLE mood_trends (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        user_id TEXT NOT NULL,
                        trend_period TEXT NOT NULL,
                        avg_mood REAL,
                        mood_variance REAL,
                        pattern_detected TEXT,
                        recommendations TEXT,
                        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    );
CREATE TABLE schema_version (
                    version TEXT PRIMARY KEY,
                    applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                );
DELETE FROM "sqlite_sequence";
COMMIT;
