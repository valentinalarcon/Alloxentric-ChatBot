import schedule
import time
from carga import load_data



def ejecutar():
    print("iwi")
    _directory = r'C:\Users\valen\OneDrive\Documentos\GitHub\Alloxentric-ChatBot\Archivos'
    _data = r'C:\Users\valen\OneDrive\Documentos\GitHub\Alloxentric-ChatBot\ChatScript\RAWDATA\ALLOXENTRIC\_DATOS\datos.txt'
    load_data(_directory,_data)


schedule.every().day.at("11:00").do(ejecutar)

while True:
    schedule.run_pending()
    time.sleep(1)