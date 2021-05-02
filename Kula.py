import math

import numpy as np


def kul(kx, ky, kz):
    # https://jekel.me/2015/Least-Squares-Sphere-Fit/
    kx = np.array(kx)
    ky = np.array(ky)
    kz = np.array(kz)

    M = np.zeros((len(kx), 4))
    M[:, 0] = kx * 2
    M[:, 1] = ky * 2
    M[:, 2] = kz * 2
    M[:, 3] = 1

    r = np.zeros((len(kx), 1))
    r[:, 0] = (kx * kx) + (ky * ky) + (kz * kz)
    s, poz, st, sy = np.linalg.lstsq(M, r, rcond=None)

    prom = math.sqrt((s[0] * s[0]) + (s[1] * s[1]) + (s[2] * s[2]) + s[3])
    return prom, s[0], s[1], s[2]



def sfe(centre=[0., 0., 0.], radius=1.,
        n_meridians=100, n_circles_latitude=None):
    if n_circles_latitude is None:
        n_circles_latitude = max(n_meridians / 2, 4)
    u, v = np.mgrid[0:2 * np.pi:n_meridians * 1j, 0:np.pi:n_circles_latitude * 1j]
    sphere_x = centre[0] + radius * np.cos(u) * np.sin(v)
    sphere_y = centre[1] + radius * np.sin(u) * np.sin(v)
    sphere_z = centre[2] + radius * np.cos(v)
    return sphere_x, sphere_y, sphere_z
