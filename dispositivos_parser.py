
import json

try:
    with open("dispositivos.json", "r") as file:
        data = json.load(file)
        dispositivos_data = data["dispositivos"]  # Accede al array dentro de "dispositivos"
    
    print("\n📡 Dispositivos de Red:")
    print("=" * 40)
    for dispositivo in dispositivos_data:
        print(f"Nombre: {dispositivo['nombre']}")
        print(f"IP: {dispositivo['ip']}")
        print(f"Estado: {dispositivo['estado'].upper()}")
        print("-" * 40)
        
except FileNotFoundError:
    print("❌ Error: El archivo 'dispositivos.json' no existe.")
except json.JSONDecodeError:
    print("❌ Error: El archivo JSON está mal formateado.")
except KeyError:
    print("❌ Error: La estructura del JSON no es la esperada (falta campo 'dispositivos')")
except Exception as e:
    print(f"❌ Error inesperado: {str(e)}")
