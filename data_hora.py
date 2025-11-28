from datetime import datetime

agora = datetime.now()
def data_numeros():
    data = agora.strftime("%Y-%m-%d")
    return data

def horario():
    hora = agora.strftime("%H:%M:%S")
    return hora