def main():
    paga = moneda(float(input("insetrte un cantidad de dinero:  ")))
    total= 0.50
    cambio= paga - total
    while paga < total:
        print("Inserte mas dinero")
        paga += moneda(float(input("insetrte un cantidad de dinero:  ")))
        cambio= round(paga - total,2)
    print(f"Su cambio es: {cambio}", "Su paga es: ", paga, "El total es: ", total)
    #return cambio, paga, total


def moneda(x):
    lista = [ 0.25,0.15,0.05]
    if x != lista[0] and x != lista[1] and x != lista[2]:
        print("Invalid input")
    else:
        return x    
main()