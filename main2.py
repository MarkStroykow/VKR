import pcreate as pc


import random
import math
import matplotlib.pyplot as plt
import matplotlib.patches as pat
import matplotlib
import numpy as np

matplotlib.use('Qt5Agg')
Vs=0
Vc=0
Vt=0
multis = 1
a = 4
N = 2#Вектор варируемых значений
I = 16
P = 52#Размер популяции
b = 0.5#Мутация
cha=26
ro = 2#Радиус ограничения
#random.seed(0)
#Создание популяции
# def p_create(p_size, i_size):
#     population_in_def = [None] * p_size
#     for i in range(p_size):
#         population_in_def[i] = i_create(i_size)
#     return population_in_def
# #Создание индивида
# def i_create(size):
#     individ = [None] * (size+3)
#     for i in range(size):
#         individ[i+3] = random.uniform(-a, a)
#         # individ[i] = round(random.uniform(-10, 10),5) #randint(0, 10)
#     return individ

# def print_p(population):
#     i=0
#     temp=[]
#     for individ in population:
#         temp.append(evklid(individ[3:]))
#         i += 1
#         print(f'{i:2.0f}' + '. ' + str(individ[0]) + ': ' + str(individ[3:]))
#     print('\n')
#     return temp, population[0][0]

# def ff(ind_r):
#     sumind = 0.
#     for i in ind_r:
#         sumind += i**2
#     if math.sqrt(sumind) > 2:
#         return sumind
#     else:
#         return 0
#
# def evklid(ind_r):
#     sumen = 0.
#     for i in ind_r:
#         sumen +=i**2
#     sq = math.sqrt(sumen)
#     return sq
#
# def fsimp(individ):
#     sumsim=0
#     for i in individ:
#         sumsim += i
#     return sumsim
#
# def write_f(individ):
#     individ[0]=ff(individ[3:])
#     individ[1]=math.sqrt(individ[0])
#     #individ[1]=evklid(individ[3:])
#     individ[2]=fsimp(individ[3:])
#     return individ

# def sort_population(population):
#     size=len(population)
#     for i in range(size):
#         write_f(population[i])
#     repeat = True
#     while repeat:
#         repeat = False
#         for i in range(0, size - 1):
#             temp = population[i]
#             pos1 = population[i][0]
#             pos2 = population[i + 1][0]
#             if pos1 > pos2:
#                 population[i] = population[i+1]
#                 population[i+1]=temp
#                 repeat = True
#     return population

# def select(population, survivors):
#     size = len(population) // 2
#     for i in range(size):
#         survivors[i] = population[i]
#     return survivors

# def get_index(parents, execute_parents):
#     size = len(parents)
#     while True:
#         index = random.randint(0, size-1)
#         if execute_parents is None or execute_parents != index:
#             return index
#
# def cross(individ1, individ2):
#     size = len(individ1)
#     point = (len(individ1)//2)+3
#     child=[None] * size
#     for i in range(3,point):
#         child[i] = individ1[i]
#     for j in range(point,size):
#         child[j] = individ2[j]
#     return child
#
# def rebild(population, parents, children_counter):
#     while children_counter < len(population):
#         p1_index = get_index(parents, None)
#         p2_index = get_index(parents, p1_index)
#         mom = parents[p1_index]
#         dad = parents[p2_index]
#         population[children_counter] = cross(mom, dad)
#         population[children_counter + 1] = cross(dad, mom)
#         children_counter += 2
#     return population

# def mutate(population, chance):
#     for i in range(chance):
#         # print('***')
#         index_ind = random.randint(0, len(population)-1)
#         index_gen = random.randint(3, len(population[1])-1)
#         individ = population[index_ind]
#         # print(population[index_ind])
#         individ[index_gen] = individ[index_gen] + random.uniform(-b, b)
#         #individ[index_gen] = round(random.uniform(-0.01, 0.01),5) #randint(0, 10)
#         population[index_ind] =  individ
#         # print(individ)

def dispscore(ary,n,mid):
    #print(mid)
    disp=0
    for i in ary:
        disp += (i - mid)**2
        #print(i)
        #print(disp)
    #disp /=n-1
    return disp/(n)

# def print_pfr(population):
#     size = len(population)
#     for i in range(size):
#         write_f(population[i])
#     i=0
#     for individ in population:
#         i += 1
#         print(f'{i:2.0f}' + '. ' + str(individ[0]) + ': ' + str(individ[3:]))
#     print('\n')
import time
def showfast(ax, xgrid, ygrid, f,xga,yga):
    ptMins = [[0.0, 0.0]]
    ax.clear()
    ax.contour(xgrid, ygrid, f)
    ax.scatter(*zip(*ptMins), marker='X', color='red', zorder=1)
    ax.scatter(xga,yga, color='green', s=2, zorder=0)
    plt.draw()
    plt.gcf().canvas.flush_events()
    #time.sleep(1)

