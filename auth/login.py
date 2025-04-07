#!/usr/bin/python3

from utils.RequestMethods import RequestMethods  # You might not be using this in Login
from click import style
from getpass import getpass
import requests
from utils.utils import save_token  # Import save_token

class Login:
    @staticmethod
    def authenticate():
        """Autenticación con manejo mejorado de respuestas"""
        try:
            email = input("Email: ")
            password = getpass("\U0001F512 Password: ")

            response = requests.post(
                "http://localhost:3030/api/auth/login",
                json={"email": email, "password": password},
                timeout=5
            )

            # Debug: Mostrar respuesta cruda del servidor
            print("\n[DEBUG] Respuesta del servidor:", response.text)

            if response.status_code == 200:
                try:
                    data = response.json()
                    print(data)

                    if data.get('data') and data['data'].get('token'):
                        token_data = {'token': data['data']['token']['token']} # Extract the token
                        if data['data'].get('token').get('expires_at'): # Check if expires_at exists
                            token_data['expires_at'] = data['data']['token']['expires_at']
                        if save_token(token_data):
                            print(style("✅ Inicio de sesión exitoso y token guardado.", fg='green'))
                            return True
                        else:
                            print(style("❌ Error al guardar el token.", fg='red'))
                            return False
                    else:
                        print(style("\n✖ El backend respondió pero sin token válido en la estructura esperada.", fg='yellow'))
                        return False
                except json.JSONDecodeError:
                    print(style(f"\n✖ Error al decodificar la respuesta JSON: {response.text}", fg='red'))
                    return False

            print(style(f"\n✖ Error del servidor (Código {response.status_code})", fg='red'))

        except requests.exceptions.RequestException as e:
            print(style(f"\n⚠ Error de conexión: {str(e)}", fg='yellow'))
        except Exception as e:
            print(style(f"\n⚠ Error inesperado: {str(e)}", fg='yellow'))

        return False