import numpy as np
import matplotlib.pyplot as plt

# Path to your forces.dat file
file_path = "postProcessing/deflectorForce/0/force.dat"

# Lists to store time and force values
time = []
total_y = []

# Read the file
with open(file_path, 'r') as f:
    for line in f:
        # Skip header lines
        if line.strip().startswith('#') or line.strip() == '':
            continue
        parts = line.strip().split()
        time.append(float(parts[0]))
        total_y.append(float(parts[2]))  # total_y is the 2nd column (0-indexed)

# Convert to NumPy arrays
time = np.array(time)
total_y = -np.array(total_y)

print(f"Deflector Force: {total_y[-1]:.4f} N")

# Plotting the y-component of the total force
plt.figure(figsize=(8, 5))
plt.plot(time, total_y, linestyle='-')
plt.xlabel('Time [s]')
plt.ylabel('Total Force in y [N]')
plt.title('Deflector Total Force (y-component) Over Time')
plt.grid(True)
plt.tight_layout()
plt.show()

# # Define the time after which to compute the average (after transient)
# transient_cutoff = 100
# steady_indices = time > transient_cutoff
# avg_total_y = np.mean(total_y[steady_indices])

# print(f"Average total_y after t = {transient_cutoff} s: {avg_total_y:.6e} N")
