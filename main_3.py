import time

numero = int(input('Digite um numero: '))
inicio = time.time()
divisores = 0
if numero == 0 or numero ==1:
  print("Não é primo")
  fim = time.time()
  Time_2=fim - inicio
  print(f't2: {Time_2:.10f}') 
else:  
  for divisor in range(1, numero):
      if numero % divisor == 0:
          divisores = divisores + 1
          if divisores > 1:
            break
  if divisores > 1:
    print('Não é primo')
    fim = time.time()
    Time_2=fim - inicio
    print(f't2: {Time_2:.10f}')
  else:
    print('É primo')
    fim = time.time()
    Time_2=fim - inicio
    print(f't2: {Time_2:.10f}')