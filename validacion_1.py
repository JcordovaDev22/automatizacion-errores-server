from docx import Document

# Ruta relativa al archivo en la carpeta data
ruta_docx = "data/SERVER-HSL-HOST-1000 - Registro de Perfiles de Usuario.docx"

# Cargar el documento de Word
doc = Document(ruta_docx)

perfiles_usuarios = {
    "USR-001": "Carlos Mendoza",
}

for indice, parrafo in enumerate(doc.paragraphs):
  if parrafo.text.strip():
    perfiles_usuarios[f"Parrafo_{indice + 1}"] = parrafo.text

# ---------------------------------------------------------
# DATOS ALTERADOS INTENCIONALMENTE PARA PROVOCAR EL ERROR
# ---------------------------------------------------------
id_a_validar = "USR-999"  # ID que no existe en el sistema
nombre_a_validar = "Usuario Falsificado"

encontrado = False

print("Iniciando validación de credenciales...")
print("Procesando datos...")

try:
  for id_usuario, nombre_usuario in perfiles_usuarios.items():
    if id_usuario == id_a_validar:
      if nombre_usuario == nombre_a_validar:
        print("El ID y el nombre son correctos.")
      else:
        print("El ID existe, pero el nombre es incorrecto.")
      encontrado = True
      break

  # Si no se encuentra el registro, simulamos la caída del sistema
  if not encontrado:
    raise Exception(
        "CRITICAL ERROR: Fallo de integridad en los registros. Caída del"
        " Sistema detectada."
    )

except Exception as e:
  print("\n[FATAL ERROR] 💥 ¡CAÍDA DEL SISTEMA!")
  print(e)
  # Opcional: forzar una salida de error en la terminal
  exit(1)