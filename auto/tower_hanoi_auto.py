import subprocess
import time
import psutil

disks = 2  # Número inicial de discos
max_disks = 4  # Número máximo de discos

while disks < max_disks:
    # Ejecutar el script tower_hanoi.py con el número actual de discos
    subprocess.run(["python", "auto/tower_hanoi.py", str(disks)])

    # Incrementar el número de discos para la próxima ejecución
    disks += 1

    # Esperar a que termine el script anterior antes de continuar
    while True:
        time.sleep(1)  # Esperar 1 segundo antes de verificar
        if not any(
            "tower_hanoi.py" in p.info["name"]
            for p in psutil.process_iter(attrs=["name"])
        ):
            break  # Salir del bucle si no hay más instancias del script en ejecución
