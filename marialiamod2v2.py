import numpy as np
import open3d as o3d
import pandas as pd
from open3d import *
from itertools import groupby
import datetime
from tkinter import filedialog
from tkinter import *
from statistics import *
from matplotlib import pyplot as plt
import csv
from tkinter import messagebox as mbox
import math
from numpy import inf


def grificar(colx,colx1,coly,coly1,colz,colz1):
    now = datetime.datetime.now()
    print ('inicio graficas   ','Hora:  ',now.hour,':',now.minute,':',now.second,'   Ano:',now.day,'/',now.month,'/',now.year,'/')
    plt.ioff()
    plt.plot([colx,colx1],[coly,coly1],'k-')
    plt.title('  x vs y  ')
    plt.show(block=False)
    #plt.plot([coly,coly1],[colz,colz1],'k-')
    #plt.title('  y vs z  ')
    #plt.show()
    #plt.plot([colx,colx1],[colz,colz1],'k-')
    #plt.title('  x vs z  ')
    #plt.show()
    #f,axs  = plt.subplots(2, 2)
    #axs[0,0].plot([colx,colx1],[coly,coly1])
    #axs[0,0].set_title('  x vs y  ')
    #axs[0,1].plot([coly,coly1],[colz,colz1])
    #axs[0,1].set_title('  y vs z  ')
    #axs[1,0].plot([colx,colx1],[colz,colz1])
    #axs[1,0].set_title('  x vs z  ')
    #plt.show(block=False)

    
    #print("diferencua")
    #print(' elevacion   ',(coly1-coly))
    #print(' avanco      ',(colx1-colx))
    m=((coly1-coly)/(colx1-colx))
    print('tipo pendiente  ', type(m))
    m = m.astype(float)
    print('tipo pendiente  ', type(m))
    mnan=m.replace([np.inf, -np.inf], np.nan)
    m=m.dropna().values
    mrad=np.arctan(m) * 180 / np.pi
    mrad[mrad == -inf] = 0
    mrad[mrad == inf] = 0
    mrad[~np.isnan(mrad)]
    #print('pendiente    ',m,'atan  ',mrad)
    
    slopes = pd.DataFrame()
    slopes['calculo num']=m
    slopes['angle']=mrad
    slopes.head()
    print(slopes)
    print('max rad  ',max(mrad),'  minimo rad ', min(mrad))
    #print(mnan.max(axis = 0, skipna = True))
    #print(mnan.min(axis = 0, skipna = True))
    #mnan=mrad.replace([np.inf, -np.inf], np.nan)
    #print('ree  ',mz1)
    #print('max mz1  ',max(mz1),min(mz1))
    #print(" antes de cluster")
    now = datetime.datetime.now()
    print ('inicio estadistica e graficas   ','Hora:  ',now.hour,':',now.minute,':',now.second,'   Ano:',now.day,'/',now.month,'/',now.year,'/')
    #https://docs.python.org/3/library/statistics.html
    #decils..
    #print('pendiente m ',type(m))
    #print('max v1  ',max(m),min(m))
    md=pd.DataFrame()
    #md=m.to_frame()
    #quantile(md)
    #print('after drop nan ')
    #print(md)
    #print('max v1  ',max(md),min(md))
    
    mnanv1=mnan.dropna().values
    #print('after drop nan ',mnan)
    #print('after drop nan ',mnanv1)
    #print('pendiente md ',type(mnanv1))
    #print('max v2 ',max(mnanv1),min(mnanv1))
    print('analisis frequencia ')
    fig = plt.figure('Freq angulos')
    hist, bin_edges = np.histogram(mrad, bins=10)
    print(hist)
    print(bin_edges)
    plt.ioff()
    plt.hist(mrad, bins = 10)
    # Add title and axis names
    #plt.title('Freq angulos')
    plt.xlabel('rangos')
    plt.ylabel('quantidade')
    plt.show(block=False)
    print(" depois de cluster")
    now = datetime.datetime.now()
    print (now.year, now.month, now.day, now.hour, now.minute, now.second)
    shiftx=int(colx[0]/100)*100
    shifty=int(coly[0]/100)*100
    colxadj=colx-shiftx;
    colyadj=coly-shifty;
    recx=colxadj.to_numpy()
    recy=colyadj.to_numpy()
    recz=colz.to_numpy()
    vas=[recx,recy,recz]
    vasa=np.array(vas)
    





root = Tk()
root.filename = filedialog.askopenfilename(initialdir = "/",title = "Select polinlinha file",filetypes = [("polilinhas","*.csv")])
print (root.filename)
#point_cloud = pd.read_csv(root.filename,delimiter=",", header=0)
point_cloud = pd.read_csv(root.filename,delimiter=";", header=0)
shape = point_cloud.shape
print('tamanho primera tentativa delimitador ";"  ',shape)
if (shape[1]<=1):
    point_cloud = pd.read_csv(root.filename,delimiter=",", header=0)
    shape = point_cloud.shape
    print('tamanho segunda tentativa delimitador ","    ',shape)
    

now = datetime.datetime.now()
print ('apertura arquivo   ','Hora:  ',now.hour,':',now.minute,':',now.second,'   Ano:',now.day,'/',now.month,'/',now.year,'/')
#print(point_cloud)  #informacao arquivo
size = point_cloud.size
shape = point_cloud.shape
print('tamaño   ',size,'  shape  ', shape,'columnas  ',shape[1],' linhas  ',len(point_cloud))
print(' ')
print(' ')
print(' ')
now = datetime.datetime.now()
print ('pos apertura archivo   ','Hora:  ',now.hour,':',now.minute,':',now.second,'   Ano:',now.day,'/',now.month,'/',now.year,'/')
#print('csv ',point_cloud)
#df=pd.DataFrame(point_cloud)
df=point_cloud
#print(' tipo variable  ',type(df),' longitud ', len(df))    #verificacao
visualdf = df[df.columns[1:10]]
print('extracao informacao linhas')
#print(visualdf)
float_array = visualdf.astype(float)
#print(" captura dados")
colx=df[visualdf.columns[2]].astype(float)
#print(type(colx),' dimension   ')
#print('   columns  ',colx)
coly=df[visualdf.columns[3]].astype(float)
colz=df[visualdf.columns[4]].astype(float)
#print('columna1')
#print([colx,coly, colz])
colx1=df[visualdf.columns[5]].astype(float)
coly1=df[visualdf.columns[6]].astype(float)
colz1=df[visualdf.columns[7]].astype(float)
avancox=colx1-colx
avancoy=coly1-coly
avancoz=colz1-colz
davancox=np.sum(avancox)
davancoy=np.sum(avancox)
davancoz=np.sum(avancox)
#print('tipo variable avancox  ',type(avancox))
#print('deltax :',davancox,' deltay  ', davancoy,' deltaz  ', davancoz)
#print('contagem   ',avancox.value_counts())
#print('maximo contagem    ',max(avancox.value_counts()),' 8% total registros  ', size*0.08)
if (max(avancox.value_counts())> size*.08):
       mbox.showwarning('Warning Message','os dados fornecidos nao contem informacao')
       print('informacao com erros')
       
else:
    #mbox.showwarning('Python','continuar.')
    #print("pontos capturados")
    grificar(colx,colx1,coly,coly1,colz,colz1)


