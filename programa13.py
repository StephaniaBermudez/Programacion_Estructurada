#algoritmo para quitar la primer letra de una cadena y dejar el resto

def main():
    print("algoritmo para quitar la primer letra de una cadena y dejar el resto")
    string = str(input("Ingresa una palabra: "))
    print("La nueva palabra es: ", string[1:]," \n")
    
    
if __name__ == "__main__":
    main()