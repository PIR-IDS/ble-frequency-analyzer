import csv
import pathlib
import os
from datetime import datetime
from datetime import timezone
 

def data_frequency_in_dico(folder, file_to_read):
    f= open(folder + "/" + file_to_read, "r")
    file = csv.reader(f)
    dico = {}
    for line in file:
        if len(line) != 0:
            if (line[0])[0] == 'A':
                address =(str(line[0][9:]))
                if address not in dico:
                    dico[address]=[]
            if (line[0])[0] == 'T':
                a = datetime.strptime(line[0][6:], '%Y-%m-%dT%H:%M:%S.000Z')
                dico[address].append(int(a.replace(tzinfo=timezone.utc).timestamp()))
    return(dico)

def calcul_frequency(liste):
    new_list = list()
    for i in range(1,len(liste)-1,1):
        a = int(liste[i+1])-int(liste[i])
        new_list.append(a)
    return new_list


def data_rssi_in_dico(folder, file_to_read):
    f= open(folder + "/" + file_to_read, "r")
    file = csv.reader(f)
    dico = {}
    for line in file:
        if len(line) != 0:
            if (line[0])[0] == 'A':
                address =(str(line[0][9:]))
                if address not in dico:
                    dico[address]=[]
            if (line[0])[0] == 'R':
                dico[address].append(int((line[0])[6:]))
    return(dico)


def rssi_analyse(folder, file_to_read, object):
    dico = data_rssi_in_dico(folder, file_to_read)
    d = dico[object][0]
    e = dico[object][-1]
    if d > e:
        return("The object have moved away")
    if e > d:
        return("The object have moved closer")
    return None 


dico = data_rssi_in_dico("./data", "input.txt")
print(dico["5e:6e:ad:bc:8c:57"])
print(calcul_frequency(dico["d0:23:c7:ba:60:c4"]))
print(calcul_frequency(dico["25:23:50:94:3b:f0"]))
print(calcul_frequency(dico["5d:8c:ca:73:fa:83"]))
print(calcul_frequency(dico["51:3a:78:ae:b2:10"]))
print(calcul_frequency(dico["3b:18:53:a9:f6:c3"]))
print(calcul_frequency(dico["5e:6e:ad:bc:8c:57"]))
print(rssi_analyse("./data", "output.txt","5e:6e:ad:bc:8c:57" ))