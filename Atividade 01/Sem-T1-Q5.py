def main():
  aves = int(input('Digite a quantidade de aves a partir do ano 1600: '))

  para  = 0.1 * aves
  pop_total = aves
  ano = 1600
  
  while pop_total > para:
    nasc = natalidade(pop_total)
    mort = mortalidade(pop_total)
    pop_total = populacao_total(pop_total)
    
    print(f'{ano},{nasc:.0f},{mort:.0f},{pop_total:.0f}')
    
    ano += 1

def natalidade(pop_total):
  return 0.01 * pop_total

def mortalidade(pop_total):
  return 0.06 * pop_total

def populacao_total(pop_total):
  return pop_total - mortalidade(pop_total) + natalidade(pop_total)

if __name__ == '__main__':
  main()
