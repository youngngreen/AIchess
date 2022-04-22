import pygame
from board.board import board
import math
from pieces.nullpiece import nullpiece
from pieces.queen import queen
from pieces.rook import rook
from pieces.knight import knight
from pieces.bishop import bishop
from minimax import minimax
import copy

from board.move import move



pygame.init()
gamedisplay= pygame.display.set_mode((400,400))
pygame.display.set_caption("AI chess")
clock=pygame.time.Clock()

chessBoard=board()
chessBoard.createboard()
chessBoard.printboard()
movex=move()
ai=minimax()

allCells= []
allpieces=[]


green = (0, 255, 0)
blue = (0, 0, 128)
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
font = pygame.font.Font('freesansbold.ttf', 32)
text = font.render('Welcome to AI chess!', True, white, black)
text1 = font.render('PLAY GAME',True, black)
text3=font.render('AI won!', True, red)
text4=font.render('Human won!', True, red)
text5=font.render('Draw!', True, red)
text6=font.render("Can you beat me?", True, green)
textRect = text.get_rect()
textRect1 = text1.get_rect()
textRect3 = text3.get_rect()
textRect4 = text4.get_rect()
textRect5 = text5.get_rect()
textRect6 = text6.get_rect()
textRect.center = (200,50)
textRect1.center = (200,200)
textRect3.center = (200,300)
textRect4.center = (200,300)
textRect5.center = (200,200)
textRect6.center = (200,300)


saki=''

quitgame=False

while not quitgame:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quitgame= True
            pygame.quit()
            quit()

        gamedisplay.blit(text, textRect)
        pygame.draw.rect(gamedisplay,(255, 255, 255),[100,180,200,40])
        gamedisplay.blit(text1,textRect1)
        gamedisplay.blit(text6, textRect6)

        if event.type==pygame.MOUSEBUTTONDOWN:
            coord = pygame.mouse.get_pos()
            if coord[0]>=180 and coord[0]<=220 and coord[1]>=180 and coord[1]<=220:
                saki='ai'
                quitgame=True


        pygame.display.update()
        clock.tick(60)


def square(x,y,w,h,color):
    pygame.draw.rect(gamedisplay,color,[x,y,w,h])
    allCells.append([color, [x,y,w,h]])

def drawchesspieces():
    xpos= 0
    ypos= 0
    color= 0
    width= 50
    height= 50
    black= (150,150,150)
    white=(255,255,255)
    number=0

    for rows in range(8):
        for column in range(8):
            if color%2==0:
                square(xpos,ypos,width,height,white)
                if not chessBoard.gameCells[rows][column].pieceonCell.tostring() == "-":
                    img = pygame.image.load("./img/"
                                            + chessBoard.gameCells[rows][column].pieceonCell.alliance[0].upper()
                                            + chessBoard.gameCells[rows][column].pieceonCell.tostring().upper()
                                            + ".png")
                    img=pygame.transform.scale(img, (50,50))
                    allpieces.append([img,[xpos,ypos],chessBoard.gameCells[rows][column].pieceonCell])

                xpos +=50

            else:
                square(xpos,ypos,width,height,black)
                if not chessBoard.gameCells[rows][column].pieceonCell.tostring() == "-":
                    img = pygame.image.load("./img/"
                                        + chessBoard.gameCells[rows][column].pieceonCell.alliance[0].upper()
                                        + chessBoard.gameCells[rows][column].pieceonCell.tostring().upper()
                                        + ".png")
                    img=pygame.transform.scale(img, (50,50))
                    allpieces.append([img,[xpos,ypos],chessBoard.gameCells[rows][column].pieceonCell])

                xpos +=50

            color +=1
            number +=1

        color +=1
        xpos=0
        ypos+=50
        for img in allpieces:
            gamedisplay.blit(img[0],img[1])

drawchesspieces()


def updateposition(x,y):
    a=x*8
    b=a+y
    return b

