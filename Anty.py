def g(prompt, vmin, vmax):
    while True:
        num = input(prompt)
        try:
            number = int(num)
        except ValueError:
            print('Podaj liczbe.')
            continue
        if number < vmin:
            print("Zbyt mała wartość liczby. Podaj liczbę całkowita od 1 do 4.")
            continue
        if number > vmax:
            print("Zbyt duza wartosc liczby. Podaj liczbe calkowita od 1 do 4.")
            continue
        break
    return number
