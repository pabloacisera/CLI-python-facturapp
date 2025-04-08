import click
from click import style
from requests import RequestException, post
from config.settings import API_URL


@click.command()
def register():
    """
    Register a new user.
    """
    click.echo(style("✏️ Registro de nuevo usuario", fg="cyan", bold=True))

    # Obtener datos con validación
    user_data = {
        "name": click.prompt("Nombre completo", type=str),
        "username": click.prompt("Nombre de usuario", type=str),
        "email": click.prompt("Email", type=str),
        "password": click.prompt("Contraseña", hide_input=True, confirmation_prompt=True),
        "role": click.prompt(
            "Rol",
            type=click.Choice(['USER', 'ADMIN', 'GUEST'], case_sensitive=False),
            show_choices=True
        ).upper()  # Aseguramos mayúsculas
    }

    click.echo(style("⏳ Enviando datos al servidor...", dim=True))

    try:
        response = post(
            f"{API_URL}/auth/register",  # Asegúrate que coincide con tu endpoint
            json=user_data,
            timeout=10
        )

        # Manejo de respuesta exitosa
        if response.status_code == 201:  # Código para creación exitosa
            result = response.json()
            click.echo(style("✅ Registro exitoso!", fg="green", bold=True))
            click.echo(f"🆔 ID: {result['user']['id']}")
            click.echo(f"👤 Nombre: {result['user']['name']}")
            return result

        # Manejo específico de errores de validación
        if response.status_code == 422:
            errors = response.json().get("detail", [])
            for error in errors:
                if error["type"] == "enum":
                    click.echo(style(f"❌ Error en el campo {error['loc'][-1]}: {error['msg']}", fg="red"))
                else:
                    click.echo(style(f"❌ Error de validación: {error['msg']}", fg="red"))
            return

        # Otros errores HTTP
        error_detail = response.json().get("detail", "Error desconocido")
        click.echo(style(f"❌ Error HTTP {response.status_code}: {error_detail}", fg="red"))

    except RequestException:
        click.echo(style("🔌 Error de conexión con el servidor", fg="red", blink=True))
    except Exception as e:
        click.echo(style(f"⚠️ Error inesperado: {str(e)}", fg="yellow"))