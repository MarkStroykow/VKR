import pcreate as pc
import random
from random import randint
import matplotlib.pyplot as plt
import matplotlib
import math
import time
import numpy as np
from matplotlib import cm
matplotlib.use('Qt5Agg')
a = 10#5.12 #создание
b = 0.1 #мутация
b2 = -0.1
#random.seed(1)
N = 8 #Длина списка
G = N #Число неравенств
population_size = 20#52 #Кол-во особей
# survivors = [None] * (population_size // 2)
D = 1.5

# class indiv():
#     def __init__(self,individ,ffunk,evk):
#         self.individ = individ
#         self.ffunk=ffunk
#         self.evk=evk


def create_individ(size):
    individ = [None] * size
    for i in range(size):
        individ[i] = random.uniform(-a, a)
        #individ[i] = round(random.uniform(-10, 10),5) #randint(0, 10)
    return individ

def create_population(p_size, i_size):
    population_in_def = [None] * p_size
    for i in range(p_size):
        population_in_def[i] = create_individ(i_size)
    return population_in_def

def evklid(ind_r):
    sumen = 0.
    for i in ind_r:
        sumen +=i**2
    sq=math.sqrt(sumen)
    return sq

def rating(ind_r):
    # if sum(ind_r) == 100:
    #     exit()
    #return pow(sum(ind_r),2)
    sumind = 0.
    sumen = 0.
    for i in ind_r:
        sumind += i**2# - 10 * math.cos(2*math.pi*i) + 10
        sumen +=i**2
    math.sqrt(sumen)
    return sumind #- 330

def sort_population(population):
    size=len(population)
    repeat = True
    while repeat:
        repeat = False
        for i in range(0, size - 1):
            temp = population[i]
            pos1 = rating(temp)
            pos2 = rating(population[i + 1])
            #pos1 = abs(rating(temp))
            #pos2 = abs(rating(population[i+1]))
            if(pos1 > pos2):# and abs(pos1) < D):
                population[i] = population[i+1]
                population[i+1]=temp
                repeat = True
    return population

def print_pop(population,count_omega,count_Aomega):
    i = 0
    temp=0
    #temp2=0
    for individ in population:
        i += 1
        temp=evklid(individ)
        #print(str(i) + '. ' + f'{rating(individ):.15f}' + ': ' + str(individ))
        print(f'{i:2.0f}' + '. ' + f'{rating(individ):.15f}' + ': ' + str(individ) + f'{temp:.15f}')
        if temp < 0.1:
            count_omega +=1
        else:
            count_Aomega +=1
    print('Лучший индивид поколения - ' + str(population[0]))
    print(' Лучший рейтинг поколения: ' + str(rating(population[0])))
    return count_omega,count_Aomega,rating(population[0])

def select(population, survivors):
    size = len(population) // 2
    for i in range(size):
        survivors[i] = population[i]
    return survivors

def get_index(parents, execute_parents):
    size = len(parents)
    while True:
        index = randint(0, size-1)
        #print(index)
        if execute_parents is None or execute_parents != index:
            return index

def cross(individ1, individ2):
    size = len(individ1)
    point = len(individ1)//2
    #point = randint(1, size-2)
    child=[None] * size
    for i in range(point):
        child[i] = individ1[i]
    for j in range(point,size):
        child[j] = individ2[j]
    #print(child)
    return child

def rebild(population, parents, children_counter):
    #cout = 0
    while children_counter < len(population):
        p1_index = get_index(parents, None)
        p2_index = get_index(parents, p1_index)
        mom = parents[p1_index]
        dad = parents[p2_index]
        #print(parents)
        #print(mom, dad)
        population[children_counter] = cross(mom, dad)
        population[children_counter + 1] = cross(dad, mom)
        children_counter += 2
    return population

def mutate(population, chance):
    for i in range(chance):
        # print('***')
        index_ind = randint(0, len(population)-1)
        index_gen = randint(0, len(population[1])-1)
        individ = population[index_ind]
        # print(population[index_ind])
        individ[index_gen] = random.uniform(b2, b)
        #individ[index_gen] = round(random.uniform(-0.01, 0.01),5) #randint(0, 10)
        population[index_ind] =  individ
        # print(individ)

def mutate_child(population, chance):
    for i in range(chance):
        # print('***')
        index_ind = randint(len(population)//2, len(population)-1)
        #print(index_ind)
        index_gen = randint(0, len(population[1])-1)
        individ = population[index_ind]
        # print(population[index_ind])
        individ[index_gen] = random.uniform(b2, b)
        print(individ[index_gen])
        #individ[index_gen] = round(random.uniform(-10, 10),5) #randint(0, 10)
        population[index_ind] =  individ
        # print(individ)







multis = 0
z = []
fi = []
while multis != 1:
    generation = 0
    population = create_population(population_size, N)
    #ogran = create_population(population_size, G)
    survivors = [None] * (population_size // 2)
    end = 0
    x = []
    x9=[]
    y9=[]
    y = [1000]
    delta = 0
    population = sort_population(population)
    best = [None] * N
    count_Aomega=0
    count_omega=0
    #while generation != 100:
    while True:
        sum_R = 0
        generation += 1
        print('Поколение:' + str(generation))
        temp = end
        count_omega,count_Aomega,end = print_pop(population,count_omega,count_Aomega)
        survivors = select(population, survivors)
        rebild(population, survivors, population_size // 2)
        mutate(population, 1)
        population = sort_population(population)
        for i in range(population_size):
             sum_R += rating(population[i])
        sum_R = sum_R//population_size
        if end < y[generation-1]:
            y.append(end)
            best = population[0]
        else:
            y.append(y[generation-1])
        if abs(end - temp) < 0.0000001:
            delta +=1
            print('Дельта: ', delta)
        else:
            delta = 0
        x.append(end)
        if delta == 20:
             break
    multis +=1
    z.append(y[generation-1])
    fi.append(best)

print('Вошлиб не вошли',count_Aomega,count_omega)
y.pop(0)
print('Лучший рейтинг', y[generation-1])
print('Лучший рейтинг', f'{y[generation-1]:.15f}')
print('Лучший индивид', best)
plt.plot(x, color='green')
plt.plot(y, color='red')
plt.xlabel('Поколение')
plt.ylabel('Максимальная приспособленность')

plt.show()
