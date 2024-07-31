import random
import pcreate as pc


def get_index(parents, execute_parents):
    size = len(parents)
    while True:
        index = random.randint(0, size-1)
        if execute_parents is None or execute_parents != index:
            return index

def cross(individ1, individ2):
    size = len(individ1)
    point = (len(individ1)//2)+3
    child=[None] * size
    for i in range(3,point):
        child[i] = individ1[i]
    for j in range(point,size):
        child[j] = individ2[j]
    return child

def select(population):
    size = len(population) // 2
    survivors =[]
    for i in range(size):
        survivors.append(population[i])
    return survivors

def sort_population(population):
    size=len(population)
    #sortP=[]
    # for i in range(0, size):
    #     sortP.append(i)
    repeat = True
    while repeat:
        repeat = False
        for i in range(0, size - 1):
            temp = population[i]
            #tempI = i
            pos1 = population[i][0]
            pos2 = population[i + 1][0]
            if pos1 > pos2:
                population[i] = population[i+1]
                #sortP[i]=sortP[i+1]
                population[i+1]=temp
                #sortP[i+1] = tempI
                repeat = True
    #print(sortP)
    return population



def mutate(population, chance, b):
    for i in range(chance):
        index_ind = random.randint(0, len(population)-1)
        index_gen = random.randint(3, len(population[1])-1)
        individ = population[index_ind]
        individ[index_gen] = individ[index_gen] + random.uniform(-b, b)
        #individ[index_gen] = round(random.uniform(-0.01, 0.01),5) #randint(0, 10)
        population[index_ind] =  individ
    return population

def rebild(population,m,mc,figure):
    parents=select(population) #25
    children_counter = len(population)//2 #25
    while children_counter < len(population):
        p1_index = get_index(parents, None)
        p2_index = get_index(parents, p1_index)
        mom = parents[p1_index]
        dad = parents[p2_index]
        population[children_counter] = cross(mom, dad)
        population[children_counter + 1] = cross(dad, mom)
        children_counter += 2
    return pc.write(mutate(population,mc,m),figure)

