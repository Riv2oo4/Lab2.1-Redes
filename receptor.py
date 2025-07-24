def verificar_y_corregir_hamming(trama: str) -> tuple:
    bits = list(map(int, trama))

    # Posiciones de los bits de paridad en Hamming
    posiciones_paridad = [0, 1, 3, 7] 

    error_pos = 0
    for i, p in enumerate(posiciones_paridad):
        suma = 0
        for j in range(len(bits)):
            if j != p and ((j + 1) & (2 ** i)) != 0:
                suma ^= bits[j]
        if suma != bits[p]:
            error_pos += 2 ** i

    if error_pos > 0:
        print(f"Error detectado en la posición {error_pos}. Corrigiendo...")
        bits[error_pos - 1] ^= 1  # Corrige el bit
        corregido = True
    else:
        corregido = False

    # Extraer los bits
    datos = [bits[i] for i in range(len(bits)) if i not in posiciones_paridad]
    mensaje_original = ''.join(map(str, datos))

    return mensaje_original, corregido, error_pos if corregido else None

def procesar_receptor(archivo):
    with open(archivo, 'r') as f:
        lineas = f.readlines()

    for i, linea in enumerate(lineas):
        trama = linea.strip()
        if not trama:
            continue
        mensaje, corregido, posicion = verificar_y_corregir_hamming(trama)
        print(f"Trama {i+1}: {trama}")
        if corregido:
            print(f"- Error corregido en bit {posicion}. Mensaje original: {mensaje}\n")
        else:
            print(f"- Sin errores. Mensaje original: {mensaje}\n")


procesar_receptor("receptor.txt")