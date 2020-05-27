from IPython.core.pylabtools import figsize
import matplotlib.pyplot as plt
import pandas as pd

def quick_eda(df,describe=False,force_cat=False,return_value = False):
    print(df.info())
    misslist = []
    numlist = []
    objlist = []
    if force_cat!=False: 
        for i in force_cat:objlist.append(i)
    dfcopy = df.copy()
    for c in df.columns:
        if c in objlist: continue
        if c.endswith('id') or c.endswith('date'):continue
        miss_rate = (len(df[df[c].isnull()])*1.0)/len(df)
        if miss_rate>0.5: 
            print('\n{0} contains too many missing values.{1:.2%} is missing.'.format(c,miss_rate)); 
            misslist.append(c);
            continue
        
        dfcopy[c]=dfcopy[c].fillna(0)
        try: dfcopy[c] = dfcopy[c].astype(int);numlist.append(c)
        except: objlist.append(c)
    
    if describe!=False: print(df[numlist].describe())
    ln =len(numlist)
    n=0
    height = ln/4+1
    figsize(4*8,height*8)
    plt.rc('font', size=12)
    plt.style.use("fivethirtyeight")
    print("\nNumberical Variables:",numlist)
    for c in numlist:
        n+=1
        p1 = plt.subplot(height,4,n)
        p1.hist(dfcopy[c])
        p1.set_title(c)

    print("\nCategory Variables:",objlist)
    for o in objlist:
        print("\nCategorical Variable: %s"%o)
        if df[o].nunique()<50: 
            print(df[o].value_counts())
        else: 
            print("\n%s contains %s unique values. Too many, will not be printed."%(df[o].nunique(),o))
    plt.show()
    if return_value ==True:  
        return misslist,numlist,objlist
