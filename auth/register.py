import json

import click
from click import style
from utils.RequestMethods import RequestMethods
from utils.utils import save_token

class Register:
    ROLES = {
        1: "USER",
        2: "ADMIN",
        3: "GUEST"
    }

    @staticmethod
    def register():
        name = input("nombre: ")
        username = input("usuario: ")
        email = input("email: ")
        password = input("contraseña: ")
        role = None
        while True:
            try:
                role_input = int(input(f"rol({', '.join(f'{key}-{value}' for key, value in Register.ROLES.items())}): "))
                if role_input in Register.ROLES:
                    role = Register.ROLES[role_input]
                    break
                else:
                    print("Rol inválido, elige un número de la lista")
            except ValueError:
                print("Por favor, ingresa un número para el rol")

        user_data = {
            "name": name,
            "username": username,
            "email": email,
            "password": password,
            "role": role
        }

        print("\nDatos del nuevo usuario:")
        print(user_data)

        try:
            response = RequestMethods.post(
                'auth/register',
                user_data,
                headers= None
            )
            if response is None:
                click.echo(style("❌ Error al registrar el usuario (sin respuesta del servidor).", fg='red'))
                return False

            try:
                response_json = response.json()
                click.echo(f"[DEBUG] Respuesta del servidor: {response_json}")

                if response.status_code == 200 and response_json.get('data'):
                    token_data = response_json['data']['token']
                    if save_token(token_data):
                        click.echo(style("✅ Inicio de sesión exitoso.", fg='green'))
                        return True
                    else:
                        click.echo(style("❌ Error al guardar el token.", fg='red'))
                        return False
                else:
                    error_message = response_json.get('message', 'Error desconocido al iniciar sesión.')
                    click.echo(style(f"❌ Fallo al iniciar sesión: {error_message}", fg='red'))
                    return False
            except json.JSONDecodeError:
                click.echo(style(f"❌ Error al decodificar la respuesta del servidor: {response.text}", fg='red'))
                return False
        except Exception as e:
            print(f'Error en la petición post: {e}')
            click.echo(style(f"❌ Error en la petición post: {e}", fg='red'))
            return False