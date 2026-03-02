import pygame, random


def run_game():
    # Initialize Pygame engine
    pygame.init()
    screen = pygame.display.set_mode((600, 400))
    pygame.display.set_caption("Snake AI Environment")
    clock = pygame.time.Clock()

    # Load and scale assets
    # Note: Make sure grass.jpg and fatasarpe2.png are in your main project folder
    image_background = pygame.image.load('grass.jpg')
    image_background = pygame.transform.scale(image_background, (600, 400))

    cell_size = 20
    head_img = pygame.image.load("fatasarpe2.png")
    head_img = pygame.transform.scale(head_img, (cell_size, cell_size))

    # Colors and initial state
    RED, GREEN = (200, 0, 0), (0, 200, 0)
    snake = [(100, 100), (80, 100), (60, 100)]
    direction = (cell_size, 0)
    food = (300, 200)

    running = True
    while running:
        clock.tick(10)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # Movement logic
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and direction != (0, cell_size): direction = (0, -cell_size)
        if keys[pygame.K_s] and direction != (0, -cell_size): direction = (0, cell_size)
        if keys[pygame.K_a] and direction != (cell_size, 0): direction = (-cell_size, 0)
        if keys[pygame.K_d] and direction != (-cell_size, 0): direction = (cell_size, 0)

        # Update position
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        snake.insert(0, new_head)

        # Growth and Collision
        if new_head == food:
            food = (random.randrange(0, 600, cell_size), random.randrange(0, 400, cell_size))
        else:
            snake.pop()

        if (new_head[0] < 0 or new_head[0] >= 600 or
                new_head[1] < 0 or new_head[1] >= 400 or new_head in snake[1:]):
            running = False

        # Drawing
        screen.blit(image_background, (0, 0))
        screen.blit(head_img, snake[0])
        for block in snake[1:]:
            pygame.draw.rect(screen, RED, (block[0], block[1], cell_size, cell_size))
        pygame.draw.rect(screen, GREEN, (food[0], food[1], cell_size, cell_size))
        pygame.display.flip()

    pygame.quit()
