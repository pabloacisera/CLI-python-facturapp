import click
from click import style
from requests import post, RequestException
from config.settings import API_URL
from helpers.token_manager import save_token
from flags.show_flags import show_flags

@click.command()
def login():
    """
    Inicio de sesión adaptado al backend FastAPI
    """
    click.echo(style("🔑 Iniciando sesión...", fg="green", bold=True))

    credentials = {
        "email": click.prompt("Email", type=str),
        "password": click.prompt("Contraseña", hide_input=True)
    }

    try:
        response = post(
            f"{API_URL}/auth/login",  # Asegúrate que coincide con tu endpoint real
            json=credentials,
            timeout=10
        )

        # Manejo de respuesta exitosa
        if response.status_code == 200:
            data = response.json()
            click.echo(style("✅ ¡Login exitoso!", fg="green", bold=True))
            click.echo(f"👤 Usuario: {data['user']['name']}")
            click.echo(f"📧 Email: {data['user']['email']}")
            click.echo(f"🔑 Rol: {data['user']['role']}")
            click.echo(style(f"🔒 Token: {data['access_token'][:15]}...", dim=True))
        
            if save_token(data['access_token']):
                click.echo(style("✅ Token guardado exitosamente", fg="green"))
                show_flags()
            else:
                click.echo(style("❌ Error al guardar el token", fg="red"))
                
            return data

        
        # Manejo específico de errores del backend
        error_detail = response.json().get("detail", "")
        if response.status_code == 400 and "Invalid credentials" in error_detail:
            click.echo(style("❌ Credenciales inválidas", fg="red", bold=True))
        else:
            click.echo(style(f"❌ Error del servidor: {error_detail}", fg="red"))

    except RequestException:
        click.echo(style("🔌 Error de conexión con el servidor", fg="red", blink=True))
    except Exception as e:
        click.echo(style(f"⚠️ Error inesperado: {str(e)}", fg="yellow"))


