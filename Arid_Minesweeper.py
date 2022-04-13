"""
course: ICS4U
filename: Arid_Minesweeper.py
name: Abdulla Arid
description: This is Minesweeper. your objective is to click on the blocks that do not have
bombs in them otherwise, you lose the game
"""
import pygame, random, sys
#called when a new bomb formation has to be called based on the game mode(easy, medium, hard)
def bombPosition(mode):
    #clears the list so its always different
    grid.clear()
    BOMB = 9
    # Create a 2 dimensional array.
    options = [0,BOMB]
    #mode is either 5, 7, or 9 based on the difficulty
    for i in range(mode):
        #k makes it a list with the same number of rows as columns, the ratios of bombs can be adjusted here
        grid.append(random.choices(options,weights = [5,2.5],k=mode))
#game starts with menu
def menu():
    run = True
    while run:
        #mouse positions
        mox, moy = pygame.mouse.get_pos()
        #fills the screen in gray
        screen.fill(Gray)
        #title of the game
        screen.blit(LargeF.render("Minesweeper",True,(0,0,0)),(110,40))
        #draws three rectangles for the menu options
        pygame.draw.rect(screen, darkGray,[50,150,400,80])
        #if the user hovers over the button it adds a border
        if mox < 450 and mox > 50 and moy < 230 and moy > 150:
            pygame.draw.rect(screen, Black,[50,150,400,80],2)
        pygame.draw.rect(screen, darkGray,[50,250,400,80])
        if mox < 450 and mox > 50 and moy < 330 and moy > 250:
            pygame.draw.rect(screen, Black,[50,250,400,80],2)
        pygame.draw.rect(screen, darkGray,[50,350,400,80])
        if mox < 450 and mox > 50 and moy < 430 and moy > 350:
            pygame.draw.rect(screen, Black,[50,350,400,80],2)
        #shows the three options' titles
        screen.blit(LargeF.render("Play",True,(0,0,0)),(190,160))
        screen.blit(LargeF.render("Help",True,(0,0,0)),(190,260))
        screen.blit(LargeF.render("Quit",True,(0,0,0)),(190,360))
        for e in pygame.event.get():
            #when the user presses on the x button it quits
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running == False
            #if the user clicks with their left mouse button
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mx, my = pygame.mouse.get_pos()
                #if clicked on first button it takes to difficulty seletion
                if mx < 450 and mx > 50 and my < 230 and my > 150:
                    screen.fill((110,110,110))
                    gameMode()
                #if clicked on second button it takes to rules page
                if mx < 450 and mx > 50 and my < 330 and my > 250:
                    rules()
                #if clicked on third button it exits
                if mx < 450 and mx > 50 and my < 430 and my > 350:
                    pygame.quit()
                    sys.exit()
                    running == False
        #updates the screen with the things drawn
        pygame.display.update()
#rules page
def rules():
    run = True
    while run:
        mox, moy = pygame.mouse.get_pos()
        #fills the screen gray
        screen.fill(Gray)
        screen.blit(LargeF.render("Help:",True,(0,0,0)),(170,40))
        #explains the game
        screen.blit(tinyF.render("-You are presented with a board of squares. Some squares contain mines (bombs),",True,(0,0,0)),(10,110))
        screen.blit(tinyF.render("others don't. If you click on a square containing a bomb, you lose. If you manage",True,(0,0,0)),(10,130))
        screen.blit(tinyF.render("to click all the squares (without clicking on any bombs) you win.",True,(0,0,0)),(10,150))
        screen.blit(tinyF.render("-Clicking a square which doesn't have a bomb reveals the number of neighbouring ",True,(0,0,0)),(10,180))
        screen.blit(tinyF.render("squares containing bombs. Use this information plus some guess work to avoid",True,(0,0,0)),(10,200))
        screen.blit(tinyF.render("the bombs.",True,(0,0,0)),(10,220))
        #draws the rectangles for the options
        pygame.draw.rect(screen, darkGray,[50,280,400,50])
        #if the user hovers over the button it adds a border
        if mox < 450 and mox > 50 and moy < 330 and moy > 280:
            pygame.draw.rect(screen, Black,[50,280,400,50],2)
        pygame.draw.rect(screen, darkGray,[50,350,400,50])
        if mox < 450 and mox > 50 and moy < 400 and moy > 350:
            pygame.draw.rect(screen, Black,[50,350,400,50],2)
        pygame.draw.rect(screen, darkGray,[50,420,400,50])
        if mox < 450 and mox > 50 and moy < 470 and moy > 420:
            pygame.draw.rect(screen, Black,[50,420,400,50],2)
        #names for the options
        screen.blit(mediumF.render("Play",True,(0,0,0)),(200,280))
        screen.blit(mediumF.render("Main Menu",True,(0,0,0)),(150,355))
        screen.blit(mediumF.render("Quit",True,(0,0,0)),(200,420))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running == False
            #if clicked with the left mouse button
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                #positions of the mouse
                mx, my = pygame.mouse.get_pos()
                #if clicked on the first option it takes to difficulty selector
                if mx < 450 and mx > 50 and my < 330 and my > 280:
                    gameMode()
                #if clicked on the second option it takes to main menu
                if mx < 450 and mx > 50 and my < 400 and my > 350:
                    menu()
                #if clicked on the third option it quits
                if mx < 450 and mx > 50 and my < 470 and my > 420:
                    pygame.quit()
                    sys.exit()
                    running == False
        #updates the screen with the things drawn
        pygame.display.update()
