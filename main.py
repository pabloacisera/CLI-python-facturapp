#!/usr/bin/python3
import click
from authentication.command_login import login
from authentication.command_register import register

@click.group()
def main():
    """Sistema de gestión"""
    pass

main.add_command(login, name='login')
main.add_command(register, name='register')

if __name__ == '__main__':
    main()