import pygame
import sys

def Screen_Text(text, font, colour, surface, x, y):
    '''
    Function takes 5 variables (text, font, colour, surface, x, y)
    Displays the text variable onto the pygame screen
    '''
    #given the text variable, set the texts font size and colour. Assign it to variable 'ScreenText'
    ScreenText = font.render(text, True, colour)
    TextPosition = ScreenText.get_rect() #set a rect for the size  of the text inputted. Set rect to variable 'TextPosition'
    TextPosition.topleft = (x,y) #Set the TOP LEFT corner of the rect to the x and y postion given
    screen.blit(ScreenText, TextPosition) #display the text.

def MainMenu():
    '''
    Function takes no argument
    Does not return a value
    Displays the main menu menu screen
    Displays to the user 3 options to choose from (Play, Help, Quit)
    '''
    running = True
    while running:
        #get the position of the mouse on the screen. set it to variable 'mouse'
        mouse = pygame.mouse.get_pos()
        screen.fill (Black) #colour the screen
        #check is the length of the list is 0. This means that the user still doesnt have a highscore
        if len(score)==0:
            Screen_Text("Highscore: ",small_font, White, screen, 10, 10) #print an empty high score
        #else the user has played at least once. this means that the length of the score list will be at least 1
        else:
            #display the SMALLEST number in the list. This number will be the highscore
            Screen_Text("Highscore: "+str(min(score))+"s", small_font, White, screen, 10, 10)

        screen.blit(load_key, (260,50)) #display the main game image
        Screen_Text("EXIT!", large_font, Light_Yellow, screen, 260,300) #display game title
        #if the mouse cursor is within the borders of the first option (Play button)
        if 315+120>mouse[0]>315 and 407+50>mouse[1]>407:
            pygame.draw.rect(screen, Light_Blue,(315,407, 120, 50)) #make a rectangle for the first option. Dim the colour of the box.
        #if the cursor is not within the borders of the of the first option
        else:
            pygame.draw.rect(screen, Dark_Blue,(315,407, 120, 50)) #make a rectangle for the first option. Darken the colour of the box
        Screen_Text("Play", medium_font, White, screen, 330,400) #display text over the first option
        #if the cursor is within the borders of the second option (Help button)
        if 315+120>mouse[0]>315 and 465+50>mouse[1]>465:
            pygame.draw.rect(screen, Light_Blue, (315,465, 120, 50)) #make a rectangle for the second option. Dim the colour of the box
        #if the cursor is not within the borders of the second option
        else:
            pygame.draw.rect(screen, Dark_Blue,(315,465, 120, 50)) #make a rectange for the second option. Darken the colour of the box
        Screen_Text("Help", medium_font, White, screen, 330,458) #display text over the second option
        #if the cursor is within the borders of the third option option (Quit button)
        if 315+120>mouse[0]>315 and 523+50>mouse[1]>523:
            pygame.draw.rect(screen, Light_Blue, (315,523, 120, 50)) #make a rectangle for the third option. Dim the colour of the box
        #if the cursor is not within the borders of the third option option
        else:
            pygame.draw.rect(screen, Dark_Blue,(315,523, 120, 50)) #make a rectangle for the third option. Darken the colour of the box
        Screen_Text("Quit", medium_font, White, screen, 330,517) #display text over the third option
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos # set and y to the event postion
                #if the user left clicks the fist option, Play
                if (315+120 > x > 315 and 407+50 > y > 407) and (event.button==1):
                    Click.play() #play the click sound effect
                    Difficulty() #call the difficulty fucntion
                #if the user left clicks the second option, Help Menu
                if (315+120 > x > 315 and 465+50 > y > 465) and (event.button==1):
                    Click.play() #play the click sound effect
                    HelpMenu() #call the Help Menu function
                #if the user left clicks the third option, Quit
                if (315+120 > x > 315 and 523+50 > y > 523) and (event.button==1):
                    Click.play() #play click sound effect
                    pygame.time.wait(150) #pause the code for 150 milliseconds to allow the click sound effect to play.
                    pygame.quit() #quit pygame
                    sys.exit() #exit python
        pygame.display.update() #update the dusplay

def HelpMenu():
    '''
    Function does not take an argument
    Returns no value
    Displays a description of the game
    Display to the user the option to go back to the main menu
    '''

    running = True
    while running:
        mouse = pygame.mouse.get_pos() #get the psotion of the cursor
        screen.fill (Black) #colour the screen
        Screen_Text("Welcome to EXIT!", medium_font, Light_Yellow, screen, 200, 200) #display an introduction
        #display a description of the game
        Screen_Text("Your goal is to escape the room before the time ends. You will solve a", small_font, White, screen, 50, 270)
        Screen_Text("series of puzzles to do so. However, be careful! The puzzles progressively", small_font, White, screen, 50, 300)
        Screen_Text("get harder. Enjoy!", small_font, White, screen, 300,330)
        #if the cursor is within the borders of the rectangle
        if 280+230>mouse[0]>280 and 575+40>mouse[1]>575:
            pygame.draw.rect(screen, Light_Blue,(280, 575, 230, 40)) #make a rectangle. Dim the colour of the box
            screen.blit(return_arrow, (245,580)) #display a return arrow
        #if the cursor is not within the borders of the rectangle
        else:
            pygame.draw.rect(screen, Dark_Blue,(280,575, 230, 40)) #make a rectangle. Darken the coour of the box
        Screen_Text("Return to Main Menu", small_font, White, screen, 286, 580) #display text over the rectangle
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits  the while loop
            #if the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the position of the mouse click
                #if the user left clicks on the option to go back to the main menu
                if (280+230 > x > 280 and 575+40 > y > 575) and (event.button==1):
                    Click.play() #Play click sound effect
                    MainMenu() #call main menu function
        pygame.display.update() #update the screen

