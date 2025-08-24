-- 🌌♾️⚡ HYPERFOCUS EMPIRE DATABASE INITIALIZATION ⚡♾️🌌
-- Ultra-Thinking Boardroom Strategic Database Schema
-- Powered by: PostgreSQL Excellence

-- Create extensions
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pg_stat_statements";

-- Strategic Decisions Table
CREATE TABLE IF NOT EXISTS strategic_decisions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    decision_id VARCHAR(255) UNIQUE NOT NULL,
    title VARCHAR(500) NOT NULL,
    description TEXT NOT NULL,
    priority VARCHAR(50) DEFAULT 'medium',
    status VARCHAR(50) DEFAULT 'pending',
    ai_recommendations JSONB,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    created_by VARCHAR(255),
    assigned_to VARCHAR(255)
);

-- Empire Systems Table
CREATE TABLE IF NOT EXISTS empire_systems (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    system_name VARCHAR(255) UNIQUE NOT NULL,
    system_type VARCHAR(100) NOT NULL,
    health_status DECIMAL(5,2) DEFAULT 0.0,
    performance_metrics JSONB,
    configuration JSONB,
    last_health_check TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Team Members Table
CREATE TABLE IF NOT EXISTS team_members (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    username VARCHAR(255) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    role VARCHAR(100) NOT NULL,
    permissions JSONB,
    last_login TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    is_active BOOLEAN DEFAULT true
);

-- Strategic Sessions Table
CREATE TABLE IF NOT EXISTS strategic_sessions (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    session_name VARCHAR(255) NOT NULL,
    session_type VARCHAR(100) NOT NULL,
    participants JSONB,
    decisions_made INTEGER DEFAULT 0,
    outcomes JSONB,
    session_data JSONB,
    started_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    ended_at TIMESTAMP WITH TIME ZONE,
    created_by UUID REFERENCES team_members(id)
);

-- Performance Metrics Table
CREATE TABLE IF NOT EXISTS performance_metrics (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    metric_name VARCHAR(255) NOT NULL,
    metric_value DECIMAL(15,4) NOT NULL,
    metric_unit VARCHAR(50),
    system_id UUID REFERENCES empire_systems(id),
    tags JSONB,
    recorded_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- Activity Logs Table
CREATE TABLE IF NOT EXISTS activity_logs (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    event_type VARCHAR(100) NOT NULL,
    event_description TEXT,
    user_id UUID REFERENCES team_members(id),
    system_id UUID REFERENCES empire_systems(id),
    event_data JSONB,
    severity VARCHAR(20) DEFAULT 'info',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW()
);

-- AI Recommendations Table
CREATE TABLE IF NOT EXISTS ai_recommendations (
    id UUID PRIMARY KEY DEFAULT uuid_generate_v4(),
    decision_id UUID REFERENCES strategic_decisions(id),
    recommendation_text TEXT NOT NULL,
    confidence_score DECIMAL(3,2),
    ai_model VARCHAR(100),
    recommendation_type VARCHAR(100),
    implementation_status VARCHAR(50) DEFAULT 'pending',
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW(),
    implemented_at TIMESTAMP WITH TIME ZONE
);

-- Create indexes for performance
CREATE INDEX IF NOT EXISTS idx_strategic_decisions_status ON strategic_decisions(status);
CREATE INDEX IF NOT EXISTS idx_strategic_decisions_priority ON strategic_decisions(priority);
CREATE INDEX IF NOT EXISTS idx_strategic_decisions_created_at ON strategic_decisions(created_at);
CREATE INDEX IF NOT EXISTS idx_empire_systems_health ON empire_systems(health_status);
CREATE INDEX IF NOT EXISTS idx_performance_metrics_recorded_at ON performance_metrics(recorded_at);
CREATE INDEX IF NOT EXISTS idx_activity_logs_event_type ON activity_logs(event_type);
CREATE INDEX IF NOT EXISTS idx_activity_logs_created_at ON activity_logs(created_at);

-- Create triggers for updated_at
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = NOW();
    RETURN NEW;
END;
$$ language 'plpgsql';

CREATE TRIGGER update_strategic_decisions_updated_at BEFORE UPDATE ON strategic_decisions FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_empire_systems_updated_at BEFORE UPDATE ON empire_systems FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();
CREATE TRIGGER update_team_members_updated_at BEFORE UPDATE ON team_members FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Insert initial empire systems
INSERT INTO empire_systems (system_name, system_type, health_status, configuration) VALUES
    ('Ultra-Thinking-Boardroom', 'command_center', 95.0, '{"windsurf_enabled": true, "ai_powered": true}'),
    ('API-Gateway', 'api_service', 90.0, '{"auth_enabled": true, "rate_limiting": true}'),
    ('PostgreSQL-Database', 'database', 98.0, '{"backup_enabled": true, "replication": false}'),
    ('Redis-Cache', 'cache', 92.0, '{"memory_limit": "256mb", "persistence": true}'),
    ('RabbitMQ-Queue', 'message_queue', 88.0, '{"ha_enabled": false, "disk_free_limit": "1GB"}'),
    ('MinIO-Storage', 'file_storage', 85.0, '{"bucket_auto_create": true, "versioning": true}'),
    ('Prometheus-Monitoring', 'monitoring', 87.0, '{"retention": "200h", "scrape_interval": "15s"}'),
    ('Grafana-Dashboard', 'visualization', 90.0, '{"auto_provisioning": true, "alerting": true}')
ON CONFLICT (system_name) DO UPDATE SET
    health_status = EXCLUDED.health_status,
    updated_at = NOW();

-- Insert default admin user
INSERT INTO team_members (username, email, role, permissions) VALUES
    ('empire_admin', 'admin@hyperfocus.zone', 'LEGENDARY_CHIEF_STRATEGIST',
     '{"strategic_decisions": "full", "system_management": "full", "team_management": "full"}'),
    ('ai_assistant', 'ai@hyperfocus.zone', 'AI_INTELLIGENCE_AMPLIFIER',
     '{"strategic_decisions": "read", "ai_recommendations": "full", "analytics": "full"}')
ON CONFLICT (username) DO NOTHING;

-- Insert sample strategic decision
INSERT INTO strategic_decisions (decision_id, title, description, priority, ai_recommendations) VALUES
    ('decision_init_001',
     'Deploy Full Empire Stack Architecture',
     'Complete deployment of multi-service architecture with databases, APIs, and monitoring for ultimate empire excellence',
     'critical',
     '["🚀 Implement container orchestration", "📊 Set up comprehensive monitoring", "🔒 Enable security protocols", "⚡ Optimize performance metrics"]')
ON CONFLICT (decision_id) DO NOTHING;

-- Create views for reporting
CREATE OR REPLACE VIEW empire_health_summary AS
SELECT
    COUNT(*) as total_systems,
    AVG(health_status) as average_health,
    MIN(health_status) as min_health,
    MAX(health_status) as max_health,
    COUNT(*) FILTER (WHERE health_status >= 90) as healthy_systems,
    COUNT(*) FILTER (WHERE health_status < 70) as critical_systems
FROM empire_systems;

CREATE OR REPLACE VIEW strategic_decision_summary AS
SELECT
    status,
    priority,
    COUNT(*) as decision_count,
    AVG(EXTRACT(EPOCH FROM (NOW() - created_at))/3600) as avg_age_hours
FROM strategic_decisions
GROUP BY status, priority;

-- Grant permissions
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO empire_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO empire_user;
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO empire_user;

COMMIT;
