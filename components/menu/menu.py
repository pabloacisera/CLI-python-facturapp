from utils.utils import load_token
import click
from click import style
from auth.login import Login


class Menu:
    @staticmethod
    def validate_token():
        token_data=load_token()
        if token_data  and token_data.get('token'):
            Menu.display_menu()
        else:
            click.echo(style(f"No existe token valido, ingrese con sus credenciales", fg="yellow"))
            Login.authenticate()

    @staticmethod
    def display_menu():
        click.echo(style("--- Menú Facturapp ---", bold=True))
        while True:
            click.echo("\nOpciones:")
            click.echo("1. Listar Propietarios (Implementar)")
            click.echo("2. Listar Propiedades (Implementar)")
            click.echo("3. Buscar (Implementar)")
            click.echo("4. Cerrar Sesión")
            click.echo("5. Salir del Sistema")

            option = input("Seleccione una opción: ")

            if option == '1':
                click.echo("Implementando la lista de propietarios...")
                # Aquí iría la lógica para listar propietarios
                return True
            elif option == '2':
                click.echo("Implementando la lista de propiedades...")
                # Aquí iría la lógica para listar propiedades
            elif option == '3':
                click.echo("Implementando la búsqueda...")
                # Aquí iría la lógica para buscar
            elif option == '4':
                from utils.utils import delete_token
                delete_token()
                click.echo(style("🔓 Sesión cerrada exitosamente.", fg='green'))
                break  # Vuelve al menú principal (start)
            elif option == '5':
                print('Saliendo del sistema.')
                exit()  # Termina la aplicación completamente
            else:
                click.echo(style("⚠️ Opción inválida. Por favor, seleccione una opción válida.", fg='yellow'))


