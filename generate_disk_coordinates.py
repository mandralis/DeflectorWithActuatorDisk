import numpy as np

disk_thickness     = 0.005
thickness_range    = [0.006,0.008]


l  = 0.1648
dy_prop = 0.0564
dy = 0.0385
dx = 0.0091
R  = 0.1016

phi = np.deg2rad(0)

d1 = dy * np.array([0,-1])
n  = l * np.array([np.cos(phi),np.sin(phi)])
d2 = dy_prop * np.array([np.sin(phi),-np.cos(phi)])

p       = d1 + n + d2
p_top   = p + d2 / dy_prop * disk_thickness
p_base  = p - d2 / dy_prop * disk_thickness

p_above_base = p + d2 / dy_prop * thickness_range[0]
p_above_top  = p + d2 / dy_prop * thickness_range[1]

p_below_top   = p - d2 / dy_prop * thickness_range[0]
p_below_base  = p - d2 / dy_prop * thickness_range[1]


print("p: ",p)
print("p_top: ",p_top)
print("p_base: ",p_base)

print("Volume of actuator disk: ", 2*disk_thickness*np.pi*R**2)

print("p_above_base: ",p_above_base)
print("p_above_top: ",p_above_top)
print("p_below_base: ",p_below_base)
print("p_below_top: ",p_below_top)

