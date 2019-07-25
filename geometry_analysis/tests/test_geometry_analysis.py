"""
Unit and regression test for the geometry_analysis package.
"""

# Import package, test suite, and other packages as needed
import geometry_analysis
import pytest
import sys
import numpy as np

def test_geometry_analysis_imported():
    """Sample test, will always pass so long as import statement worked"""
    assert "geometry_analysis" in sys.modules

def test_calculate_distance():
    """Test the calculate_distance function"""
    r1 = np.array([0, 0, -1])
    r2 = np.array([0, 1, 0])
    expected_distance = np.sqrt(2.)
    calculated_distance = geometry_analysis.calculate_distance(r1, r2)

    assert expected_distance == calculated_distance 

    def test_calculate_angle():
        """Test the calculate_angle function"""
        rA = np.array([0, 0, 1])
        rB = np.array([0, 1, 0])
        rC = np.array([1, 0, 0])
        expected_angle = 90
        calculated_angle = geometry_analysis.calculate_angle(rA, rB, rC)

        assert expected_angle == calculated_angle
