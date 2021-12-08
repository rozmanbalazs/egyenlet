import cmath
from gekko import GEKKO

def elso():
    print("---Elsőfokút választottál---")
    while True:
        try:
            print("Az egyenlet legyen 0-val egyenlő")
            a=float(input("Szám1:"))
            b=float(input("Szám2:"))
            
            if a != 0:
                break
                    
            elif a == 0.0 and b == 0.0:
                print("minden X megoldás.")
                raise SystemExit
            
                
        except ValueError:
            print("Hibás Érték")

    m = GEKKO()
    x = m.Var()

    m.Equation(a*x+b==0)
    m.solve(disp=False)
    print(f"az X értéke = {x.value}")
    
def masod():
    print("---Másodfokút választottál---")
    while True:
        try:
            a = float(input("Hány másodfokú x van? "))
            b = float(input("Hány x van? "))
            c = float(input("Mennyi a szám? "))
            
            if a == 0.0:
                elso()
                break
            
            elif b == 0.0:
                raise ValueError
            
            elif a != 0 or b != 0:
                break
                
            elif b == 0:
                m.Equation(a*x+b==0)
                m.solve(disp=False)



        except ValueError:
            print("Hibás Érték")
            

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
