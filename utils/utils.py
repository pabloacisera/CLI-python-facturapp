import os
import json
from pathlib import Path
from click import style


def get_token_path():
    """Devuelve la ruta para guardar el token"""
    home = Path.home()
    token_dir = home / ".municipalidad_cli"
    token_dir.mkdir(exist_ok=True, mode=0o700)
    return token_dir / "token.json"

def save_token(token_data):
    """Guarda el token"""
    token_path = get_token_path()
    try:
        with open(token_path, 'w') as f:
            json.dump({
                'token': token_data.get('token'),
                'expires_at': token_data.get('expires_at')
            }, f)
        os.chmod(token_path, 0o600)
        return True
    except Exception as e:
        print(style(f"Error guardando token: {e}", fg="red"))
        return False

def load_token():
    """Carga el token si existe y es válido"""
    token_path = get_token_path()
    try:
        with open(token_path, "r") as f:
            data = json.load(f)
            if not data.get('token'):
                return None
            return data
    except (FileNotFoundError, json.JSONDecodeError):
        return None
    except Exception as e:
        print(style(f"Error leyendo token: {e}", fg='yellow'))
        return None

def validate_token(token):
    """Verifica la validez del token con el backend"""
    # Implementación pendiente según tu API
    return True  # Temporalmente siempre válido

def delete_token():
    token_path = get_token_path()
    try:
        if os.path.exists(token_path):
            os.remove(token_path)
            print(style("🔓 Sesión cerrada. El token ha sido eliminado.", fg="green"))
        else:
            print(style("⚠️ No se encontró ningún token para eliminar.", fg="yellow"))
        return True
    except Exception as e:
        print(style(f"Error al eliminar el token: {e}", fg="red"))
        return False