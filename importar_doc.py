from docx import Document

# Ruta a tu archivo de Word
ruta_docx = r"C:\Users\maest\Documents\JIRA\HOTEL_SAN_LUIS\ANEXOS\GEMINI\PERFILES_DE_USUARIO\SERVER-HSL-HOST-1000 - Registro de Perfiles de Usuario.docx"

# Cargar el documento
doc = Document(ruta_docx)

# Crear un diccionario estructurando el contenido
Perfiles_Usuario = {"Id": "USR-001", "Nombre": "Carlos Mendoza", "Nacionalidad": "Ecuatoriana", "Estado_Civil": "Soltero", "Edad": "28", "Telefono": "0991234567", "Direccion": "Av. 9 de Octubre, Milagro", "Profesion": "Ingeniero de Sistemas"}


# Recorrer los párrafos del documento
for indice, parrafo in enumerate(doc.paragraphs):
  if parrafo.text.strip():  # Evitar párrafos vacíos
    # Usamos el número de párrafo como clave
    Perfiles_Usuario[f"Parrafo_{indice + 1}"] = parrafo.text

# Ejemplo para verificar el resultado
print(Perfiles_Usuario)
print(f"Total de registros importados: {len(Perfiles_Usuario)}")