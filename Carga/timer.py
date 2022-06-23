import schedule
import time
from carga import load_data



def ejecutar():
    _directory = r'C:\Users\valen\OneDrive\Documentos\GitHub\Alloxentric\RAWDATA\ALLOXENTRIC\ARCHIVOS'
    _data = r'C:\Users\valen\OneDrive\Documentos\GitHub\Alloxentric\RAWDATA\ALLOXENTRIC\_DATOS\datos.txt'
    load_data(_directory,_data)


schedule.every(20).seconds.do(ejecutar)

while True:
    schedule.run_pending()
    time.sleep(1)