def show(ax, xgrid, ygrid, f,xga,yga,r):
    #ptMins = [[0.0, 0.0]]
    #ax.clear()
    ax.contour(xgrid, ygrid, f)
    #ax.scatter(*zip(*ptMins), marker='o', color='green', zorder=1)
    for i in range(len(xga)):
        if math.sqrt(xga[i]**2+yga[i]**2) > r:
            ax.scatter(xga[i], yga[i], color='red', s=2, zorder=0)
        else:
            ax.scatter(xga,yga, color='yellow', s=2, zorder=0)
    #plt.draw()
    plt.gcf().canvas.flush_events()
    #time.sleep(1)

# def showpdd(ax, xgrid, ygrid, f,xga,yga,r,tX,tY,ship):
#     #ax.clear()
#     #ptMins = [[0.0, 0.0]]
#     #ax.contour(xgrid, ygrid,f)
#     #ax.contour([4,-4], [4,-4], f)
#     #ax.scatter(*zip(*ptMins), marker='o', color='green', zorder=1)
#     ship += 1
#     if tX == tY:
#         for i in range(len(xga)):
#             if math.sqrt(xga[i]**2+yga[i]**2) > r:
#                 None#Первая популяция
#             else:
#                 ax.scatter(xga[i],yga[i], color='green', s=2, zorder=0)
#     else:
#         for i in range(len(xga)):
#             if math.sqrt(xga[i]**2+yga[i]**2) > r and math.sqrt(tX[i]**2+tY[i]**2) < r:
#                 if math.sqrt(xga[i]**2+yga[i]**2) < 1.7:
#                     None
#                 else:
#                     ax.scatter(xga[i], yga[i], color='red', s=2, zorder=0)
#                 #ax.scatter(tX[i], tY[i], color='red', s=2, zorder=0)
#             elif math.sqrt(xga[i]**2+yga[i]**2) < r and math.sqrt(tX[i]**2+tY[i]**2) > r:
#                 if math.sqrt(xga[i]**2+yga[i]**2) < 1.7:
#                     None
#                 else:
#                     ax.scatter(xga[i], yga[i], color='red', s=2, zorder=0)
#                 #ax.scatter(tX[i], tY[i], color='red', s=2, zorder=0)
#             elif math.sqrt(xga[i]**2+yga[i]**2) <= r:
#                 ax.scatter(xga[i], yga[i], color='green', s=2, zorder=0)
#             elif math.sqrt(xga[i] ** 2 + yga[i] ** 2) > r and math.sqrt(tX[i] ** 2 + tY[i] ** 2) > r:
#                 None
#     #plt.draw()
#     plt.gcf().canvas.flush_events()
#     if tX == tY:
#         time.sleep(2)
#
#     tempX = xga
#     tempY = yga
#     #time.sleep(1)
#     return ship, tempX, tempY

