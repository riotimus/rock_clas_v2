import numpy as np
import open3d as o3d
import pandas as pd
from open3d import *


from tkinter import filedialog
from tkinter import *

root = Tk()
root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("data files","*.csv"),("all files","*.*")))
print (root.filename)

input_path="your_path_to_file/"
output_path="your_path_to_output_folder/"
dataname="bancada superior cajati_traces_VG-70-65 fair.csv"
point_cloud = pd.read_csv(root.filename)
df=pd.DataFrame(point_cloud)
print('quantidade linhas orig' ,len(df))
print('quantidade cols sem cabecerp  orig' ,len(df.columns))

cols=[2,3,4,5,6,7]
df1 = df[df.columns[2:7]]
print('quantidade linhas sem cabecerp' ,len(df1))
print('quantidade cols sem cabecerp' ,len(df1.columns))
print((df1.values))
o3d.visualization.draw_geometries([df1.values])

#wit column names
#dataframe[['column1','column2']]
#to select by iloc and specific columns with index number:
#dataframe.iloc[:,[1,2]]
#with loc column names can be used like
#dataframe.loc[:,['column1','column2']]
