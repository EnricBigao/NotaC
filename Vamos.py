def diferencas_divididas(x, y):
    n = len(x)
    coeficientes = y.copy()
    
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            coeficientes[i] = (coeficientes[i] - coeficientes[i-1]) / (x[i] - x[i-j])
    
    return coeficientes

def polinomio_interpolador(coeficientes, x_pontos, x):
    n = len(x_pontos)
    p = coeficientes[n-1]
    for k in range(n-2, -1, -1):
        p = p * (x - x_pontos[k]) + coeficientes[k]
    return p

def exponencial(x, precisao=15):
    resultado = 1.0
    termo = 1.0
    for i in range(1, precisao):
        termo *= x / i
        resultado += termo
    return resultado

def decimal_para_binario(numero, precisao=10):
    parte_inteira = int(numero)
    parte_fracionaria = numero - parte_inteira
    
    # Converter parte inteira
    if parte_inteira == 0:
        binario_inteiro = "0"
    else:
        binario_inteiro = ""
        while parte_inteira > 0:
            binario_inteiro = str(parte_inteira % 2) + binario_inteiro
            parte_inteira //= 2
    
    # Converter parte fracionária
    binario_fracionario = ""
    for _ in range(precisao):
        parte_fracionaria *= 2
        bit = int(parte_fracionaria)
        binario_fracionario += str(bit)
        parte_fracionaria -= bit
    
    if binario_fracionario:
        return f"{binario_inteiro}.{binario_fracionario}"
    else:
        return binario_inteiro

# Pontos para interpolação
x_pontos = [0, 0.5, 1, 1.5, 2]
y_pontos = [exponencial(x) for x in x_pontos]

coeficientes = diferencas_divididas(x_pontos, y_pontos)

# Formatação do resultado
print("Sejam x_pontos = [0, 0.5, 1, 1.5, 2]")
print("\nOs coeficientes das diferenças divididas são:")
for i, coef in enumerate(coeficientes):
    print(f"a{i} = {coef} (decimal) = {decimal_para_binario(coef)} (binário)")

print("\nA tabela de diferenças divididas é:")
print("x\t\tf(x)\t\tDif. 1ª ordem\tDif. 2ª ordem\tDif. 3ª ordem\tDif. 4ª ordem")
for i in range(len(x_pontos)):
    linha = f"{x_pontos[i]}\t\t{y_pontos[i]:.6f}"
    for j in range(i):
        dif = coeficientes[j+1]
        for k in range(j+1):
            dif *= (x_pontos[i] - x_pontos[k])
        linha += f"\t\t{dif:.6f}"
    print(linha)

# Calcular o valor do polinômio para x = 1.25
x_interpolado = 1.25
y_interpolado = polinomio_interpolador(coeficientes, x_pontos, x_interpolado)
y_real = exponencial(x_interpolado)

print(f"\nPara x = {x_interpolado}:")
print(f"Valor interpolado = {y_interpolado:.6f} (decimal) = {decimal_para_binario(y_interpolado)} (binário)")
print(f"Valor real = {y_real:.6f} (decimal) = {decimal_para_binario(y_real)} (binário)")
print(f"Erro absoluto = {abs(y_real - y_interpolado):.6f}")