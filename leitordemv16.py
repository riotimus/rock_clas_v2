import numpy as np
import open3d as o3d
import pandas as pd
from open3d import *


from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("data files","*.txt"),("all files","*.xyz")))
print (root.filename)
point_cloud = pd.read_csv(root.filename,delimiter=" ", header=None)
print('len',len(point_cloud))
#print('csv ',point_cloud)
df=pd.DataFrame(point_cloud)
visualdf = df[df.columns[0:3]]
#print('quantidade cols sem cabecerp  orig' ,len(df.columns),' quantidade linhas orig' ,len(df))
#print(type(df.values))
float_array = visualdf.astype(float)
#print(type(float_array))
#print((float_array))
colx=df[df.columns[0]].astype(float)
coly=df[df.columns[1]].astype(float)
colz=df[df.columns[2]].astype(float)
#print('columna1')
#print(colx)
#print('columna2')
#print(coly)
shiftx=int(colx[0]/100)*100
shifty=int(coly[0]/100)*100
#print(int(shiftx/100)*100)
#print(int(shifty/100)*100)
#print('  fftghr   ',shiftx,'  tipo var ',type(shiftx), 'jkjrkjsrkj',shifty,'  tipo var ',type(shifty) )
#print('len',len(df1.values))
#o3d.visualization.draw_geometries([df1.values])
colxadj=colx-shiftx;
colyadj=coly-shifty;
#print('columna1 ajustadas')
#print(type(colxadj))
recx=colxadj.to_numpy()
recy=colyadj.to_numpy()
recz=colz.to_numpy()
#print(colxadj)
#recx=colxadj.to_frame()
#print(type(recx))
#print(recx)
#print(recy)
#print(recz)
vas=[recx,recy,recz]
vasa=np.array(vas)
#print(vas,type(vas))
#print(vasa,type(vasa))
#print(vasa.transpose())
#print(df[df.columns[3:6]]/255)
colorv=(df[df.columns[3:6]]/255).to_numpy()
normv=(df[df.columns[6:9]]/255).to_numpy()
#wit column names
#dataframe[['column1','column2']]
#to select by iloc and specific columns with index number:
#dataframe.iloc[:,[1,2]]
#with loc column names can be used like
#dataframe.loc[:,['column1','column2']]
pcd = o3d.geometry.PointCloud()
pcd.points = o3d.utility.Vector3dVector(vasa.transpose())
pcd.colors = o3d.utility.Vector3dVector(colorv)
pcd.normals = o3d.utility.Vector3dVector(normv)
o3d.visualization.draw_geometries([pcd])
