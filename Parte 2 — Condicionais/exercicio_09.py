nota1 = float(input("Insira sua primeira nota: "))
nota2 = float(input("Insira sua segunda nota: "))
nota3 = float(input("Insira sua terceira nota: "))

media = (nota1 + nota2 +nota3)/3

if media >= 6.0:
  print("sua nota final é: ", media, "Parabéns, você foi aprovado!")
elif media >=4.0 and media <= 5.9:
  print("sua nota final é: ", media, "Você está de recuperação.")
elif media >10:
    print("Nota inválida, insira uma nota entre 0 e 10.")
else:
  print("sua nota final é: ", media, "Infelizmente, você foi reprovado.")