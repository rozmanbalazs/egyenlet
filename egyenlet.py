from sympy import symbols, solve
a=float(input("Szám1:"))
b=float(input("Szám2:"))
x=symbols('x')
expr = x+a+b
sol = solve(expr)

sol
print(sol)