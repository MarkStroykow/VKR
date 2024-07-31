import pcreate as pc
import psurce as ps
import showp as sh
import pcount as pt
import math
P = 52
a = 4
m = 0.3
mc = 26
ro = 1

def print_p(population):
    i=0
    for individ in population:
        i += 1
        print(f'{i:2.0f}' + '. ' + str(individ[0]) + ': ' + str(individ[3:]))
    print('\n')
    return 0

def dispscore(ary,n,mid):
    disp=0
    for i in ary:
        disp += (i - mid)**2
    return disp/(n)

def omegas(dtary,pdtary,m):
    print('Дт', sum(dtary) / m, 'ПДт', sum(pdtary) / m)
    ddtary = dispscore(dtary, m, sum(dtary) / m)
    dpdtary = dispscore(pdtary, m, sum(pdtary) / m)
    print('Разнообразие мн. Дт:', ddtary)
    print('СКО Дт:',math.sqrt(ddtary),'СКО ПДт:', math.sqrt(dpdtary))
    print()

    return 0

names=['Гипершар','Гиперкуб','Симплекс']
V = 2

while V < 9:
    # md = []
    # mp = []
    # sd = []
    # sp = []
    # mm = []
    for figure in names:
        print(figure)
        print('|X| = ', V)
        dtc = []
        pdtc = []
        multis = 0
        while multis != 100:
            multis +=1
            population = pc.write(pc.create(V,P,a),figure)
            temp = 0
            delta= 0
            dx,dy,px,py = [],[],[],[]
            xi,yi=[4]*P,[4]*P
            countdt=0
            countpdt=0
            te=[100]*P
            ts=[100]*P
            tempS=[100]*P
            temptestS=[100]*P
            de = 0
            while de != 99:
                de+=1
                population = ps.rebild(population,m,mc,figure)
                population = ps.sort_population(population)

                if abs(population[0][0] - temp) < 0.0000001:
                    delta += 1
                    # print('Дельта: ', delta)
                else:
                    delta = 0
                if delta == 1000:
                    break
                #print_p(population)


                temp = population[0][0]
                if figure == 'Гипершар':
                    #sh.mainshow(population,ro,xi,yi,dx,dy,px,py) #Круг
                    countdt,countpdt,te = pt.countcircle(population,ro,te,countdt,countpdt)
                if figure == 'Гиперкуб':
                    #sh.mainshow1(population, ro, dx, dy, px, py,temptestS) #Квадрат
                    countdt, countpdt = pt.countsquare(population, ro, countdt, countpdt, tempS)
                if figure == 'Симплекс':
                    #sh.mainshow2(population, ro+ro, xi, yi, dx, dy, px, py)#Треугольник
                    countdt, countpdt, ts = pt.counttringle(population, ro+ro, ts, countdt, countpdt)
                for i in range(P):
                    tempS.append(population[i][3:])
                    tempS.pop(0)
                for i in range(P):
                    temptestS.append(population[i][3:])
                    temptestS.pop(0)
            #print('Дт', len(dx), 'ПДт', len(px))
            #print('Дт', countdt, 'ПДт', countpdt)
            if figure == 'Гипер111шар':
                print('Дт', len(dx), 'ПДт', len(px))
                print('Дт', countdt, 'ПДт', countpdt)
                sh.showpdd(dx, dy, px, py,figure)

            #sh.showpdd(dx, dy, px, py)
            dtc.append(countdt)
            pdtc.append(countpdt)

        omegas(dtc, pdtc, multis)
        #md.append(sum(dtc) / multis)
        #mp.append(sum(pdtc) / multis)
        #sd.append(math.sqrt(dispscore(dtc, multis, sum(dtc) / multis)))
        #sp.append(math.sqrt(dispscore(pdtc, multis, sum(pdtc) / multis)))
        #mm.append(dispscore(dtc, multis, sum(dtc) / multis))



    V += 2
    #print(md,'\n',sd,'\n',mp,'\n',sp,'\n',mm)


