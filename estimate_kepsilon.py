U = 2
I = 0.05
Cmu = 0.09
l = 2*0.114

k = 1.5*(U*I)**2
epsilon = Cmu * k**(1.5)/l
nut = Cmu*(k**2)/epsilon

print("k: ", k)
print("epsilon: ", epsilon)
print("nut: ", nut)