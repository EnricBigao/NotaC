import math

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

def decimal_para_binario(numero):
    if numero == 0:
        return "0"
    
    parte_inteira = int(numero)
    parte_fracionaria = numero - parte_inteira
    
    binario_inteiro = bin(parte_inteira)[2:]
    
    binario_fracionario = ""
    precisao = 10  # Número de casas decimais para a parte fracionária
    
    for _ in range(precisao):
        parte_fracionaria *= 2
        bit = int(parte_fracionaria)
        binario_fracionario += str(bit)
        parte_fracionaria -= bit
    
    return f"{binario_inteiro}.{binario_fracionario}"

# Função exponencial
def exponencial(x):
    return math.exp(x)

# Pontos para interpolação
x_pontos = [0, 0.5, 1, 1.5, 2]
y_pontos = [exponencial(x) for x in x_pontos]

coeficientes = diferencas_divididas(x_pontos, y_pontos)

print("Coeficientes do polinômio interpolador (base decimal):")
for i, coef in enumerate(coeficientes):
    print(f"a{i} = {coef}")

print("\nCoeficientes do polinômio interpolador (base binária):")
for i, coef in enumerate(coeficientes):
    binario = decimal_para_binario(coef)
    print(f"a{i} = {binario}")

# Calcular o valor do polinômio para x = 1.25
x_interpolado = 1.25
y_interpolado = polinomio_interpolador(coeficientes, x_pontos, x_interpolado)
y_real = exponencial(x_interpolado)

print(f"\nValor interpolado para x = {x_interpolado}:")
print(f"y (interpolado, decimal) = {y_interpolado}")
print(f"y (interpolado, binário) = {decimal_para_binario(y_interpolado)}")
print(f"y (real, decimal) = {y_real}")
print(f"y (real, binário) = {decimal_para_binario(y_real)}")
print(f"Erro absoluto = {abs(y_real - y_interpolado)}")
