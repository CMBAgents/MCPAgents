import math
import pytest
from harmonic_oscillator import HarmonicOscillator

def test_angular_frequency():
    ho = HarmonicOscillator(mass=1.0, spring_constant=4.0)
    # Expected angular frequency: sqrt(4.0/1.0) = 2.0
    assert math.isclose(ho.angular_frequency(), 2.0)

def test_displacement():
    ho = HarmonicOscillator(mass=1.0, spring_constant=4.0)
    amplitude = 5
    time_value = math.pi / 4
    phase = 0
    # Expected displacement: 5*cos(omega * time_value + phase)
    # where omega = 2, so 5*cos(2*(pi/4)) = 5*cos(pi/2) = 0
    assert math.isclose(ho.displacement(amplitude, time_value, phase), 0, abs_tol=1e-7)
