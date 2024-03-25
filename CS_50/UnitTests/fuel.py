def main():
    fraction = input("Enter a fraction in X/Y format: ")
    percentage = convert(fraction)
    print(f"The percentage is: {percentage}")
    number = int(input("Enter a number: "))
    result = gauge(number)
    print(f"The gauge result is: {result}")


def convert(fraction):
    x,y= fraction.split("/")
    x= int(x)
    y= int(y)
    if x > y:
        raise ValueError("X should not be greater than Y")
    elif y == 0:
        raise ZeroDivisionError("Y should not be 0")
    else:
        
        percentage = round(x / y * 100)
    return max(0, min(100, percentage))
    


def gauge(percentage):
    if percentage < 1:
        return "E"
    elif percentage >= 99:
        return "F"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()