# Cifrado César y Traducción usando Listas de Python (Soporta 26 y 27 letras)
try:
    from deep_translator import GoogleTranslator
    HAS_TRANSLATOR = True
except ImportError:
    HAS_TRANSLATOR = False

# Generación de alfabetos explícitamente como LISTAS usando chr() y ord()
ALFABETO_MIN_26 = [chr(i) for i in range(ord('a'), ord('z') + 1)]
ALFABETO_MAY_26 = [chr(i) for i in range(ord('A'), ord('Z') + 1)]

# Inserción de 'ñ' / 'Ñ' para el alfabeto de 27 letras
ALFABETO_MIN_27 = list(ALFABETO_MIN_26)
ALFABETO_MIN_27.insert(ALFABETO_MIN_27.index('n') + 1, 'ñ')

ALFABETO_MAY_27 = list(ALFABETO_MAY_26)
ALFABETO_MAY_27.insert(ALFABETO_MAY_27.index('N') + 1, 'Ñ')


def quitar_acentos(texto):
    """Normaliza tildes a vocales simples usando listas de caracteres."""
    lista_caracteres = list(texto)
    reemplazos = {
        'á': 'a', 'é': 'e', 'í': 'i', 'ó': 'o', 'ú': 'u', 'ü': 'u',
        'Á': 'A', 'É': 'E', 'Í': 'I', 'Ó': 'O', 'Ú': 'U', 'Ü': 'U'
    }

    for i in range(len(lista_caracteres)):
        if lista_caracteres[i] in reemplazos:
            lista_caracteres[i] = reemplazos[lista_caracteres[i]]

    return "".join(lista_caracteres)


def cifrar_cesar(texto, desplazamiento, incluir_ene=True):
    """Cifra un texto usando posiciones en listas (26 o 27 letras)."""
    alf_min = ALFABETO_MIN_27 if incluir_ene else ALFABETO_MIN_26
    alf_may = ALFABETO_MAY_27 if incluir_ene else ALFABETO_MAY_26
    n = len(alf_min)

    texto_limpio = quitar_acentos(texto)
    lista_entrada = list(texto_limpio)
    lista_resultado = []

    for caracter in lista_entrada:
        if caracter in alf_min:
            idx = alf_min.index(caracter)
            nueva_pos = (idx + desplazamiento) % n
            lista_resultado.append(alf_min[nueva_pos])
        elif caracter in alf_may:
            idx = alf_may.index(caracter)
            nueva_pos = (idx + desplazamiento) % n
            lista_resultado.append(alf_may[nueva_pos])
        else:
            lista_resultado.append(caracter)

    return "".join(lista_resultado)


def descifrar_cesar(texto_cifrado, desplazamiento, incluir_ene=True):
    """Descifra un texto aplicando desplazamiento negativo."""
    return cifrar_cesar(texto_cifrado, -desplazamiento, incluir_ene)


def traducir_texto(texto, origen='es', destino='en'):
    """Traduce un texto de un idioma a otro con manejo de errores."""
    if not HAS_TRANSLATOR:
        return "[Librería 'deep-translator' no instalada]"
    try:
        return GoogleTranslator(source=origen, target=destino).translate(
            texto.lower()
        )
    except Exception as e:
        return f"[No se pudo traducir: {e}]"


def fuerza_bruta_cesar(texto_cifrado, incluir_ene=True):
    """Muestra todas las combinaciones posibles de descifrado."""
    n = 27 if incluir_ene else 26
    return {
        clave: descifrar_cesar(texto_cifrado, clave, incluir_ene)
        for clave in range(1, n)
    }


# Ejemplo de prueba
if __name__ == "__main__":
    # Texto cifrado correcto (Clave = 1, Alfabeto de 26 letras)
    cifrado = (
        "MBT NFOUFT GVFSUFT EJTDVUFO TPCSF JEFBT, "
        "MBT NFOUFT QSPNFEJP EJTDVUFO TPCSF BDPOUFDJNJFOUPT, "
        "MBT NFOUFT EFCJMFT EJTDVUFO TPCSF QFSTPOBT"
    )
    clave = 1

    descifrado = descifrar_cesar(cifrado, clave, incluir_ene=False)
    traducido = traducir_texto(descifrado, origen='es', destino='en')

    print("--- DEMOSTRACIÓN CIFRADO CÉSAR ---")
    print("Cifrado:   ", cifrado)
    print("Descifrado:", descifrado)
    print("Traducido: ", traducido)
