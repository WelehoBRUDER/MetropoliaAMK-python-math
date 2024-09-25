import numpy as np
from sympy import symbols, solve
import matplotlib.pyplot as plt
x, y, z = symbols('x, y, z')
la = np.linalg

matrice_a = np.array(([-1, 2], [3, -5]))
matrice_b = np.array(([2, 0], [-1, 4]))

# 2A + 3B
matrice_sum = matrice_a * 2 + matrice_b * 3
print(f"Matriisi 2A+3B = \n{matrice_sum}")

# A - B
matrice_less = matrice_a - matrice_b
print(f"Matriisi A-B = \n{matrice_less}")

print("<------- Yhtälöryhmät ------->")
print("5x+3y=9\n2x+y=4")
print(f"V: {solve(
    [5*x + 3*y -9,
    2*x + y -4],
    [x, y])}")
print("2x+y+z=6\nx+3y+z=2\n2x+y+2z=9")
print(f"V: {solve(
    [2*x + y + z -6,
    x + 3*y + z -2,
     2*x + y + 2*z -9],
    [x, y, z])}")
print("x+y+3z=-1\n3x+y+z=5\n2x+y+2z=2")
print(f"V: {solve(
    [x + y + 3*z + 1,
    3*x + y + z -5,
     2*x + y + 2*z -2
     ],
    [x, y, z])}")

