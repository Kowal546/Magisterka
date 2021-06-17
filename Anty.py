def g(prompt, vmin, vmax):
    while True:
        num = input(prompt)
        try:
            number = int(num)
        except ValueError:
            print('Podaj liczbe.')
            continue
        if number < vmin:
            print("Zbyt mała wartość liczby. Podaj liczbę całkowita od: ", vmin, "do: ", vmax)
            continue
        if number > vmax:
            print("Zbyt duza wartosc liczby. Podaj liczbę całkowita od: ", vmin, "do: ", vmax)
            continue
        break
    return number
