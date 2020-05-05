#programa que ordene 10 numeros de mayor a menor
import random

def show(numbers):
    print("\nNumeros a ordenar: ", numbers)
    numbers.sort(reverse = True)
    print("\nNumeros ordenados de manera descendente: ",numbers,"\n")
    

def main():
    numbers =[]
    print("\nPrograma que ordene 10 nuemros de mayor a menor\n")
    print("1)introducir numeros de manera aleatoria")
    print("2)Intruducir numeros manualmente")
    opc = int(input("Selecciona una opción: "))
    
    if opc == 1:
        for i in range(10):
            numbers.append(random.randint(1,100))
        show(numbers)
    elif opc == 2:
        for i in range(10):
            print("Numero",i +1)
            numbers.append(int(input())) #Meter cosas al arreglo 
        show(numbers)
            
            
    
    
if __name__ == "__main__":
    main()