#game difficulty selector
def gameMode():
    run = True
    while run:
        mox, moy = pygame.mouse.get_pos()
        #fills the screen in gray
        screen.fill(Gray)
        #title of page is drawn
        screen.blit(LargeF.render("Game Mode:",True,(0,0,0)),(110,40))
        #draws the rectangles for the options
        pygame.draw.rect(screen, darkGray,[50,120,400,60])
        #if the user hovers over the button it adds a border
        if mox < 450 and mox > 50 and moy < 180 and moy > 120:
            pygame.draw.rect(screen, Black,[50,120,400,60],2)
        pygame.draw.rect(screen, darkGray,[50,220,400,60])
        if mox < 450 and mox > 50 and moy < 280 and moy > 220:
            pygame.draw.rect(screen, Black,[50,220,400,60],2)
        pygame.draw.rect(screen, darkGray,[50,320,400,60])
        if mox < 450 and mox > 50 and moy < 380 and moy > 320:
            pygame.draw.rect(screen, Black,[50,320,400,60],2)
        pygame.draw.rect(screen, darkGray,[50,420,400,60])
        if mox < 450 and mox > 50 and moy < 480 and moy > 420:
            pygame.draw.rect(screen, Black,[50,420,400,60],2)
        #displays the titles for the options
        screen.blit(LargeF.render("Easy",True,(0,0,0)),(190,120))
        screen.blit(LargeF.render("Medium",True,(0,0,0)),(170,220))
        screen.blit(LargeF.render("Hard",True,(0,0,0)),(190,320))
        screen.blit(LargeF.render("Back to Menu",True,(0,0,0)),(100,420))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running == False
            #if clicked with left mouse button
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                #mouse positions
                mx, my = pygame.mouse.get_pos()
                #if clicked on first positon the mode is set to easy(5x5) and it calls onto the game screen
                if mx < 450 and mx > 50 and my < 180 and my > 120:
                    mode = 5
                    #creates the positons for the bombs
                    bombPosition(mode)
                    gameScreen(mode)
                #if clicked on second positon the mode is set to medium(7x7) nd it calls onto the game screen
                if mx < 450 and mx > 50 and my < 280 and my > 220:
                    mode = 7
                    #creates the positons for the bombs
                    bombPosition(mode)
                    gameScreen(mode)
                #if clicked on third positon the mode is set to hard(9x9) nd it calls onto the game screen
                if mx < 450 and mx > 50 and my < 380 and my > 320:
                    mode = 9
                    #creates the positons for the bombs
                    bombPosition(mode)
                    gameScreen(mode)
                #if clicked on the fourth option, it goes to menu
                if mx < 450 and mx > 50 and my < 480 and my > 420:
                    menu()
        #updates screen with whats been drawn
        pygame.display.update()
