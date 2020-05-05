#algoritmo para obtener moda,media y la desviacion estandar
import random 

def mean(stats):
    mean = 0 
    for stat in stats:
        mean += stat
    return mean/len(stats)

def mode(stats):
    repeats = 0 #cuenta las veces que se repite un numero 
    
    for i in stats:
        n = stats.count(i)
        if n > repeats:
            repeats = n
    aux = []
    
    for i in stats:
        n = stats.count(i)
        if n == repeats and i not in aux:
            aux.append(i)
            
    if len(aux)!= len(stats):
        return aux[0]
    else:
        return "No hay moda"

def desviation(mean, stats):
    standard = 0
    variation = 0
    for i  in range(len (stats)):
        variation += (stats[i]- mean)**2
    standard = (variation/len(stats))**.5 #es .5 por que la raiz se pone a la 1/2 ,doble asterico para sacar raiz 
    return standard
    

def main():
    stats=[]
    print("\nalgoritmo para obtener moda,media y desviacion estandar\n")
    count= int(input("cuantos datos deseas evaluar"))
 
    for _ in  range(count):
        stats.append(random.randint(0,100))#randit es para enteros, es parte de la libreria random
        
    aux = mean(stats)
    print("\nDatos a evaluar: ",stats)
    print("\nLa media es:",aux)
    print("La moda es:",mode(stats))
    print("La desviacion estandar es:",desviation(aux, stats))
    print()
    
     
    
    
if __name__ == "__main__":
    main ()