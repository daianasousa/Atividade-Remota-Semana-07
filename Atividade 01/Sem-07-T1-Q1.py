def main():
  lebre = 0
  minutos = 0
  tartaruga_metros = tartaruga = float(input('Digite quantos metros a tartarugas sairá à frente da lebre: '))
  while True:
    if lebre < tartaruga:
      tartaruga += 1
      lebre += 10
      minutos += 1
    else:
      print(f'A lebre levará {minutos:.0f} minutos para alcaçar a tartaruga')
      break

if __name__ == '__main__':
  main()
