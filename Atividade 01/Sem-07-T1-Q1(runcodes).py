def main():
  lebre = 0 # metros
  minutos = 0 # minutos
  tartaruga_metros = tartaruga = float(input())
  while True:
    if lebre < tartaruga:
      tartaruga += 1
      lebre += 10
      minutos += 1
    else:
      print(minutos)
      break

if __name__ == '__main__':
  main()
