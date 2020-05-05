#programa que recibe una palabra y la guarda en un archivo
def save(text):
    file = open("programa_6_archivo.txt","w") #lectura o escritira W o R
    file.write(text)
    file.close()
    return "\n file saved successfully...\n"
    
def main ():
    print("\nPrograma que recibe una palabra y la guarda en un archivo\n")
    text = str(input("ingresa una palabra: "))
    print(save(text))
    
    
     
if __name__ == "__main__":
    main()