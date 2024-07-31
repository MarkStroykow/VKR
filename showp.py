import math
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import matplotlib

matplotlib.use('Qt5Agg')

def supshow(figure):
    plt.ion()
    fig, ax = plt.subplots()
    fig.set_size_inches(6, 6)
    ax.set_xlim(-4.5, 4.5)
    ax.set_ylim(-4.5, 4.5)
    if figure == 'Гипершар':
        ax.add_patch(pat.Circle((0, 0), 1,fill=False))
    if figure == 'Гиперкуб':
        ax.add_patch(pat.Rectangle((1, -1),-2, 2, fill=False))
    if figure == 'Симплекс':
        ax.add_patch(pat.Polygon(([0, 0],[2,0],[0,2]), fill=False))
    #ax.add_patch(pat.Polygon(([0, 0],[4,0],[0,4]), fill=False))
    ax.add_patch(pat.Rectangle((4, -4), -8, 8, fill=False))
    return ax

import time
def showpdd(dx,dy,px,py,figure):
    ax = supshow(figure)
    #ax.scatter(dx, dy, color='green', s=2, zorder=0)
    ax.scatter(px, py, color='red', s=2, zorder=0)
    ax.scatter(dx, dy, color='green', s=2, zorder=0)
    plt.gcf().canvas.flush_events()
    time.sleep(100)
    return 0

def mainshow(population,ro,xi,yi,dx,dy,px,py):

    for i in range(len(population)):
        if sum(xi) == 208:
            if math.sqrt(population[i][3]**2 + population[i][4]**2) > ro:
                None  # Первая популяция
            else:
                dx.append(population[i][3])
                dy.append(population[i][4])
        else:
            if math.sqrt(population[i][3]**2 + population[i][4]**2) > ro and math.sqrt(xi[i]**2 + yi[i]**2) < ro:
                if math.sqrt(population[i][3]**2 + population[i][4]**2) > 0.8:
                    px.append(population[i][3])
                    py.append(population[i][4])
                    # px.append(xi[i])
                    # py.append(yi[i])
            elif math.sqrt(population[i][3]**2 + population[i][4]**2) < ro and math.sqrt(xi[i]**2 + yi[i]**2) > ro:
                if math.sqrt(population[i][3]**2 + population[i][4]**2) > 0.8:
                    px.append(population[i][3])
                    py.append(population[i][4])
                    # px.append(xi[i])
                    # py.append(yi[i])
            elif math.sqrt(population[i][3]**2 + population[i][4]**2) <= ro:
                dx.append(population[i][3])
                dy.append(population[i][4])
            elif math.sqrt(population[i][3]**2 + population[i][4]**2) > ro and math.sqrt(xi[i]**2 + yi[i]**2) > ro:
                None

    for ge in population:
        xi.append(ge[3])
        xi.pop(0)
        yi.append(ge[4])
        yi.pop(0)
    #print(xi)
        #ax = supshow()
        #showpdd

    return dx,dy,px,py,xi,yi

def sqt(ind,ro):
    h = False
    for ge in ind:
        if abs(ge) < ro:
            h = True
        else:
            h = False
            break
    if h:
        return True
    else:
        return False


def mainshow1(population,ro,dx,dy,px,py,temptestS):
    for i in range(len(population)):
        if temptestS[0] == 100:
            if sqt(population[i][3:], ro) == True:
                dx.append(population[i][3])
                dy.append(population[i][4])
        else:
            if sqt(population[i][3:], ro) == True and sqt(temptestS[i], ro) == False:
                if math.sqrt(population[i][4]**2 + population[i][3]**2) > 0.7:
                    px.append(population[i][3])
                    py.append(population[i][4])
            elif sqt(population[i][3:], ro) == False and sqt(temptestS[i], ro) == True:
                if math.sqrt(population[i][4]**2 + population[i][3]**2) > 0.7:
                    px.append(population[i][3])
                    py.append(population[i][4])
            elif sqt(population[i][3:], ro):
                dx.append(population[i][3])
                dy.append(population[i][4])

    return dx,dy,px,py

def fsimp(x,y):
    sumsim=0
    for i in [x,y]:
        if i >= 0:
            sumsim += i
        else:
            return 9999
    return sumsim

def mainshow2(population,ro,xi,yi,dx,dy,px,py):

    for i in range(len(population)):
        if sum(xi) == 208:
            if population[i][2] > ro:
                None  # Первая популяция
            else:
                dx.append(population[i][3])
                dy.append(population[i][4])
        else:
            if population[i][2] > ro and fsimp(xi[i],yi[i]) < ro:
                #if (population[i][3] + population[i][4]) > 1.8:
                    px.append(population[i][3])
                    py.append(population[i][4])
                    # px.append(xi[i])
                    # py.append(yi[i])
            elif population[i][2] < ro and fsimp(xi[i],yi[i]) > ro:
                #if (population[i][3] + population[i][4]) > 1.8:
                    px.append(population[i][3])
                    py.append(population[i][4])
                    # px.append(xi[i])
                    # py.append(yi[i])
            elif population[i][2] <= ro:
                dx.append(population[i][3])
                dy.append(population[i][4])
            elif population[i][2] > ro and fsimp(xi[i],yi[i]) > ro:
                None

    for ge in population:
        xi.append(ge[3])
        xi.pop(0)
        yi.append(ge[4])
        yi.pop(0)
    #print(xi)
        #ax = supshow()
        #showpdd

    return dx,dy,px,py,xi,yi