def givecolour(x,y):

    if y%2==0:
        if x%2==0:
            return [143,155,175]
        else:
            return [66,134,244]

    else:
        if x%2==0:
            return [66,134,244]
        else:
            return[143,155,175]


if saki=='ai':

    moves=[]
    enpassant=[]
    promote=[]
    promotion=False
    turn=0

    array=[]
    quitgame=False

    while not quitgame:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                quitgame= True
                pygame.quit()
                quit()


            if movex.checkw(chessBoard.gameCells)[0]=='checked' and len(moves)==0 :
                array=movex.movesifcheckedw(chessBoard.gameCells)
                if len(array)==0:
                    saki='end1'
                    quitgame=True
                    break

            if movex.checkb(chessBoard.gameCells)[0]=='checked' and len(moves)==0 :
                array=movex.movesifcheckedb(chessBoard.gameCells)
                if len(array)==0:
                    saki='end2'
                    quitgame=True
                    break


            if movex.checkb(chessBoard.gameCells)[0]=='notchecked' and turn%2==1 and len(moves)==0 :
                check=False
                for x in range(8):
                    for y in range(8):
                        if chessBoard.gameCells[y][x].pieceonCell.alliance=='Black' and turn%2==1:
                            moves1=chessBoard.gameCells[y][x].pieceonCell.legalmoveb(chessBoard.gameCells)
                            lx1=movex.pinnedb(chessBoard.gameCells,moves1,y,x)
                            if len(lx1)==0:
                                continue
                            else:
                                check=True
                            if check==True:
                                break
                    if check==True:
                        break


                if check==False:
                    saki='end3'
                    quitgame=True
                    break

            if movex.checkw(chessBoard.gameCells)[0]=='notchecked' and turn%2==0 and len(moves)==0 :
                check=False
                for x in range(8):
                    for y in range(8):
                        if chessBoard.gameCells[y][x].pieceonCell.alliance=='White' and turn%2==0:
                            moves1=chessBoard.gameCells[y][x].pieceonCell.legalmoveb(chessBoard.gameCells)
                            lx1=movex.pinnedw(chessBoard.gameCells,moves1,y,x)
                            if len(lx1)==0:
                                continue
                            else:
                                check=True
                            if check==True:
                                break
                    if check==True:
                        break


                if check==False:
                    saki='end3'
                    quitgame=True





            if not turn%2==0 and promotion==False:

                turn=turn+1
                sc=copy.deepcopy(chessBoard.gameCells)
                y,x,fx,fy=ai.evaluate(sc)
                m=fy
                n=fx
                if chessBoard.gameCells[y][x].pieceonCell.tostring()=='K' or chessBoard.gameCells[y][x].pieceonCell.tostring()=='R':
                    chessBoard.gameCells[y][x].pieceonCell.moved=True

                if chessBoard.gameCells[y][x].pieceonCell.tostring()=='K' and m==x+2:
                    chessBoard.gameCells[y][x+1].pieceonCell=chessBoard.gameCells[y][x+3].pieceonCell
                    s=updateposition(y,x+1)
                    chessBoard.gameCells[y][x+1].pieceonCell.position=s
                    chessBoard.gameCells[y][x+3].pieceonCell=nullpiece()
                if chessBoard.gameCells[y][x].pieceonCell.tostring()=='K' and m==x-2:
                    chessBoard.gameCells[y][x-1].pieceonCell=chessBoard.gameCells[y][0].pieceonCell
                    s=updateposition(y,x-1)
                    chessBoard.gameCells[y][x-1].pieceonCell.position=s
                    chessBoard.gameCells[y][0].pieceonCell=nullpiece()


                if not len(enpassant)==0:
                    chessBoard.gameCells[enpassant[0]][enpassant[1]].pieceonCell.enpassant=False
                    enpassant=[]
                if chessBoard.gameCells[y][x].pieceonCell.tostring()=='P' and y+1==n and x+1==m and chessBoard.gameCells[n][m].pieceonCell.tostring()=='-':
                    chessBoard.gameCells[y][x+1].pieceonCell=nullpiece()
                if chessBoard.gameCells[y][x].pieceonCell.tostring()=='P' and y+1==n and x-1==m and chessBoard.gameCells[n][m].pieceonCell.tostring()=='-':
                    chessBoard.gameCells[y][x-1].pieceonCell=nullpiece()

                if chessBoard.gameCells[y][x].pieceonCell.tostring()=='P' and n==y+2:
                    chessBoard.gameCells[y][x].pieceonCell.enpassant=True
                    enpassant=[n,m]

                if chessBoard.gameCells[y][x].pieceonCell.tostring()=='P' and y+1==n and y==6:
                    promotion=True


                if promotion==False:

                    chessBoard.gameCells[n][m].pieceonCell=chessBoard.gameCells[y][x].pieceonCell
                    chessBoard.gameCells[y][x].pieceonCell=nullpiece()
                    s=updateposition(n,m)
                    chessBoard.gameCells[n][m].pieceonCell.position=s
                    allCells.clear()
                    allpieces.clear()
                    chessBoard.printboard()
                    drawchesspieces()
                    moves=[]

                if promotion==True:

                    if chessBoard.gameCells[y][x].pieceonCell.tostring()=='P':
                        chessBoard.gameCells[y][x].pieceonCell=nullpiece()
                        chessBoard.gameCells[n][m].pieceonCell=queen('Black',updateposition(n,m))
                        allCells.clear()
                        allpieces.clear()
                        chessBoard.printboard()
                        drawchesspieces()
                        moves=[]
                        promote=[]
                        promotion=False






            if event.type==pygame.MOUSEBUTTONDOWN:
                if movex.checkw(chessBoard.gameCells)[0]=='checked' and len(moves)==0 :
                    array=movex.movesifcheckedw(chessBoard.gameCells)
                    coord=pygame.mouse.get_pos()
                    m=math.floor(coord[0]/50)
                    n=math.floor(coord[1]/50)
                    imgx=pygame.transform.scale(pygame.image.load("./img/red_square.png",), (50,50))
                    mx=[]
                    ma=[]
                    for move in array:
                        if(move[1]==m and move[0]==n):
                            mx=[move[3]*50,move[2]*50]
                            ma=[move[2],move[3]]
                            moves.append(ma)
                            gamedisplay.blit(imgx,mx)
                            x=move[1]
                            y=move[0]
                    break

                if not len(promote)==0:
                    coord = pygame.mouse.get_pos()
                    m=math.floor(coord[0]/50)
                    n=math.floor(coord[1]/50)
                    if  chessBoard.gameCells[promote[5][0]][promote[5][1]].pieceonCell.alliance=='White':
                        for i in range(len(promote)):
                            if i==4:
                                turn=turn-1
                                break
                            if promote[i][0]==n and promote[i][1]==m:
                                if i==0:
                                    chessBoard.gameCells[promote[4][1]][promote[4][0]].pieceonCell=queen('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameCells[promote[5][0]][promote[5][1]].pieceonCell=nullpiece()
                                    break
                                if i==1:
                                    chessBoard.gameCells[promote[4][1]][promote[4][0]].pieceonCell=rook('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameCells[promote[5][0]][promote[5][1]].pieceonCell=nullpiece()
                                    break
                                if i==2:
                                    chessBoard.gameCells[promote[4][1]][promote[4][0]].pieceonCell=knight('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameCells[promote[5][0]][promote[5][1]].pieceonCell=nullpiece()
                                    break
                                if i==3:
                                    chessBoard.gameCells[promote[4][1]][promote[4][0]].pieceonCell=bishop('White',updateposition(promote[4][1],promote[4][0]))
                                    chessBoard.gameCells[promote[5][0]][promote[5][1]].pieceonCell=nullpiece()
                                    break

                    allCells.clear()
                    allpieces.clear()
                    chessBoard.printboard()
                    drawchesspieces()
                    promote=[]
                    promotion=False







                if not len(moves)==0:
                    coord = pygame.mouse.get_pos()
                    m=math.floor(coord[0]/50)
                    n=math.floor(coord[1]/50)
                    for move in moves:
                        if move[0]==n and move[1]==m:
                            turn=turn+1
                            if chessBoard.gameCells[y][x].pieceonCell.tostring()=='k' or chessBoard.gameCells[y][x].pieceonCell.tostring()=='r':
                                chessBoard.gameCells[y][x].pieceonCell.moved=True



                            if chessBoard.gameCells[y][x].pieceonCell.tostring()=='k' and m==x+2:
                                chessBoard.gameCells[y][x+1].pieceonCell=chessBoard.gameCells[y][x+3].pieceonCell
                                s=updateposition(y,x+1)
                                chessBoard.gameCells[y][x+1].pieceonCell.position=s
                                chessBoard.gameCells[y][x+3].pieceonCell=nullpiece()
                            if chessBoard.gameCells[y][x].pieceonCell.tostring()=='k' and m==x-2:
                                chessBoard.gameCells[y][x-1].pieceonCell=chessBoard.gameCells[y][0].pieceonCell
                                s=updateposition(y,x-1)
                                chessBoard.gameCells[y][x-1].pieceonCell.position=s
                                chessBoard.gameCells[y][0].pieceonCell=nullpiece()



                            if not len(enpassant)==0:
                                chessBoard.gameCells[enpassant[0]][enpassant[1]].pieceonCell.enpassant=False
                                enpassant=[]

                            if chessBoard.gameCells[y][x].pieceonCell.tostring()=='p' and y-1==n and x+1==m and chessBoard.gameCells[n][m].pieceonCell.tostring()=='-':
                                chessBoard.gameCells[y][x+1].pieceonCell=nullpiece()
                            if chessBoard.gameCells[y][x].pieceonCell.tostring()=='p' and y-1==n and x-1==m and chessBoard.gameCells[n][m].pieceonCell.tostring()=='-':
                                chessBoard.gameCells[y][x-1].pieceonCell=nullpiece()

                            if chessBoard.gameCells[y][x].pieceonCell.tostring()=='p' and n==y-2:
                                chessBoard.gameCells[y][x].pieceonCell.enpassant=True
                                enpassant=[n,m]


                            if chessBoard.gameCells[y][x].pieceonCell.tostring()=='p' and y-1==n and y==1:
                                promotion=True



                            if promotion==False:

                                chessBoard.gameCells[n][m].pieceonCell=chessBoard.gameCells[y][x].pieceonCell
                                chessBoard.gameCells[y][x].pieceonCell=nullpiece()
                                s=updateposition(n,m)
                                chessBoard.gameCells[n][m].pieceonCell.position=s
                    if promotion==False:
                        allCells.clear()
                        allpieces.clear()
                        chessBoard.printboard()
                        drawchesspieces()
                        moves=[]

                    if promotion==True:




                        if  chessBoard.gameCells[y][x].pieceonCell.tostring()=='p' and x==7 and y==1:
                            pygame.draw.rect(gamedisplay,(0,0,0),[x*50-50,(y*50)+50,100,100])
                            imgx=pygame.transform.scale(pygame.image.load("./img/WQ.png",), (50,50))
                            imgx1=pygame.transform.scale(pygame.image.load("./img/WR.png",), (50,50))
                            imgx2=pygame.transform.scale(pygame.image.load("./img/WN.png",), (50,50))
                            imgx3=pygame.transform.scale(pygame.image.load("./img/WB.png",), (50,50))
                            gamedisplay.blit(imgx,[x*50-50,(y*50)+100])
                            gamedisplay.blit(imgx1,[(x*50),(y*50)+100])
                            gamedisplay.blit(imgx2,[x*50-50,(y*50)+50])
                            gamedisplay.blit(imgx3,[(x*50),(y*50)+50])
                            promote=[[y+2,x-1],[y+2,x],[y+1,x],[y+1,x],[m,n],[y,x]]

                        elif chessBoard.gameCells[y][x].pieceonCell.tostring()=='p':
                            pygame.draw.rect(gamedisplay,(0,0,0),[x*50,(y*50)+50,100,100])
                            imgx=pygame.transform.scale(pygame.image.load("./img/WQ.png",), (50,50))
                            imgx1=pygame.transform.scale(pygame.image.load("./img/WR.png",), (50,50))
                            imgx2=pygame.transform.scale(pygame.image.load("./img/WN.png",), (50,50))
                            imgx3=pygame.transform.scale(pygame.image.load("./img/WB.png",), (50,50))
                            gamedisplay.blit(imgx,[x*50,(y*50)+100])
                            gamedisplay.blit(imgx1,[(x*50)+50,(y*50)+100])
                            gamedisplay.blit(imgx2,[x*50,(y*50)+50])
                            gamedisplay.blit(imgx3,[(x*50)+50,(y*50)+50])
                            promote=[[y+2,x],[y+2,x+1],[y+1,x],[y+1,x+1],[m,n],[y,x]]










                else:
                    drawchesspieces()
                    coords = pygame.mouse.get_pos()
                    x=math.floor(coords[0]/50)
                    y=math.floor(coords[1]/50)
                    mx=[]
                    if(chessBoard.gameCells[y][x].pieceonCell.alliance=='White'):
                        moves=chessBoard.gameCells[y][x].pieceonCell.legalmoveb(chessBoard.gameCells)
                        if(chessBoard.gameCells[y][x].pieceonCell.tostring()=='k'):
                            ax=movex.castlingw(chessBoard.gameCells)
                            if not len(ax)==0:
                                for l in ax:
                                    if l=='ks':
                                        moves.append([7,6])
                                    if l=='qs':
                                        moves.append([7,2])
                        if(chessBoard.gameCells[y][x].pieceonCell.tostring()=='p'):
                            ay=movex.enpassantb(chessBoard.gameCells,y,x)
                            if not len(ay)==0:
                                if ay[1]=='r':
                                    moves.append([y-1,x+1])
                                else:
                                    moves.append([y-1,x-1])


                    if chessBoard.gameCells[y][x].pieceonCell.alliance=='White':
                        lx=movex.pinnedw(chessBoard.gameCells,moves,y,x)
                    moves=lx

                    if not turn%2==0:
                        moves=[]

                    if chessBoard.gameCells[y][x].pieceonCell.alliance=='Black':
                        moves=[]

                    if chessBoard.gameCells[y][x].pieceonCell.tostring()=='-':
                        moves=[]


                    imgx=pygame.transform.scale(pygame.image.load("./img/red_square.png",), (50,50))
                    for move in moves:
                        mx=[move[1]*50,move[0]*50]
                        gamedisplay.blit(imgx,mx)









        for img in allpieces:
            gamedisplay.blit(img[0],img[1])




        pygame.display.update()
        clock.tick(60)


if saki=='end1':
    quitgame=False
    while not quitgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame= True
                pygame.quit()
                quit()

            gamedisplay.blit(text3,textRect3)


            pygame.display.update()
            clock.tick(60)

if saki=='end2':
    quitgame=False
    while not quitgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame= True
                pygame.quit()
                quit()

            gamedisplay.blit(text4,textRect4)
         #  pygame.draw.rect(gamedisplay,(66,134,244),[400,400,400,400])


            pygame.display.update()
            clock.tick(60)

if saki=='end3':
    quitgame=False
    while not quitgame:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quitgame= True
                pygame.quit()
                quit()

            gamedisplay.blit(text5,textRect5)
            #  pygame.draw.rect(gamedisplay,(66,134,244),[400,400,400,400])


            pygame.display.update()
            clock.tick(60)