#game screen. parameter is game mode(easy(5),medium(7),and hard(9))
def gameScreen(mode):
    #resets the list that determines if the number of blocks exposed is equal to the number of regular blocks(0)in the grid list
    blockExpose.clear()
    #for testing
    #print(grid)
    while True:
        #Title of game
        main = mediumF.render("Minesweeper",True,(0,0,0))
        #the game is run on a grey screen
        screen.fill(Gray)
        #sets initial x point and y point then the size of the squares
        #if on easy mode
        if mode == 5:
            x= 80
            y = 100
            size = 50
        #if on medium mode
        if mode == 7:
            x= 50
            y = 80
            size = 50
        #if on hard mode
        if mode == 9:
            x = 30
            y = 60
            size = 40
        #for the number of rows in the grid and the number of columns, it creates a square block
        for row in range(mode):
            for column in range(mode):
                colour = (110,255,110)
                #colour = (255,255,255)
                if grid[row][column] == 9:
                    colour = (255,255,255)
                #adds a square to the screen, then adds a margin dependent on the mode. The for loop is based off of the game mode.
                """" For testing, replace 'White' on the next line with 'colour'"""
                pygame.draw.rect(screen, darkGray,[x,y,size,size])
                #margin sizes
                #if on easy mode
                if mode == 5:
                    x+= 70
                #if on medium mode
                if mode == 7:
                    x+= 60
                if mode == 9:
                    x+= 50
            #resets initial x points, then creates the margins for the y axis
            #if on easy mode
            if mode == 5:
                x= 80
                y += 80
            #if on medium mode
            if mode == 7:
                x= 50
                y += 60
            #if on hard mode
            if mode == 9:
                x= 30
                y += 48
        #creates quit button on right
        pygame.draw.rect(screen, darkGray,[380,10,100,40])
        screen.blit(smallF.render("Quit",True,(0,0,0)),(395,8))
        #creates main menu button on left
        pygame.draw.rect(screen, darkGray,[20,10,100,40])
        screen.blit(smallF.render("Menu",True,(0,0,0)),(30,8))
        #adds 'Minesweeper' text
        #if on easy or medium
        if mode == 5 or mode == 7:
            screen.blit(main,(150,30))
        #if on hard
        if mode == 9:
            screen.blit(main,(150,10))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running == False
            #while loop so that drawn objects stay on screen
            clicked = True
            while clicked:
                click(mode,clicked)
        #updates the screen with drawn objects
        pygame.display.update()
def click(mode,clicked):
    pygame.display.update()
    #sets initial x point and y point then the size of the squares
    #if on easy mode
    if mode == 5:
        x= 80
        xend = x + 50
        y = 100
        yend = y + 50
    #if on medium mode
    if mode == 7:
        x= 50
        xend = x + 50
        y = 80
        yend = y + 50
    if mode == 9:
        x= 30
        xend = x + 40
        y = 60
        yend = y + 40
    for i in blockExpose:
        #if the number of items on blockexpose list are equal to the number of non bombs(0) in the grid, it takes the user to the win screen
        if i == (sum([row.count(0) for row in grid])+1):
            win(mode)
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running == False
        #if the user user clicks withn the left mouse button
        if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
            #mouse positions
            mx, my = pygame.mouse.get_pos()
            #if the user clicks on the quit button on the right it quits
            if mx < 480 and mx > 380 and my < 50 and my > 10:
                pygame.quit()
                sys.exit()
                running == False
            #if the user clicks on the menu button on the left side it takes the usr to the main menu
            if mx < 120 and mx > 20 and my < 50 and my > 10:
                menu()
            #goes through the items in the grid based on the game mode
            for row in range(mode):
                for column in range(mode):
                    #if the user clicks on a block
                    if mx >= x and mx <= xend and my >= y and my <= yend:

                        if grid[row][column] == 0:
                            #if the block has already been pressed and its not a bomb it passes the if statement
                            if grid[row][column] == "pressed":
                                pass
                            #if the block has no bomb in it and hasnt been pressed,it calls the expose function to display the number,
                            #then appends a number to the block expose list. It then sets the position to 'pressed'
                            else:
                                expose(mode,row,column,x,y)
                                blockExpose.append(1)
                                grid[row][column] = "pressed"
                        #if the block pressed is a bomb it calls the explode function thats displaus all the bombs, then displays the loss screen
                        if grid[row][column] == BOMB:
                            explode(mode)
                            loss(mode)
                    #same positions as the block creating from the gamescreen() function
                    #if on easy mode
                    if mode == 5:
                        x += 70
                        xend = x + 50
                    #if on medium mode
                    if mode == 7:
                        x += 60
                        xend = x + 50
                    #if on hard mode
                    if mode == 9:
                        x += 50
                        xend = x + 40
                #same positions as the block creating from the gamescreen() function
                #if on easy mode
                if mode == 5:
                    x= 80
                    xend = x + 50
                    y += 80
                    yend = y + 50
                #if on medium mode
                if mode == 7:
                    x= 50
                    xend = x + 50
                    y += 60
                    yend = y + 50
                #if on hard mode
                if mode == 9:
                    x= 30
                    xend = x + 40
                    y += 48
                    yend = y + 40
