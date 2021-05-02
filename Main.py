from Kula import kul, sfe
from Anty import *
from Wybory import wyb
import re

import numpy as np
import matplotlib.pyplot as plt
import math

# from mpl_toolkits.mplot3d import Axes3D

data = 0


def inf():
    print('''Informacje o programie''')


def dan():
    global data
    data = np.loadtxt('new.txt')


def pun():
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.scatter(data[:, 0], data[:, 1], data[:, 2], s=0.5)
    ax.view_init(20, 20)
    plt.show()


def sta():
    global data, central_point

    distances = np.array([])
    for item in data:
        distance = abs(math.sqrt((item[0] - central_point[0]) ** 2 + (item[1] - central_point[1]) ** 2 + (
                item[2] - central_point[2]) ** 2) - radius)
        distances = np.append(distances, distance)

    print('Średnia odległość punktu od sfery: %f' % (np.average(distances)))
    print('Maksymalna odległość punktu od sfery: %f' % (np.max(distances)))
    print('Minimalna odległość punktu od sfery: %f' % (np.min(distances)))
    print('Odchylenie standardowe: %f' % (np.std(distances)))


def mix(mu):
    global data, central_point

    distances = np.array([])
    for item in data:
        distance = math.sqrt((item[0] - central_point[0]) ** 2 + (item[1] - central_point[1]) ** 2 + (
                item[2] - central_point[2]) ** 2)
        distances = np.append(distances, distance)
    ma = np.max(distances)
    mi = np.min(distances)
    if mu == 0:
        print('Promień kuli opisanej na punktach: %f' % (np.max(distances)))
    elif mu == 1:
        print('Promień kuli wpisanej w punkty: %f' % (np.min(distances)))

    return ma, mi


def end():
    exit()


while True:
    print('''Witaj w programie
    
    Wybierz jedna z nastepujacych opcji:
    1: Wyswietl informacje o programie
    2: Pobierz dane
    3: Wyświetl umiejscowienie punktów na osi
    4: Oblicz kule średniokwadratową ze wszystkich punktów
    5: Statystyka
    6: Wyświetl kule średniokwadratową wraz z umiejscowieniem punktów na osi
    7: Wyświetl kule opsianą na punktach
    8: Wyświetl kule wpisaną w punkty
    9: Ustal 25 punktów referencyjnych
    10: Oblicz kulę średniokwadratową z punktów referencyjnych
    11: Wyświetl kule średniokwadratową z 25 punktów wraz z umiejscowieniem punktów na osi
    12: Porównaj kulę średniokwadratową ze wszystkich punktów z kulą średniokwadratową z punktów referenyjnych
    ''')
    command = g('Wybierz polecenie: ', 1, 12)
    if command == 1:
        inf()
    elif command == 2:
        dan()
    elif command == 3:
        pun()
    elif command == 4:
        (radius, x, y, z) = kul(data[:, 0], data[:, 1], data[:, 2])
        central_point = [x, y, z]
        print('Promień kuli wynosi:', radius, '\nWspółrzędna x środka wynosi:', x, '\nWspółrzędna y środka wynosi:', y,
              '\nWspółrzędna z środka wynosi:', z)
    elif command == 5:
        sta()
    elif command == 6:
        fig = plt.figure(figsize=[20, 20])
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], s=2, c='r')
        ax.plot_wireframe(*sfe(central_point, radius))
        ax.view_init(19, 20)
        plt.show()
    elif command == 7:
        maa, mii, = mix(0)
        fig = plt.figure(figsize=[20, 20])
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], s=5, c='r')
        ax.plot_wireframe(*sfe(central_point, maa))
        ax.view_init(30, 30)
        plt.show()
    elif command == 8:
        maa, mii, = mix(1)
        fig = plt.figure(figsize=[20, 20])
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(data[:, 0], data[:, 1], data[:, 2], s=5, c='r')
        ax.plot_wireframe(*sfe(central_point, mii))
        ax.view_init(30, 30)
        plt.show()
    elif command == 9:
        ni = wyb(x, y, z, radius, data)
        co = 0
        for ee in range(len(ni)):
            co += 1
            print('Położenie punktu nr: ', co, '\nX: ', ni[ee].x, '  Y: ', ni[ee].y, '  Z: ', ni[ee].z)
    elif command == 10:
        wx = []
        wy = []
        wz = []
        for i in range(len(ni)):
            wx.append(ni[i].x)
            wy.append(ni[i].y)
            wz.append(ni[i].z)
        (rad, xxx, yyy, zzz) = kul(wx, wy, wz)
        cent = [xxx, yyy, zzz]
        print('Kula średniokwadtawoa z 25 punktów', '\nPromień kuli wynosi:', rad, '\nWspółrzędna x środka wynosi:',
              xxx, '\nWspółrzędna y środka wynosi:', yyy,
              '\nWspółrzędna z środka wynosi:', zzz)
    elif command == 11:
        fig = plt.figure(figsize=[20, 20])
        ax = fig.add_subplot(111, projection='3d')
        ax.scatter(wx, wy, wz, s=2, c='r')
        ax.plot_wireframe(*sfe(cent, rad))
        ax.view_init(19, 20)
        plt.show()
    elif command == 12:
        print('Różnice pomiędzy kulą średniokwadratową ze wszystkich punktów a kulą śedniokwadratową z 25 punktów:')
        print('Promień:', math.fabs(radius - rad), '\nPołożenie środka w osi:')
        print('x:', math.fabs(x - xxx))
        print('y:', math.fabs(y - yyy))
        print('z:', math.fabs(z - zzz))
