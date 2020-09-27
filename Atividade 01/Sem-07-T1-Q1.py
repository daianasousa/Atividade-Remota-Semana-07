def main():
  lebre = 0
  tartaruga_metros = tartaruga = float(input('Digite quantos metros a tartarugas sairá à frente da lebre: '))
  while True:
    tartaruga += 1
    if lebre < tartaruga:
      lebre += 10
    elif lebre == tartaruga:
      min = lebre / 10
      break
  print(f'A lebre levará {min:.0f} minutos para alcaçar a tartaruga')

if __name__ == '__main__':
  main()