import math


# def countcircle(population,ro,xc,yc,countdtc,countpdtc):
#
#     for i in range(len(population)):
#         if sum(xc) == 208:
#             if math.sqrt(population[i][3]**2 + population[i][4]**2) > r o:
#                 None  # Первая популяция
#             else:
#                 countdtc+=1
#         else:
#             if math.sqrt(population[i][3]**2 + population[i][4]**2) > ro and math.sqrt(xc[i]**2 + yc[i]**2) < ro:
#                 if math.sqrt(population[i][3]**2 + population[i][4]**2) > 1.8:
#                     countpdtc+=1
#             elif math.sqrt(population[i][3]**2 + population[i][4]**2) < ro and math.sqrt(xc[i]**2 + yc[i]**2) > ro:
#                 if math.sqrt(population[i][3]**2 + population[i][4]**2) > 1.8:
#                     countpdtc+=1
#             elif math.sqrt(population[i][3]**2 + population[i][4]**2) <= ro:
#                 countdtc+=1
#             elif math.sqrt(population[i][3]**2 + population[i][4]**2) > ro and math.sqrt(xc[i]**2 + yc[i]**2) > ro:
#                 None
#
#     for ge in population:
#         xc.append(ge[3])
#         xc.pop(0)
#         yc.append(ge[4])
#         yc.pop(0)
#
#
#     return countdtc,countpdtc,xc,yc

def countcircle(population,ro,tempE,countdtc,countpdtc):

    for i in range(len(population)):
        if sum(tempE) == 5200:
            if population[i][1] > ro:
                None  # Первая популяция
            else:
                countdtc+=1
        else:
            if population[i][1] > ro and tempE[i] < ro:
                if population[i][1] > 0.8:
                #if population[i][1] > 0:
                    countpdtc+=1
            elif population[i][1] < ro and tempE[i] > ro:
                if population[i][1] > 0.8:
                #if population[i][1] > 0:
                    countpdtc+=1
            elif population[i][1] <= ro:
                countdtc+=1
            elif population[i][1] > ro and tempE[i] > ro:
                None

    for ge in population:
        tempE.append(ge[1])
        tempE.pop(0)


    return countdtc,countpdtc,tempE

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


def countsquare(population,ro,countdts,countpdts,tempS):
    for i in range(len(population)):
        if tempS[0] == 100 :
            if sqt(population[i][3:],ro) == True:
                countdts+=1
        else:
            if sqt(population[i][3:],ro) == True and sqt(tempS[i],ro) == False:
                countpdts += 1
            elif sqt(population[i][3:], ro) == False and sqt(tempS[i], ro) == True:
                countpdts += 1
            elif sqt(population[i][3:], ro):
                countdts += 1

    return countdts,countpdts

def counttringle(population,hr,tempS,countdtt,countpdtt):
    for i in range(len(population)):
        if sum(tempS) == 5200:
            if population[i][2] > hr:
                None  # Первая популяция
            else:
                countdtt+=1
        else:
            if population[i][2] > hr and tempS[i] < hr:
                #if population[i][2] > 1.8:
                #if population[i][1] > 0:
                    countpdtt+=1
            elif population[i][2] < hr and tempS[i] > hr:
                #if population[i][2] > 1.8:
                #if population[i][1] > 0:
                    countpdtt+=1
            elif population[i][2] <= hr:
                countdtt+=1
            elif population[i][2] > hr and tempS[i] > hr:
                None

    for ge in population:
        tempS.append(ge[2])
        tempS.pop(0)


    return countdtt,countpdtt,tempS
