"""# Calcul des couts
Timeline["passation_cost"] = Timeline["event_type"].apply(lambda x :F if x==3 else 0)
Timeline["Time_gap"] = Timeline["time"].diff(periods=-1)*-1
Timeline["Time_gap"] = Timeline["Time_gap"].apply(lambda x : 0 if math.isnan(x) else x)
Timeline["stock_cost"] = Timeline["stock"]*h * Timeline["Time_gap"]
Timeline["Loss_cost"] = Timeline["perte_magasin"]*p
Timeline["Total_cost"] = Timeline["Loss_cost"]+Timeline["stock_cost"]+Timeline["late_cost"]+Timeline["passation_cost"]
Timeline["Cum_cost"]= Timeline["Total_cost"].cumsum()
Timeline["mean_cost"] = Timeline["Cum_cost"]/Timeline["time"]

#Indicateurs de stock
stock_avg = sum(Timeline["stock"]*Timeline["Time_gap"])/Timeline.loc[i,"time"]

def line_plot(x,serie,col="black",al=1 ,lab = ""):
    plt.plot([0,max(serie)],[x,x],c=col,alpha = al,label = lab)


#Plot the stock
plt.plot(Timeline.time, Timeline.stock,label = "Stock")
line_plot(stock_avg,Timeline.time,"black",0.8,"Average")
line_plot(r,Timeline.time,"red",0.6,"Recommend threshold")
line_plot(K,Timeline.time,"orange",0.6,"Priority threshold")
plt.title("Stock evolution over time")
plt.xlim(0,max(Timeline.time))
plt.ylim(0,max(Timeline.stock)+20)
plt.legend()
plt.show()

#Plot the cost
plt.plot(Timeline.time,Timeline.mean_cost)
plt.show()"""

import numpy as np
import pandas as pd
import math
from os import listdir
from os.path import isfile, join

lambda1 = 15 #Commande hors ligne
lambda2 = 30 #Commande en ligne
L = 1 #Délai de livraison approvisionnement
W=1 # Délai acceptable pour une commande en ligne
F=18 #Cout de passation de commande
h = 0.05 #Cout de stockage
p = 20 #Cout de perte unitaire
b = 5 #Indemnité de retard
Q = 180 #Quantité de commande
r = 60 #Point de recommande
K = 10 #Priorité de classe
K = 60 #Change the value

path = "G:\Mon Drive\COURS\GI06\IF29\Stock_Simulation\Export_stp1"
files = [f for f in listdir(path) if isfile(join(path, f))]
new_path = "G:\Mon Drive\COURS\GI06\IF29\Stock_Simulation\Export_stp2"

for f in files : 
    Timeline = pd.read_csv(path+"\\"+f,index_col=0)
    Timeline.loc[0,"time"]= 0
    Timeline["passation_cost"] = Timeline["event_type"].apply(lambda x :F if x==3 else 0)
    Timeline["Time_gap"] = Timeline["time"].diff(periods=-1)*-1
    Timeline["Time_gap"] = Timeline["Time_gap"].apply(lambda x : 0 if math.isnan(x) else x)
    Timeline["stock_cost"] = Timeline["stock"]*h * Timeline["Time_gap"]
    Timeline["Loss_cost"] = Timeline["perte_magasin"]*p
    Timeline["Total_cost"] = Timeline["Loss_cost"]+Timeline["stock_cost"]+Timeline["late_cost"]+Timeline["passation_cost"]
    Timeline["Cum_cost"]= Timeline["Total_cost"].cumsum()
    Timeline["mean_cost"] = Timeline["Cum_cost"]/Timeline["time"]
    
    Timeline.to_csv(new_path+"\\STP2_"+f)

