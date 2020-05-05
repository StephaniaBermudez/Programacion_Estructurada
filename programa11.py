#algoritmo que reciba un numero flotante entre 1.0 y el 10.0 y que lo ordene,imprimiento con letra el numero
#mas grande
import random

def show(numbers):
    print("\nNumeros ingresados: ", numbers)
    numbers.sort()
    print("\nLos numeros ordenados: ",numbers)
    aux = int(numbers[9])
    string = " "
    
    if aux == 9:
        string  ="nueve"
    elif aux == 8:
        string ="ocho"
    elif aux == 7:
        string ="siete"
    elif aux == 6:
        string ="seis"
    elif aux == 5:
        string = "cinco"
    elif aux == 4:
         string = "cuatro"
    elif aux == 3:
        string = "tres"
    elif aux == 2:
        string = "dos"
    else:
        string = "uno"
    
    print("\nEl numero mas grade es: ", string, "\n")
    
    

def main():
    numbers = []
    print("Algoritmo que reciba un numero flotante entre 1.0 y el 10.0 y que lo ordene ,imprimiendo con letra el mas grande")
    print("1)introducir numeros de manera aleatoria")
    print("2)Intruducir numeros manualmente")
    opc = int(input("Selecciona una opción: "))
    
    if opc == 1:
        for i in range(10):
            numbers.append(random.uniform(1.0,10.0))
        show(numbers)
    elif opc == 2:
        for i in range(10):
            print("Numero",i +1)
            numbers.append(float(input())) 
        show(numbers)
    
    
if __name__ == "__main__":
    main()