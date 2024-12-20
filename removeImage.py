from rembg import remove
from PIL import Image, UnidentifiedImageError

# Rutas corregidas
input_path = 'C:/wamp64/www/PYTHON/a.jpg'
output_path = 'C:/wamp64/www/PYTHON/b.jpg'

try:
    # Procesar la imagen
    inp = Image.open(input_path)
    output = remove(inp)
    
    # Convertir a modo RGB si es necesario
    if output.mode == 'RGBA':
        output = output.convert('RGB')
    
    output.save(output_path)

    # Abrir la imagen resultante
    Image.open(output_path).show()
except FileNotFoundError:
    print(f"El archivo {input_path} no fue encontrado.")
except UnidentifiedImageError:
    print(f"El archivo {input_path} no es una imagen válida.")
except Exception as e:
    print(f"Ocurrió un error: {e}")