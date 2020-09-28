def main():
  nasc  = aux = int(input('Digite a sua Data de nascimento:  '))
  for i in range(1):
    soma = 0

    while nasc > 0:
      soma += nasc % 10
      nasc //= 10
  
    print(f'Seu número da sorte é o {soma}')

if __name__ == '__main__':
  main()