def Difficulty():
    '''
    Function takes no argument
    Does not return a value
    Displays to the screen the different difficulties the user can pick from (Easy, Medium, Hard)
    Displays the option to go back to the main menu or the game intro
    '''
    running = True
    while running:
        mouse = pygame.mouse.get_pos() #get the position of the cursor
        screen.fill(Black) #colour the screen
        Screen_Text("Please Select the Difficulty Level", medium_font, White, screen, 80,80) #Ask the user to select a difficulty level
        #if cursor is within the range of the first option (EASY mode)
        if 300+200 > mouse[0] > 300 and 200+70 > mouse [1] > 200:
            pygame.draw.rect(screen, (192,192,192), (300,200,200,70)) #display a Light gray box
        #if the cursor is not within the range of the first option
        else:
            pygame.draw.rect(screen, Gray, (300,200,200,70)) #display a dark gray box
        Screen_Text("Easy", medium_font, White, screen, 350,205) #disply text over the first option
        #if cursor is within the range of the second option (MEDIUM mod)
        if 300+200 > mouse[0] > 300 and 300+70 > mouse [1] > 300:
            pygame.draw.rect(screen, (192,192,192), (300, 300, 200,70)) #display  light gray box
        #if the cursor is not within the range of the second option
        else:
            pygame.draw.rect(screen, Gray, (300, 300, 200,70)) #display a dark gray box
        Screen_Text("Medium", medium_font, White, screen, 315,305) #display text over the the second option
        #if the cursor is within the range of the third option (HARD mod)
        if 300+200 > mouse[0] > 300 and 400+70 > mouse [1] > 400:
            pygame.draw.rect(screen, (192,192,192), (300, 400, 200,70)) #display a light gray box
        #if the cursor is not within the range of the third option
        else:
            pygame.draw.rect(screen, Gray, (300, 400, 200,70)) #display a dark gray box
        Screen_Text("Hard", medium_font, White, screen, 345,405) #display text over the third option
        #if the cursor is within the range of the fourth option (Main Menu button)
        if 280+230>mouse[0]>280 and 575+40>mouse[1]>575:
            pygame.draw.rect(screen, Light_Blue,(280, 575, 230, 40)) #make lighter coloured box
            screen.blit(return_arrow, (245,580)) #display a return a arrow
        #if the cursor is not within the range of the fourth option
        else:
            pygame.draw.rect(screen, Dark_Blue,(280,575, 230, 40)) #make a darker coloured box
        Screen_Text("Return to Main Menu", small_font, White, screen, 286, 580) #display text over the fourth option
        dt = 0 #set a delta time variable which returns the time since the last time a while loop has been run. we will use this variable later on to make a timer.
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the postion of the mouse click
                #if the user left clicks the first option, Easy
                if (300+200 > x > 300 and 200+70 > y > 200) and (event.button==1):
                    Click.play() #play click sound effect
                    time = 600 #set the timer to be 600s
                    global start_time #call the global 'start_time' variable.
                    start_time = 600 #Change the global stat_time variable to 600 seconds. we will use this later to calculate the highscore
                    GameIntro(time, dt) #call the GameIntro function and pass time and dt
                #if the user left clicks the second option, medium
                elif (300+200 > x > 300 and 300+70 > y > 300) and (event.button==1):
                    Click.play() #play click sound effect
                    time = 400 #set the timer to be 400 seconds
                    start_time = 400 #Change the global stat_time variable to 400 seconds. we will use this later to calculate the highscore
                    GameIntro(time, dt) #call the GameIntro fucntion and pass time and dt
                #if the user left clicks the third option, Hard
                elif (300+200 > x > 300 and 400+70 > y > 400) and (event.button==1):
                    Click.play() #play the click sound effect
                    time = 150 #set the timer to be 150 seconds
                    start_time = 150 #Change the global stat_time variable to 150 seconds. we will use this later to calculate the highscore
                    GameIntro(time, dt) #call the GameIntro function and pass time and dt varibales
                #if the user left clicks the fourth option (return to main menu)
                elif (280+230 > x > 280 and 575+40 > y > 575) and (event.button==1):
                    Click.play() #play click sound effect
                    MainMenu() #call the main menu function
        pygame.display.update() #update the screen

def GameIntro(time, dt):
    '''
    Function takes 2 arguments, time and dt
    Does not return a value
    Introduces the user to the game
    Passes the 2 variables to the PlayGame fuction
    '''
    running = True
    while running:
        mouse = pygame.mouse.get_pos() #get the postion of the cursor
        screen.fill(Black) #colour the screen
        screen.blit(OxygenTank, (270,150)) #display image
        pygame.draw.rect(screen, Red, (0, 570, 800, 100)) #colour the bottom of the screen with the colour Red
        #introduce the user
        Screen_Text("You are stuck at an office. The main oxygen supply tank is broken and you", small_font, White, screen, 15, 580)
        Screen_Text("are now using your backup tank...", small_font, White, screen, 220, 610)
        #if the cursor is is within the borders of the circle button
        if 768+25>mouse[0]>743 and 639+25>mouse[1]>614:
            pygame.draw.circle(screen, Light_Blue,(768,639),25) #display a light coloured cirlce
        #if the cursor is not within the borders of the circle button
        else:
            pygame.draw.circle(screen, Dark_Blue,(768,639),25) #display a dark coloured circle
        screen.blit(next_arrow,(754,624)) #display the 'next' arrow on the circle
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the postion of mouse click
                #if user right clicks the cirlce
                if (768+25> x >743 and 639+25> y >614) and (event.button==1):
                    Click.play() #play click sound effect
                    running = False #set running to False. this exits this while loop, and enters the next while loop
        pygame.display.update()#update the screen
    while True:
        mouse = pygame.mouse.get_pos() #get the postion of the cursor
        screen.fill(Black) #colour the screen
        screen.blit(timer, (270,150)) #display image
        pygame.draw.rect(screen, Red, (0, 570, 800, 100)) #colour the bottom of the screen with the colour red
        #introduction
        Screen_Text("However, you only have a limited time for your oxygen tank. You have to", small_font, White, screen, 20, 580)
        Screen_Text("leave before your oxygen tank runs out!", small_font, White, screen,200, 610)
        #if the cursor is within thr range of the cirlce button
        if 768+25>mouse[0]>743 and 639+25>mouse[1]>614:
            pygame.draw.circle(screen, Light_Blue,(768,639),25) #display a light coloured circle
        #if the cursor is not within the range of the circle button
        else:
            pygame.draw.circle(screen, Dark_Blue,(768,639),25) #display a dark coloured circle
        Screen_Text("Start", small_font, White, screen, 745,624) #display text over the circle
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the postion of the mouse click
                #if the user right clicks on the circle
                if (768+25 > x > 743 and 639+25 > y > 614) and (event.button==1):
                    Click.play() #play click sound effect
                    inventory = [] #set an empty list to store stuff in. We will use this later on to check if the user solved all the puzzles or not.
                    PlayGame(time, inventory, dt) #call the PlayGame function and pass the 3 variables, time, inventory and dt
        pygame.display.update() #update the screen

def numbers():
    '''
    Function does not take an argument
    Does not return a value
    Displays the number pad
    '''
    #display numbers
    screen.blit(Number0, (285,250))
    screen.blit(Number1, (325,250))
    screen.blit(Number2, (365,250))
    screen.blit(Number3, (405,250))
    screen.blit(Number4, (445,250))
    screen.blit(Number5, (285,300))
    screen.blit(Number6, (325,300))
    screen.blit(Number7, (365,300))
    screen.blit(Number8, (405,300))
    screen.blit(Number9, (445,300))

