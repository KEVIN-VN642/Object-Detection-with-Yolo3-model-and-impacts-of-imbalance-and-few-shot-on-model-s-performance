import numpy as np
import pandas as pd

def parse_voc_annotation(file):
    #file="train/train_ann.csv"
    f=pd.read_csv(file)
    count_labels=f.groupby("labelclass_name")["labelclass_name"].count()
    seen_labels=count_labels.to_dict()
    
    f_ints=[]
    for image in sorted(np.unique(f["filepath"])):
        dt={}
        image_ann=f[f["filepath"]==image]
        dt["filename"]=image_ann.iloc[0,]["filepath"]
        dt["height"]=image_ann.iloc[0,]["im_height"]
        dt["width"]=image_ann.iloc[0,]["im_width"]
        objects=[]
        for i in range(image_ann.shape[0]):
            ob={}
            ob["name"]=image_ann.iloc[i,]["labelclass_name"]
            ob["xmin"]=image_ann.iloc[i,]["x_min"]
            ob["xmax"]=image_ann.iloc[i,]["x_max"]
            ob["ymin"]=image_ann.iloc[i,]["y_min"]
            ob["ymax"]=image_ann.iloc[i,]["y_max"]
            objects.append(ob)
        dt["object"]=objects
        f_ints.append(dt)
    return f_ints, seen_labels
    
 