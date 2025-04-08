from .command_login import login  # <-- Importación relativa
from .command_register import register

__all__ = ['login']  # <-- Exporta explícitamente el comando
__all__ = ['register']