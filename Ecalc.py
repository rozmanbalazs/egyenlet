import cmath
from sympy import symbols, solve

def elso():
    print("---Elsőfokút választottál---")
    while True:
        try:
            a=float(input("Szám1:"))
            b=float(input("Szám2:"))
            break

        except ValueError:
            print("Hibás érték")

    x=symbols('x')
    expr = x+(a+b)*-1
    sol = solve(expr)

    sol
    print("x = "+str(sol))
    
def masod():
    print("---Másodfokút választottál---")
    while True:
        try:
            a = float(input("Hány másodfokú x van? "))
            b = float(input("Hány x van? "))
            c = float(input("Mennyi a szám? "))
            break
        
        except ValueError:
            print("Hibás Érték")
            
    d = (b**2) - (4*a*c)

    sol1 = (-b-cmath.sqrt(d))/(2*a)
    sol2 = (-b+cmath.sqrt(d))/(2*a)

    print('A megoldások a következők: {0} és {1}'.format(sol1,sol2))

while True:
    try:
        print("<--- Mód választás --->")
        mode_select = int(input("Elsőfokú - 0, Másodfokú - 1\n input: "))

        if mode_select == 0 or mode_select == 1:
            break

        else:
            raise ValueError

    except ValueError:
        print("\nhibás Érték (csak 0, 1 et használj)")


if mode_select == 0:
    elso()

elif mode_select == 1:
    masod()