import random
import math


def p_create(p_size, i_size,t):
    population_in_def = [None] * p_size
    for i in range(p_size):
        population_in_def[i] = i_create(i_size,t)
    return population_in_def

def i_create(size,a):
    individ = [None] * (size+3)
    for i in range(size):
        individ[i+3] = random.uniform(-a, a)   # +7 сделать на ост штуки поставить 3:
        # individ[i] = round(random.uniform(-10, 10),5) #randint(0, 10)
    return individ

def create(V, N, II):
    return p_create(N, V, II)



def ffc(ind_r):
    sumind = 0.
    for i in ind_r:
        sumind += i**2
    if math.sqrt(sumind) > 1:
        return sumind
    else:
        return 0

def sqt(ind):
    h = False
    for ge in ind:
        if abs(ge) < 1:
            h = True
        else:
            h = False
            break
    if h:
        return True
    else:
        return False

def ffs(ind_r):
    sumind = 0.
    #bo = sqt(ind_r)
    for i in ind_r:
        sumind += i**2
    if sqt(ind_r):
        #print(ind_r)
        return 0
    else:
        return sumind

def trg(ind):
    h = False
    for ge in ind:
        if ge > 0:
            h = True
        else:
            h = False
            break
    if h:
        #print(sum(ind))
        return sum(ind)
    else:
        return 9999

def fft(ind_r):
    sumind = 0.
    for i in ind_r:
        sumind += i**2
    if trg(ind_r) > 2:
        return sumind
    else:
        #print(ind_r)
        return 0

def evklid(ind_r):
    sumen = 0.
    for i in ind_r:
        sumen +=i**2
    sq = math.sqrt(sumen)
    return sq

def fsimp(individ):
    sumsim=0
    for i in individ:
        if i >= 0:
            sumsim += i
        else:
            return 9999
    return sumsim

def write_f(individ,figure):
    if figure == 'Гипершар':
        individ[0]=ffc(individ[3:])
    elif figure == 'Гиперкуб':
        individ[0]=ffs(individ[3:])
    elif figure == 'Симплекс':
        individ[0]=fft(individ[3:])
    #individ[1]=math.sqrt(individ[0])
    individ[1]=evklid(individ[3:])
    individ[2]=fsimp(individ[3:])
    return individ

def write(population,figure):
    for i in range(len(population)):
        population[i] = write_f(population[i],figure)
    return population