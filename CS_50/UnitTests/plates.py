def main():
    s= input("Escriba su placa: ")
    if is_valid(s):
        print("Placa válida")
    else:
        print("Placa inválida")


def is_valid(s):
    if len(s) >= 6:
        return False
    if len(s) <2:
        return False
    lista= [" ",",",".","-","_","/"]
    for i in s:
        if i in lista:
            return False
    if s[-2]== '0':
        return False    
    if s[-2:-1].isdigit():
        return True
    if s[0].isalpha() and s[1].isalpha():
        return True    
    else:
        return False


if __name__ == "__main__":
    main()