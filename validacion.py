from docx import Document

# 1. Ruta relativa a tu archivo en la carpeta data
ruta_docx = "data/SERVER-HSL-HOST-1000 - Registro de Perfiles de Usuario.docx"

# 2. Cargar el documento de Word
doc = Document(ruta_docx)

# 3. Diccionario base o poblado dinámicamente con los párrafos/rows del documento
perfiles_usuarios = {
    "USR-001": "Carlos Mendoza",
}

# Agregamos el contenido de los párrafos leídos del Word al diccionario
for indice, parrafo in enumerate(doc.paragraphs):
  if parrafo.text.strip():
    perfiles_usuarios[f"Parrafo_{indice + 1}"] = parrafo.text

# 4. Datos que deseas validar (puedes cambiar estos valores para probar)
id_a_validar = "USR-001"
nombre_a_validar = "Carlos Mendoza"

encontrado = False

# 5. Ciclo para recorrer y validar en los datos reales del archivo
for id_usuario, nombre_usuario in perfiles_usuarios.items():
  if id_usuario == id_a_validar:
    if nombre_usuario == nombre_a_validar:
      print(f"Éxito: El ID '{id_usuario}' y el nombre son correctos.")
    else:
      print(
          f"Advertencia: El ID '{id_usuario}' existe, pero el nombre asociado es"
          f" diferente."
      )
    encontrado = True
    break

if not encontrado:
  print(f"Error: El ID '{id_a_validar}' no existe en el sistema.")

# Muestra el total de registros cargados para verificación
print(f"\nTotal de registros analizados en el diccionario: {len(perfiles_usuarios)}")