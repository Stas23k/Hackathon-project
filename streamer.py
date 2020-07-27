from streamz import Stream
import numpy as np
import matlab.engine
from mat4py import loadmat
from pathlib import Path
# import matlab.engine - optional 


datout = loadmat('datout.mat')
lenout = loadmat('lenout.mat')


def mat_2_py_streamer (datout_mat:np.uint8, lenout_mat:np.uint8, folder_path=Path().absolute()):
    """This function receives two parameters from the EEG Neurofeedback system (Curry7) in Matlab formt and stream it to python.

    Parameters
    ----------
    datout : np.uint8
        First Neurofeedback parameter vector.
    lenout : np.uint8
        Second Neurofeedback parameter vector.
    path: pathlib path
        Pathlib path to the folder with the data.    

    Returns
    -------
    datout_py : np.ndarray (???)
    proccessed dataout information in python format.
    lenout_py : np.ndarray (???)
    proccessed lenout information in python format.
    """

    def load_mat_data(mat_data:str): # This function loads matlab mat file to python dict
        py_data = loadmat(mat_data)
        return py_data

  # def load_mat_data(mat_data):  # Alternative approach to data loading.
  #     eng = matlab.engine.start_matlab()
  #     py_data = eng.load(mat_data, nargout=1)
    
    def dict_2_np(mat_dict:dict):
        np_data=np.array(list(mat_dict.values()))
        return np_data
    
