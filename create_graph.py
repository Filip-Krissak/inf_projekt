import matplotlib.pyplot as plt
import numpy as np
import matplotlib as mpl
from unidecode import unidecode
import json

def DataZaRok(data,rok,typGrafu,typNadob):
    grafoveData = [0,0,0,0,0,0,0,0,0,0,0,0]
    for i in range(len(data["data"])):
        if data["data"][i]["date"][:4] == rok:
            if data["data"][i]["date"][5:7] == "01":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[0] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[0] += data["data"][i]["amount"]
                else:
                    grafoveData[0] += data["data"][i]["amount"]
                    
            elif data["data"][i]["date"][5:7] == "02":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[1] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[1] += data["data"][i]["amount"]
                else:
                    grafoveData[1] += data["data"][i]["amount"]

            elif data["data"][i]["date"][5:7] == "03":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[2] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[2] += data["data"][i]["amount"]
                else:
                    grafoveData[2] += data["data"][i]["amount"]

            elif data["data"][i]["date"][5:7] == "04":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[3] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[3] += data["data"][i]["amount"]
                else:
                    grafoveData[3] += data["data"][i]["amount"]

            elif data["data"][i]["date"][5:7] == "05":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[4] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[4] += data["data"][i]["amount"]
                else:
                    grafoveData[4] += data["data"][i]["amount"]

            elif data["data"][i]["date"][5:7] == "06":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[5] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[5] += data["data"][i]["amount"]
                else:
                    grafoveData[5] += data["data"][i]["amount"]

            elif data["data"][i]["date"][5:7] == "07":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[6] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[6] += data["data"][i]["amount"]
                else:
                    grafoveData[6] += data["data"][i]["amount"]

            elif data["data"][i]["date"][5:7] == "08":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[7] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[7] += data["data"][i]["amount"]
                else:
                    grafoveData[7] += data["data"][i]["amount"]

            elif data["data"][i]["date"][5:7] == "09":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[8] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[8] += data["data"][i]["amount"]
                else:
                    grafoveData[8] += data["data"][i]["amount"]

            elif data["data"][i]["date"][5:7] == "10":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[9] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[9] += data["data"][i]["amount"]
                else:
                    grafoveData[9] += data["data"][i]["amount"]

            elif data["data"][i]["date"][5:7] == "11":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[10] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[10] += data["data"][i]["amount"]
                else:
                    grafoveData[10] += data["data"][i]["amount"]

            elif data["data"][i]["date"][5:7] == "12":
                if data["data"][i]["bottle_can"] == True and typNadob == 1:
                    grafoveData[11] += data["data"][i]["amount"]
                elif data["data"][i]["bottle_can"] == False and typNadob == 2:
                    grafoveData[11] += data["data"][i]["amount"]
                else:
                    grafoveData[11] += data["data"][i]["amount"]
    if typGrafu==2:
        for i in range(len(grafoveData)):
            if i==1:
                grafoveData[i]=grafoveData[i]/28
            elif (i<8 and i%2!=0) or (i>7 and i%2==0):
                grafoveData[i]=grafoveData[i]/31
            elif (i<8 and i%2==0) or (i>7 and i%2!=0):
                grafoveData[i]=grafoveData[i]/30
    print(grafoveData)
    return(grafoveData)

def nakresliDataZaRok(data, rok, typGrafu, typNadob):
    fig, ax = plt.subplots()
    if typGrafu==1:
        ax.bar(["január", "február", "marec", "apríl", "máj", "jún", "júl", "august", "september", "október", "november", "december"], data)
        nazovTypGrafu='Celkový počet'
    elif typGrafu==2:
        ax.plot(data)
        ax.set_xticks(np.arange(0, 12), ["január", "február", "marec", "apríl", "máj", "jún", "júl", "august", "september", "október", "november", "december"])
        nazovTypGrafu='Denný priemer'
    
    if typNadob==0:
        nazovNadoby='fliaš a plechoviek'
    elif typNadob==1:
        nazovNadoby='fliaš'
    elif typNadob==2:
        nazovNadoby='plechoviek'

    ax.set_title(nazovTypGrafu + " vhodených " + nazovNadoby + " za rok " + rok + " (v mesiacoch)")
    plt.show()

fileName = "data.json"

with open(fileName, "r") as json_file:
    data = json.load(json_file)

rok=input("Rok:")
print()

print("1: Celkový počet")
print("2: Priemer")
typGrafu=int(input("?"))
print()

print("0: Fľaše a plechovky")
print("1: Fľaše")
print("2: Plechovky")
typNadob=int(input("?"))


nakresliDataZaRok(DataZaRok(data, rok, typGrafu, typNadob), rok, typGrafu, typNadob)