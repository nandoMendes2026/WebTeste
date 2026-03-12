def calcular_salario():
  """Calcula o salário de um funcionário."""

  # Leitura dos dados de entrada
  numero_funcionario = int(input("Digite o número do Functionary: "))
  horas_trabalhadas = int(input("Digite as horas trabalhadas: "))
  valor_por_hora = float(input("Digite o valor recebido por hora: "))

  # Cálculo do salário
  salario = horas_trabalhadas * valor_por_hora


  # Impressão do resultado
  print(f"Funcionário número = {numero_funcionario}")
  print(f"Sário a receber = U$ {salario:.2f}")

# Chamada da função para executar o cálculo
calcular_salario()