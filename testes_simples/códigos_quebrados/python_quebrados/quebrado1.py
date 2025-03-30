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

print(calcular_media([2, 2, 2, 2]))
print(encontrar_maior([2, 3, 8, 4, 5]))
print(contar_pares([2, 3, 8, 4, 5]))