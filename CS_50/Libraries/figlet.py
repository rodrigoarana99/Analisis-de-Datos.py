import sys
import random
import pyfiglet

def display_text(text, font=None):
    if font:
        figlet_text = pyfiglet.figlet_format(text, font=font)
    else:
        figlet_text = pyfiglet.figlet_format(text)
    print(figlet_text)

def main():
    if len(sys.argv) == 1:
        text = input("Enter the text to display: ")
        display_text(text)
    elif len(sys.argv) == 3 and (sys.argv[1] == '-f' or sys.argv[1] == '--font'):
        font = sys.argv[2]
        text = input("Enter the text to display: ")
        display_text(text, font)
    else:
        print("Usage:")
        print("To display text in a random font: python figlet.py")
        print("To display text in a specific font: python figlet.py -f <font_name>")
        sys.exit(1)

if __name__ == "__main__":
    main()