# def supshow():
#
#     x = np.arange(-4,4,0.1)
#     y = np.arange(-4,4,0.1)
#     xgrid, ygrid = np.meshgrid(x, y)
#     funk = xgrid**2+ygrid**2
#     plt.ion()
#     fig, ax = plt.subplots()
#     fig.set_size_inches(6, 6)
#
#     ax.set_xlim(-4.5, 4.5)
#     ax.set_ylim(-4.5, 4.5)
#     ax.add_patch(pat.Circle((0, 0), 2,fill=False))
#     ax.add_patch(pat.Rectangle((4, -4), -8, 8, fill=False))
#     return ax, xgrid, ygrid, funk
#
#
# ax, xgrid, ygrid, funk = supshow()
matplotlib.use('Qt5Agg')
while N < 9:
    print('Для |X| = ', N)
    dS = (ro / (pow(P, 1 / N))) * math.sqrt(N)
    #print(dS)
    countmultis = 0
    sumCircleAo = []
    sumCircleo = []
    sumCubeAo = []
    sumCubeo = []
    sumTringleAo = []
    sumTringleo = []
    mn = 0
    testcircle=[]
    while countmultis != multis:
        shipa = 0
        tempX=[]
        tempY=[]
        generation = 0
        population = p_create(P, N)
        survivors = [None] * (P // 2)
        all_E=[a]*P
        all_S=[a]*P
        #print('Множество S')
        print_p(population)
        Circle_omega, Circle_Aomega= 0,0
        Cube_omega, Cube_Aomega = 0,0
        Tringle_omega, Tringle_Aomega = 0,0
        delta,temp = 0,0
        tempP=[[a]*P]*P
        while True:
            xg = []
            yg = []
            # sort_population(population)
            # if abs(population[0][0] - temp) < 0.0000001:
            #     delta += 1
            #     #print('Дельта: ', delta)
            # else:
            #     delta = 0
            temp_Cube_omega,temp_Cube_Aomega=0,0
            for i in range(P): #омеги по гиперкубу
                for j in range(N):
                    if abs(tempP[i][j+3]) > ro and abs(population[i][j+3]) < ro:
                        temp_Cube_Aomega +=1
                    elif abs(tempP[i][j+3]) < ro and abs(population[i][j+3]) > ro:
                        temp_Cube_Aomega +=1
                    elif abs(population[i][j+3]) <= ro:
                        temp_Cube_omega +=1
            Cube_omega += (temp_Cube_omega//N)//2
            Cube_Aomega +=(temp_Cube_Aomega//N)//2
            #show(ax, xgrid, ygrid, funk,xg,yg,ro)
            #showfast(ax, xgrid, ygrid, funk, xg, yg)
            for i in range(P): #Омеги по треугольнику
                if all_E[i] < ro and population[i][2] > ro:
                    Tringle_Aomega += 1
                elif all_E[i] > ro and population[i][2] < ro:
                    Tringle_Aomega += 1
                elif population[i][2] <= ro:
                    Tringle_omega +=1
            all_S = []
            for i in range(P):
                all_S.append(population[i][2])
            for i in range(P): #Омеги по шару
                tempE=evklid(population[i][3:])

                if all_E[i] < ro and tempE > ro:
                    Circle_Aomega += 1
                elif all_E[i] > ro and tempE < ro:
                    Circle_Aomega += 1
                elif tempE <= ro:
                    Circle_omega +=1
#            print('Поколение: ',generation)
            all_E,temp = print_p(population)
            tempP=population
            survivors = select(population, survivors)
            #rebild(population, survivors, P // 2)
            #mutate(population, cha)
            generation+=1

            # if delta == 70:
            #     break
            for ge in range(P//2):
                yg.append(survivors[ge][4])
                xg.append(survivors[ge][3])
            #print(yg,xg)
            shipa,tempX,tempY=showpdd(ax, xgrid, ygrid, funk, xg, yg, ro,tempX,tempY,shipa)
        #print(all_E)
        #print('Поколение: ', generation)
        #print('Circle_Aomega,Circle_omega: ',Circle_Aomega,Circle_omega)
        #mn += generation*20
        sumCircleAo.append(Circle_Aomega)
        sumCircleo.append(Circle_omega)
        sumCubeAo.append(Cube_Aomega)
        sumCubeo.append(Cube_omega)
        sumTringleAo.append(Tringle_Aomega)
        sumTringleo.append(Tringle_omega)
        print(countmultis)
        countmultis += 1
        testcircle.append(sum(sumCircleo)/countmultis)

        #skoAo += Circle_Aomega**2
    #print(sumCircleAo)
    #print(sumCircleo)
    # if N == 2:
    #     Vs=3.1416*(ro**2)
    # if N == 4:
    #     Vs=4.9348*(ro**4)
    # if N == 6:
    #     Vs=5.1677*(ro**6)
    # if N == 8:
    #     Vs=4.0587*(ro**8)
    # Vc=ro**N
    # Vt=0.5*(ro**N)
    #print_pfr(population)

    # plt.plot(sumCircleo,'green')
    # plt.plot(sumCircleAo, 'red')
    # plt.plot(testcircle, 'yellow')
    # plt.show()
    print('ready stop')
    print(generation)
    time.sleep(100)
    print('Гиперфсфера')
    print('Среднее по мультистарту нормированное число найденных ДТ,ПДТ', sum(sumCircleo)/multis, sum(sumCircleAo)/multis)
    dispo = dispscore(sumCircleo,multis,sum(sumCircleo)/multis)
    skoo = math.sqrt(dispo)
    skoAo = math.sqrt(dispscore(sumCircleAo,multis,sum(sumCircleAo)/multis))
    print('ско Д. ско ПД', skoo,skoAo)
    print('Дисп', dispo)
    print()
    print('Гиперкуб')
    print('Среднее по мультистарту нормированное число найденных ДТ,ПДТ', sum(sumCubeo) / multis, sum(sumCubeAo) / multis)
    dispo = dispscore(sumCubeo, multis, sum(sumCubeo) / multis)
    skoo = math.sqrt(dispo)
    skoAo = math.sqrt(dispscore(sumCubeAo, multis, sum(sumCubeAo) / multis))
    print('ско Д. ско ПД', skoo, skoAo)
    print('Дисп', dispo)
    print()
    print('Симплекс')
    print('Среднее по мультистарту нормированное число найденных ДТ,ПДТ', sum(sumTringleo) / multis, sum(sumTringleAo) / multis)
    dispo = dispscore(sumTringleo, multis, sum(sumTringleo) / multis)
    skoo = math.sqrt(dispo)
    skoAo = math.sqrt(dispscore(sumTringleAo, multis, sum(sumTringleAo) / multis))
    print('ско Д. ско ПД', skoo, skoAo)
    print('Дисп', dispo)
    print()
    N+=9

    plt.show()
    #time.sleep(5)