#Programa que pregunte el nombree de la mama de goku
import time
import os 
def main():
    flag = False
    while flag == False:     
        print("\nprograma que pregunte el nombre de la mamá de Goku y que lo siga preguntando hasta que acierte\n")
        name = str(input("Cual es el nombre de la mamá de goku: "))
        if name =="Gina" or name == "gina": #Or se cumple una condicion o la otra dentro del mismo if
            flag = True
            print("\nFelicidades, has acertado ")
            
        else:
            print("\n Vuelve a intentar perdedor!")
            time.sleep(1)
            os.system("cls")
    
if __name__ == "__main__":
    main()