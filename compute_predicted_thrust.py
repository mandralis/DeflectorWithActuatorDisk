import numpy as np

vi  = 3.5
rho = 1.225
R   = 0.1016
A   = np.pi * R**2

T = 2 * rho * A * vi**2

print("T: ", T)

dp_0  = 2951.63                 # without relaxation
dp_60 = 4583.43                 # with relaxation 0.9
dp_90 = 3179.94                 # with relaxation 0.9
V     = 0.00032429278662239857

print("T_num_0: ", dp_0 * V)
print("T_num_60: ", dp_60 * V)
print("T_num_90: ", dp_90 * V)