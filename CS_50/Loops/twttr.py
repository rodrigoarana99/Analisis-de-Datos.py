#x= input("insterte su twett: ")
#lista= ["a","e","i","o","u"]
#for i in x:
 #   while i in lista:
  #     x= x.replace(i, "")	
   #    ouput= x
    #   print(ouput)
     #  break
#else:
#    print(x)

def remove_vowels(text):
    vowels = "aeiouAEIOU"
    text_without_vowels = ''.join(char for char in text if char not in vowels)
    return text_without_vowels

# Get input from the user
text_input = input("Enter a text string: ")

# Remove vowels from the text
text_without_vowels = remove_vowels(text_input)

# Display the result
print(f"The text without vowels is: {text_without_vowels}")
