def consonant(text):
    vowels = ["A" , "a" , "E" , "e" , "I" , "i" , "O" , "o" , "U" , "u" ," "]
    result = ""
    
    for letter in text:
        if letter not in vowels:
            result += letter 
    return result

    
def main ():
    print("\nprograma que sume las consonantes\n")
    text = input ("ingresa el texo: ")
    aux = consonant(text)
    print("el resultado es: ", len (aux))
    

if __name__ == "__main__":
    main()