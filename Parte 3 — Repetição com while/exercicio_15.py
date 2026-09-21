positivos = 0

while True:
    numero = int(input("Digite um número (0 para parar): "))
    if numero == 0:
        break
    if numero > 0:
        positivos += 1

print(f"Você digitou {positivos} números positivos.")