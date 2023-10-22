#Protocolo.-Descrifrado
#Equipo GUIMO
#García Ambrosio Aldo
#Hernández Vera Gabriel
#Ponce Espino Miguel Angel
#Salinas Aquino Omar Ivan


#Función en python que segmenta el binario introducido en binarios de 15 digistos
def Dividir_Binario(binario):
    Segmentos = [binario[i:i+15] for i in range(0, len(binario), 15)]
    return Segmentos


Confirmar  = "S"

while Confirmar.upper() == "S":
    Cadena_Final = ""
    fx = 0
    Binario = input("Ingrese el binario: \n")
    #Validamos que el dato ingresado
    if Binario != "":
        segmentos = Dividir_Binario(Binario)

        #Revertimos todas las operaciones de encriptar
        for i in range(len(segmentos)):
            Bin = segmentos[i]
            fx = int(Bin,2)
            Cod_ASCII= int((fx ** 0.5) + 32)
            caracter = chr(Cod_ASCII)
            # Construimos la cadena final
            Cadena_Final += caracter

        #Imprimimos la cadena descifrada
        print("Descencriptación Exitosa: \n", Cadena_Final ,"\n")
        Confirmar = input("¿Desea Continuar? S/N: ")
    else:
        print("Entrada no valida, porfavor ingrese un binario")
    

