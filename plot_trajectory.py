import numpy as np
import matplotlib.pyplot as plt
from harmonic_oscillator import HarmonicOscillator

def main():
    mass = 1.0
    spring_constant = 4.0
    oscillator = HarmonicOscillator(mass, spring_constant)
    omega = oscillator.angular_frequency()
    amplitude = 5.0
    phase = 0.0

    # Generate time values from 0 to 2 seconds
    t = np.linspace(0, 2, 200)
    # Calculate displacement for each time value
    x = [oscillator.displacement(amplitude, t_val, phase) for t_val in t]

    plt.figure(figsize=(8, 4))
    plt.plot(t, x, label=f'Amplitude={amplitude}, ω={omega:.2f}')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Harmonic Oscillator Trajectory')
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
