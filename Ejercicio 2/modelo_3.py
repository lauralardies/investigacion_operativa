import sympy as sym
from sympy import symbols
from sympy.plotting import plot
# Función objetivo: Max(Z)=x1+2x2
f1 = "10-x" #<=
f2 = "x+1" #<=
f3 = "x-1" #>=
f4 = "4" # <=
x = symbols('x')
plot(f1, f2, f3, f4, (x, 15, 0))