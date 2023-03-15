# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/generic.ipynb.

# %% auto 0
__all__ = ['load_pickle', 'dump_pickle', 'sed_script', 'split_list', 'lmap', 'mmap', 'fprint']

# %% ../nbs/generic.ipynb 3
import os
import pickle
import re
import multiprocessing

# %% ../nbs/generic.ipynb 5
def load_pickle(pickle_file):
    "read a pickle file"
    if os.path.isfile(pickle_file) == False:
        return
    with open(pickle_file, "rb") as h:
        result = pickle.load(h)
    return result

# %% ../nbs/generic.ipynb 6
def dump_pickle(obj,pickle_file,protocol=3):
    "dump an object to pickle file"
    with open(pickle_file, "wb") as h:
        pickle.dump(obj, h, protocol=protocol)

# %% ../nbs/generic.ipynb 8
def sed_script(script,replace_array):
    """
    Find and replace variable names in script
    This is useful to use with the lsd_interactive library to replace names in scripts
    """
    with open(script, "r") as h:
        lines = h.readlines()
    with open(script, "w") as h:
        for line in lines:
            for var,hard in replace_array:
                line = re.sub(
                    var, 
                    str(hard),
                    # str(hard) if type(hard)!=str else f"'{hard}'",
                    line)
            h.write(line)

# %% ../nbs/generic.ipynb 15
def split_list(li:list,chunks:int):
    "split a list into N chunks"
    le = int(len(li)/(chunks-1))
    res = [li[(i*le):(i+1)*le] for i in range(chunks)]
    if res[-1] == []: res.pop()
    return res

# %% ../nbs/generic.ipynb 16
def lmap(func,li:list):
    "map a list with funtion"
    return list(map(func,li))

# %% ../nbs/generic.ipynb 17
def mmap(func,li:list,cpus:int):
    "wrapper of multiprocessing.Pool.map"
    with multiprocessing.Pool(cpus) as pool:
        res = pool.map(func,li)
    return res

# %% ../nbs/generic.ipynb 19
def fprint(string:str):
    "wrapper to print with flush"
    print(string,end='\n',flush=True)