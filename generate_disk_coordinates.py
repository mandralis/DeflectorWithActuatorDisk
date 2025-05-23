import numpy as np
from numpy import cos, sin

thrust = 1.0
rho = 1.225

disk_thickness     = 0.005
thickness_range    = [0.006,0.01]

phi      = np.deg2rad(90)
l        = 0.1648
dy_prop  = 0.0564
dy       = 0.0385
dx       = 0.0091
R        = 0.1016

# incorporate deflector rotation
pivot    = np.array([-0.0784,0.0805])
th       = np.deg2rad(10)
R        = np.array([[cos(-th),-sin(-th)],
                     [sin(-th), cos(-th)]])
delta    = R @ -pivot + pivot

print("delta: ", delta)

d1 = R @ (-pivot + dy * np.array([0,-1])) + pivot
n  = R @ (l * np.array([np.cos(phi),np.sin(phi)]))
d2 = R @ (dy_prop * np.array([np.sin(phi),-np.cos(phi)]))

p       = d1 + n + d2
p_top   = p + d2 / dy_prop * disk_thickness
p_base  = p - d2 / dy_prop * disk_thickness

p_above_base = p + d2 / dy_prop * thickness_range[0]
p_above_top  = p + d2 / dy_prop * thickness_range[1]

p_below_top   = p - d2 / dy_prop * thickness_range[0]
p_below_base  = p - d2 / dy_prop * thickness_range[1]

d2hat = d2/np.linalg.norm(d2)
print("-d2hat: ", -d2hat)

print("p: ",p)
print("p_top: ",p_top)
print("p_base: ",p_base)

print("p_above_base: ",p_above_base)
print("p_above_top: ",p_above_top)
print("p_below_base: ",p_below_base)
print("p_below_top: ",p_below_top)

V = 2*disk_thickness*np.pi*R**2
print("Volume of actuator disk: ", V)
print("Force per unit volume per unit density (acceleration): ", thrust*d2hat/(V*rho))


