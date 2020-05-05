#inversa de una cadena

def main ():
    print("\nInversa de una cadena\n")
    string = input("ingresa la cadena: ")
    inverted = string[:: -1]#dos puntos dentro es para inicio o final en una cada 
    print("La cadena inversa es: ",inverted)
    

if __name__ == "__main__":
    main ()
    