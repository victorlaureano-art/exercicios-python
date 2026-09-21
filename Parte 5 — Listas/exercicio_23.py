numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
numero3 = input("Digite o terceiro número: ")
numero4 = input("Digite o quarto número: ")
numero5 = input("Digite o quinto número: ")
print("Os números digitados foram:", numero1, numero2, numero3, numero4, numero5)
print("A soma dos números digitados é:", int(numero1) + int(numero2) + int(numero3) + int(numero4) + int(numero5))

if numero1 > numero2 and numero1 > numero3 and numero1 > numero4 and numero1 > numero5:
    print("O maior número digitado foi:", numero1)
elif numero2 > numero1 and numero2 > numero3 and numero2 > numero4 and numero2 > numero5:
    print("O maior número digitado foi:", numero2)
elif numero3 > numero1 and numero3 > numero2 and numero3 > numero4 and numero3 > numero5:
    print("O maior número digitado foi:", numero3)
elif numero4 > numero1 and numero4 > numero2 and numero4 > numero3 and numero4 > numero5:
    print("O maior número digitado foi:", numero4)
elif numero5 > numero1 and numero5 > numero2 and numero5 > numero3 and numero5 > numero4:
    print("O maior número digitado foi:", numero5)