def PlayGame(time, inventory, dt):
    '''
    Function takes 3 variables, time, inventory, and dt
    Does not return a value
    Displays the game map to the user with a timer
    Checks if the user solved all the puzzles.
    Passes the 3 variables to the next puzzle the user travels to
    '''
    running = True
    while running:
        mouse = pygame.mouse.get_pos() #get the postion of the cursor
        screen.fill (Black) #colour the screen
        clicks = [] #set an empty list to track how many times the user clicks. We will use this later on in the number pad functions
        #DRAW WALLS
        pygame.draw.rect(screen, (32,32,32), (0,0, 800, 355))
        #DRAW BOOKSHELF
        pygame.draw.rect(screen, Light_Brown, (350,100, 250,250))
        pygame.draw.lines(screen, Dark_Brown, True, [(350,100), (600,100),(600, 350), (350,350)], 8)
        pygame.draw.line(screen, Dark_Brown,(350,150), (600,150), 8)
        pygame.draw.line(screen, Dark_Brown,(350,200), (600,200), 8)
        pygame.draw.line(screen, Dark_Brown,(350,250), (600,250), 8)
        pygame.draw.line(screen, Dark_Brown,(350,300), (600,300), 8)
        #DRAW BOOKS
        #blue books
        pygame.draw.rect (screen, Dark_Blue, (400, 105, 13, 42))
        pygame.draw.rect (screen, Dark_Blue, (584, 105, 13, 42))
        pygame.draw.rect (screen, Dark_Blue, (540, 155, 13, 42))
        pygame.draw.rect (screen, Dark_Blue, (410, 305, 13, 42))
        #white books
        pygame.draw.rect (screen, White, (571, 105, 13, 42))
        pygame.draw.rect (screen, White, (370, 155, 13, 42))
        pygame.draw.rect (screen, White, (470, 305, 13, 42))
        #red books
        pygame.draw.rect (screen, Red, (520, 305, 13, 42))
        pygame.draw.rect (screen, Red, (527, 155, 13, 42))
        #yellow books
        pygame.draw.rect (screen, Light_Yellow, (355, 205, 13, 42))
        pygame.draw.rect (screen, Light_Yellow, (383, 155, 13, 42))
        pygame.draw.rect (screen, Light_Yellow, (483, 305, 13, 42))
        #black books
        pygame.draw.rect (screen, Black, (355, 255, 13, 42))
        pygame.draw.rect (screen, Black, (545, 305, 13, 42))
        pygame.draw.rect (screen, Black, (430, 205, 13, 42))
        #DRAW DOOR
        pygame.draw.rect(screen, (255,153,51), (100,100, 120, 255))
        #door knob
        pygame.draw.circle(screen, Black,(200,220),10)
        #DRAW CLOCK
        pygame.draw.circle(screen, White, (700,130),45)
        #clock arms
        pygame.draw.rect(screen, Black, (700,90, 5, 43))
        pygame.draw.rect(screen, Gray, (701, 103, 3, 30))
        #DRAW DESK
        pygame.draw.rect(screen, Dark_Brown, (700, 450, 90, 100))
        #chair
        pygame.draw.rect(screen, Gray, (650, 420, 12, 130))
        pygame.draw.rect(screen, Gray, (650, 495, 50, 12))
        #laptop
        #if the cursor is within the borders of the laptop
        if 760+8>mouse[0]>760 and 400+50>mouse[1]>400 or 720+48>mouse[0]>720 and 442+8>mouse[1]>442:
            #draw light grey laptop
            pygame.draw.rect(screen, Gray, (720, 442, 48, 8))
            pygame.draw.rect(screen, Gray, (760, 400, 8, 50))
        #if the cursor is not within the borders of the laptop
        else:
            #draw dark coloured laptop
            pygame.draw.rect(screen, (224,224,224), (760, 400, 8, 50))
            pygame.draw.rect(screen, (224,224,224), (720, 442, 48, 8))
        #DRAW CHEST
        pygame.draw.rect(screen, Gold, (70, 580, 110, 65))
        pygame.draw.rect(screen, Black,(70,600, 110, 3))
        pygame.draw.rect(screen, Black, (119, 600, 10,10))
        #DRAW CARPET
        pygame.draw.rect(screen, Dark_Brown, (100,400,380,150))
        #Draw TRASH CAN
        pygame.draw.polygon(screen, Gray, [(540,560), (550,620), (600,620), (610, 560)])
        #PICTURE FRAME
        screen.blit(Frame,(253,130))
        #if the cursor is within the borders of the picture frame
        if 253+64 > mouse[0] > 253 and 130+64 > mouse[1] > 130:
            Screen_Text("11", large_font, Light_Brown, screen, 250,425) #display the numbers '11.' this number is the laptop pin
        #if the cursor is within the borders of the button to go back to the main menu
        if 10+123 > mouse[0] > 10 and 10+30 > mouse[1] > 10:
            pygame.draw.rect(screen, Light_Blue, (10, 10, 123, 30)) #draw a light coloured box
        #if the cursor is not within the borders of the button
        else:
            pygame.draw.rect(screen, Dark_Blue, (10, 10, 123, 30)) #draw a dark coloured box
        Screen_Text("Main Menu", small_font, White, screen, 13,10) #display text over the button
        #if the cursor is within the borders of the button to quit
        if 42+52 > mouse[0] > 42 and 50+30 > mouse[1] > 50:
            pygame.draw.rect(screen, Light_Blue, (42, 50, 52, 30)) #draw a light coloured box
        #if the cursor is not within the borders of the button
        else:
            pygame.draw.rect(screen, Dark_Blue, (42, 50, 52, 30)) #draw a dark coloured box
        Screen_Text("Quit", small_font, White, screen, 45, 50) #display text over the button
        Screen_Text("Hint: Check the laptop", pygame.font.SysFont("Times New Roman", 14), White, screen, 650,640) #display a hint to the user
        dt = clock.tick()/1000 #divide our framerate by 1000 to convert to seconds
        time -= dt #subtract dt from our time (in seconds)
        total_mins = round(time//60) # minutes left
        total_sec = round(time-(60*(total_mins))) #seconds left
        Screen_Text("Time Left: "+str(total_mins)+":%02d" % total_sec, small_font, White, screen, 300, 10) #display timer
        pygame.display.flip() #allows only timer portion of the screen to update rather than the whole sccreen
        #if the timer hits 0
        if time <= 0:
            TimesUp() #call the TimesUp function
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the postion of the mouse click
                #if the user left clicks on the laptop
                if (760+8 > x > 760 and 400+50 > y > 400 or 720+48>x>720 and 442+8 > y > 442) and (event.button==1):
                    Click.play() #play click sound effect
                    Laptop(time, clicks, inventory, dt) #call laptop function. pass the time, clicks, inventory, and dt variables
                #if the user left clicks on the bluebooks
                elif (584+13>x>584 and 105+42>y>105) and (event.button==1):
                    #check if the user solved the Laptop puzzle before moving onto the BlueBooks
                    if not("Laptop" in inventory):
                        pass
                    #else the user solved the laptop puzzle
                    else:
                        Click.play() #play click sound effect
                        BlueBook(time, inventory, dt) #call the bluebook function. pass time, inventory and dt variables
                #if the user left clicks on the red book
                elif (520+13 > x > 520 and 305+42 > y > 305) and (event.button==1):
                    #check if the user solved the BlueBook puzzle before moving onto the RedeBook
                    if not("BlueBook" in inventory):
                        pass
                    #else the user solved the BlueBook puzzle
                    else:
                        Click.play() #play click sound effect
                        RedBook(time, clicks, inventory, dt) #call the red book function and pass the four vaiables
                #if the user left clicks on the black book
                elif (355+13 > x > 355 and 255+42 > y > 255) and (event.button==1):
                    #check if the user solved the RedBook puzzle before moving onto the BlackBook
                    if not ("RedBook" in inventory):
                        pass
                    #else the user solved the RedBook puzzle
                    else:
                        Click.play() #play click sound effect
                        BlackBook(time, clicks, inventory, dt) #call the black book function and pass the time, clicks, inventory and dt variables
                #if the user left clicks on the the chest
                elif (119+10 > x > 119 and 600+10 > y > 600) and (event.button==1):
                    #check if the user solved the BlackBook puzzle before moving onto the Chest
                    if not ("BlackBook" in inventory):
                        pass
                    #else the user solved the BlackBook puzzle
                    else:
                        Click.play() #play click sound effect
                        Chest(time, clicks, inventory, dt) #call the chest function and pass the time, clicks, inventory, and dt variables
                #if the user left clicks on the door handle
                elif (190 < x < 210 and 210 < y < 230) and (event.button==1):
                    #check if every puzzle is stored in the inside the inventory. This checks if the user actually solved all the puzzles
                    #if the user solved all the puzzles
                    if "key" in inventory and 'Laptop' in inventory and 'BlueBook' in inventory and 'RedBook' in inventory and 'BlackBook' in inventory:
                        Click.play()#play click sound effect
                        global start_time #call the global 'start_time'. REMEMBER: this variable contains the intial start time.
                        start_time-=time #subtract the time left from the inttial time in order to calculate the score
                        score.append(round(start_time)) #add the users score to the list 'score'
                        Door()#call the door function
                    #if the user did not solve all the puzzles
                    else:
                        Click.play() #play click sound effect
                        status = 'Door' #set 'Door' to varible status. We will use this later in the Incorrect Input Fucntion
                        IncorrectInput(time, inventory, status, dt) #call the incorrectInput function and pass the time, inventory, status, and dt variables
                #if user left clicks on the Main Menu button
                elif (10+123 > x > 10 and 10+30 > y > 10) and (event.button==1):
                    Click.play() #play click sound effect
                    MainMenu() #call the main menu fucntion
                #if user left clicks on the quit button
                elif (42+52 > x > 42 and 50+30 > y > 50) and (event.button==1):
                    Click.play() #play click sound effect
                    pygame.time.wait(150) #pause the code for 150 milliseconds to allow the click sound effect to play.
                    pygame.quit() #quit pygame
                    sys.exit() #exit python
        pygame.display.update() #update the screen

def IncorrectInput(time, inventory, status, dt):
    '''
    Function takes four arguments (time, inventory, status, and dt)
    Does not return a value
    Checks using variable 'status' if the user is trying escape without having to solve all the puzzles
    Checks using variable 'status' if the user did not input the correct code in a puzzle
    Passes the time, inventory, and dt variable back to PlayGame function
    '''
    running = True
    #if the user is trying to escape without having to solve all the puzzles
    if status == 'Door':
        time-=10 #deduct 10 seconds from the their time
    while running:
        mouse = pygame.mouse.get_pos() #get the position of the cursor
        screen.fill (Black)#colour the screen
        #if the status variable is 'Door,' this means that the user is trying to escape without solving all the puzzles
        if status == 'Door':
            Screen_Text("You still have some puzzles to solve!", medium_font, Red, screen, 35, 100) #inform the user that they have not solved all the puzzles yet
            Screen_Text("You lost 10 seconds of your time", small_font, Red, screen, 230, 170) #inform the user that lost 10 seconds of their time

        #if the status variable is 'Incorrectinput,' this means that the user did not enter the correct pin for a puzzle
        elif status == 'IncorrectInput':
            Screen_Text("Incorrect!", large_font, Red, screen, 210,100) #inform the user
        screen.blit (Incorrect, (255,250)) #display incorrect image
        #if the cursor is within the borders of the button to go back to the map
        if 280+230>mouse[0]>280 and 575+40>mouse[1]>575:
            pygame.draw.rect(screen, Light_Blue,(280, 575, 230, 40)) #draw a light coloured box
            screen.blit(return_arrow, (245,580)) #display a return arrow
        #if the cursor is not within the borders of the button to go back to the map
        else:
            pygame.draw.rect(screen, Dark_Blue,(280,575, 230, 40)) #draw a dark coloured box
        Screen_Text("Return to the Office", small_font, White, screen, 295,580) #display text over the box
        dt = clock.tick()/1000 #divide our framerate by 1000 to convert to seconds
        time -= dt #subtract dt from our time (in seconds)
        total_mins = round(time//60) # minutes left
        total_sec = round(time-(60*(total_mins))) #seconds left
        Screen_Text("Time Left: "+str(total_mins)+":%02d" % total_sec, small_font, White, screen, 300, 10) #display timer
        pygame.display.flip() #allows only timer portion of the screen to update rather than the whole sccreen
        #if the timer hits 0
        if time <= 0:
            TimesUp() #call the TimesUp function
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the postion of the mouse click
                #if the user left clicks the button to go back to the game map
                if (280+230>x>280 and 575+40>y>575) and (event.button==1):
                    Click.play() #play click sound effect
                    PlayGame(time, inventory, dt) #call PlayGame function and pass the time, inventory, and dt variables

def BlueBook(time, inventory, dt):
    '''
    Function takes 3 arguments (time, inventory, and dt)
    does not return a value
    Displays the Blue book puzzle to the user
    Checks if the user solved the puzzle
    Passes the 3 varbiable back to the PlayGame function
    '''
    running = True
    while running:
        mouse = pygame.mouse.get_pos() #get the postion of the cursor on the screen
        screen.fill (Black) #colour the scren
        #if the cursor is within the borders of the button to go back to game map
        if 280+230>mouse[0]>280 and 575+40>mouse[1]>575:
            pygame.draw.rect(screen, Light_Blue,(280, 575, 230, 40)) #draw a light coloured box
            screen.blit(return_arrow, (245,580)) #display a a return arrow
        #if the cursor is not within the borders of the button
        else:
            pygame.draw.rect(screen, Dark_Blue,(280,575, 230, 40)) #draw a dark coloured box
        Screen_Text("Return to the Office", small_font, White, screen, 295,580) #display text over the button
        #explain the puzzle
        Screen_Text ("One of these images contains your next hint. Hover your", small_font, White, screen, 100,100)
        Screen_Text ("cursor over them to find it!", small_font, White, screen, 250,130)
        #display images on the screen
        screen.blit(Star, (100,550))
        screen.blit(TextIcon, (50,400))
        screen.blit (Google, (300, 400))
        screen.blit (Search, (400,300))
        screen.blit (Flashlight, (610,400))
        screen.blit (Vegetable, (650, 520))
        screen.blit (Camera, (100, 200))
        screen.blit (Brake, (600, 200))
        screen.blit (CheckList, (300, 200))
        #if the cursor is within the borders of the flashlight icon
        if 610+64>mouse[0]>610 and 400+64>mouse[1]>400:
            inventory.append('BlueBook') #add 'BlueBook' to the inventory. this confirms that the user did solve this puzzle
            Screen_Text("Check the Red Books", small_font, (51,255,51), screen, 285,530) #display the hint
        #if the cursor is within the borders of the other images (not including the flashlight image)
        elif 100+64>mouse[0]>100 and 550+64>mouse[1]>550 or 50+64>mouse[0]>50 and 400+64>mouse[1]>400 or 300+64>mouse[0]>300 and 400+64>mouse[1]>400 or 400+64>mouse[0]>400 and 300+64>mouse[1]>300 or 650+64>mouse[0]>650 and 520+64>mouse[1]>520 or 100+64>mouse[0]>100 and 200+64>mouse[1]>200 or 600+64>mouse[0]>600 and 200+64>mouse[1]>200 or 300+64>mouse[0]>300 and 200+64>mouse[1]>200:
            Screen_Text("Not this image!", small_font, Red, screen, 315, 530) #display text.

        dt = clock.tick()/1000 #divide our framerate by 1000 to convert to seconds
        time -= dt #subtract dt from our time (in seconds)
        total_mins = round(time//60) # minutes left
        total_sec = round(time-(60*(total_mins))) #seconds left
        Screen_Text("Time Left: "+str(total_mins)+":%02d" % total_sec, small_font, White, screen, 300, 10) #display timer
        pygame.display.flip() #allows only timer portion of the screen to update rather than the whole sccreen
        #if the timer hits 0
        if time <= 0:
            TimesUp() #call the TimesUp function
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the postion of the mouse click
                #if the user left clicks the button to go back to the game map
                if (280+230>x>280 and 575+40>y>575) and (event.button==1):
                    Click.play() #play click sound effect
                    PlayGame(time, inventory, dt) #call the PlayGame function and pass the time, inventory, and dt variables

def RedBook(time, clicks, inventory, dt):
    '''
    Function takes 4 arguments (time, clicks, inventory, and dt)
    Does not return a value
    Displays a code entry puzzle
    checks if the user inputted the correct code
    Passes the variables to the next function
    '''
    running = True
    while running:
        mouse = pygame.mouse.get_pos() #get the postion of the cursor on the screen
        screen.fill(Black) #colour the screen
        #explain the puzzle
        Screen_Text("Enter the 3 Pin Code", medium_font, White, screen, 175,90)
        Screen_Text("Hint: Clock?", pygame.font.SysFont("Times New Roman", 14), White, screen, 345,150) #display hint
        pygame.draw.rect(screen, White, (245,180, 275,60)) #draw a rectangle to imitate an input screen
        numbers() #call the numbers function. this displays the number pad
        #if the cursor is within the borders of the button to go back to game map
        if 280+230>mouse[0]>280 and 575+40>mouse[1]>575:
            pygame.draw.rect(screen, Light_Blue,(280, 575, 230, 40)) #draw a light coloured box
            screen.blit(return_arrow, (245,580)) #display a return arrow
        #if the cursor is not wtihin the borders of the button
        else:
            pygame.draw.rect(screen, Dark_Blue,(280,575, 230, 40)) #draw a dark coloured bx
        Screen_Text("Return to the Office", small_font, White, screen, 295,580) #display text over the button

        dt = clock.tick()/1000 #divide our framerate by 1000 to convert to seconds
        time -= dt #subtract dt from our time (in seconds)
        total_mins = round(time//60) # minutes left
        total_sec = round(time-(60*(total_mins))) #seconds left
        Screen_Text("Time Left: "+str(total_mins)+":%02d" % total_sec, small_font, White, screen, 300, 10) #display timer
        pygame.display.flip() #allows only timer portion of the screen to update rather than the whole sccreen
        #if the timer hits 0
        if time <= 0:
            TimesUp() #call the TimesUp function
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the postion of the mouse click
                #if the mouse click is within the range of the number pad size. NOTE: this puzzle will require 3 entries (three numbers to solve)
                if 285 < x < 445+32 and 250 < y < 300+32:
                    #if the user left clicks on the number 3
                    if (405+32 > x > 405 and 250+32 > y > 250) and (event.button==1):
                        Click.play() #play click sound effect
                        clicks.append(3) #add the number 3 to the 'clicks' list
                        #if the lenngth of the list is equal to 3, this means that the code entered in incorrect
                        if len(clicks)>=3:
                            status = "IncorrectInput" #set the status to 'IncorrectInput'
                            IncorrectInput(time, inventory, status, dt) #call the IncorectInput function and pass the 3 varialbes + the status varialbes
                    #if the use left clicks on the number 6
                    elif (325+32 > x > 325 and 300+32 > y > 300) and (event.button==1):
                        Click.play() #play click sound effect
                        clicks.append(6) #add the number 6 to the list
                        #if the length of the list is equal to 3, this means that the code entered in incorrect
                        if len(clicks)>=3:
                            status = "IncorrectInput"  #set the status to 'IncorrectInput'
                            IncorrectInput(time, inventory, status, dt) #call the IncorectInput function and pass the 3 varialbes + the status varialbes
                    #if the user left clicks on the number 0
                    elif (285+32 > x > 285 and 250+32 > y > 250) and (event.button==1):
                        Click.play() #play click sound effect
                        clicks.append(0) #add the number 6 to 'clicks' list
                        #check if the number 3 has index 0 in the list, if 6 has index 1 in the list, and 0 has index 2 in the list. This means that the code inputted is correct
                        if ((3 in clicks)==True and clicks.index(3)==0) and ((6 in clicks)==True and clicks.index(6)==1) and ((0 in clicks)==True and clicks.index(0)==2):
                            puzzle = "RedBook" #set the puzzle to "RedBook". we will use this later in the CorrectInput function
                            inventory.append("RedBook") #add 'RedBook' to the inventory. this confirms that the user has solved this puzzle
                            CorrectInput(time, puzzle, inventory, dt) #call the IncorectInput function and pass the 3 varialbes + the status variable
                        #if the length of the list is equal to 3, this means that the code entered in incorrect
                        if len(clicks)>=3:
                            status = "IncorrectInput" #set the status to 'IncorrectInput'
                            IncorrectInput(time, inventory, status, dt) #call the IncorectInput function and pass the 3 varialbes + the status varialbes
                    #if the user clicks on every other number (not including 3, 6 or 0)
                    elif not (405+32 > x > 405 and 250+32 > y > 250)  or (325+32 > x > 325 and 300+32 > y > 300)  or (285+32 > x > 285 and 250+32 > y > 250):
                        #if user right clicks
                        if event.button==1:
                            Click.play() #play click sound effect
                            clicks.append("Incorret") #add 'incorrect' to the 'clicks' list
                        #if the length of the list is equal to 3, this means that the code entered in incorrect
                        if len(clicks)>=3:
                            status = "IncorrectInput" #set the status to 'IncorrectInput'
                            IncorrectInput(time, inventory, status, dt) #call the IncorectInput function and pass the 3 varialbes + the status varialbes
                #if the user left clicks on the button to go back to the game map
                if (280+230>x>280 and 575+40>y>575) and (event.button==1):
                    Click.play() #play click sound effect
                    PlayGame(time, inventory, dt) #call the PlayGame function and pass the 3 variables
        pygame.display.update() #update the screen


def Laptop(time, clicks, inventory, dt):
    '''
    Function takes 4 arguments (time, clicks, inventory, and dt)
    Does not return a value
    Displays a code entry puzzle
    checks if the user inputted the correct code
    Passes the variables to the next function
    '''
    running = True
    while running:
        mouse = pygame.mouse.get_pos() #get the postion of the cursor on the screen
        screen.fill(Black) #colour screen
        #explain the puzzle
        Screen_Text("Enter The 2 Pin Laptop Password", medium_font, White, screen, 60,100)
        pygame.draw.rect(screen, White, (245,180, 275,60)) #draw a white rectangle to imitate an input screen
        numbers() #call the numbes function. This will display the number pad
        #if the cursor is within the borders of the button to return to the game map
        if 280+230>mouse[0]>280 and 575+40>mouse[1]>575:
            pygame.draw.rect(screen, Light_Blue,(280, 575, 230, 40)) #draw a light coloured box
            screen.blit(return_arrow, (245,580)) #display a return arrow
        #if the cursor is not within the borders of the button
        else:
            pygame.draw.rect(screen, Dark_Blue,(280,575, 230, 40)) #draw a dark coloured box
        Screen_Text("Return to the Office", small_font, White, screen, 295,580) #display text over the button

        dt = clock.tick()/1000 #divide our framerate by 1000 to convert to seconds
        time -= dt #subtract dt from our time (in seconds)
        total_mins = round(time//60) # minutes left
        total_sec = round(time-(60*(total_mins))) #seconds left
        Screen_Text("Time Left: "+str(total_mins)+":%02d" % total_sec, small_font, White, screen, 300, 10) #display timer
        pygame.display.flip() #allows only timer portion of the screen to update rather than the whole sccreen
        #if the timer hits 0
        if time <= 0:
            TimesUp() #call the TimesUp function
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked. NOTE: This puzzle requires two entries (2 numbers)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the position of the mouse click
                #if the user clicks within the borders of the number pad
                if 285 < x < 445+32 and 250 < y < 300+32:
                    #if the user right clicks on numb on 1
                    if (325+32> x > 325 and 250+32 > y > 250) and (event.button==1):
                        Click.play() #play click sound effect
                        clicks.append (1) #add the number 1 to to list 'clicks'
                        #if the length of the list is 2 and number 1 IS in the list
                        if ((1 in clicks)==True) and len(clicks)==2:
                            #if the number 1 is at index 0 and 1. NOTE: This means that the user solved the puzzle
                            if (clicks[0]==1) and (clicks[1]==1):
                                puzzle = "Laptop" #set puzzle to 'Laptop'. We we will use this later in the CorrectInput function
                                inventory.append('Laptop') #add 'Laptop' to the inventory. This confirms that the user did solve the puzzle
                                CorrectInput(time, puzzle, inventory, dt) #call the the CorrectInput function and pass the time, puzzle, inventory, and dt variables
                            #if the number 1 IS NOT at index 0 and 1 in the list. this means that the user did not input the correct code
                            else:
                                status = "IncorrectInput" #set the status to 'IncorrectInput'. we will use this later in the IncorrectInput function
                                IncorrectInput(time, inventory, status, dt) #call the IncorrectInput function and pass the time, inventory, status, and dt variables
                    #if the user clicks on the numbers (not including the number 1)
                    else:
                        #if the user right clicks
                        if event.button==1:
                            Click.play() #play click sound effect
                            clicks.append("Incorret") #add 'Incorrect' to the 'clicks' list
                        #if the length of the list is 2. This means that the use did not input the correct code
                        if len(clicks)>=2:
                            status = "IncorrectInput" #se tht status to 'IncorrectInput'. we will use this in the IncorrectInput function
                            IncorrectInput(time, inventory, status, dt) #call the the IncorrectInput function and pass the time, inventory, status, and dt variables
                #if the user right clicks on the button to go back to game map
                if (280+230 > x > 280 and 575+40 > y > 575) and (event.button==1):
                    Click.play() #play click sound effect
                    PlayGame(time, inventory, dt) #call PlayGame function and pass the time, inventory and dt variables.
        pygame.display.update() #update the screen

def CorrectInput(time, puzzle, inventory, dt):
    '''
    Function takes four arguments (time, puzzle, inventory, and dt)
    Does not return a value
    Checks using variable 'puzzle' which puzzle the user solved, and outputs the appropriate hint
    Passes the time, inventory, and dt variable back to PlayGame function
    '''
    running = True
    while running:
        mouse = pygame.mouse.get_pos() #get the position of the cursor on the screen
        screen.fill(Black) #colour the screen
        #Display text informing the user that they solved the puzzle
        Screen_Text("Correct!", large_font, (51,255,51), screen, 240,100)
        screen.blit (Correct, (320,230)) #display correct image
        #if user solved the Laptop puzzle
        if puzzle == "Laptop":
            #display the Laptop hint
            Screen_Text("Your next hint is inside one of the Blue Books!", small_font, White, screen, 160,450)
        #if user solved the RedBook puzzle
        elif puzzle == "RedBook":
            #display the RedBook hint
            Screen_Text("Your next hint is inside one of the Black Books!", small_font, White, screen, 160,450)
        #if the user solved the BlackBook puzzle
        elif puzzle == "BlackBook":
            #display the BlackBook puzzle
            Screen_Text("The secret pin is 749183", small_font, White, screen, 280,450)
        #if the user solved the Chest puzzle
        elif puzzle == "chest":
            inventory.append("key") #add 'Key' to the list. This is the last puzzle. We add 'key' to the list in order to confirm that the user solved the puzzle
            #display text
            Screen_Text("You found the Key to the door. Use it to escape!", small_font, White, screen, 120,450)
            screen.blit(Door_Key, (600,450)) #display key image
        #if the cursor is within the borders of the button to go back to the game map
        if 280+230>mouse[0]>280 and 575+40>mouse[1]>575:
            pygame.draw.rect(screen, Light_Blue,(280, 575, 230, 40)) #draw a light coloured box
            screen.blit(return_arrow, (245,580)) #display a return arrow image
        #if the cursor is not within the borders of the button
        else:
            pygame.draw.rect(screen, Dark_Blue,(280,575, 230, 40)) #draw a dark coloured box
        Screen_Text("Return to the Office", small_font, White, screen, 295,580) #display text over the button

        dt = clock.tick()/1000 #divide our framerate by 1000 to convert to seconds
        time -= dt #subtract dt from our time (in seconds)
        total_mins = round(time//60) # minutes left
        total_sec = round(time-(60*(total_mins))) #seconds left
        Screen_Text("Time Left: "+str(total_mins)+":%02d" % total_sec, small_font, White, screen, 300, 10) #display timer
        pygame.display.flip() #allows only the timer portion of the screen to update rather than the whole sccreen
        #if the timer hits 0
        if time <= 0:
            TimesUp() #call the TimesUp function
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the postion of the mouse click
                #if the user right clicks on the button to go back
                if (280+230>x>280 and 575+40>y>575) and (event.button==1):
                    Click.play() #play click sound effect
                    PlayGame(time, inventory, dt) #call the PlayGame function and pass the time, inventory, and dt variables

def BlackBook(time, clicks, inventory, dt):
    '''
    Function takes 4 arguments (time, clicks, inventory, and dt)
    Does not return a value
    Displays a code entry puzzle
    checks if the user inputted the correct code
    Passes the variables to the next function
    '''
    running = True
    while running:
        mouse = pygame.mouse.get_pos() #get the postion of the cursor on the screen
        screen.fill(Black) #colour the screen
        #explain the puzzle
        Screen_Text("Enter the 5 Pin Code", medium_font, White, screen, 175,90)
        pygame.draw.rect(screen, White, (245,180, 275,60)) #draw a white box to imitate an input screen
        numbers() #call the numbers function. This will display our number pad
        #if the cursor is within the borders of the button to go back to the game map
        if 280+230>mouse[0]>280 and 575+40>mouse[1]>575:
            pygame.draw.rect(screen, Light_Blue,(280, 575, 230, 40)) #draw a light coloured box
            screen.blit(return_arrow, (245,580)) #display a return arrow image
        #if the cursor is not within the borders of the button to go back
        else:
            pygame.draw.rect(screen, Dark_Blue,(280,575, 230, 40)) #draw a dark coloured box
        Screen_Text("Return to the Office", small_font, White, screen, 295,580) #display text over the buttton

        dt = clock.tick()/1000 #divide our framerate by 1000 to convert to seconds
        time -= dt #subtract dt from our time (in seconds)
        total_mins = round(time//60) # minutes left
        total_sec = round(time-(60*(total_mins))) #seconds left
        Screen_Text("Time Left: "+str(total_mins)+":%02d" % total_sec, small_font, White, screen, 300, 10) #display timer
        pygame.display.flip() #allows only timer portion of the screen to update rather than the whole sccreen
        #if the timer hits 0
        if time <= 0:
            TimesUp() #call the TimesUp function
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
            #if the mouse button is clicked. NOTE: this puzzle rquires 5 entries (5 pin Code)
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to position of the mouse click
                #if the user clicks within the borders of the number pad
                if 285 < x < 445+32 and 250 < y < 300+32:
                    #if the user left clicks on the number 3
                    if (405+32 > x > 405 and 250+32 > y > 250) and (event.button==1):
                        Click.play() #play click sound effect
                        clicks.append(3) #add the number 3 to the list
                        #if the len of the 'clicks' list is 5, the user did not input the correct pin
                        if len(clicks)>=5:
                            status = "IncorrectInput" #set status to 'IncorrectInput'. we will use this in the IncorrectInput fucntion
                            IncorrectInput(time, inventory, status, dt) #call the IncorrectInput function and pass the time, inventory, status, and dt varaibles
                    #if the user left clicks on the number 4
                    elif (445+32 > x > 445 and  250+32 > y > 250) and (event.button==1):
                        Click.play() #play click sound effect
                        clicks.append(4) #add the number 4 to the 'clicks' list
                        #if the lenth of the 'clicks' list is 5, this means that the user did not input the correct pin
                        if len(clicks)>=5:
                            status = "IncorrectInput" #set 'IncorrectInput' to status. we will use this in the IncorrectInput function
                            IncorrectInput(time, inventory, status, dt) #call the IncorrectInput function and pass the time, inventory, status, and dt varaibles
                    #if the user left clcicks on the number 2
                    elif (365+32 > x > 365 and 250+32 > y > 250) and (event.button==1):
                        Click.play() #play the click sound effect
                        clicks.append(2) #add the number 2 to 'clicks' list
                        #if the length of 'clicks' list is 5, then the user diod not input the correct pin
                        if len(clicks)>=5:
                            status = "IncorrectInput" #set 'IncorrectInput' to the status. we will use this in the IncorrectInput function
                            IncorrectInput(time, inventory, status, dt) #call the IncorrectInput function and pass the time, inventory, status, and dt variables
                    #if the user left clicks on thr number 1
                    elif (325+32 > x > 325 and 250+32 > y > 250) and (event.button==1):
                        Click.play() #play click sound effect
                        clicks.append(1) #add the number 1 to the 'clicks' list
                        #if the length of the list is 5, then then the user did not input the correct input
                        if len(clicks)>=5:
                            status = "IncorrectInput" #set status to 'IncorrectInput'. we will use this later in the IncorrectInput function
                            IncorrectInput(time, inventory, status, dt) #call the incorrectInput function and pass the time, inventory, status and dt variables
                    #if the user left clicks on the number 5
                    elif (285+32 > x > 285 and 300+32 > y > 300) and (event.button==1):
                        Click.play() #play the click sound effect
                        clicks.append(5) #add the number 5 to the 'clicks' list
                        #check if the number 3 has index 0 in the list, if 4 has index 1, if 2 has index 2, if 1 has index 3, and if 5 has index 4. this means that the user inputted the correct pin
                        if ((3 in clicks)==True and clicks.index(3)==0) and ((4 in clicks)==True and clicks.index(4)==1) and ((2 in clicks)==True and clicks.index(2)==2) and ((1 in clicks)==True and clicks.index(1)==3) and ((5 in clicks)==True and clicks.index(5)==4):
                            puzzle = "BlackBook" #set the puzzle to 'BlackBook'. we will use in the CorrectInput function
                            inventory.append("BlackBook") #add 'BlackBook' to the inventory. this confirms that the user successfully solved the puzzle
                            CorrectInput(time, puzzle, inventory, dt) #call the CorrectInput function and pass the time, puzzle, inventory, and dt variables
                        #if the length of the list is 5, then the user did not input the correct Pin
                        if len(clicks)>=5:
                            status = "IncorrectInput" #set status to 'IncorrectInput'. we will use this in the IncorrectInput function
                            IncorrectInput(time, inventory, status, dt) #Call the IncorrectInput function and pass the time, inventory, status, and dt variables
                    #if the user on other numbers (not including 3, 4, 2, 1, and 5)
                    elif not (405+32 > x > 405 and 250+32 > y > 250) or (365+32 > x > 365 and 250+32 > y > 250) or (445+32 > x > 445 and 250+32 > y > 250):
                        #if the user right clicks
                        if event.button==1:
                            Click.play() #Play click sound effect
                            clicks.append("Incorret") #add 'Incorrect' to the list
                        #if the length of the list is 5
                        if len(clicks)>=5:
                            status = "IncorrectInput" #set status to 'IncorrectInput'. we will use this later in the IncorrectInput function
                            IncorrectInput(time, inventory, status, dt) #call the IncorrectInput function and pass the time, inventory, status, and dt variables
                #if the user left clicks on the button to go back to the game map
                if (280+230>x>280 and 575+40>y>575) and (event.button==1):
                    Click.play() #play click sound effect
                    PlayGame(time, inventory, dt) #call the PlayGame function and pass the time, inventory, and dt variables
        pygame.display.update() #update the screen

def Chest (time, clicks, inventory, dt):
    '''
    Function takes 4 arguments (time, clicks, inventory, and dt)
    Does not return a value
    Displays a code entry puzzle
    checks if the user inputted the correct code
    Passes the variables to the next function
    '''
    running = True
    while running:
            mouse = pygame.mouse.get_pos() #get the postion of the cursor on the screen
            screen.fill(Black) #colour the screen
            #explain the puzzle
            Screen_Text("Enter the 6 Pin Code", medium_font, White, screen, 175,90)
            pygame.draw.rect(screen, White, (245,180, 275,60)) #draw a white rectangle to imitate an input screen
            numbers() #call the numbers function. this will display the number pad.
            #if the cursor is within the borders of the button to go back to the game map
            if 280+230>mouse[0]>280 and 575+40>mouse[1]>575:
                pygame.draw.rect(screen, Light_Blue,(280, 575, 230, 40)) #draw a light coloured box
                screen.blit(return_arrow, (245,580)) #display a return arrow image
            #if the cursor is not within the borders to go back
            else:
                pygame.draw.rect(screen, Dark_Blue,(280,575, 230, 40)) #draw a dark coloured box
            Screen_Text("Return to the Office", small_font, White, screen, 295,580) #display text over the buttton

            dt = clock.tick()/1000 #divide our framerate by 1000 to convert to seconds
            time -= dt #subtract dt from our time (in seconds)
            total_mins = round(time//60) # minutes left
            total_sec = round(time-(60*(total_mins))) #seconds left
            Screen_Text("Time Left: "+str(total_mins)+":%02d" % total_sec, small_font, White, screen, 300, 10) #display timer
            pygame.display.flip() #allows only timer portion of the screen to update rather than the whole sccreen
            #if the timer hits 0
            if time <= 0:
                TimesUp() #call the TimesUp function
            #Set a for loop to get events from the game
            for event in pygame.event.get():
                #if the user presses the 'X' button on the top right
                if event.type == pygame.QUIT:
                    pygame.quit() #quit pygame
                    sys.exit() #exit python
                    running == False #set running to False. this exits the while loop
                #if the mouse button is clicked. NOTE: this puzzle rquires 6 entries (6 pin Code)
                if event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos #set x and y to position of the mouse click
                    if 285 < x < 445+32 and 250 < y < 300+32:
                        #if the user left clicks on the number 7
                        if (365+32 > x > 365 and 300+32 > y > 300) and (event.button==1):
                            Click.play() #play the click sound effect
                            clicks.append(7) #add the number 7 to the list
                            #if the length of the list is 6, then then the user did not input the correct input
                            if len(clicks)>=6:
                                status = "IncorrectInput" #set status to 'IncorrectInput'. we will use this later in the IncorrectInput function
                                IncorrectInput(time, inventory, status, dt) #call the incorrectInput function and pass the time, inventory, status and dt variables
                        #if the user left clicks on the number 4
                        elif (445+32 > x > 445 and  250+32 > y > 250) and (event.button==1):
                            Click.play() #play the click sound effect
                            clicks.append(4) #add the number 4 to list
                            #if the length of the list is 6, then then the user did not input the correct input
                            if len(clicks)>=6:
                                status = "IncorrectInput" #set status to 'IncorrectInput'. we will use this later in the IncorrectInput function
                                IncorrectInput(time, inventory, status, dt) #call the incorrectInput function and pass the time, inventory, status and dt variables
                        #if the user left clicks on the number 9
                        elif (445+32 > x > 445 and 300+32 > y > 300) and (event.button==1):
                            Click.play() #play click sound effect
                            clicks.append(9) #add the number 9 to the list
                            #if the length of the list is 6, then then the user did not input the correct input
                            if len(clicks)>=6:
                                status = "IncorrectInput" #set status to 'IncorrectInput'. we will use this later in the IncorrectInput function
                                IncorrectInput(time, inventory, status, dt) #call the incorrectInput function and pass the time, inventory, status and dt variables
                        #if the user left clicks on the number 1
                        elif (325+32 > x > 325 and 250+32 > y > 250) and (event.button==1):
                            Click.play() #play click sound effect
                            clicks.append(1) #add the number 1 to the list
                            #if the length of the list is 6, then then the user did not input the correct input
                            if len(clicks)>=6:
                                status = "IncorrectInput" #set status to 'IncorrectInput'. we will use this later in the IncorrectInput function
                                IncorrectInput(time, inventory, status, dt) #call the incorrectInput function and pass the time, inventory, status and dt variables
                        #if the user left clicks on the number 8
                        elif (405+32 > x > 405 and 300+32 > y > 300) and (event.button==1):
                            Click.play() #play click sound effect
                            clicks.append(8) #add the number 8 to the list
                            #if the length of the list is 6, then then the user did not input the correct input
                            if len(clicks)>=6:
                                status = "IncorrectInput" #set status to 'IncorrectInput'. we will use this later in the IncorrectInput function
                                IncorrectInput(time, inventory, status, dt) #call the incorrectInput function and pass the time, inventory, status and dt variables
                        #if the user left clicks on the number 3
                        elif (405+32 > x > 405 and 250+32 > y > 250) and (event.button==1):
                            Click.play() #play click sound effect
                            clicks.append(3) #add the number 3 to the list
                            #if the 7 has index 0 in the list, 4 has index 1, 9 has index 2, 1 has index 3, 8 has index 4, and 3 has index 5. This means that the user inputted the correct pin
                            if ((7 in clicks)==True and clicks.index(7)==0) and ((4 in clicks)==True and clicks.index(4)==1) and ((9 in clicks)==True and clicks.index(9)==2) and ((1 in clicks)==True and clicks.index(1)==3) and ((8 in clicks)==True and clicks.index(8)==4) and ((3 in clicks)==True and clicks.index(3)==5):
                                puzzle = "chest" #set puzzle to chest. We will use this in the CorrectInput function
                                CorrectInput(time, puzzle, inventory, dt) #call the correct input function and pass the time, puzzle, inventory, and dt variables
                            #if the length of the list is 6, this means that the user did not input the correct pin
                            if len(clicks)>=6:
                                status = "IncorrectInput" #set status to IncorrectInput. we will use this in the IncorrectInput function
                                IncorrectInput(time, inventory, status, dt) #call the IncorrectInput function and pass the time, inventory, status and dt varaibles
                        #if the user inputs other numbers(not including 7, 4, 9, 1, 8, and 3)
                        elif not (405+32 > x > 405 and 250+32 > y > 250) or (365+32 > x > 365 and 250+32 > y > 250) or (445+32 > x > 445 and 250+32 > y > 250):
                            #if left clicked
                            if event.button==1:
                                Click.play() #play click sound effect
                                clicks.append("Incorret") #add 'Incorrect' to the list
                            #if the length of the list is 6
                            if len(clicks)>=6:
                                status = "IncorrectInput" #set the status to 'IncorrectInput'. we will use this later in the IncorrectInput function
                                IncorrectInput(time, inventory, status, dt) #call the IncorrectInput function and pass the time, inventory, status, and dt variables
                    #if the user left clicks button to go back to the game loop
                    if (280+230>x>280 and 575+40>y>575) and (event.button==1):
                        Click.play() #play click sound effect
                        PlayGame(time, inventory, dt) #call PlayGame function
            pygame.display.update() #update screen

def Door():
    '''
    Function takes no argument
    Returns no value
    Informs to the user that they escaped
    '''
    running = True
    while True:
        mouse = pygame.mouse.get_pos() #get the postion of the cursor on the screen
        screen.fill(Black) #colour the screen
        #display message
        Screen_Text("Congratulations! You Escaped.", medium_font, (51,255,51), screen, 90,100)
        screen.blit (Open_Door, (270,230)) #display image
        #if the cursor is within the borders of the button to go back to main menu
        if 265+275>mouse[0]>265 and 575+40>mouse[1]>575:
            pygame.draw.rect(screen, Light_Blue,(265, 575, 275, 40)) #draw light coloured box
            screen.blit(return_arrow, (230,580)) #display return arrow
        #if the cursor is not within the borders of the button to go back to main menu
        else:
            pygame.draw.rect(screen, Dark_Blue,(265,575, 275, 40)) #Draw dark coloured box
        Screen_Text("Return to the main menu", small_font, White, screen, 280,580) #display text over the button
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
                #if the mouse button is clicked.
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the position of the mouse click
                #if user left clicks on the button
                if (280+230>x>280 and 575+40>y>575) and (event.button==1):
                    Click.play() #play click sound effects
                    MainMenu() #call the main menu function
        pygame.display.update() #update the screen

def TimesUp():
    '''
    Function takes not argument
    Returns no value
    Displays a times up screen if the user fails to escape before the time ends
    '''
    running = True
    Lose.play()#play the lose sound effect
    while running:
        mouse = pygame.mouse.get_pos() #get the postion of the cursor on the screen
        screen.fill(Black) #colour the screen
        #display message
        Screen_Text("Sadly you weren't able to escape!", medium_font, Red, screen, 60,100)
        screen.blit (Dead, (260,230)) #display image
        #if the cursor is within the borders of the button to go backto main menu
        if 265+275>mouse[0]>265 and 575+40>mouse[1]>575:
            pygame.draw.rect(screen, Light_Blue,(265, 575, 275, 40)) #draw a light coloured button
            screen.blit(return_arrow, (230,580)) #display return arrow image
        #if the cursor is not within the border of the button
        else:
            pygame.draw.rect(screen, Dark_Blue,(265,575, 275, 40)) #Draw dar coloured box
        Screen_Text("Return to the main menu", small_font, White, screen, 280,580) #display text of the button
        #Set a for loop to get events from the game
        for event in pygame.event.get():
            #if the user presses the 'X' button on the top right
            if event.type == pygame.QUIT:
                pygame.quit() #quit pygame
                sys.exit() #exit python
                running == False #set running to False. this exits the while loop
                #if the mouse button is clicked.
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos #set x and y to the position of the mouse click
                #if user left clicks on the button
                if (265+275>x>265 and 575+40>y>575) and (event.button==1):
                    Click.play() #play click sound effects
                    MainMenu() #call the main menu function
        pygame.display.update() #update the screen

pygame.init() #initiat pygame
screen = pygame.display.set_mode((800,670)) #create a pygame screen that is 800 pixels wide and 670 pixels tall

pygame.display.set_caption("EXIT!") #set our game caption
icon = pygame.image.load('key.png')
pygame.display.set_icon(icon) #set the game icon picture
clock = pygame.time.Clock() #track time in pygame. set the number to variable 'clock'
#Set frequent colours that I will use. RGB (Red, Green, Blue)
Dark_Blue = (51,153,255)
Light_Blue = (102,178,255)
Light_Yellow = (204,204,0)
Dark_Brown = (102,51,0)
Light_Brown = (204,102,0)
White = (255,255,255)
Red = (153,0,0)
Black = (0,0,0)
Gray = (160,160,160)
Gold = (255,128,0)
#IMAGES
OxygenTank = pygame.image.load('LowOxygen.png')
load_key = pygame.image.load('old.png')
return_arrow = pygame.image.load('return.png')
next_arrow = pygame.image.load ('next.png')
timer = pygame.image.load ('time.png')
Number0 = pygame.image.load ('Number0.png')
Number1 = pygame.image.load ('Number1.png')
Number2 = pygame.image.load ('Number2.png')
Number3 = pygame.image.load ('Number3.png')
Number4 = pygame.image.load ('Number4.png')
Number5 = pygame.image.load ('Number5.png')
Number6 = pygame.image.load ('Number6.png')
Number7 = pygame.image.load ('Number7.png')
Number8 = pygame.image.load ('Number8.png')
Number9 = pygame.image.load ('Number9.png')
Incorrect = pygame.image.load ('incorrect.png')
Correct = pygame.image.load ('correct.png')
Star = pygame.image.load ('star.png')
TextIcon = pygame.image.load('texticon.png')
Google = pygame.image.load ('google.png')
Search = pygame.image.load ('search.png')
Flashlight = pygame.image.load ('flashlight.png')
Vegetable = pygame.image.load ('vegetable.png')
Camera = pygame.image.load ('camera.png')
Brake = pygame.image.load ('brake.png')
CheckList = pygame.image.load ('checklist.png')
Door_Key = pygame.image.load ('door_key.png')
Open_Door = pygame.image.load ('door.png')
Dead = pygame.image.load ('dead.png')
Frame = pygame.image.load ('frame.png')
#SOUNDS
Click = pygame.mixer.Sound('Click.wav')
music = pygame.mixer.music.load('Music.wav')
Lose = pygame.mixer.Sound('LoseSoundEffect.wav')
pygame.mixer.music.play(-1)

large_font = pygame.font.SysFont("Times New Roman",90) #Set a large sized font that will be used the game
medium_font = pygame.font.SysFont ("Times New Roman", 50) #Set a medium sized font that will used in the game
small_font = pygame.font.SysFont("Times New Roman", 25) #Set a small sized font that will be used in the game
score = [] #set an empty list to store all of the users scores. (run times)
start_time = 0 #set a variable to save the intial time for each game. The value of this variable will change once the user selects a specific difficulty level
MainMenu() #call the Main Menu function. this function starts the game