#called when a non bomb has been called
def expose(mode,row,column,x,y):
    #minimum rows in the grid
    Min = 0
    #maximum rows in the grid
    Max = mode-1
    #block to the right
    maxRow=row+1
    #block to the left
    minRow=row-1
    #block to the bottom
    maxColumn=column+1
    #block to the top
    minColumn=column-1
    #count of bombs beside block
    cnt = 0
    i=row-1
    j=column-1
    #if on easy or medium mode
    if mode == 5 or mode == 7:
        pygame.draw.rect(screen, White,[x,y,50,50])
    if mode == 9:
        pygame.draw.rect(screen, White,[x,y,40,40])
    while i<=maxRow:
        #while the column on top is less than the column below
        while j<=maxColumn:
            #if they are on the grid and a bomb is on that spot, it adds 1 to the counter
            if (i>=Min and i<=Max and j>=Min and j<=Max):
                if grid[i][j] == BOMB:
                    cnt+=1
            #checks the next column
            j+=1
        #checks the next row
        i+=1
        j=minColumn
    #print(cnt)
    cntN = mediumF.render(str(cnt),True,(180,0,0))
    cntS = smallF.render(str(cnt),True,(250,0,0))
    #if on easy mode
    if mode == 5:
        screen.blit(cntN,(x+15,y+5))
    #if on medium mode
    if mode == 7:
        screen.blit(cntN,(x+15,y+5))
    #if on hard mode
    if mode == 9:
        screen.blit(cntS,(x+12,y))
    pygame.display.update()
#when the user clicks on a bomb, the loss screen is called
def loss(mode):
    while True:
        mox, moy = pygame.mouse.get_pos()
        #fills the screen gray
        screen.fill(Gray)
        #adds title
        screen.blit(LargeF.render("You Have Lost!",True,(0,0,0)),(100,90))
        #adds rectangles for the options
        pygame.draw.rect(screen, darkGray,[50,150,400,80])
        #if the user hovers over the button it adds a border
        if mox < 450 and mox > 50 and moy < 230 and moy > 150:
            pygame.draw.rect(screen, Black,[50,150,400,80],2)
        pygame.draw.rect(screen, darkGray,[50,250,400,80])
        if mox < 450 and mox > 50 and moy < 330 and moy > 250:
            pygame.draw.rect(screen, Black,[50,250,400,80],2)
        pygame.draw.rect(screen, darkGray,[50,350,400,80])
        if mox < 450 and mox > 50 and moy < 430 and moy > 350:
            pygame.draw.rect(screen, Black,[50,350,400,80],2)
        #titles for the options
        screen.blit(LargeF.render("Play Again",True,(0,0,0)),(140,160))
        screen.blit(LargeF.render("Main Menu",True,(0,0,0)),(140,260))
        screen.blit(LargeF.render("Quit",True,(0,0,0)),(190,360))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running == False
            #if the user clicks with the left mouse button
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                #mouse positions
                mx, my = pygame.mouse.get_pos()
                #if the user clicks on the first option it creates the grid again with the same mode then calls the game screen
                if mx < 450 and mx > 50 and my < 230 and my > 150:
                    bombPosition(mode)
                    gameScreen(mode)
                #if the user clicks on the second option it goes to the menu
                if mx < 450 and mx > 50 and my < 330 and my > 250:
                    menu()
                #if the user clicks the third option it exits the program
                if mx < 450 and mx > 50 and my < 430 and my > 350:
                    pygame.quit()
                    sys.exit()
                    running == False
        #updates the screen with the items drawn on it
        pygame.display.update()
