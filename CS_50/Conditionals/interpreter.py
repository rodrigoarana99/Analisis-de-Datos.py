def calculate_expression(x, operator, z):
    if operator == '+':
        return x + z
    elif operator == '-':
        return x - z
    elif operator == '*':
        return x * z
    elif operator == '/':
        if z == 0:
            raise ValueError("Cannot divide by zero")
        return x / z
    else:
        raise ValueError("Invalid operator")

def main():
    try:
        user_input = input("Enter an arithmetic expression (x y z): ")
        x, operator, z = user_input.split()
        x, z = int(x), int(z)
        result = calculate_expression(x, operator, z)
        print(f"Result: {result:.1f}")

    except ValueError as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()

