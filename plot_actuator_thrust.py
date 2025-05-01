import numpy as np
import matplotlib.pyplot as plt

# File paths (adjust if needed)
file_below = 'postProcessing/pBelow/0/volFieldValue.dat'
file_above = 'postProcessing/pAbove/0/volFieldValue.dat'

# Function to load time and average pressure data from a volFieldValue.dat file
def load_data(filename):
    times = []
    pressures = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith('#'):
                parts = line.split()
                times.append(float(parts[0]))
                pressures.append(float(parts[1]))
    return np.array(times), np.array(pressures)

# Load data
time_below, p_below = load_data(file_below)
time_above, p_above = load_data(file_above)

# Ensure time arrays match
if not np.allclose(time_below, time_above):
    raise ValueError("Time steps in above and below files do not match.")

time = time_below

# Constants
rho = 1.225  # kg/m^3
A = np.pi * 0.1016**2  # m^2

# Compute force
force = -(p_below - p_above) * rho * A

# Compute average force after 150 seconds
# mask = time >= 150
# if np.any(mask):
#     avg_force_after_150 = np.mean(force[mask])
#     print(f"Average force for t ≥ 150 s: {avg_force_after_150:.4f} N")
# else:
#     print("No data points at or beyond 150 seconds to compute average.")
print(f"Actuator Thrust: {force[-1]:.4f} N")

# Plot
plt.figure()
plt.plot(time, force, label='Force')
# if np.any(mask):
    # plt.hlines(avg_force_after_150, time.min(), time.max(), linestyles='--', label=f'Avg (t ≥ 150s): {avg_force_after_150:.2f} N')
plt.xlabel('Time (s)')
plt.ylabel('Force (N)')
plt.title('Actuator Disk Force over Time')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
