def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

#“Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
       
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
main()