import pygame
import random
import math

# Inicializando o pygame
pygame.init()

# Cores
white = (255, 255, 255)  # formato rgb
red = (255, 0, 0)
black = (8, 95.2, 6.4)  # Correção na definição da cor preta

# Criando janela
screen_width = 900
screen_height = 600
gameWindow = pygame.display.set_mode((screen_width, screen_height))

# Título do jogo
pygame.display.set_caption("Phelipe Quintes")
pygame.display.update()
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 55)


def text_screen(text, color, x, y):
    screen_text = font.render(text, True, color)
    gameWindow.blit(screen_text, [x, y])

def plot_snake(gameWindow, color, snk_list, snake_size):
    for x, y in snk_list:
        pygame.draw.circle(gameWindow, color, (x, y), snake_size // 2)  # Ajuste no desenho do círculo da cobra

# Loop do Jogo
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    velocity_x = 0
    velocity_y = 0
    snk_list = []
    snk_length = 1

    food_x = random.randint(20, screen_width - 20)
    food_y = random.randint(60, screen_height - 20)
    score = 0
    init_velocity = 4
    snake_size = 30
    fps = 60  # fps = frames por segundo
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            text_screen("Try Again", red, 100, 250)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gameloop()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_LEFT:
                        velocity_x = -init_velocity
                        velocity_y = 0
                    if event.key == pygame.K_UP:
                        velocity_y = -init_velocity
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = init_velocity
                        velocity_x = 0

            snake_x = snake_x + velocity_x
            snake_y = snake_y + velocity_y

            if abs(snake_x - food_x) < snake_size // 2 and abs(snake_y - food_y) < snake_size // 2:
                score += 5
                food_x = random.randint(20, screen_width - 30)
                food_y = random.randint(60, screen_height - 30)
                snk_length += 5

            gameWindow.fill(white)
            text_screen("Score: " + str(score * 10), red, 5, 5)
            pygame.draw.circle(gameWindow, red, (food_x, food_y), snake_size // 2)  # Correção no desenho do círculo da comida
            pygame.draw.line(gameWindow, red, (0, 40), (900, 40), 5)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list) > snk_length:
                del snk_list[0]

            for segment in snk_list[:-1]:
                if segment[0] == snake_x and segment[1] == snake_y:
                    game_over = True

            if snake_x >= screen_width:
                snake_x = 0
            elif snake_x < 0:
                snake_x = screen_width - snake_size

            if snake_y >= screen_height:
                snake_y = 50
            elif snake_y < 50:
                snake_y = screen_height - snake_size

            plot_snake(gameWindow, black, snk_list, snake_size)
        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

gameloop()