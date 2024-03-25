x= input("insterte su archivo: ")
if  x.endswith ( ".gif")  or  x.endswith(".jpg") or x.endswith(".png") or x.endswith(".jpeg") or  x.endswith(".pdf") or x.endswith("txt"):
        x=x.replace(".","/")
        print(x)
else:
        print("no es un archivo valido")

    
