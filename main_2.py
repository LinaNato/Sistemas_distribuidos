import time

vetor = []
num =int(input('Digite um número: '))

inicio4 = time.time()

for n in range(1,num+1):
 if num % n == 0:
  vetor.append(n)
  if len(vetor) > 2:
   fim4 = time.time()
   print('Não é primo')
   Time_4 = fim4 - inicio4
   print(f't4: {Time_4:.10f}')
   break
if len(vetor) == 2:
  fim4 = time.time()
  print('É primo')
  Time_4 = fim4 - inicio4
  print(f't4: {Time_4:.10f}')
  