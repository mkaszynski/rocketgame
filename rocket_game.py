import pygame
import pygame.locals as pg_locals
import time as t

WELCOME_TXT = 'Hello! Welcome to rocket game.'

def wrap_text(text, font, colour, x, y, screen, allowed_width):
    # first, split the text into words
    words = text.split()

    # now, construct lines out of these words
    lines = []
    while len(words) > 0:
        # get as many words as will fit within allowed_width
        line_words = []
        while len(words) > 0:
            line_words.append(words.pop(0))
            fw, fh = font.size(' '.join(line_words + words[:1]))
            if fw > allowed_width:
                break

        # add a line consisting of those words
        line = ' '.join(line_words)
        lines.append(line)

    y_offset = 0
    for line in lines:
        fw, fh = font.size(line)

        # (tx, ty) is the top-left of the font surface
        tx = x
        ty = y + y_offset
        y_offset += fh

        font_surface = font.render(line, True, colour)
        screen.blit(font_surface, (tx, ty))


# def :
#     return (random.randint(0, 255),
#             random.randint(0, 255),
#             random.randint(0, 255))

def add_line(screen, text, x, y):
    # used to print the status of the variables
    text = font.render(text, True, white) 
    text_rect = text.get_rect()
    text_rect.topleft = (x, y)
    screen.blit(text, text_rect)
    

green = 255
blue = 255


black = (0, 0, 0)
white = (255, 255, 255)

first_t = 1

TICKS = 60
vel_y = 0

GRAVITY = -3
ANTIGRAVITY = 3

pygame.init()
font = pygame.font.Font('freesansbold.ttf', 32)
jump_num = 0.001

# set the screen size
full_screen = True
if full_screen:
    info = pygame.display.Info()
    SCREEN_WIDTH, SCREEN_HEIGHT = info.current_w, info.current_h - 95
else:
    SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 600

screen = pygame.display.set_mode((0, 0))


HEIGHT = 10
GROUND_Y = SCREEN_HEIGHT - HEIGHT

pos_x = 0.5 * SCREEN_WIDTH
pos_y = GROUND_Y

my_color = (255, 0, 0)
bounce = 0
gravity = 1000
friction = 0.5
y_pos_y = pos_y
jump = 5
vel_x_2 = 0
first_t = 0
pos_x_2 = 0.5 * SCREEN_WIDTH + 40
vel_x = 0
vel_y = 0
monney = 0
gas = 100
rocket_on = False
# use this clock to limit the update of the game
clock = pygame.time.Clock()

unn = True
while unn:
    screen.fill((200, 0, 255))# make entire screen black
    add_line(screen, 'Kaszynski studios',
                     550, 250)
    pygame.event.poll()
    pygame.display.update()
    t.sleep(2)
    clock.tick(TICKS)
    unn = False

first_time = True
running = True
while running:
    screen.fill((0, green, blue))  # make entire screen black
    
    # display welcome text
    if first_time:
        
        wrap_text(WELCOME_TXT, font, 'white', 400, 200, screen,
                  SCREEN_WIDTH // 2)

        pygame.event.poll()
        keys = pygame.key.get_pressed()
        pygame.display.update()

        if keys[pg_locals.K_RETURN]:
            first_time = False
        
        
        continue        

    pygame.display.set_caption('rocket game')

    GROUND_Y = SCREEN_HEIGHT - HEIGHT
    on_ground = pos_y == GROUND_Y

    # update events
    pygame.event.poll()

    keys = pygame.key.get_pressed()
    
    if True:
        if keys[pg_locals.K_d]:
            vel_x = 10
        if keys[pg_locals.K_a]:
            vel_x = -10
        
        pos_x_2 =+ vel_x_2
            
        if vel_y > 0:
            vel_y = vel_y + 0.5
        
        # simulate drag
        vel_x -= friction *vel_x
        if abs(vel_x) < 0.5:
            vel_x = 0
            
        monney = monney*0.5 + vel_y * -1
    
    pos_x += vel_x

    # bounds checking
    if pos_x < 0:
        pos_x = 0
        vel_x = vel_x * -1
    if pos_x > SCREEN_WIDTH - HEIGHT:
        pos_x = SCREEN_WIDTH - HEIGHT
        vel_x = vel_x * -1
    
    if keys[pg_locals.K_q]:
        running = False
    if keys[pg_locals.K_w]:
        if gas > 0:
            vel_y -= jump
            # jump += jump_num
            gas = gas - 0.02
            rocket_on = True
            jump = jump + jump_num
    
    blue = ((pos_y - 663) * 0.1 ) + 255
    green = ((pos_y - 663) * 0.1 ) + 255
    
    if blue > 255:
        blue = 255
    if green > 255:
        blue = 255
    
    if not keys[pg_locals.K_w]:
        rocket_on = False
            
    if pos_x_2 < 0:
        pos_x_2 = 0
        vel_x_2 = vel_y * -1
            
    if blue < 0:
        blue = 0
    if green < 0:
        green = 0
            
    if y_pos_y > 0.5*SCREEN_HEIGHT:
        y_pos_y = 0.5*SCREEN_HEIGHT
    
    if gas < 0:
        gas = 0
    
    # falls to the roof
    if gravity < 0:
        vel_y -= 1
    
    if pos_y > -600000000:
        gravity = 0
        
    
    # update position using velocity
    pos_y += vel_y
    # slowly return to 0
    vel_y += gravity
        
    # if pos_y < 0:
    #     pos_y = 0
    #     vel_y *= bounce * -1  # make bounce
    #     my_color = 
    if pos_y > GROUND_Y:
        pos_y = GROUND_Y
        # must reset velocity as well
        vel_y *= bounce * -1# make bounce
        jump = 5
        
        
    # simulate drag
    if abs(vel_y) < 3.0:
        vel_y = 3.0
    
    ground = pygame.Rect(0, -1 * pos_y + 1.5 * SCREEN_HEIGHT + 4*HEIGHT, SCREEN_WIDTH, SCREEN_HEIGHT)
    pygame.draw.rect(screen, (0, 150, 0), ground)
    
    rect = pygame.Rect(pos_x, y_pos_y, HEIGHT, HEIGHT*5)
    pygame.draw.rect(screen, my_color, rect)
    
    if rocket_on == True:
        rect = pygame.Rect(pos_x, y_pos_y + 50, HEIGHT, HEIGHT)
        pygame.draw.rect(screen, (255, 255, 0), rect)
        
    
    add_line(screen, f' Height: {((pos_y - 663) * -1 ) * 0.1:.2f}m',
             0, 0)
    add_line(screen, f'Gas: {gas:.2f}',
             0, 45)
    pygame.display.update()

    # wait until next tick
    clock.tick(TICKS)

pygame.quit()
