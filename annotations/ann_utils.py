import numpy as np
import pandas as pd

def count_img(df):
    labels=[]
    im_count=[]
    for label in np.unique(df['labelclass_name']):
        df1=df[df['labelclass_name']==label]
        im_count.append(len(np.unique(df1['filepath'])))
        labels.append(label)
        
    return pd.DataFrame({"Label":labels,"No of Images":im_count})

def count_label(df):
    label_count=df.groupby('labelclass_name')['labelclass_name'].count()
    return pd.DataFrame({"Label":list(label_count.index),"No of annotations":list(label_count.values)})
    