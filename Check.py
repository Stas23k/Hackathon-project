import numpy as np
from datetime import datetime
from datetime import timedelta
from time_window import TimeWindow
from pathlib import Path
from mat4py import loadmat
from streamz import Stream
import pandas as pd




# Mocked data
# datout=np.uint8(np.random.randint(10, high=None, size=10, dtype='uint8'))
# lenout=np.uint8(np.random.randint(10, high=None, size=10, dtype='uint8'))
 
# delta = timedelta(seconds=5)
#tw = TimeWindow.from_timedelta(since, delta)


#for value in values:
#    since = datetime.now()
#    tw = TimeWindow.from_timedelta(since, delta)
#    while tw>0:
#          print(value)
#          continue



#print(Path().absolute())

#datout = loadmat('datout.mat')
#print(type(datout))
#lenout = loadmat('lenout.mat')
# x=lenout.values()


def load_mat_data(mat_data:str):
    py_data = loadmat(mat_data)
    return py_data

def dict_2_np(mat_dict:dict):
    np_data=np.array(list(mat_dict.values()))
    return np_data


#def data_giver(data_array:np):
    
   # for column in data_array.T:
        # NF_instance(column[0],column[1])
    
#    return column   



#x=dict_2_np(load_mat_data('datout.mat'))
#y=dict_2_np(load_mat_data('lenout.mat'))

#z=np.concatenate((x,y))
#data=data_giver(z)
#print(data)

#print(z[1,0])

datout_source = Stream()
lenout_source = Stream()

a=datout_source.map(load_mat_data).map(dict_2_np)
b=lenout_source.map(load_mat_data).map(dict_2_np)


c = a.zip(b).map(np.concatenate).sink(print)

#datout_source.emit('datout.mat')
# datout_source.emit('lenout.mat')


# np_data_datout=source.emit(datout.values())


#vals = np.array(list(lenout.values()))
#vals = np.array(list(lenout.values()))
#print(lenout)

# source.map(list).sink(np.array)

#lenout_dict=load_mat_data('lenout.mat')
# datout = load_mat_data('datout.mat')
#source = Stream()


#x=source.map(list).map(np.array)
#source.emit(lenout.values())


