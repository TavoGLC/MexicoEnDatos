# -*- coding: utf-8 -*-
"""

@author: TavoGLC

-México en datos-

"""

###############################################################################
#                    Importando Paquetes a utilizar 
###############################################################################

import numpy as np
import pandas as pd 
import geopandas as gp

import matplotlib.pyplot as plt

###############################################################################
#                   Funciones de Estilo de las Gráficas  
###############################################################################

#Estilo general de las gráficas
def PlotStyle(Axes,Title):
    
    Axes.spines['top'].set_visible(False)
    Axes.spines['right'].set_visible(False)
    Axes.spines['bottom'].set_visible(True)
    Axes.spines['left'].set_visible(True)
    Axes.xaxis.set_tick_params(labelsize=14)
    Axes.yaxis.set_tick_params(labelsize=14)
    Axes.set_title(Title)
    
    
#Estilo General de los mapas 
def MapStyle(Axes,Title):
    
    Axes.spines['top'].set_visible(False)
    Axes.spines['right'].set_visible(False)
    Axes.spines['bottom'].set_visible(False)
    Axes.spines['left'].set_visible(False)
    Axes.set_xticks([])
    Axes.set_yticks([])
    Axes.set_title(Title)

###############################################################################
#                      Gráficas de los datos  
###############################################################################

GlobalDirectory= "Aquí es donde esta la dirección de los datos"
CurrentData=GlobalDirectory+'\\'+"Aquí se pone el nombre del archivo"

shpFile="Aquí es donde se pone la dirección del archivo shp del mapa de méxico"

DataFrame=pd.read_csv(CurrentData)
ColNames=list(DataFrame.columns.values)


plt.figure(1)

cData=list(DataFrame[ColNames[3]])
Colors=plt.cm.viridis(np.linspace(0, 1,25),alpha=1)

ax=plt.gca()
N, bins, patches = ax.hist(cData, bins=25,edgecolor='white', linewidth=1)

ax.set_xlabel(ColNames[3],fontsize=14,fontweight='bold')
ax.set_ylabel('Frecuencia',fontsize=14,fontweight='bold')

for i in range(len(patches)):
    
    patches[i].set_facecolor(Colors[i])

PlotStyle(ax,'')

plt.figure(2,figsize=(14,5))

DataFrame.groupby(ColNames[1])[ColNames[3]].mean().plot(kind='bar',color=plt.cm.viridis(np.linspace(0, 1,33),alpha=1))

ax=plt.gca()

ax.set_xlabel(ColNames[1],fontsize=14,fontweight='bold')
ax.set_ylabel(ColNames[3],fontsize=14,fontweight='bold')

PlotStyle(ax,'')

###############################################################################
#                                 Mapas 
###############################################################################

Data=list(DataFrame.groupby(ColNames[1])[ColNames[4]].mean())
Order=[1,2,18,14,0,11,22,13,15,17,6,8,16,31,3,21,23,29,12,20,27,4,26,5,7,25,9,32,24,19,28,30]

OrderedData=[Data[val] for val in Order]

MaxVal=max(OrderedData)
ScaledVals=pd.DataFrame({'Data':[val/MaxVal for val in OrderedData]})

shapes = gp.read_file(shpFile)

nShp=shapes.join(ScaledVals)

plt.figure(1)

nShp.plot(edgecolor='black',column='Data',cmap='viridis',figsize=(12,12))

ax=plt.gca()
MapStyle(ax,'')

