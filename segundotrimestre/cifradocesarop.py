import pyperclip


def cesar(texto, clave):
    """Aplica desplazamiento César al texto para una clave dada."""
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
    # Lee automáticamente el contenido del portapapeles sin solicitar input al usuario
    texto = pyperclip.paste()

    print("=== PROBABILIDADES DE DESCIFRADO CÉSAR (26 OPCIONES) ===")
    print(f"Texto del portapapeles: \"{texto}\"\n")

    for clave in range(26):
        print(f"Clave {clave:2d}: {cesar(texto, clave)}")
