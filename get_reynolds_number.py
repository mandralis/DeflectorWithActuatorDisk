import numpy as np 

# Re = U c / nu where c is the typical chord length 
nu = 1.5e-5  # at 20 degrees
R  = 0.1016
r  = 0.75 * R
omega = 4000 / 60 * 2 * np.pi
U     = omega * r 
c     = 0.025
Re    = U * c / nu

print("Re: ", Re)

