from utils.utils import load_token, validate_token
from click import style

def check_auth():
    """Verifica y valida credenciales al iniciar la app"""
    token_data = load_token()

    if not token_data:
        print(style("🔐 No hay sesión activa", fg='yellow'))
        return False
    
    if validate_token(token_data['token']):
        print(style("✅ Sesión válida detectada", fg='green'))
        return True
    
    print(style("⚠ Sesión inválida o expirada", fg='red'))
    return False