import pygame
pygame.init()
pygame.mixer.init(44100, -16, 2, 2048) # (frequency, size, channels, buffer)

#Base needed code block 
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock() #Capital C in clock...
running = True

"""
    Soundboard Code by Jack
"""

BUTTON_LENGTH = 200
BUTTON_WIDTH = 200

#Creating the Rect Objects
for i in range(12):
    row = i // 6
    col = i % 6
    x = 15 + (col * 210)
    if row == 0:
        y = 50
    else:
        y = 260
    rect = pygame.Rect(x, y, BUTTON_LENGTH, BUTTON_WIDTH)

# rect_one = pygame.Rect(15, 50, 200, 200)
# rect_two = pygame.Rect(225, 50, 200, 200)
# rect_three = pygame.Rect(435, 50, 200, 200)
# rect_four = pygame.Rect(645, 50, 200, 200)
# rect_five = pygame.Rect(855, 50, 200, 200)
# rect_six = pygame.Rect(1065, 50, 200, 200)
# rect_seven = pygame.Rect(15, 260, 200, 200)
# rect_eight = pygame.Rect(225, 260, 200, 200)
# rect_nine = pygame.Rect(435, 260, 200, 200)
# rect_ten = pygame.Rect(645, 260, 200, 200)
# rect_eleven = pygame.Rect(855, 260, 200, 200)
# rect_twelve = pygame.Rect(1065, 260, 200, 200)

#Soundcode 
sound_one = pygame.mixer.Sound(r"C:\Users\Jack\Ian Hislop's Finest Moments ｜ Have I Got News For You [fqLJC5mdGQk].wav") #r means raw so the backslashes aren't escape characters

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill("black") #Background, update to purple
    #Code goes here
    pygame.draw.rect(screen, ("blue"), rect_one)
    pygame.draw.rect(screen, ("blue"), rect_two)
    pygame.draw.rect(screen, ("blue"), rect_three)
    pygame.draw.rect(screen, ("blue"), rect_four)
    pygame.draw.rect(screen, ("blue"), rect_five)
    pygame.draw.rect(screen, ("blue"), rect_six)
    pygame.draw.rect(screen, ("blue"), rect_seven)
    pygame.draw.rect(screen, ("blue"), rect_eight)
    pygame.draw.rect(screen, ("blue"), rect_nine)
    pygame.draw.rect(screen, ("blue"), rect_ten)
    pygame.draw.rect(screen, ("blue"), rect_eleven)
    pygame.draw.rect(screen, ("blue"), rect_twelve)
    
    #If mouse goes over, need to implement if clicked on 
    x, y = pygame.mouse.get_pos()
    if rect_one.collidepoint(x,y): 
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(screen, ("purple"), rect_one)
    elif rect_two.collidepoint(x,y): 
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(screen, ("purple"), rect_two)
    elif rect_three.collidepoint(x,y): 
        pygame.draw.rect(screen, ("pink"), rect_three)
        if pygame.mouse.get_pressed()[0]:
            pygame.draw.rect(screen, ("purple"), rect_three)
            #pygame.mixer.Sound.play(sound_one)
    
    pygame.display.flip() #shows new frames drawn on screen so you can see them
    clock.tick(60) #60fps
    
pygame.mixer.Sound.stop #stop playing sound
pygame.quit()
