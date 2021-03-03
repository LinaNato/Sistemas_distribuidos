import time

def TestaPrimo(n):
  EhPrimo = 1
  d = 2
  if (n <= 1):
    EhPrimo = 0

  while (EhPrimo == 1 and d <= n /2):
    if (n % d  == 0):
      EhPrimo = 0
    d = d + 1
  return EhPrimo

n = int(input('Digite um número: '))
inicio = time.time()
print (TestaPrimo(n))
fim = time.time()
print(fim - inicio)