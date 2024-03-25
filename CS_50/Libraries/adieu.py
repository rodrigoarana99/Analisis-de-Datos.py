import inflect
from inflect import engine


def main():
    names()

def names():
    p = inflect.engine()
    lista = []
    while True:
        x = input("Escribe un nombre: ")
        if x == "":
            break
        lista.append(x)
        print(f"Adieu!, Adieu! to {p.join(lista)}")
    print(lista)

main()
   