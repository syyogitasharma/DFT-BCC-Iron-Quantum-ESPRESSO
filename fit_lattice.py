
import numpy as np

# Data near the minimum
a = np.array([2.90, 2.92, 2.94])
E = np.array([
    -254.28850053,
    -254.28919064,
    -254.28872617
])

# Quadratic fitting
coeff = np.polyfit(a, E, 2)

# Position of minimum energy
a0 = -coeff[1] / (2 * coeff[0])
E0 = np.polyval(coeff, a0)

print(f"Equilibrium lattice parameter = {a0:.5f} Angstrom")
print(f"Minimum fitted energy = {E0:.8f} Ry")
