def diferencas_divididas(x, y):
    n = len(x)
    coeficientes = y.copy()
    tabela = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        tabela[i][0] = y[i]
    
    for j in range(1, n):
        for i in range(n - j):
            tabela[i][j] = (tabela[i+1][j-1] - tabela[i][j-1]) / (x[i+j] - x[i])
            if i == 0:
                coeficientes[j] = tabela[i][j]
    
    return coeficientes, tabela

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
    if numero < 0:
        return "-" + decimal_para_binario(abs(numero), precisao)
    
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

coeficientes, tabela = diferencas_divididas(x_pontos, y_pontos)

# Formatação do resultado
print("Sejam x_pontos = [0, 0.5, 1, 1.5, 2]")

print("\nOs coeficientes das diferenças divididas são:")
for i, coef in enumerate(coeficientes):
    print(f"a{i} = {coef:.6f} (decimal) = {decimal_para_binario(coef)} (binário)")

print("\nA tabela de diferenças divididas é:")
print("x\t\tf(x)\t\tDif. 1ª ordem\tDif. 2ª ordem\tDif. 3ª ordem\tDif. 4ª ordem")
for i in range(len(x_pontos)):
    linha = f"{x_pontos[i]}\t\t{tabela[i][0]:.6f}"
    for j in range(1, len(x_pontos) - i):
        linha += f"\t\t{tabela[i][j]:.6f}"
    print(linha)

print("\nExplicação da relação entre coeficientes e tabela:")
print("- O primeiro coeficiente (a0) é o valor de f(x) para o primeiro ponto (x = 0).")
print("- Cada coeficiente subsequente (a1, a2, etc.) é o primeiro valor calculado")
print("  em cada coluna da tabela de diferenças divididas.")
print("- Por exemplo, a1 é o primeiro valor da coluna 'Dif. 1ª ordem',")
print("             a2 é o primeiro valor da coluna 'Dif. 2ª ordem', e assim por diante.")

print(f"\nO valor de exp[0, 0.5, 1, 1.5, 2] é: {coeficientes[-1]:.6f} (decimal) = {decimal_para_binario(coeficientes[-1])} (binário)")
print("Este é o coeficiente de mais alta ordem (a4) e representa a diferença dividida de quarta ordem.")

# Calcular o valor do polinômio para x = 1.25
x_interpolado = 1.25
y_interpolado = polinomio_interpolador(coeficientes, x_pontos, x_interpolado)
y_real = exponencial(x_interpolado)

print(f"\nPara x = {x_interpolado}:")
print(f"Valor interpolado = {y_interpolado:.6f} (decimal) = {decimal_para_binario(y_interpolado)} (binário)")
print(f"Valor real = {y_real:.6f} (decimal) = {decimal_para_binario(y_real)} (binário)")
print(f"Erro absoluto = {abs(y_real - y_interpolado):.6f}")

# Demonstração da conversão binária para número negativo
numero_negativo = -3.25
print(f"\nDemonstração da conversão binária para número negativo:")
print(f"{numero_negativo} em binário: {decimal_para_binario(numero_negativo)}")