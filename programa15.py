#algoritmo que recibe 10 numeros e imprime los primos
import random 

def isPrime(num):
    if num < 1:
        return False
    elif num == 2:
        return num 
    else:
        for i in range(2, num):
            if num % i == 0:
                return False 
            return num
    

def main():
    print("algoritmo que recibe 10 numeros e imprime los primos")
    numbers =[]
    primes = []
    for _ in range(10):
        numbers.append(random.randint(1,100))
        
    print("Numeros ingresados: ",numbers, "\n")
    
    for i in range(10):
        result = isPrime(numbers[i])
        if result is not False: 
            if result not in  primes:
                primes.append(result)

    if len(primes) == 0:
        print("No hay numeros primos\n")
    else:
        primes.sort()
        print("Los numeros primos son: ", primes, "\n")
    
if __name__ == "__main__":
    main()