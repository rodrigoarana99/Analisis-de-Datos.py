def main():
    x= input("Enter the time: ")
    if 7< convert(x) < 10:
        print("Breakfast")
    elif 10<convert(x)<15:
        print("Lunch")
    else:
        print("Dinner")    

def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

if __name__ == "__main__":
    main()






