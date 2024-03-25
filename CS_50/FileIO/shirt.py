import sys
from PIL import Image, ImageOps
import os

def main():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments ")
    if  len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    else:
        format = [".jpg", ".jpeg", ".png"]
        inp = os.path.splitext(sys.argv[1])
        outp = os.path.splitext(sys.argv[2])
        if outp[1].lower() not in format:
            sys.exit("Invalid output")
        elif inp[1].lower() != outp[1].lower():
            sys.exit("Input and output have different extensions")
        else:
            imagen(sys.argv[1], sys.argv[2])

def imagen(input, output):
    shirt = Image.open("shirt.jpg")
    with Image.open(input) as input:
            input_cropped = ImageOps.fit(input, shirt.size)
            input_cropped.paste(shirt, mask = shirt)
            input_cropped.save(output)

if __name__ == "__main__":
    main()   