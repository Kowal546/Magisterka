import math


class Punkt:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z


punkty = []


def wyb(x0, y0, z0, r, dat):
    def pkt(xx0, yy0, zz0, rr, al, fi):
        z1 = (rr * math.sin(math.radians(al))) + zz0
        x1 = (rr * math.cos(math.radians(al))) + xx0
        r1 = xx0 - x1
        xx = (r1 * math.cos(math.radians(fi))) + xx0
        yy = (r1 * math.sin(math.radians(fi))) + yy0
        now_pkt = Punkt(xx, yy, z1)
        punkty.append(now_pkt)

    xx1 = x0
    yy1 = y0
    zz1 = z0 + r
    now_punk = Punkt(xx1, yy1, zz1)
    punkty.append(now_punk)
    alf = [112.5, 112.5, 112.5, 112.5, 135, 135, 135, 135, 135, 135, 135, 135, 157.5, 157.5, 157.5, 157.5, 180, 180,
           180, 180, 180, 180, 180, 180]
    fii = [0, 90, 180, 270, 22.5, 67.5, 112.5, 157.5, 202.5, 247.5, 292.5, 337.5, 45, 135, 225, 315, 22.5, 67.5, 112.5,
           157.5, 202.5, 247.5, 292.5, 337.5]

    for i in range(len(alf)):
        pkt(x0, y0, z0, r, alf[i], fii[i])

    pky = []

    def sred(r, t, u):
        dist = 0.5
        while 1:
            X = 0
            Y = 0
            Z = 0
            count = 0
            for p in range(len(dat[:, 0])):
                if ((math.fabs(r - dat[p, 0]) <= dist) & (math.fabs(t - dat[p, 1]) <= dist) & (
                        math.fabs(u - dat[p, 2]) <= dist)):
                    X += dat[p, 0]
                    Y += dat[p, 1]
                    Z += dat[p, 2]
                    count += 1
            if count < 3:
                dist += 0.01
            else:
                u = X / count
                i = Y / count
                o = Z / count
                break

        return u, i, o

    for p in range(len(punkty)):
        roz = 0.001
        flag = 0
        while flag != 1:
            if flag == 0:
                for i in range(len(dat[:, 0])):
                    if ((math.fabs(punkty[p].x - dat[i, 0]) <= roz) and (
                            math.fabs(punkty[p].y - dat[i, 1]) <= roz) and (
                            math.fabs(punkty[p].z - dat[i, 2]) <= roz)):
                        punk = Punkt(dat[i, 0], dat[i, 1], dat[i, 2])
                        pky.append(punk)
                        flag = 1
            if (roz == 0.001) and flag == 0:
                roz = 0.005
            elif (roz == 0.005) and flag == 0:
                roz = 0.01
            elif flag == 0:
                w, o, q = sred(punkty[p].x, punkty[p].y, punkty[p].z)
                punk = Punkt(w, o, q)
                pky.append(punk)
                break
    return pky
