import pygame, time, pandas, random
from pygame.locals import *

pygame.font.init()
pygame.init()


def Format(question):

    ql = question.split(" ")
    num = 0
    word = 0

    for i in ql:
        word +=1
        num+=len(i)
        if num>= 13:
            break

    line1 = ""
    line2 = ""
    retlist = []

    for index, value in enumerate(ql):
        if index<word:
            line1+=(f"{value} ")
        else:
            line2+=(f"{value} ")
    
    retlist.append(line1)
    retlist.append(line2)

    return retlist


game_exit = False
game_start = False
score_screen = False
first = True
questionOver = True

width = 750  
height = 495

orange = (255, 128, 0)
green = (0, 255, 0)
white = (255,255,255)
black = (0,0,0,0)

clock = pygame.time.Clock()
fps = 50


gameWindow = pygame.display.set_mode((width,height))
windowName = pygame.display.set_caption("Quizz!")
pygame.display.update()

bg1 = pygame.image.load("Images/quizTime.jpg")
bg2 = pygame.image.load("Images/quizBG.jpg")

start = pygame.image.load("IMages/StartButton.png")

font = pygame.font.Font('Images/Orbitron.ttf', 32) 
font2 = pygame.font.Font('Images/Orbitron.ttf', 52) 
font3 = pygame.font.Font('Images/Orbitron.ttf', 100) 

pygame.mixer.init() 
pygame.mixer.music.set_volume(0.7) 


while not game_exit:
    while not game_start and not score_screen:
        if game_exit:
            break
        csv_data = pandas.read_csv("Questions.csv")
        df = pandas.DataFrame(csv_data)
        queslist = df.values.tolist()

        correctCount = 0
        mouse = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if mouse[0]>345 and mouse[0]<445 and mouse[1]<325 and mouse[1]>225: 
                    game_start = True

        gameWindow.blit(bg1,(0,0))
        gameWindow.blit(font2.render("Quizzz!", True, white),(290,140))
        gameWindow.blit(start,(345,225))
        pygame.display.update()
        clock.tick(fps)

        if first:
            pygame.mixer.music.load("Music/Intro.mp3") 
            pygame.mixer.music.play() 
            time.sleep(5.5)


        first = False



    qno = 1

    while game_start and not score_screen:
        if game_exit:
            break

        if qno<11:
            if questionOver:
                questionset = random.choice(queslist)
                question = questionset[0]
                OpA = questionset[1]
                OpB = questionset[2]
                OpC = questionset[3]
                OpD = questionset[4] 
                correctAnswer = questionset[5]
                queslist.remove(questionset)
                questionOver = False

            ycordQ = 100
            ycordA = 265
            ycordB = 265
            ycordC = 358
            ycordD = 358

            mouse = pygame.mouse.get_pos()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_exit = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if mouse[0]>61 and mouse[0]<357 and mouse[1]<310 and mouse[1]>266: #A
                        answer = "A"
                        if answer == correctAnswer:
                            pygame.mixer.music.load("Music/Correct.mp3") 
                            pygame.mixer.music.play() 
                            time.sleep(5.5)
                            correctCount+=1
                        else:
                            pygame.mixer.music.load("Music/Wrong.mp3") 
                            pygame.mixer.music.play() 
                            time.sleep(3.5)

                        questionOver = True
                    if mouse[0]>390 and mouse[0]<690 and mouse[1]<310 and mouse[1]>266: #B
                        answer = "B"
                        if answer == correctAnswer:
                            pygame.mixer.music.load("Music/Correct.mp3") 
                            pygame.mixer.music.play()
                            time.sleep(5.5)
                            correctCount+=1
                        else:
                            pygame.mixer.music.load("Music/Wrong.mp3") 
                            pygame.mixer.music.play() 
                            time.sleep(3.5)

                        questionOver = True
                    if mouse[0]>61 and mouse[0]<357 and mouse[1]<399 and mouse[1]>357: #C
                        answer = "C"
                        if answer == correctAnswer:
                            pygame.mixer.music.load("Music/Correct.mp3") 
                            pygame.mixer.music.play() 
                            time.sleep(5.5)
                            correctCount+=1
                        else:
                            pygame.mixer.music.load("Music/Wrong.mp3") 
                            pygame.mixer.music.play()
                            time.sleep(3.5) 

                        questionOver = True
                    if mouse[0]>390 and mouse[0]<690 and mouse[1]<399 and mouse[1]>357: #D
                        answer = "D"
                        if answer == correctAnswer:
                            pygame.mixer.music.load("Music/Correct.mp3") 
                            pygame.mixer.music.play() 
                            time.sleep(5.5)
                            correctCount+=1
                        else:
                            pygame.mixer.music.load("Music/Wrong.mp3") 
                            pygame.mixer.music.play()
                            time.sleep(3.5) 

                        questionOver = True

            gameWindow.blit(bg2,(0,0))
            for x in Format(question):
                gameWindow.blit(font.render(x, True, white),(200,ycordQ))
                ycordQ+=40
            for x in Format(OpA):
                gameWindow.blit(font.render(x, True, white),(70,ycordA))
                ycordA+=40
            for x in Format(OpB):
                gameWindow.blit(font.render(x, True, white),(400,ycordB))
                ycordB+=40
            for x in Format(OpC):
                gameWindow.blit(font.render(x, True, white),(70,ycordC))
                ycordC+=40
            for x in Format(OpD):
                gameWindow.blit(font.render(x, True, white),(400,ycordD))
                ycordD+=40

            pygame.display.update()
            clock.tick(fps) 
            if questionOver:
                qno +=1

        else:
            score_screen = True
            game_start = False


    while not game_start and score_screen:
        if game_exit:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_exit = True

        gameWindow.fill(black)
        gameWindow.blit(font3.render("Your score:", True, white),(55,100))
        gameWindow.blit(font3.render(f"{correctCount}/10", True, white),(257,250))
        pygame.display.update()
        clock.tick(fps)
        time.sleep(4)
        score_screen = False
        

pygame.quit()
quit()
