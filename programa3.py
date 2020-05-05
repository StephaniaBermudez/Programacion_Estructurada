def anti_vowel(text):
    vowels = ["A" , "a" , "E" ,"e", "I" , "i" , "O" , "o" , "U" , "u"] 
    result = ""
    
    for letter in text:
        if letter not in vowels:
            result += letter #acumular 
    return result 
    
def main():
     print("\nprograma que quite todas las vocales de un texto\n")
     text = input ("ingresa el texto: ")
     aux = anti_vowel(text)
     print("El resultado es: ", aux) 
     

if __name__== "__main__":
    main()