def main():
  #valor na poupança inicial
  poupanca = 10000
  #Rendimento mensal
  r_poupanca = (0.7 / 100)
  #Taxa mensal 
  taxa_carro = (0.4 / 100)

  meses = 1

  aplicacao = poupanca + (poupanca * r_poupanca)
  carro = float(input('Valor inicial do carro: R$ '))
  preço_carro = carro + (carro * taxa_carro)

  while True:
    if aplicacao < preço_carro:
      aplicacao += (aplicacao * r_poupanca)
      preço_carro += (preço_carro * taxa_carro)
      meses += 1
    else:
      print(f'Vai demorar {meses} meses para você pode compra o carro à vista')
      break
if __name__ == '__main__':
  main()