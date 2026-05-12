# test_prometheusmonitor.py
"""
Tests for PrometheusMonitor module.
"""

import unittest
from prometheusmonitor import PrometheusMonitor

class TestPrometheusMonitor(unittest.TestCase):
    """Test cases for PrometheusMonitor class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = PrometheusMonitor()
        self.assertIsInstance(instance, PrometheusMonitor)
        
    def test_run_method(self):
        """Test the run method."""
        instance = PrometheusMonitor()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
