import random 
liczba = random.randint(1, 100)
i = 1

while i <= 7:
    use = int(input('Podaj liczbę od 1 do 100: '))
    if 1 <= use <= 100:   
        if use > liczba:
            i += 1
            print('szukana liczba jest mniejsza, spróbuj raz jeszcze')
        elif use < liczba:
            i += 1
            print('szukana liczba jest większa, spróbuj raz jeszcze')
        else :
            print('wygrałeś')
            break
    else:
        print('podałeś błędną liczbę')
        break