#when the user clicks all the blocks without bombs it calls this function
def win(mode):
    while True:
        mox, moy = pygame.mouse.get_pos()
        #fills the screen with gray
        screen.fill(Gray)
        screen.blit(LargeF.render("You Have Won!",True,(0,0,0)),(100,90))
        #displays rectangles for the options
        pygame.draw.rect(screen, darkGray,[50,150,400,80])
        #if the user hovers over the button it adds a border
        if mox < 450 and mox > 50 and moy < 230 and moy > 150:
            pygame.draw.rect(screen, Black,[50,150,400,80],2)
        pygame.draw.rect(screen, darkGray,[50,250,400,80])
        if mox < 450 and mox > 50 and moy < 330 and moy > 250:
            pygame.draw.rect(screen, Black,[50,250,400,80],2)
        pygame.draw.rect(screen, darkGray,[50,350,400,80])
        if mox < 450 and mox > 50 and moy < 430 and moy > 350:
            pygame.draw.rect(screen, Black,[50,350,400,80],2)
        #displays text for the options
        screen.blit(LargeF.render("Play Again",True,(0,0,0)),(140,160))
        screen.blit(LargeF.render("Main Menu",True,(0,0,0)),(140,260))
        screen.blit(LargeF.render("Quit",True,(0,0,0)),(190,360))
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                running == False
            #if the user clicks with the left mouse button
            if e.type == pygame.MOUSEBUTTONDOWN and e.button == 1:
                mx, my = pygame.mouse.get_pos()
                #if the user clicks the first option it creates a new grid with the same mode and then calls the game screen
                if mx < 450 and mx > 50 and my < 230 and my > 150:
                    bombPosition(mode)
                    gameScreen(mode)
                #if the user clicks the second option it calls the main menu
                if mx < 450 and mx > 50 and my < 330 and my > 250:
                    menu()
                #if the user clicks the third option it exits
                if mx < 450 and mx > 50 and my < 430 and my > 350:
                    pygame.quit()
                    sys.exit()
                    running == False
        #updates the screen with whats been drawn
        pygame.display.update()
#called when a bomb is clicked
def explode(mode):
    #title text
    main = mediumF.render("Minesweeper",True,(0,0,0))
    #sets initial x point and y point then the size of the squares
    #if on easy mode
    if mode == 5:
        x= 80
        y = 100
        size = 50
    #if on medium mode
    if mode == 7:
        x= 50
        y = 80
        size = 50
    #if on hard mode
    if mode == 9:
        x = 30
        y = 60
        size = 40

    for row in range(mode):
        for column in range(mode):
            #adds a picture of a bomb on all of the bombs on the game grid
            if grid[row][column] == BOMB:
                screen.blit(bombPic,(x,y))
            #margins for x axis
            #if on easy mode
            if mode == 5:
                x+= 70
            #if on medium mode
            if mode == 7:
                x+= 60
            if mode == 9:
                x+= 50
        #resets x starting point and sets y axis margins
        #if on easy mode
        if mode == 5:
            x= 80
            y += 80
        #if on medium mode
        if mode == 7:
            x= 50
            y += 60
        if mode == 9:
            x= 30
            y += 48
    #adds 'Minesweeper' text
    #if on easy or medium mode
    if mode == 5 or mode == 7:
        screen.blit(main,(150,30))
    #if on hard mode, text needs more space
    if mode == 9:
        screen.blit(main,(150,10))
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
            running == False
        clicked = True
    #adds the explosion sound effect
    pygame.mixer.music.play(0)
    #updates the display with all the bombs added
    pygame.display.update()
    #pauses the screen for 2 seconds so that the bombs could remain.
    pygame.time.delay(2000)
#initializes pygame
pygame.init()
#create the screen
screen = pygame.display.set_mode((500,500))
#font sizes
tinyF = pygame.font.SysFont("Times New Roman",14)
smallF = pygame.font.SysFont("Times New Roman",35)
mediumF = pygame.font.SysFont("Times New Roman",40)
LargeF = pygame.font.SysFont("Times New Roman",50)
#colours
Black = (0,0,0)
darkGray = (90,90,90)
Gray = (130,130,130)
White = (255,255,255)
#sound for explosion
pygame.mixer.music.load('Explosion+11.wav')
#title and icon
pygame.display.set_caption("Minesweeper")
icon = pygame.image.load("bomb.png")
pygame.display.set_icon(icon)
#bomb when exploded
bombPic = pygame.image.load("bomb100.png")
bombPic = pygame.transform.scale(bombPic,(40,40))
#grid for bomb placement. created in bombPosition() function
grid = []
#list that adds 1 everytime a block is clicked
blockExpose = []
BOMB = 9
#main menu function. no while loop is added in the main program because the main menu funciton contains a while loo[]
menu()
