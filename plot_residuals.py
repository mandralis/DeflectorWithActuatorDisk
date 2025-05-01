import numpy as np
import matplotlib.pyplot as plt

# Path to your solverInfo file
fname = 'postProcessing/solverInfo/0/solverInfo.dat'

# Load columns: time (0), Ux_final (3), Uy_final (6), Uz_final (9), p_final (14)
time, Ux, Uy, Uz, p = np.loadtxt(
    fname,
    skiprows=2,
    usecols=(0, 3, 6, 9, 14),
    unpack=True
)

plt.figure()
plt.semilogy(time, Ux, label='Ux residual')
plt.semilogy(time, Uy, label='Uy residual')
plt.semilogy(time, Uz, label='Uz residual')
plt.semilogy(time, p,  label='p residual')
plt.xlabel('Time')
plt.ylabel('Residual (final)')
plt.legend()
plt.tight_layout()
plt.show()
