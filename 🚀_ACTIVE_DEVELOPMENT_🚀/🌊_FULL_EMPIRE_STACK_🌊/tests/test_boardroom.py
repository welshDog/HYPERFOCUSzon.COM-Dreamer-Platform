"""
🧪 Test Suite for Ultra-Thinking Boardroom
Tests for the HyperFocus Zone Empire core functionality
"""

import sys
from pathlib import Path

import pytest

# Add core directory to path for testing
core_path = Path(__file__).parent.parent / "core"
sys.path.insert(0, str(core_path))

from ultra_thinking_boardroom_local import UltraThinkingBoardroom


class TestUltraThinkingBoardroom:
    """Test cases for Ultra-Thinking Boardroom functionality"""

    def setup_method(self):
        """Set up test environment"""
        self.boardroom = UltraThinkingBoardroom()

    def test_initialization(self):
        """Test boardroom initialization"""
        assert self.boardroom.empire_mode == "ULTRA_LEGENDARY"
        assert self.boardroom.status == "OPERATIONAL"
        assert self.boardroom.windsurf_key is not None
        assert len(self.boardroom.windsurf_key) > 0

    def test_status_command(self):
        """Test status command response"""
        response = self.boardroom.process_command("status")
        assert "Empire Status" in response
        assert "operational" in response.lower()

    def test_windsurf_command(self):
        """Test windsurf AI integration command"""
        response = self.boardroom.process_command("windsurf")
        assert "Windsurf AI Integration" in response
        assert "ACTIVE" in response

    def test_empire_command(self):
        """Test empire infrastructure command"""
        response = self.boardroom.process_command("empire")
        assert "Empire Infrastructure" in response
        assert "Ultra-Thinking Boardroom" in response

    def test_help_command(self):
        """Test help command provides command list"""
        response = self.boardroom.process_command("help")
        assert "COMMANDS" in response
        assert "status" in response
        assert "windsurf" in response
        assert "empire" in response

    def test_deploy_command(self):
        """Test deployment capabilities command"""
        response = self.boardroom.process_command("deploy")
        assert "DEPLOYMENT CAPABILITIES" in response
        assert "Docker" in response
        assert "Local Development" in response

    def test_ai_command(self):
        """Test AI thinking capabilities command"""
        response = self.boardroom.process_command("ai")
        assert "AI THINKING CAPABILITIES" in response
        assert "Strategic Planning" in response

    def test_unknown_command(self):
        """Test unknown command handling"""
        response = self.boardroom.process_command("unknown_command")
        assert "Unknown command" in response
        assert "unknown_command" in response
        assert "help" in response

    def test_case_insensitive_commands(self):
        """Test commands are case insensitive"""
        response_lower = self.boardroom.process_command("status")
        response_upper = self.boardroom.process_command("STATUS")
        response_mixed = self.boardroom.process_command("StAtUs")

        assert response_lower == response_upper == response_mixed

    def test_command_trimming(self):
        """Test commands handle whitespace properly"""
        response_normal = self.boardroom.process_command("status")
        response_spaces = self.boardroom.process_command("  status  ")

        assert response_normal == response_spaces

    def test_empty_command(self):
        """Test empty command handling"""
        response = self.boardroom.process_command("")
        assert "Unknown command" in response


class TestBoardroomPerformance:
    """Performance tests for Ultra-Thinking Boardroom"""

    def setup_method(self):
        """Set up performance test environment"""
        self.boardroom = UltraThinkingBoardroom()

    def test_command_response_time(self, benchmark):
        """Benchmark command response time"""

        def run_status_command():
            return self.boardroom.process_command("status")

        result = benchmark(run_status_command)
        assert "Empire Status" in result

    def test_initialization_time(self, benchmark):
        """Benchmark boardroom initialization"""

        def create_boardroom():
            return UltraThinkingBoardroom()

        boardroom = benchmark(create_boardroom)
        assert boardroom.empire_mode == "ULTRA_LEGENDARY"

    def test_multiple_commands_performance(self):
        """Test performance with multiple rapid commands"""
        import time

        commands = ["status", "windsurf", "empire", "help", "deploy", "ai"] * 10
        start_time = time.time()

        for command in commands:
            response = self.boardroom.process_command(command)
            assert len(response) > 0

        end_time = time.time()
        total_time = end_time - start_time

        # Should handle 60 commands in under 1 second
        assert total_time < 1.0

        # Average response time should be under 10ms
        avg_time = total_time / len(commands)
        assert avg_time < 0.01


class TestBoardroomAccessibility:
    """Accessibility tests for neurodivergent users"""

    def setup_method(self):
        """Set up accessibility test environment"""
        self.boardroom = UltraThinkingBoardroom()

    def test_clear_command_responses(self):
        """Test responses are clear and structured"""
        response = self.boardroom.process_command("help")

        # Should have clear structure with bullet points or numbering
        assert "•" in response or "-" in response or "1." in response

        # Should not be too long (ADHD-friendly)
        lines = response.split("\n")
        assert len(lines) < 20

    def test_consistent_formatting(self):
        """Test consistent emoji and formatting across commands"""
        commands = ["status", "windsurf", "empire", "help", "deploy", "ai"]

        for command in commands:
            response = self.boardroom.process_command(command)

            # Should have emoji indicators
            emoji_count = sum(1 for char in response if ord(char) > 127)
            assert emoji_count > 0, f"Command '{command}' lacks visual indicators"

    def test_predictable_responses(self):
        """Test responses are predictable and consistent"""
        # Same command should always return same response
        response1 = self.boardroom.process_command("status")
        response2 = self.boardroom.process_command("status")

        # Content should be identical (allowing for timestamp differences)
        assert "Empire Status" in response1
        assert "Empire Status" in response2


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
