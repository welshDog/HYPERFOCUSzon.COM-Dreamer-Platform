-- HyperFocus Zone Neurodivergent Customizations
-- Optimized for ADHD, Autism, and Dyslexia users

-- Create initial admin user
INSERT IGNORE INTO `leantime_user` (
    `id`, `username`, `firstname`, `lastname`, `email`, `phone`, `password`,
    `role`, `status`, `clientId`, `notifications`, `created`, `modified`
) VALUES (
    1, 'hyperfocus_admin', 'HyperFocus', 'Admin', 'admin@hyperfocuszone.com', '',
    '$2y$10$92IXUNpkjO0rOQ5byMi.Ye4oKoEa3Ro9llC/.og/at2.uheWG/igi', -- password: 'password'
    'admin', 'active', 0, 1, NOW(), NOW()
);

-- Create ADHD-optimized project templates
INSERT IGNORE INTO `leantime_projects` (
    `name`, `details`, `clientId`, `hourBudget`, `assignedUsers`, `type`, `state`
) VALUES
('ADHD Hyperfocus Sprint', 'Short, intensive project bursts for ADHD brains', 0, 40, '', 'project', 1),
('Autism-Friendly Workflow', 'Structured, predictable project management', 0, 80, '', 'project', 1),
('Sensory-Safe Collaboration', 'Low-stimulation project environment', 0, 60, '', 'project', 1);

-- Create neurodivergent-friendly task categories
INSERT IGNORE INTO `leantime_ticketTypes` (
    `name`, `color`
) VALUES
('Hyperfocus Task', '#FF6B6B'),
('Break Reminder', '#4ECDC4'),
('Sensory Break', '#45B7D1'),
('Social Interaction', '#96CEB4'),
('Executive Function', '#FFEAA7'),
('Routine Check', '#DDA0DD');