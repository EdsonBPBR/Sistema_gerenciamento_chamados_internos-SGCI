from datetime import datetime

def data_numeros():
    data = datetime.now().strftime("%Y-%m-%d")
    return data

def horario():
    hora = datetime.now().strftime("%H:%M:%S")
    return hora