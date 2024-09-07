def evaluar(caracter):
    if caracter.isupper():# pregunto si es mayuscula
        return "Es letra mayúscula"
    elif caracter.islower(): # pregunto si es minuscula
        return "Es letra minúscula"
    elif caracter.isdigit(): # pregunto si es numero
        return "Es número"
    else:
        return "No es letra ni número" # pregunto si es otro caracter
    

if __name__ == '__main__':
    print("Caracter:", end='')
    caracter = input()
        
    respuesta = evaluar(caracter)
    print(respuesta)
