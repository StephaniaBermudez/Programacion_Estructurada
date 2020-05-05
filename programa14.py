#algoritmo que quite la primera y ultima linea

def main():
    print("algoritmo para quitar la primera y ultima letra de una cadena")
    string = str(input("Ingresa una palabra: "))
    aux = len(string) -1 
    print("La nueva palabra es: ", string[1: aux]," \n")
    
    
if __name__ == "__main__":
    main()