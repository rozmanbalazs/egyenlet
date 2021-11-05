from operator import eq
from sympy import symbols, Eq, solve
a=float(input("Szám1: "))
b=float(input("Szám2: "))
x = symbols('x')
eq1 = Eq(x*2 +a*x + b)
Eq(x, 0)

sol = solve(eq1, dict=True)
sol
print(eq)