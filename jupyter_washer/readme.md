
# Jupyter Washer
A module that helps you prettify the scripts exported from Jupyter Notebook, and pretend that you haven't used Jupyter Notebook as an IDE.



## Why is it necessary

A script exported from Jupyter Notebook tends to look like this:

```python
# In[1]:
import os

# In[2]:
os.getcwd()



# In[3]:
# write a loop
for i in range(1,10):
	print i
```

The script above contains too many missing lines and input row numbers, which may look a little messy and distractive, especially when the script is long and complex.

**Jupyter Washer** helps you clean the scripts by deleting the unnecessary missing lines and input row numbers, while retaining normal codes and comments.

```python
import os

os.getcwd()

# write a loop
for i in range(1,10):
	print i
```

## How to get it

You can copy the **.py** file into a directory from which you can import, or you can just copy the codes of the **pls_wash** function from **jupyter_washer.py**.



## How to use it
Use the **pls_wash** function:
The function takes two parameters:
```python
pls_wash(file_path,backup=True)
```
The parameter **file_path** is the path of your script. You can use absolute or  relative paths, while absolute paths are recommended. If no file_path is given, you will be asked to type a path.

If **backup=True**, your script will be backed up before being washed, which means a copy of it will be saved into the same directory. Otherwise the original script will be simply overwritten with no back-up. The default value for this parameter is 'True'.
