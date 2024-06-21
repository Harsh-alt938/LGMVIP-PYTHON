import pygame
import sys
import random

pygame.init()

FPS = 15
LIGHT_YELLOW = (255, 255, 153)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600
VELOCITY = 10
SNAKE_WIDTH = 15
APPLE_SIZE = 20
TOP_WIDTH = 40

verysmall_font = pygame.font.SysFont('Times New Roman', 15)
small_font = pygame.font.SysFont('Verdana', 20)
medium_font = pygame.font.SysFont('Comic Sans MS', 28, True)
large_font = pygame.font.SysFont('Roboto', 65, True, True)
instruction_font = pygame.font.SysFont('Times New Roman', 20, False)
clock = pygame.time.Clock()

canvas = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption('Snake Game')

snake_img = pygame.image.load('snake.png')
apple_img = pygame.image.load('apple2.png')
tail_img = pygame.image.load('tail.png')
apple_img_rect = apple_img.get_rect()

pygame.mixer.music.load('snake_theme.mp3')
game_over_sound = pygame.mixer.Sound('game_over.wav')

def start_game():
    canvas.fill(LIGHT_YELLOW) 
  
    start_font1 = large_font.render("Welcome to snake game", True, BLUE)
    start_font2 = medium_font.render("Play Game", True, RED, YELLOW)
    start_font3 = medium_font.render("Instructions", True, RED, YELLOW)
    start_font4 = medium_font.render("Quit", True, RED, YELLOW)
    start_font5 = medium_font.render("Creator", True, RED, YELLOW)

    start_font1_rect = start_font1.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100))
    start_font2_rect = start_font2.get_rect(center=(WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 50))
    start_font3_rect = start_font3.get_rect(center=(WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT / 2 + 100))
    start_font4_rect = start_font4.get_rect(center=(WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT/2 + 200))
    start_font5_rect = start_font5.get_rect(center=(WINDOW_WIDTH/2 + 100, WINDOW_HEIGHT / 2 + 150))

    canvas.blit(start_font1, start_font1_rect)
    canvas.blit(start_font2, start_font2_rect)
    canvas.blit(start_font3, start_font3_rect)
    canvas.blit(start_font4, start_font4_rect)
    canvas.blit(start_font5, start_font5_rect)

    made_by_text = small_font.render("Made by: Harsh Bhardwaj", True, BLUE)
    made_by_rect = made_by_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT - 20))
    canvas.blit(made_by_text, made_by_rect)

    pygame.display.update()
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    gameloop()
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_font3_rect.collidepoint(x, y):
                    start_inst(start_font1, start_font1_rect)
                elif start_font2_rect.collidepoint(x, y):
                    gameloop()
                elif start_font5_rect.collidepoint(x, y):
                    creator()
                elif start_font4_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()

