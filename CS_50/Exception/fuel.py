def main():
   print(fuel())
def fuel():
    while True:
        x = int(input('x: '))
        y = int(input('y: '))
        operacion = (x / y) 
        try:
            if operacion*100 > 99:
                return "F"
            elif operacion*100 < 1:
                return "E"
            else:
                print(f"{x}/"f"{y}")
                return round(operacion*100,2)
        except ZeroDivisionError:
            return "Error: Division by zero"
        except ValueError:
            return "Error: Invalid value"
main()    