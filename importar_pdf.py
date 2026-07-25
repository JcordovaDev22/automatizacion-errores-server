from pypdf import PdfReader

# Ruta a tu archivo PDF
ruta_pdf = r"C:\Users\maest\Documents\JIRA\HOTEL_SAN_LUIS\ANEXOS\GEMINI\PERFILES_DE_USUARIO\SERVER-HSL-HOST-1000 - Registro de Perfiles de Usuario.pdf"

# Inicializar el lector de PDF
lector = PdfReader(ruta_pdf)

# Crear un diccionario para almacenar el contenido por páginas
Perfiles_Usuario = {"Id": "USR-001", "Nombre": "Carlos Mendoza", "Nacionalidad": "Ecuatoriana", "Estado_Civil": "Soltero", "Edad": "28", "Telefono": "0991234567", "Direccion": "Av. 9 de Octubre, Milagro", "Profesion": "Ingeniero de Sistemas"}

# Recorrer cada página y guardarla en el diccionario
for indice, pagina in enumerate(lector.pages):
  texto = pagina.extract_text()
  # Guardamos usando el número de página como clave (empezando en 1)
  Perfiles_Usuario[f"Pagina_{indice + 1}"] = texto

# Ejemplo para verificar el resultado
print(Perfiles_Usuario["Pagina_1"])
print(f"Total de registros importados: {len(Perfiles_Usuario)}")