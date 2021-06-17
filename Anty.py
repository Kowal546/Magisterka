def g(prompt, vmin, vmax):
    while True:
        num = input(prompt)
        try:
            number = int(num)
        except ValueError:
            print('Podaj liczbe.')
            continue
        if number < vmin:
            print("Zbyt mała wartość liczby. Podaj liczbę całkowita od 1 do 10.")
            continue
        if number > vmax:
            print("Zbyt duza wartosc liczby. Podaj liczbe calkowita od 1 do 10.")
            continue
        break
    return number
