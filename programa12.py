#algoritmo que regresa cantidad de dinero por dias trabajados
def main():
    print("\nAlgoritmo que regresa cantidad de dinero por días trabajados\n")
    hours =float(input("Ingresa el numero de horas trabajadas: "))
    rate =float(input("Ingresa la tarifa por hora: "))
    days = hours/8 
    total = hours*rate
    
    print("\nTotal de días trabajados: ",days)
    print("Total de dinero: ",total, "\n")
    
    
    
if __name__ == "__main__":
        main()