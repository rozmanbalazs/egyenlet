#BALÁZS EZT MÉG NE HASZNÁLD MERT MŰKÖDIK DE ELVILEG SZAR


from sympy import symbols, solve
a=float(input("Szám1:"))
b=float(input("Szám2:"))
x=symbols('x')
expr = (x**2)+a+b
sol = solve(expr)

sol
print(sol)
