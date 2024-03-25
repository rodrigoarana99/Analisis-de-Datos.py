import emoji 
def main():
    print(emojize("Python is :thumbs_up:")) 
    print(emojize("Python is :red_heart:"))

def emojize(text):
    return emoji.emojize(text) 

main()