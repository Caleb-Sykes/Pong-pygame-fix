import pygame

pygame.init()

display_height = 600
display_width = 900

black = (0,0,0)
white = (255,255,255)
grey = (96, 96, 96)
yellow = (255, 233, 0)
dark_yellow = (183, 148, 20)
orange = (255, 147, 7)
orange2 = (255, 102, 0)
dark_orange = (175, 105, 0)
green = (0, 255, 12)
dark_green = (3, 130, 8)
dark_red = (114, 9, 0)
brown = (81, 48, 16)
red = (255,0,0)
blue = (0,97,255)
dark_blue = (20, 85, 188)
purple = (197, 66, 244)
dark_purple = (162, 52, 201)

gamedisplay = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()
gamedisplay.fill(white)
pygame.display.flip()

# A tool to display any text on any surface
def text_objects(text, font, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

# A tool to display the characters on-screen whilst adjusting color and size
def game_subject(text,dw,dh,color,size):
    largeText = pygame.font.Font('freesansbold.ttf',size)
    TextSurf, TextRect = text_objects(text, largeText, color)
    TextRect.center = (dw,dh)
    gamedisplay.blit(TextSurf, TextRect)

# A tool to display buttons
def button(msg,x,y,w,h,ic,ac,action=None):
    mouse1 = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse1[0] > x and y+h > mouse1[1] > y:
        pygame.draw.rect(gamedisplay, ac,(x,y,w,h))
        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textsurf, textrect = text_objects (msg,smalltext,black)
        textrect.center = ( (x+(w/2)), (y+(h/2)) )
        gamedisplay.blit(textsurf,textrect)
        if click[0] == 1 and action != None:
            if action == "play":
                game_loop()
    else:
        pygame.draw.rect(gamedisplay, ic,(x,y,w,h))
        smalltext = pygame.font.Font("freesansbold.ttf",20)
        textsurf, textrect = text_objects (msg,smalltext,black)
        textrect.center = ( (x+(w/2)), (y+(h/2)) )
        gamedisplay.blit(textsurf,textrect)

# Program In-game loop
def game_loop():

    # position of ball
    posx = 450
    posy = 300

    # boolean variables
    loop = True
    left = True
    right = False
    up = False
    up_div2 = False
    down = False
    down_div2 = False

   # quit and escape function
    while loop:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              quit()
          pressed = pygame.key.get_pressed()
          if pressed[pygame.K_ESCAPE]:
             quit()

      # update and fill screen black
      pygame.display.update()
      gamedisplay.fill(black)

      # ball direction
      if left == True:
          posx -= 10
      elif right == True:
          posx += 10

      if up == True:
          posy -= 10
      elif up == False:
          posy == 0

      if up_div2 == True:
          posy -= 5
      elif up_div2 == False:
          posy == 0

      if down == True:
          posy += 10
      elif down == False:
          posy == 0

      if down_div2 == True:
          posy += 5
      elif down_div2 == False:
          posy == 0

      # Arena Decor
      arena1 = pygame.Rect(display_width/2,0,5,250)
      pygame.draw.rect(gamedisplay,green,arena1)

      arena2 = pygame.Rect(display_width/2,350,5,250)
      pygame.draw.rect(gamedisplay,green,arena2)

      pygame.draw.circle(gamedisplay,green,(450,300),40)

      # ball Logic
      ball_pos = (posx,posy,25,25)
      ball = pygame.draw.rect(gamedisplay,white,ball_pos)

      # Player Logic
      x,y = pygame.mouse.get_pos()
      player_pos = pygame.Rect(10,y,10,100)

      # division of player block
      q1 = pygame.Rect(10,y,10,20)
      q2 = pygame.Rect(10,y+20,10,20)
      q3 = pygame.Rect(10,y+40,10,20)
      q4 = pygame.Rect(10,y+60,10,20)
      q5 = pygame.Rect(10,y+80,10,20)

      player = pygame.draw.rect(gamedisplay,green,player_pos)
      ai = pygame.draw.rect(gamedisplay,green,(880,posy,10,100))

      # barriers
      bar_t = pygame.draw.rect(gamedisplay,black,(-1,0,901,1))
      bar_b = pygame.draw.rect(gamedisplay,black,(-6,601,901,5))

      # collision reaction
      if q1.colliderect(ball_pos) == True:
          left = False
          right = True
          up = True
          #print("q1 is working")
      elif q2.colliderect(ball_pos) == True:
          left = False
          right = True
          up_div2 = True
          #print("q2 is working")
      elif q3.colliderect(ball_pos) == True:
          left = False
          right = True
          down_div2 = True
          #print("q3 is working")
      elif q4.colliderect(ball_pos) == True:
          left = False
          right = True
          down_div2 = True
          #print("q4 is working")
      elif q5.colliderect(ball_pos) == True:
          left = False
          right = True
          down = True
          #print("q5 is working")
      elif ai.colliderect(ball_pos) == True:
          left = True
          Right = False
          #print("goal worx")
      elif bar_t.colliderect(ball_pos) == True and posy <= 5:
          down = True
          up = False
          #print("bar top worx")
      elif bar_t.colliderect(ball_pos) == True and posy >= 10:
          down = True
          up = False
          #print("bar top worx")
      elif bar_b.colliderect(ball_pos) == True and posy <= 5:
          down = False
          up_div2 = True
          #print("bar bottom worx")
      elif bar_b.colliderect(ball_pos) == True and posy >= 10:
          down = False
          up = True
          #print("bar bottom worx")

      #NOTWORKING
      if posx <= -1:
          posx = 450
          posy = 300
          up = False
          down = False
          left = True
          right = False
      elif posx >= 901:
          posx = 450
          posy = 300
          up = False
          down = False
          left = False
          right = True

      # screen update and FPS counter
      pygame.display.update()
      clock.tick(60)

def any_key():
    intro = True
    half_w = display_width/2
    half_h = display_height/2

    while intro:
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              quit()
          pressed = pygame.key.get_pressed()
          if pressed[pygame.K_SPACE]:
             game_loop()

      pygame.display.update()
      gamedisplay.fill(black)

      game_subject("Press Space Bar to Start Pong",half_w,half_h,green,40)

      pygame.display.update()
      clock.tick(60)

any_key()
game_loop()
quit()
