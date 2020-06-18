import numpy as np
import open3d as o3d
import pandas as pd

input_path="your_path_to_file/"
output_path="your_path_to_output_folder/"
dataname="bancada superior cajati_traces_VG-70-65 fair.csv"
point_cloud = pd.read_csv(dataname)
df=pd.DataFrame(point_cloud)
cols=[2,3,4,5,6,7]
print('quantidade linhas' ,len(df))
