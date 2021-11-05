import sympy as sym

def elso():
    print("---Írd be az első fokú egyenletedet---")
    print("Egyenlet beviteli példa: 2*x+6-5,6")
    print("A példa értéke: 2x+6-5=6")

    while True:
        try:
            raw_egyenlet_input = input("Egyenlet: ")
            
            
            symbol = sym.symbols('x y a b c')
            eq1 = sym.Eq( raw_egyenlet_input)

            result = sym.solve(eq1,symbol)
            result = str(result)[1:-1]
            print(f"a megoldás X = {result}")

        except ValueError:
            print("Hibás egyenlet")
    
def masod():
    print("teszt1")

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
