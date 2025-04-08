from cryptography.fernet import Fernet

# Genera una nueva clave Fernet
key = Fernet.generate_key()

# Muestra la clave generada
print(key.decode())  # Esta es la clave que debes usar en tu archivo .env
