from models.models import extrair_dados
from werkzeug.security import check_password_hash

dados = extrair_dados('usuarios_admin')
def verifica_login(email, senha):
    """
    Realiza a verificação, uma busca linear, de todos os registros
    
    :param email: Description
    :param senha: Description
    """
    sucesso_login = False
    usuario = None
    for registro in dados.values():
        if registro['email'] == email and check_password_hash(registro['senha'], str(senha)):
            sucesso_login = True
            usuario = registro
            break
    return sucesso_login, usuario