def creator():
    my_img = pygame.image.load('image1.jpg')
    canvas.fill(LIGHT_YELLOW)
    my_img_rect = my_img.get_rect(center=(WINDOW_WIDTH/2, my_img.get_height()/2 + 20))
    canvas.blit(my_img, my_img_rect)

    start_inst1 = large_font.render("Harsh Bhardwaj", False, GREEN)
    start_inst1_rect = start_inst1.get_rect(center=(WINDOW_WIDTH/2, 420))
    canvas.blit(start_inst1, start_inst1_rect)

    start_inst2 = small_font.render("Hello guys, This is Harsh Bhardwaj. Thanks for playing my game.", True, BLUE)
    start_inst3 = small_font.render("This is a very simple game, developed using python", True, BLUE)
    canvas.blit(start_inst2, (10, 470))
    canvas.blit(start_inst3, (10, 500))
    canvas.blit(start_inst1, (10, 530))

    start_inst5 = medium_font.render("<<BACK", True, RED, YELLOW)
    start_inst5_rect = start_inst5.get_rect(center=(WINDOW_WIDTH - start_inst5.get_width()/2, WINDOW_HEIGHT - start_inst5.get_height()/2))
    canvas.blit(start_inst5, start_inst5_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_inst5_rect.collidepoint(x, y):
                    start_game()
        pygame.display.update()

def start_inst(start_font1, start_font1_rect):
    canvas.fill(LIGHT_YELLOW)
    canvas.blit(start_font1, start_font1_rect)
    start_inst1 = instruction_font.render("☛Objective: Control the snake to eat fruit and grow longer.", True, BLUE)
    start_inst2 = instruction_font.render("☛Controls: Use arrow keys to change the snake's direction.", True, BLUE)
    start_inst3 = instruction_font.render("☛Movement: Snake moves continuously; avoid walls and itself.", True, BLUE)
    start_inst4 = instruction_font.render("☛Growth: Eating fruit makes the snake longer.", True, BLUE)
    start_inst5 = instruction_font.render("☛Scoring: Earn points for each fruit eaten.", True, BLUE)
    start_inst6 = instruction_font.render("☛Game Over: Ends if snake collides; restart for a higher score.", True, BLUE)
    start_inst7 = medium_font.render("<<BACK", True, RED, YELLOW)
    start_inst5_rect = start_inst5.get_rect(center=(WINDOW_WIDTH-100, WINDOW_HEIGHT - 100))

    canvas.blit(start_inst1, (WINDOW_WIDTH/16, WINDOW_HEIGHT/2))
    canvas.blit(start_inst2, (WINDOW_WIDTH/16, WINDOW_HEIGHT/2 + 30))
    canvas.blit(start_inst3, (WINDOW_WIDTH/16, WINDOW_HEIGHT/2 + 60))
    canvas.blit(start_inst4, (WINDOW_WIDTH/16, WINDOW_HEIGHT/2 + 90))
    canvas.blit(start_inst5, (WINDOW_WIDTH/16, WINDOW_HEIGHT/2 + 120))
    canvas.blit(start_inst6, (WINDOW_WIDTH/16, WINDOW_HEIGHT/2 + 150))
    canvas.blit(start_inst7, start_inst5_rect)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if start_inst5_rect.collidepoint(x, y):
                    start_game()
        pygame.display.update()

def gameover(score):
    pygame.mixer.music.stop()
    game_over_sound.play()

    canvas.fill(LIGHT_YELLOW)

    font_gameover1 = large_font.render('GAME OVER', True, GREEN)
    font_gameover2 = medium_font.render("Play Again", True, RED, YELLOW)
    font_gameover3 = medium_font.render("Quit", True, RED, YELLOW)

    font_gameover1_rect = font_gameover1.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2 - 100))
    font_gameover2_rect = font_gameover2.get_rect(center=(WINDOW_WIDTH / 2 + 150, WINDOW_HEIGHT / 2 + 20))
    font_gameover3_rect = font_gameover3.get_rect(center=(WINDOW_WIDTH / 2 + 150, WINDOW_HEIGHT / 2 + 70))

    canvas.blit(font_gameover1, font_gameover1_rect)
    canvas.blit(font_gameover2, font_gameover2_rect)
    canvas.blit(font_gameover3, font_gameover3_rect)

    save_high_score(score)
    highest_score = load_high_score()
    highest_score_text = small_font.render(f"Highest Score: {highest_score}", True, BLUE)
    canvas.blit(highest_score_text, (20, 10))

    made_by_text = small_font.render("Made by: Harsh Bhardwaj", True, BLUE)
    made_by_rect = made_by_text.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT - 20))
    canvas.blit(made_by_text, made_by_rect)

    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if font_gameover2_rect.collidepoint(x, y):
                    gameloop()
                elif font_gameover3_rect.collidepoint(x, y):
                    pygame.quit()
                    sys.exit()

def save_high_score(score):
    with open('highest_score.txt', 'w') as file:
        file.write(str(score))

def load_high_score():
    try:
        with open('highest_score.txt', 'r') as file:
            return int(file.read().strip())
    except FileNotFoundError:
        return 0

def snake(snakelist, direction):
    if direction == 'right':
        head = pygame.transform.rotate(snake_img, 270)
        tail = pygame.transform.rotate(tail_img, 270)
    elif direction == 'left':
        head = pygame.transform.rotate(snake_img, 90)
        tail = pygame.transform.rotate(tail_img, 90)
    elif direction == 'up':
        head = pygame.transform.rotate(snake_img, 0)
        tail = pygame.transform.rotate(tail_img, 0)
    elif direction == 'down':
        head = pygame.transform.rotate(snake_img, 180)
        tail = pygame.transform.rotate(tail_img, 180)

    canvas.blit(head, snakelist[-1])
    canvas.blit(tail, snakelist[0])

    for XnY in snakelist[1:-1]:
        pygame.draw.rect(canvas, BLUE, (XnY[0], XnY[1], SNAKE_WIDTH, SNAKE_WIDTH))

