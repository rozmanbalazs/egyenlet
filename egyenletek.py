import sympy as sym

def elso():
    
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
