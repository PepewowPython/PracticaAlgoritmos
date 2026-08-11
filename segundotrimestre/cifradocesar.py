import pyperclip


def cesar(texto, clave):
    """Cifra o descifra texto desplazando caracteres segun la clave."""
    res = []
    for c in texto:
        if 'a' <= c <= 'z':
            res.append(chr((ord(c) - 97 + clave) % 26 + 97))
        elif 'A' <= c <= 'Z':
            res.append(chr((ord(c) - 65 + clave) % 26 + 65))
        else:
            res.append(c)
    return "".join(res)


if __name__ == "__main__":
    print("--- CIFRADO CÉSAR (Con Pyperclip) ---")
    opcion = input("1. Pegar texto del portapapeles\n2. Escribir texto manualmente\nOpción (1/2): ").strip()

    texto = pyperclip.paste() if opcion == "1" else input("Ingrese texto: ")
    print(f"Texto de entrada: {texto}")

    clave = int(input("Ingrese desplazamiento (ej: 3 cifrar, -3 descifrar): "))
    resultado = cesar(texto, clave)

    pyperclip.copy(resultado)
    print(f"\nResultado: {resultado}")
    print("¡Resultado copiado automáticamente al portapapeles!")
