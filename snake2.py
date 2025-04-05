import pygame
import random

pygame.init()


WIDTH, HEIGHT = 600,600
CELL_SIZE = 20
FOOD_LIFESPAN = 5000  

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()


background_image = pygame.image.load("images/grass.png")  
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


snake_image = pygame.image.load("images/snake.png") 
food_image_1 = pygame.image.load("images/apple.png") 
food_image_2 = pygame.image.load("images/banana.png")  
food_image_3 = pygame.image.load("images/cherry.png")  

snake_image = pygame.transform.scale(snake_image, (CELL_SIZE, CELL_SIZE))
food_image_1 = pygame.transform.scale(food_image_1, (CELL_SIZE, CELL_SIZE))
food_image_2 = pygame.transform.scale(food_image_2, (CELL_SIZE, CELL_SIZE))
food_image_3 = pygame.transform.scale(food_image_3, (CELL_SIZE, CELL_SIZE))


snake = [(100, 100), (90, 100), (80, 100)]
direction = (CELL_SIZE, 0)


food = None
food_value = 1
food_image = food_image_1
food_spawn_time = pygame.time.get_ticks()

def generate_food():
    
    global food_value, food_image, food_spawn_time
    while True:
        new_food = (
            random.randint(0, (WIDTH // CELL_SIZE) - 1) * CELL_SIZE,
            random.randint(0, (HEIGHT // CELL_SIZE) - 1) * CELL_SIZE
        )
        if new_food not in snake: 
            food_spawn_time = pygame.time.get_ticks()  
            food_value = random.choice([1, 2, 3])  
            food_image = food_image_1 if food_value == 1 else (food_image_2 if food_value == 2 else food_image_3)
            return new_food


food = generate_food()


score = 0
level = 1
speed = 7 
food_per_level = 3  
font = pygame.font.Font(None, 36)

def check_collision(head):
    
    return (
        head in snake or 
        head[0] < 0 or head[1] < 0 or 
        head[0] >= WIDTH or head[1] >= HEIGHT 
    )


running = True
while running:
   
    screen.blit(background_image, (0, 0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

   
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and direction != (CELL_SIZE, 0):
        direction = (-CELL_SIZE, 0)
    if keys[pygame.K_RIGHT] and direction != (-CELL_SIZE, 0):
        direction = (CELL_SIZE, 0)
    if keys[pygame.K_UP] and direction != (0, CELL_SIZE):
        direction = (0, -CELL_SIZE)
    if keys[pygame.K_DOWN] and direction != (0, -CELL_SIZE):
        direction = (0, CELL_SIZE)

  
    new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
    if check_collision(new_head):
        running = False  
    snake.insert(0, new_head)

   
    if new_head == food:
        score += food_value  
        food = generate_food() 
        
        if score // food_per_level >= level:
            level += 1
            speed += 1  
    else:
        snake.pop()  
    
   
    if pygame.time.get_ticks() - food_spawn_time > FOOD_LIFESPAN:
        food = generate_food()  
    
   
    for segment in snake:
        screen.blit(snake_image, segment)
    

    screen.blit(food_image, food)
    
    
    score_text = font.render(f"Score: {score}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (10, 40))

    pygame.display.update()
    clock.tick(speed)  

pygame.quit()
