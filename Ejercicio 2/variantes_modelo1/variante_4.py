import sympy as sym
from sympy import symbols
from sympy.plotting import plot
# Función objetivo: Max(Z)=x
f1 = "10-x" #<=
f2 = "1+x" #<=
f3 = "4" #<=
x = symbols('x')
plot(f1, f2, f3, (x, -1, 15))