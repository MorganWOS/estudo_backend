def calcular_media(numeros):
    soma = 0
    for num in numeros:
        soma += num
    media = soma / len(numeros)
    return media

def encontrar_maior(numeros):
    maior = 0
    for num in numeros:
        if num > maior:
            maior = num
    return maior

def contar_pares(numeros):
    count = 0
    for num in numeros:
        if num % 2 == 0:
            count += 1
    return count