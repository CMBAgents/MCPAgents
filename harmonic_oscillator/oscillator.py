import math

class HarmonicOscillator:
    """
    A class representing a simple harmonic oscillator.
    """

    def __init__(self, mass: float, spring_constant: float):
        """
        Initialize the harmonic oscillator with mass and spring constant.
        """
        self.mass = mass
        self.spring_constant = spring_constant

    def angular_frequency(self) -> float:
        """
        Calculate and return the angular frequency.
        ω = sqrt(k/m)
        """
        return math.sqrt(self.spring_constant / self.mass)

    def displacement(self, amplitude: float, time: float, phase: float = 0) -> float:
        """
        Calculate and return the displacement at a given time.
        x(t) = A cos(ωt + φ)
        """
        omega = self.angular_frequency()
        return amplitude * math.cos(omega * time + phase)
