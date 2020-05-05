
def save(text,fileName):
    file = open( fileName + ".txt","w") #lectura o escritura W o R
    file.write(text)
    file.close()
    return "\n file saved successfully...\n"
    
def main ():
    print("\nPrograma que recibe una palabra y la guarda en un archivo\n")
    text = str(input("ingresa una palabra: "))
    fileName = str(input("Como deseas nombrar el archivo: "))
    print(save(text, fileName))
    
    
     
if __name__ == "__main__":
    main()