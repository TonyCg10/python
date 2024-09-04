import pygame
import sys

# Inicializar Pygame
pygame.init()

# Definir colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Super Pygame")

# Variables del jugador
player_size = 50
player_x, player_y = WIDTH // 2, HEIGHT - player_size - 10
player_speed = 5
jump_power = 10
is_jumping = False
jump_count = 10
is_on_ground = True

clock = pygame.time.Clock()

# Bucle principal
while True:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed

    # Lógica del salto
    if is_on_ground and keys[pygame.K_SPACE]:
        is_jumping = True
        is_on_ground = False

    if is_jumping:
        player_y -= jump_count * 2
        jump_count -= 1
        if jump_count < 0:
            is_jumping = False
            jump_count = 10

    if not is_on_ground:
        if player_y < HEIGHT - player_size - 10:
            player_y += jump_count * 2
            jump_count -= 1
            if jump_count < 0:
                is_on_ground = True
                jump_count = 10

    # Dibujar al jugador en la pantalla
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))

    # Actualizar la pantalla
    pygame.display.update()

    # Controlar la velocidad del juego
    clock.tick(30)
