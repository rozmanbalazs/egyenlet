#BALÁZS EZT MÉG NE HASZNÁLD MERT MŰKÖDIK DE ELVILEG SZAR
#NEM TUDOM ÓRÁN TESZTELNI, ÍGY JÓ LEHET



from sympy import symbols, solve
import math
a=float(input("Szám1:"))
b=float(input("Szám2:"))
x=symbols('x')
expr1 = (x**2)+a+b
expr = math.sqrt(expr)
sol = solve(expr)

sol
print(sol)
