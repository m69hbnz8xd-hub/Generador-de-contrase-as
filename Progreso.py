import random
import string
import time
import sys
import subprocess
import shutil


def ensure_pyperclip():
    """Intentar importar pyperclip. Si no está instalado, tratar de instalarlo automáticamente."""
    try:
        import pyperclip
        return pyperclip
    except ImportError:
        print("La librería 'pyperclip' no está instalada. Intentando instalarla...")
        try:
            subprocess.check_call([sys.executable, "-m", "pip", "install", "--user", "pyperclip"], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        except Exception as e:
            print(f"Instalación automática falló: {e}")
            return None

        # Intentar importar de nuevo
        try:
            import pyperclip
            return pyperclip
        except ImportError:
            return None

def generar_contrasena():
    print("--- GENERADOR DE CONTRASEÑAS ---")

    longitud = 0
    caracteres_disponibles = ""

    # Bucle de validación de entrada
    while True:
        try:
            # 1. Ingresar número de caracteres
            entrada = input("\nIngresa la longitud de la contraseña (número): ")
            longitud = int(entrada)
            
            if longitud <= 0:
                print("Error: La longitud debe ser mayor a 0.")
                continue # Regresa al inicio del bucle
            break
        except ValueError:
            print("Error: Debes ingresar un número válido.")
            