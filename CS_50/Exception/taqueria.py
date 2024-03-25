precios ={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    taqueria()

def taqueria():
    lista = []
    total = 0
    try:
        while True:
            x = input("Pedido?: ").strip().title()  
            if x == "Salir": 
                break
            if x in precios:
                lista.append(x)  
                total += precios[x]  
                print(f"Total hasta ahora: ${total:.2f}") 
            else:
                print("Lo siento, ese artículo no está en el menú.") 

    except EOFError:
        pass

    print("\n¡Gracias por tu pedido!")
    print("Artículos ordenados:")
    for item in lista:
        print(item)
main()