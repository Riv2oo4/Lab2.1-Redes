def hamming_encode(data_bits):
    m = len(data_bits)
    r = 0
    while 2**r < m + r + 1:
        r += 1

    n = m + r  
    code = ['0'] * (n + 1)

    j = 0
    for i in range(1, n + 1):
        if (i & (i - 1)) != 0:
            code[i] = data_bits[j]
            j += 1

    for i in range(r):
        p = 2**i
        total = 0
        for k in range(1, n + 1):
            if (k & p) and k != p:
                total += int(code[k])
        code[p] = str(total % 2)

    return ''.join(code[1:])

if __name__ == "__main__":
    data_bits = input("Ingrese una trama en binario (ejemplo 110101): ").strip()
    if not data_bits or any(c not in '01' for c in data_bits):
        print("Error: la trama debe ser una secuencia de 0s y 1s.")
        exit(1)

    codeword = hamming_encode(data_bits)
    print(f"Mensaje original (bits): {data_bits}")
    print(f"Trama Hamming generada : {codeword}")

    with open('emisor.txt', 'w') as f:
        f.write(codeword)

    print("La trama Hamming ha sido guardada en 'emisor.txt'")