def game_paused():
    paused_font1 = large_font.render("Game Paused", True, RED)
    paused_font_rect1 = paused_font1.get_rect(center=(WINDOW_WIDTH/2, WINDOW_HEIGHT/2))
    canvas.blit(paused_font1, paused_font_rect1)
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pause_xy = event.pos
                if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                    if pause_xy[1] > 0 and pause_xy[1] < 50:
                        return

def gameloop():
    while True:
        pygame.mixer.music.play(-1, 0.0)

        LEAD_X = 0
        LEAD_Y = 100
        direction = 'right'
        score = small_font.render("Score: 0", True, RED)
        APPLE_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
        APPLE_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
        snakelist = []
        snakelength = 3
        pause_font = verysmall_font.render('pause', True, RED)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        if direction == 'right':
                            pass
                        else:
                            direction = 'left'
                    if event.key == pygame.K_RIGHT:
                        if direction == 'left':
                             pass
                        else:
                            direction = 'right'
                    if event.key == pygame.K_UP:
                        if direction == 'down':
                            pass
                        else:
                            direction = 'up'
                    if event.key == pygame.K_DOWN:
                        if direction == 'up':
                            pass
                        else:
                            direction = 'down'
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pause_xy = event.pos
                    if pause_xy[0] > (WINDOW_WIDTH - 50) and pause_xy[0] < WINDOW_WIDTH:
                        if pause_xy[1] > 0 and pause_xy[1] < 50:
                            game_paused()

            if direction == 'up':
                LEAD_Y -= VELOCITY
                if LEAD_Y < TOP_WIDTH:
                    gameover(snakelength - 3)
            elif direction == 'down':
                LEAD_Y += VELOCITY
                if LEAD_Y > WINDOW_HEIGHT - SNAKE_WIDTH:
                    gameover(snakelength - 3)
            elif direction == 'right':
                LEAD_X += VELOCITY
                if LEAD_X > WINDOW_WIDTH - SNAKE_WIDTH:
                    gameover(snakelength - 3)
            elif direction == 'left':
                LEAD_X -= VELOCITY
                if LEAD_X < 0:
                    gameover(snakelength - 3)

            snakehead = [LEAD_X, LEAD_Y]
            snakelist.append(snakehead)

            snake_head_rect = pygame.Rect(LEAD_X, LEAD_Y, SNAKE_WIDTH, SNAKE_WIDTH)
            apple_rect = pygame.Rect(APPLE_X, APPLE_Y, APPLE_SIZE, APPLE_SIZE)
            if snake_head_rect.colliderect(apple_rect):
                APPLE_X = random.randrange(0, WINDOW_WIDTH - 10, 10)
                APPLE_Y = random.randrange(TOP_WIDTH, WINDOW_HEIGHT - 10, 10)
                snakelength += 1
                score = small_font.render("Score: " + str(snakelength - 3), True, RED)

            if len(snakelist) > snakelength:
                del snakelist[0]
                for point in snakelist[:-1]:
                    if point == snakehead:
                        gameover(snakelength - 3)

            canvas.fill(LIGHT_YELLOW)
            snake(snakelist, direction)
            canvas.blit(score, (20, 10))
            pygame.draw.line(canvas, GREEN, (0, TOP_WIDTH), (WINDOW_WIDTH, TOP_WIDTH))
            pygame.draw.line(canvas, YELLOW, (WINDOW_WIDTH - 60, 0), (WINDOW_WIDTH - 60, TOP_WIDTH))
            pygame.draw.rect(canvas, YELLOW, (WINDOW_WIDTH - 60, 0, 60, TOP_WIDTH))
            canvas.blit(pause_font, (WINDOW_WIDTH - 45, 10))
            canvas.blit(apple_img, (APPLE_X, APPLE_Y))
            pygame.display.update()

            clock.tick(FPS)

start_game()
