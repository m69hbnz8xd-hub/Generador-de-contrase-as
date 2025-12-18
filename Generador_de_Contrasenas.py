import random
import string
import sys
import subprocess
import shutil


def ensure_pyperclip():
    """Intentar importar pyperclip """
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
            
            # 2. Seleccionar tipos de caracteres
            print("\nSelecciona los tipos de caracteres (s/n):")
            usar_mayus = input("¿Incluir Mayúsculas? ").lower() == 's'
            usar_minus = input("¿Incluir Minúsculas? ").lower() == 's'
            usar_nums = input("¿Incluir Números? ").lower() == 's'
            usar_simb = input("¿Incluir Símbolos? ").lower() == 's'
        except ValueError:
            print("Error: Debes ingresar un número válido.")
            continue
        else:
            # Validar que al menos un tipo de carácter esté seleccionado
            if not (usar_mayus or usar_minus or usar_nums or usar_simb):
                print("Error: Debes seleccionar al menos un tipo de carácter.")
                continue
            
            # Construir el conjunto de caracteres disponibles
            if usar_mayus:
                caracteres_disponibles += string.ascii_uppercase
            if usar_minus:
                caracteres_disponibles += string.ascii_lowercase
            if usar_nums:
                caracteres_disponibles += string.digits
            if usar_simb:
                caracteres_disponibles += string.punctuation
            
            break # Salir del bucle de validación
    # Generar la contraseña
    contrasena = ''.join(random.choice(caracteres_disponibles) for _ in range(longitud))
    print(f"\nContraseña generada: {contrasena}")
    
    # Intentar copiar al portapapeles: primero asegurar pyperclip, luego fallback a pbcopy en macOS
    pyperclip = ensure_pyperclip()
    if pyperclip is not None:
        try:
            pyperclip.copy(contrasena)
            print("La contraseña ha sido copiada al portapapeles.")
        except Exception as e:
            print(f"Error al copiar con pyperclip: {e}")
    else:
        # Fallback a pbcopy (macOS)
        if shutil.which("pbcopy"):
            try:
                subprocess.run(["pbcopy"], input=contrasena.encode(), check=True)
                print("La contraseña ha sido copiada al portapapeles (usando pbcopy).")
            except Exception as e:
                print(f"No se pudo copiar al portapapeles mediante pbcopy: {e}")
        else:
            print("No se pudo copiar al portapapeles: 'pyperclip' no disponible y 'pbcopy' no encontrado.")


if __name__ == "__main__":
    try:
        generar_contrasena()
    except KeyboardInterrupt:
        print("\nInterrumpido por el usuario.")
        sys.exit(0)

