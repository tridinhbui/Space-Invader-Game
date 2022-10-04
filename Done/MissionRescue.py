import pygame, random, time, sys
pygame.init()
m = 100
headImg = pygame.transform.scale(pygame.image.load("/Users/buidinhtri/Downloads/136704587_1980154498790647_3140694850297221092_n.bmp"),(m,m))
bodyImg = pygame.transform.scale(pygame.image.load("/Users/buidinhtri/Downloads/gold-coins-png-image-coins-gold-coins-clip-art-coin-catalog-png-3657_2560.bmp"),(m,m))
humanImg = pygame.transform.scale(pygame.image.load("/Users/buidinhtri/Downloads/gold-coins-png-image-coins-gold-coins-clip-art-coin-catalog-png-3657_2560.bmp"),(m,m))
gameSurface = pygame.display.set_mode((1600,800))
background = pygame.image.load('/Users/buidinhtri/Desktop/Python Basic/Game /universe.bmp')
background = pygame.transform.scale(background,(800,500))

pygame.display.set_caption('RocketRescue')
rockpos = [200,80]
rockbody = [[200,80],[130,80],[60,80]]

#Toa do human
humanx = random.randrange(1,158)
humany = random.randrange(1,78)
if humanx %7 != 0: humanx += 1
if humany %7 != 0: humany += 1
humanpos = [humanx*10, humany*10]
humanflat = True

direction = "Right"
changeto = direction
score = 0

#Color
red = pygame.Color(255,0,0)
blue = pygame.Color(65,105,255)
black = pygame.Color(0,0,0)
gray = pygame.Color(128,128,128)
white  = pygame.Color(255,255,255)

def show_score(choice = 1):
    sfont = pygame.font.SysFont('san', 20)
    ssurf = sfont.render("Score: {0}".format(score), True,black)
    srect= ssurf.get_rect()
    if choice == 1:
        srect.midtop = (70,20)
    else:
        srect.midtop = (360,230)
    gameSurface.blit(ssurf,srect)

def game_over():
    gfont = pygame.font.SysFont("san", 40)
    gsurf = gfont.render("Game over!",True,red)
    rect = gsurf.get_rect()
    rect.midtop = (420,150)
    gameSurface.blit(gsurf,rect)
    show_score(0)
    time.sleep(0)
    # pygame.quit()
    # sys.exit()

while True:
    pygame.time.delay(400)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        #xu li phim
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                changeto = 'RIGHT'
            if event.key == pygame.K_LEFT:
                changeto = 'LEFT'
            if event.key == pygame.K_UP:
                changeto = 'UP'
            if event.key == pygame.K_DOWN:
                changeto = 'DOWN'
            if event.key == pygame.K_ESCAPE:
                pygame.event.post(pygame.event.Event(pygame.QUIT))
    
#Huong di
    if changeto == "RIGHT" and not direction == "LEFT":
        direction = "RIGHT"
    if changeto == "LEFT" and not direction == "RIGHT":
        direction = "LEFT"
    if changeto == "UP" and not direction == "DOWN":
        direction = "UP"
    if changeto == "DOWN" and not direction == "UP":
        direction = "DOWN"

    if direction == "RIGHT" :
        rockpos[0] += m
    if direction == "LEFT" :
        rockpos[0] -= m
    if direction == "UP" :
        rockpos[1] -= m
    if direction == "DOWN" :
        rockpos[1] += m

    #Lam dai ra
    rockbody.insert(0,list(rockpos))
    if rockpos[0] == humanpos[0] and rockpos[1] == humanpos[1]:
        score +=1
        humanflat = False
    else:
        rockbody.pop()
    
    #Tao ra nguoi
    if humanflat == False:
        humanx = random.randrange(1,158)
        humany = random.randrange(1,78)
        if humanx % 7 != 0: humanx += 1
        if humany % 7 != 0: humany += 1
        humanpos = [humanx*10, humany*10]
    humanflat = True
    
    #Cap nhat len cua so
    gameSurface.fill(white)

    for pos in rockbody:
        gameSurface.blit(bodyImg,pygame.Rect(pos[0], pos[1],m,m))
    gameSurface.blit(headImg,pygame.Rect(rockbody[0][0],rockbody[0][1],m,m))
    gameSurface.blit(humanImg,pygame.Rect(humanpos[0],humanpos[1],m,m))

        #Canh bien
    if rockpos[0] > 1580 or rockpos[0] < 10:
        game_over
    if rockpos[1] > 780 or rockpos[1] <10:
        game_over()

    for b in rockbody[1:]:
        if rockpos[0] == b[0] and rockpos[1] == b[1]:
            game_over

    #Duong vien
    pygame.draw.rect(gameSurface, gray,(10,10,1580,780),2)
    show_score()
    pygame.display.flip()
