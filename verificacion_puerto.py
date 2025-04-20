try:
    puerto = int(input("Ingrese un número de puerto (0-65535): "))
    
    if 0 <= puerto <= 1023:
        print(f"El puerto {puerto} es un **puerto bien conocido** (servicios estándar: HTTP, SSH, FTP).")
    elif 1024 <= puerto <= 49151:
        print(f"El puerto {puerto} es un **puerto registrado** (aplicaciones de usuario).")
    elif 49152 <= puerto <= 65535:
        print(f"El puerto {puerto} es un **puerto dinámico/privado** (uso temporal).")
    else:
        print("❌ Error: El número no está en el rango válido (0-65535).")
except ValueError:
    print("❌ Error: Debes ingresar un número entero.")