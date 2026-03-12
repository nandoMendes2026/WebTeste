def contar_numeros():
  """Conta quantos números pares, ímpares, positivos e negativos foram digitados."""

  pares = 0
  impares = 0
  positivos = 0
  negativos = 0

  for _ in range(5):
    numero = int(input("Digite um número: "))

    if numero % 2 == 0:
      pares += 1
    else:
      impares += 1

    if numero > 0:
      positivos += 1
    elif numero < 0:
      negativos += 1

  print(f"Pares: {pares}")
  print(f"Impares: {impares}")
  print(f"Positivos: {positivos}")
  print(f"Negativos: {negativos}")

# Chamada da função para executar o programa
contar_numeros()