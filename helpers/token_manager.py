import os
from cryptography.fernet import Fernet
from config.settings import SECRET_KEY

# Generar un clave cifrada a partir del secret
print(f"SECRET_KEY: {SECRET_KEY}")
cipher = Fernet(SECRET_KEY.encode())

TOKEN_FILE_PATH="token.dat"

def save_token(token: str):
    try:
        encrypted_token = cipher.encrypt(token.encode())
        with open(TOKEN_FILE_PATH, "wb") as file:
            file.write(encrypted_token)
        return True
    except Exception as e:
        print(f"Error al guardar el token: {str(e)}")
        return False

def get_token():
    try:
        if not os.path.exists(TOKEN_FILE_PATH):
            print("El archivo del token no existe.")
            return None
        with open(TOKEN_FILE_PATH, "rb") as file:
            encrypted_token = file.read()
        decrypted_token = cipher.decrypt(encrypted_token)
        return decrypted_token.decode()
    except Exception as e:
        print(f"Error al obtener el token: {str(e)}")
        return None


def delete_token():
    """
    Elimina el archivo que contiene el token.
    """
    # Verifica si el archivo existe
    if os.path.exists(TOKEN_FILE_PATH):
        os.remove(TOKEN_FILE_PATH)
        return True
    return False

def token_exists():
    """
    Verifica si el token existe.
    """
    return os.path.exists(TOKEN_FILE_PATH)
    