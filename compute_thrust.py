import pandas as pd
import numpy as np
import os

# Paths to postProcessing data
above_path = "postProcessing/pAbove/0/volFieldValue_0.dat"
below_path = "postProcessing/pBelow/0/volFieldValue_0.dat"

# Load the data
above_df = pd.read_csv(above_path, delim_whitespace=True, comment="#", names=["Time", "pAbove"])
below_df = pd.read_csv(below_path, delim_whitespace=True, comment="#", names=["Time", "pBelow"])

# Merge on Time
merged = pd.merge(above_df, below_df, on="Time")

# Compute pressure difference and thrust
vi = 1.0
radius = 0.114  # in meters
rho = 1.225  # kg/m^3, air density at sea level
area = np.pi * radius ** 2
merged["deltaP"] = merged["pBelow"] - merged["pAbove"]
merged["Thrust"] = rho * merged["deltaP"] * area  # need to mutiply by density since kinematic pressure
merged["Thrust_AD"] = 2 * rho * area * vi**2 # need to mutiply by density since kinematic pressure

# Output to file
output_dir = "postProcessing/actuatorThrustDelta/0"
os.makedirs(output_dir, exist_ok=True)
output_file = os.path.join(output_dir, "thrustFromDeltaP.dat")
merged.to_csv(output_file, sep="\t", index=False)

print(f"\n✅ Thrust computed and saved to: {output_file}")
print(merged.tail())
