import sys
import time

def verificar_hardlog_dongle():
    print("[*] Buscando dispositivo USB HardLog Dongle en los puertos del equipo...")
    time.sleep(1.5)
    
    # Simulación de lectura exitosa del hardware
    dongle_detectado = True
    id_hardware = "HL-USB-Z5000-X99"
    
    if dongle_detectado:
        print(f"[+] ¡Dispositivo detectado exitosamente! ID: {id_hardware}")
        return True
    else:
        print("[-] Error: No se encontró ninguna llave HardLog Dongle conectada.")
        return False

def autenticar_servidor(autorizado):
    if autorizado:
        print("\n[INFO] Validando credenciales de USB HardLog Dongle...")
        time.sleep(1)
        print("[ACCESO CONCEDIDO] Credenciales aceptadas.")
        print("--> Conexión establecida exitosamente con el área: **SERVER-DATA-CENTER-Z5000**")
    else:
        print("\n[ACCESO DENEGADO] Credenciales inválidas.")

if __name__ == "__main__":
    print("=== SISTEMA DE CONTROL DE ACCESO HARDLOG ===")
    if verificar_hardlog_dongle():
        autenticar_servidor(autorizado=True)
    else:
        sys.exit(1)