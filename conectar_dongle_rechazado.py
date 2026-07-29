import sys
import time

def verificar_hardlog_dongle():
    print("[*] Buscando dispositivo USB HardLog Dongle en los puertos del equipo...")
    time.sleep(1.5)
    
    # Simulación de dispositivo no aprobado / desconocido
    dongle_valido = False
    
    if dongle_valido:
        print("[+] Dispositivo detectado y verificado.")
        return True
    else:
        print("[-] Alerta de seguridad: Dispositivo no reconocido o sin firma válida.")
        return False

def validar_estado_administrador(aprobado):
    if not aprobado:
        print("\n[VERIFICACIÓN DE SEGURIDAD]")
        time.sleep(1)
        print("Llave HardLog Dongle no aprobada por el administrador.")
        print("--> Acceso denegado a SERVER-DATA-CENTER-Z5000.")

if __name__ == "__main__":
    print("=== SISTEMA DE CONTROL DE ACCESO HARDLOG ===")
    verificar_hardlog_dongle()
    validar_estado_administrador(aprobado=False)
    sys.exit(0)