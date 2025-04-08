import click

def show_flags():
    click.echo(click.style("🔍 Opciones disponibles", fg="blue", bold=True))
    click.echo("1. --get-properties: Obtener propiedades")
    click.echo("2. --get-owners: Obtener propietarios")

    click.echo("🚀 Esperando la selección del usuario...")  # Esto es para depurar

    while True:  # Usamos un ciclo infinito para evitar la recursión
        flag = click.prompt(
            "Selecciona una opción (flag) que desea ejecutar...", type=str
        )
        
        click.echo(f"Has seleccionado: {flag}")  # Esto es para depurar
        
        if flag == '--get-properties':
            click.echo(click.style("🔍 Opción seleccionada: --get-properties", fg="green"))
            # Aquí puedes agregar la lógica para manejar la opción 1
            break  # Salir del ciclo cuando se elige una opción válida

        elif flag == '--get-owners':
            click.echo(click.style("🔍 Opción seleccionada: --get-owners", fg="green"))
            # Aquí puedes agregar la lógica para manejar la opción 2
            break  # Salir del ciclo cuando se elige una opción válida

        else:
            click.echo(click.style("❌ Opción no válida", fg="red"))
            # No necesitamos llamar recursivamente, el ciclo se repetirá hasta que se elija una opción válida
