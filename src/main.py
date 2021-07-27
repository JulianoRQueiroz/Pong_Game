import pygame

# Constantes e variáeis 
WHITE = (255, 255, 255) # "Raquetes" 
BLACK = (0, 0, 0)       # Background

WIDTH = 600     # Largura 
HEIGHT = 600    # Comprimento

pygame.init()
game_font = pygame.font.SysFont('Ubuntu', 40)

delay = 30       

paddle_speed = 20   # velocidade das "raquetes"

paddle_widht = 10   # largura das "raquetes"
paddle_height = 100 # altura das "raquetes"

p1_x_pos = 10
p1_y_pos = HEIGHT / 2 - paddle_height / 2  # centralizando "raquete" p1

p2_x_pos = WIDTH - paddle_widht - 10
p2_y_pos = HEIGHT / 2 - paddle_height / 2  # centralizando "raquete" p1

p1_score = 0      # Pontuação P1
p2_score = 0      # Pontuação P2

p1_up = False
p1_down = False
p2_up = False
p2_down = False


ball_x_pos = WIDTH / 2 
ball_y_pos = HEIGHT / 2 
ball_widht = 8 
ball_x_vel = -10
ball_y_vel = 0