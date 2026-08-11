import pyperclip
import re

# Diccionario de palabras comunes en español para puntuación
PALABRAS_COMUNES = {
    "EL", "LA", "LOS", "LAS", "UN", "UNA", "UNOS", "UNAS", "DE", "DEL",
    "A", "AL", "EN", "CON", "POR", "PARA", "SIN", "SOBRE", "ENTRE", "HASTA",
    "DESDE", "Y", "O", "QUE", "SI", "NO", "COMO", "PERO", "MAS", "SU", "SUS",
    "MI", "TU", "SE", "LE", "LES", "ME", "TE", "NOS", "ESTE", "ESTA", "ESTOS",
    "ESTAS", "TODOS", "TODAS", "OTRO", "OTROS", "OTRA", "OTRAS", "MISMO",
    "CADA", "VER", "HOMBRES", "PARTE", "LUGAR", "MUY", "CUANDO", "DONDE"
}

# Frecuencias relativas de letras en el idioma español
FRECUENCIAS_ESP = {
    'A': 0.1253, 'B': 0.0142, 'C': 0.0468, 'D': 0.0586, 'E': 0.1368,
    'F': 0.0069, 'G': 0.0101, 'H': 0.0070, 'I': 0.0625, 'J': 0.0044,
    'K': 0.0002, 'L': 0.0804, 'M': 0.0315, 'N': 0.0671, 'O': 0.0868,
    'P': 0.0251, 'Q': 0.0088, 'R': 0.0687, 'S': 0.0798, 'T': 0.0463,
    'U': 0.0393, 'V': 0.0090, 'W': 0.0001, 'X': 0.0022, 'Y': 0.0090, 'Z': 0.0052
}


def cesar(texto, clave):
    """Cifra o descifra texto desplazando caracteres según la clave."""
    res = []
    for c in texto:
        if 'a' <= c <= 'z':
            res.append(chr((ord(c) - 97 + clave) % 26 + 97))
        elif 'A' <= c <= 'Z':
            res.append(chr((ord(c) - 65 + clave) % 26 + 65))
        else:
            res.append(c)
    return "".join(res)


def puntuar_texto(texto):
    """Evalúa qué tan probable es que un texto esté en español."""
    palabras = re.findall(r'\b[A-Za-zÁÉÍÓÚáéíóúÑñ]+\b', texto.upper())
    coincidencias_palabras = sum(1 for p in palabras if p in PALABRAS_COMUNES)

    total_letras = sum(1 for c in texto if c.isalpha())
    if total_letras == 0:
        return 0

    puntaje_frecuencia = 0
    for c in texto.upper():
        if c in FRECUENCIAS_ESP:
            puntaje_frecuencia += FRECUENCIAS_ESP[c]

    return (coincidencias_palabras * 50) + (puntaje_frecuencia / total_letras * 100)


def resolver_automatico(texto):
    """Prueba todas las 26 claves y detecta automáticamente la clave correcta."""
    mejor_clave = 0
    mejor_puntaje = -1
    mejor_texto = texto

    for clave in range(26):
        candidato = cesar(texto, clave)
        score = puntuar_texto(candidato)
        if score > mejor_puntaje:
            mejor_puntaje = score
            mejor_clave = clave
            mejor_texto = candidato

    return mejor_clave, mejor_texto


if __name__ == "__main__":
    print("--- CIFRADO CÉSAR AUTOMÁTICO / MANUAL ---")
    opcion_texto = input("1. Pegar texto del portapapeles\n2. Escribir texto manualmente\nOpción (1/2): ").strip()

    texto = pyperclip.paste() if opcion_texto == "1" else input("Ingrese texto: ")
    print(f"\nTexto de entrada: \"{texto}\"")

    opcion_modo = input("\n1. Resolver automáticamente (Detectar clave)\n2. Usar clave manual\nOpción (1/2, por defecto 1): ").strip()

    if opcion_modo in ("", "1"):
        clave, resultado = resolver_automatico(texto)
        print(f"\n¡Clave detectada automáticamente!: {clave}")
        print(f"Resultado descifrado: {resultado}")
    else:
        clave = int(input("Ingrese desplazamiento (ej: 3 cifrar, -3 descifrar): "))
        resultado = cesar(texto, clave)
        print(f"\nClave utilizada: {clave}")
        print(f"Resultado: {resultado}")

    pyperclip.copy(resultado)
    print("¡Resultado copiado automáticamente al portapapeles!")
