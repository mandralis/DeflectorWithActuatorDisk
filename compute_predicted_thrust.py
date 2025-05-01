import numpy as np

vi  = 3.5
rho = 1.225
R   = 0.1016
A   = np.pi * R**2

T = 2 * rho * A * vi**2

print("T: ", T)

dp = 2951.63
V  = 0.00032429278662239857

print("T_num: ", dp * V)