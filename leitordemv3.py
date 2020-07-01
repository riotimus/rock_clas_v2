import numpy as np
import open3d as o3d
import pandas as pd
from open3d import *


from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("data files","*.txt"),("all files","*.xyz")))
print (root.filename)
point_cloud = pd.read_csv(root.filename,delimiter=" ")
print('len',len(point_cloud))
print('csv ',point_cloud)
df=pd.DataFrame(point_cloud)
print('quantidade cols sem cabecerp  orig' ,len(df.columns),' quantidade linhas orig' ,len(df))
print(type(df.values))
float_array = df.values.astype(np.float)
print(type(float_array))
print((float_array))
#print('len',len(df1.values))
#o3d.visualization.draw_geometries([df1.values])

#wit column names
#dataframe[['column1','column2']]
#to select by iloc and specific columns with index number:
#dataframe.iloc[:,[1,2]]
#with loc column names can be used like
#dataframe.loc[:,['column1','column2']]
