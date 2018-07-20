import os
################################################################
# This code was written by Ji-Sang to run sxdefectalign easily.
# Modified on 20 July 2018
################################################################

def locationLOCPOT(a):
    if 'LOCPOT' in a:
        pass
    else:
        if a[-1] == '/':
            a += 'LOCPOT'
        else:
            a += '/LOCPOT'
    return a

def generateCommand(defect,bulk,center,charge,eps):
    temp = './sxdefectalign --ecut 30 --charge '
    temp += str(charge) + ' '
    temp += ' --eps '
    #temp += ' --tensor '
    temp += str(eps) + ' --center '
    temp += ','.join(list(map(str,center))) + ' --relative --vdef '
    temp += defect + ' --vref '
    temp += bulk + ' --vasp'
    print(temp)
    return temp

#0POSCAR
#1   1.00000000000000
#2    10.0  ... 
#3     0.0  ... 
#4     0.0  ... 
#5   C   ...
#6     8 ...
#7Selective dynamics
#8Direct
#9  0.0 0.0 0.0

def getCenter(folder,atom):
    a = open(folder+'/POSCAR')
    b = a.readlines()
    a.close()

    NIONS = sum(list(map(int,b[6].split())))

    if 'ele' in b[7]:
        pos = 8
    else:
        pos = 7

    if atom == -1:
        atom = atom + NIONS
    print('Position of the selected atom :',b[pos+atom])
    return b[pos+atom].split()

def calcCharge(defect,neutral):
    a = open(defect+'/OUTCAR')
    b = a.readlines()
    a.close()
    ND = 0
    i = 0
    while ND == 0:
        if 'NELECT' in b[i]:
            ND = float(b[i].split()[2])
        else:
            i+=1
    a = open(neutral+'/OUTCAR')
    b = a.readlines()
    a.close()
    NP = 0
    i = 0
    while NP == 0:
        if 'NELECT' in b[i]:
            NP = float(b[i].split()[2])
        else:
            i+=1
    print('NELECT of the neutral system: ',NP)
    print('NELECT of the charged system: ',NP)
    return int(ND-NP)

def returnPot(direction):
    print('Among 0, 1, and 2, you chose: ',direction)
    a = open('vline-eV-a'+str(direction)+'.dat')
    b = a.readlines()
    temp = []
    marker = 0
    i = 0
    while marker == 0:
        if '&' in b[i]:
            marker = i+1
        else:
            i+=1
    for i in range(marker,len(b)):
        t = list(map(float,b[i].split()))
        temp.append(t[2])
    return temp

def execute(defect,neutral,bulk,center,direction):
    print('--------------')
    charge = calcCharge(defect,neutral)
    defect = locationLOCPOT(defect)
    bulk = locationLOCPOT(bulk)
    string = generateCommand(defect,bulk,center,charge,eps)
    os.system(string)

    print('--------------')
    data = returnPot(direction)
    I = int(round(((float(center[direction])-0.5) % 1)*len(data)))
    C = data[I]
    string += ' -C ' + str(C)
    print(string)
    os.system(string)

############################################################
eps = '33.5'
bulk = 'bulk'
############################################################
center = map(float,getCenter(defect,-1))
defect = '1'
neutral = '0'
direction = 0
execute(defect,neutral,bulk,center)