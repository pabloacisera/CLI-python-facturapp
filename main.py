#!/usr/bin/python3
import click
from click import style
from auth.login import Login
from auth.register import Register
from components.menu.menu import Menu
from utils.utils import load_token, delete_token


@click.group()
def main():
    """Sistema de gestión"""
    pass

@main.command()
def start():
    """Inicia la aplicación"""
    while True:
        token_data = load_token()

        click.echo("\nMenu de acceso:")
        options = []
        if not token_data or not token_data.get('token'):
            options.append("1. Logear")
            options.append("2. Registrar")
            options.append("3. Acceder a Facturapp")
            options.append("4. Salir")
        else:
            options.append("3. Acceder a Facturapp")
            options.append("4. Cerrar Sesión")
            options.append("5. Salir")

        for option_text in options:
            click.echo(option_text)

        option = input("Seleccione una opción: ")

        if option == '1' and not token_data:
            login_instance = Login()
            if login_instance.authenticate():
                click.echo(style("✅ Inicio de sesión exitoso", fg='green'))
            else:
                click.echo(style("❌ Fallo al iniciar sesión", fg='red'))
        elif option == '2' and not token_data:
            Register.register()
        elif option == '3':
            if token_data and token_data.get('token'):
                print('\n--- Menú Facturapp ---')
                Menu.display_menu()
            else:
                click.echo(style("🔒 No hay sesión activa. Por favor, inicie sesión.", fg='yellow'))
        elif option == '4':
            if not token_data:
                print('Saliendo del sistema.')
                break  # Correctly breaks the while loop
            else:
                delete_token()
                click.echo(style("🔓 Sesión cerrada. Volviendo al menú de acceso.", fg='green'))
        elif option == '5' and token_data:
            print('Saliendo del sistema.')
            break  # Correctly breaks the while loop
        else:
            click.echo(style("⚠️ Opción inválida. Por favor, seleccione una opción válida.", fg='yellow'))

if __name__ == '__main__':
    main()