import sympy as sym
from sympy import symbols
from sympy.plotting import plot
# Función objetivo: Max(Z)=x1+x2
f1 = "10-x" #<=
f2 = "1+x" #<=
f3 = "4" #<=
Z1 = "16-x"
Z2 = "14-x"
Z3 = "13-x"
x = symbols('x')
plot(f1, f2, f3, Z1, Z2, Z3, (x, -1, 15))