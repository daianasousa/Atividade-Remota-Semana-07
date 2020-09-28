def main():
    
    tempo = 0
    taxa_A = (2 / 100)
    taxa_B = (3 / 100)
    p_1 = int(input())
    p_2 = int(input())

    if p_1 > p_2:
        pais_A = p_1
        pais_B = p_2


    elif p_2 > p_1:
        pais_A = p_2
        pais_B = p_1

    populacao_A = (pais_A + (pais_A * taxa_A))
    opulacao_B = (pais_B + (pais_B * taxa_B))

    while True:
        if pais_A > pais_B:
            pais_A += (pais_A * taxa_A)
            pais_B += (pais_B * taxa_B)
            tempo += 1
        elif pais_A < pais_B:
            print(tempo)
            break
        
if __name__=='__main__':
    main()
