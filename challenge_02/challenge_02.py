mensaje = "&###@&*&###@@##@##&######@@#####@#@#@#@##@@@@@@@@@@@@@@@*&&@@@@@@@@@####@@@@@@@@@#########&#&##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@##@@&"

def decodificar_mensaje(mensaje):
    valor_numerico = 0
    resultado = ""

    for caracter in mensaje:
        if caracter == "#":
            valor_numerico += 1
        elif caracter == "@":
            valor_numerico -= 1
        elif caracter == "*":
            valor_numerico *= valor_numerico
        elif caracter == "&":
            resultado += str(valor_numerico)

    return resultado

mensaje_codificado = decodificar_mensaje(mensaje)
print(mensaje_codificado)
