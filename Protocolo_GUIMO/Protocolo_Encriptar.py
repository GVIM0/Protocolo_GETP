#Protocolo.-Cifrado
#Equipo GUIMO
#García Ambrosio Aldo
#Hernández Vera Gabriel
#Ponce Espino Miguel Angel
#Salinas Aquino Omar Ivan

Confir = "S"

while Confir.upper() == "S":
    Texto = input("Ingrese un texto: ")
    Bin_Fin = ""

    # Validamos que el dato ingresado sea valido
    if Texto != "":
        Bin_Fin = ""
        for i in range(len(Texto)):
            Letra = Texto[i]
            #Transformamos de caracter a código ASCII
            Cod_ASCII = ord(Letra)

            # Aseguramos que Func esté en un rango que produzca binariados de 15 dígitos
            Func = ((Cod_ASCII - 32) % (2**15)) ** 2

            Binario = format(Func, '015b')  # Aseguramos que el binario tenga siempre 15 dígitos

            # Construimos la cadena de binarios
            Bin_Fin += Binario
        
        print("Encriptación Exitosa: \n", Bin_Fin, "\n")
    else:
        print("Entrada no válida. Ingrese una cadena de texto.")

    Confir = input("¿Desea Continuar? S/N: ")

