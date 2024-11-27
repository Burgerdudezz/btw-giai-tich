import numpy as np
import matplotlib.pyplot as plt

# Given constants
v = 20  # speed in m/s
r = 50  # radius in meters
mass = 1000  # mass in kg

# Calculate centripetal acceleration and force
a_c = v**2 / r  # centripetal acceleration
F_c = mass * a_c  # centripetal force

print(f"Centripetal Acceleration: {a_c:.2f} m/s²")
print(f"Centripetal Force: {F_c:.2f} N")

# Generate data for varying radius and speed
radii = np.linspace(10, 100, 100)  # radii from 10m to 100m
speeds = np.linspace(10, 30, 100)  # speeds from 10 m/s to 30 m/s

# Calculate centripetal acceleration and force for varying radius
a_c_radii = v**2 / radii
F_c_radii = mass * a_c_radii

# Calculate centripetal force for varying speed (at constant radius)
a_c_speeds = speeds**2 / r
F_c_speeds = mass * a_c_speeds

# Plotting
plt.figure(figsize=(12, 6))

# Plot 1: Centripetal acceleration vs radius
plt.subplot(1, 2, 1)
plt.plot(radii, a_c_radii, label='Centripetal Acceleration (m/s²)', color='blue')
plt.xlabel('Radius (m)')
plt.ylabel('Acceleration (m/s²)')
plt.title('Centripetal Acceleration vs Radius')
plt.grid(True)
plt.legend()

# Plot 2: Centripetal force vs speed
plt.subplot(1, 2, 2)
plt.plot(speeds, F_c_speeds, label='Centripetal Force (N)', color='red')
plt.xlabel('Speed (m/s)')
plt.ylabel('Force (N)')
plt.title('Centripetal Force vs Speed')
plt.grid(True)
plt.legend()

# Show the plots
plt.tight_layout()
plt.show()
