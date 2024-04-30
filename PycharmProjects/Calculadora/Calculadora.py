def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def multiply(x, y):
  return x * y

def divide(x, y):
  if y == 0:
      return 'Error! Division by zero is not allowed.'
  else:
      return x / y

while True:
  print("Operações disponíveis:")
  print("1. Soma")
  print("2. Subtração")
  print("3. Multiplicação")
  print("4. Divisão")

  choice = input("\nEscolha a operação(1/2/3/4): ")

  if choice in ('1', '2', '3', '4'):
      num1 = float(input("\nDigita o primeiro número: "))
      num2 = float(input("\nDigita o segundo número: "))

      if choice == '1':
          print("\n", num1, "+", num2, "=", add(num1, num2))

      elif choice == '2':
          print("\n", num1, "-", num2, "=", subtract(num1, num2))

      elif choice == '3':
          print("\n", num1, "*", num2, "=", multiply(num1, num2))

      elif choice == '4':
          print("\n", num1, "/", num2, "=", divide(num1, num2))

      next_calculation = input("\nQuer continuar a operação? (yes/no): ")
      if next_calculation == "no":
        print("\nSaíndo da Calculadora...")
        break

  else:
      print("Entrada invalida")