import pandas as pd
import os 
import time 
import pathlib
from datetime import datetime

def date_time (fichero):
    ti_m = os.path.getmtime(fichero) 
    m_ti = time.ctime(ti_m)
    t_obj = time.strptime(m_ti) 
  
    T_date = time.strftime("%Y-%m-%d", t_obj) 
    T_time = time.strftime("%H:%M:%S", t_obj)
    return  T_date, T_time


def load_data(_directory, _data):
    #ruta donde se encuentra la carpeta de los archivos csv

    directory = pathlib.Path(_directory)

    #fecha y tiempo actual
    now = datetime.now(); now_date= now.date(); now_time = now.time().strftime("%H:%M:%S")


    #hora y fecha de todos los archivos dentro de la carpeta
    for fichero in directory.iterdir():
        T_date, T_time = date_time(fichero)

        if(str(now_date) == T_date):
            dataset = pd.read_csv(fichero,sep=';')
            dataset.to_csv(_data)

        

