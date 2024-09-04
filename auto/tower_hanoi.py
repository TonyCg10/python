import sys
import psutil
import os
import csv


def hanoi(disks, source, helper, destination):
    moves = []  # List to store the moves

    def move_disk(start, end):
        moves.append((start, end))  # Append the move to the list of moves

    def move_tower(height, start, end, temp):
        if height >= 1:
            move_tower(height - 1, start, temp, end)
            move_disk(start, end)
            move_tower(height - 1, temp, end, start)

    move_tower(disks, source, destination, helper)
    return moves  # Return the list of moves


def print_tower(disks, moves):
    tower = [[] for _ in range(3)]
    for i in range(disks, 0, -1):
        tower[0].append(str(i))
    for move in moves:
        disk = tower[move[0] - 1].pop()
        tower[move[1] - 1].append(disk)
        print(f"Move disk {disk} from tower {move[0]} to tower {move[1]}:")
        for level in range(disks - 1, -1, -1):
            line = " | ".join(
                tower[i][level] if level < len(tower[i]) else " " for i in range(3)
            )
            print("  " + line)
    print(f"\nTotal moves: {len(moves)}")

    # Print memory usage
    memory_info = psutil.Process().memory_info()
    usage_mb = memory_info.rss / (1024 * 1024)  # Convert from bytes to megabytes
    print(f"RAM usage: {usage_mb:.2f} MB")

    # Print CPU usage
    cpu_percent = psutil.Process().cpu_percent()
    print(f"CPU usage: {cpu_percent:.2f}%")

    # Nombre del archivo CSV
    file_path = "auto/towe_hanoi_movements_data.csv"

    # Verificar si el archivo CSV ya existe
    file_exists = os.path.exists(file_path)

    with open(file_path, mode="a" if file_exists else "w", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Total Moves", "RAM Usage (MB)", "CPU Usage (%)"])

        # Obtener los datos y escribir una nueva fila en el archivo CSV
        writer.writerow([f"{len(moves)}", f"{usage_mb:.2f} MB", f"{cpu_percent:.2f}%"])

    print("CSV file generated successfully.")


if __name__ == "__main__":
    disks = (
        int(sys.argv[1]) if len(sys.argv) > 1 else 3
    )  # Obtener el número de discos de los argumentos de línea de comandos
    moves = hanoi(disks, 1, 2, 3)
    print_tower(disks, moves)
