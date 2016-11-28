from IPython.core.pylabtools import figsize
import matplotlib.pyplot as plt
import pandas as pd


def quick_eda(df):
    print df.info()
    numlist = []
    objlist = ['ref_date','categoryid']
    for c in df.columns:
        if c in objlist: continue
        if c.endswith('id') or c.endswith('date'):continue
        if float(len(df[df[c].isnull()]))/len(df)>0.5: print'\n%s contains too many missing values.Drop.'%c; continue
        df[c]=df[c].fillna(0)
        try: df[c] = df[c].astype(int);numlist.append(c)
        except: objlist.append(c)

    ln =len(numlist)
    n=0
    height = ln/4+1
    figsize(4*8,height*8)
    plt.rc('font', size=12)
    plt.style.use("fivethirtyeight")
    print "\nNumberical Variables:",numlist
    for c in numlist:
        n+=1
        p1 = plt.subplot(height,4,n)
        p1.hist(df[c])
        p1.set_title(c)

    print "\nCategory Variables:",objlist
    for o in objlist:
        print "\nCategorical Variable: %s"%o
        if df[o].nunique()<50: print df[o].value_counts()
        else: print "\n%s contains too many unique values. Can't print."%o 
    plt.show()
