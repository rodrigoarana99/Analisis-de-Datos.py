import random
def main():
    game()
def game ():
    x= random.randint(1,10)
    y= int(input("Adivina el número: "))
    while True:
        if y == x:
            print("Felicidades, adivinaste el número")
            break
        if y > x:
            y= int(input("El número es más pequeño: "))
        else:
            y= int(input("El número es más grande: "))
main()