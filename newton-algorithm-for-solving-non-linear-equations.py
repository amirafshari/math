import numpy as np
from sympy import symbols, diff, Symbol, Matrix, Array

# Define the variables
x, y, z = symbols('x y z')

# Inputs
e = 1e-5
X = [2.5, 0.25, 1.5]



for i in range(5):
    J = [  []  ,  []  ,  []  ]
    F = [x**2 + y**2 + z**2 - 9, x*y*z-1, x + y - z**2]
    # Jacobian == J(x)
    for i in range(3):
        for n in [x,y,z]:
            d = diff(F[i], n)  
            J[i].append(d.doit())
    # F(X) Value
    for i in range(3):
        F[i] = F[i].subs({x:X[0], y:X[1], z:X[2]})
        # J(X) Value
        for j in range(3):
            J[i][j] = J[i][j].subs({x:X[0], y:X[1], z:X[2]})

    # Solve Matrix Equation
    J = np.array(J, dtype=float)
    F = np.array(F, dtype=float)
    H = np.linalg.solve(J, -1*F)

    # Update X, X1, X2, ...
    X += H
    
