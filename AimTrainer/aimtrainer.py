import pygame
import random
import math


pygame.init()


#Random Color maker
colors=[]
for i in range(50):
    r= random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    colors.append((r,g,b))


#Solid Color
colour= (255,233,0)

#Display size
width= 1600
height= 900


#Display setup
display= pygame.display.set_mode((width,height))


#Framerate
clock= pygame.time.Clock()


#First circle ubication and draw
cx=random.randint(20,width-20)
cy=random.randint(20,height-20)
r=18
pygame.draw.circle(display,colour,(cx,cy),r)


#Storage variables
numero_de_circulos=0
tiempos=0
contador_tiempos=0
promedio_de_tiempo=0
clicks_por_fuera=0
porcentaje_clicks_acertados=0

#Font setup
font=pygame.font.SysFont('timesnewroman',  30)


#Text setup and variables made in a fstring to admit variables
text = font.render(f"Circulos clicekados: {numero_de_circulos}", True, (0,0,0), (255,255,255))
text1 = font.render(f"Promedio de tiempo: {promedio_de_tiempo}", True, (0,0,0), (255,255,255))
text2 = font.render(f"Porcentaje de aciertos: {porcentaje_clicks_acertados}", True, (0,0,0), (255,255,255))

#Setup of x and y positions of text indicating number of circles
xpos=265
ypos=34
textRect = text.get_rect()
textRect.center = (xpos // 2, ypos // 2)


#Setup of x and y positions of text indicating time average
x1pos=2600
y1pos=34
text1Rect = text1.get_rect()
text1Rect.center = (x1pos // 2, y1pos // 2)


#Setup of x and y positions of text indicating hit percentage
x2pos=1200
y2pos=34
text2Rect = text2.get_rect()
text2Rect.center = (x2pos // 2, y2pos // 2)



#Usefull for getting sizes
    #print(text1.get_width())
    #print(text1.get_height())

#Get time before initiating the cycle
tiempo1=pygame.time.get_ticks()


#Loop
while True:

    #Text display
    display.blit(text, textRect)
    display.blit(text1, text1Rect)
    display.blit(text2, text2Rect)



    for event in pygame.event.get():


        #Get out
        if event.type == pygame.QUIT:
            quit()
            break
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                x = pygame.mouse.get_pos()[0]
                y = pygame.mouse.get_pos()[1]
                #relative position to the circle
                sqx = (x-cx)**2
                sqy = (y-cy)**2


                #Someone at the circle
                if sqx+sqy<=r**2:
                    #Stats de tiempo
                    tiempo2=pygame.time.get_ticks()
                    contador_tiempos+=1
                    tiempos+=tiempo2-tiempo1
                    tiempo1=tiempo2
                    promedio_de_tiempo= round(tiempos/contador_tiempos,1)


                    #Stats number of circles hitted
                    numero_de_circulos+=1


                    #Stats hit percentage
                    print("Veces: " + str(contador_tiempos) + " Cagadas: "+ str(clicks_por_fuera))
                    porcentaje_clicks_acertados=round((contador_tiempos/(contador_tiempos+clicks_por_fuera))*100,1)


                    #Remaking of texts
                    text = font.render(f"Circulos clicekados: {numero_de_circulos}", True, (0,0,0), (255,255,255))
                    text1 = font.render(f"Promedio de tiempo: {promedio_de_tiempo}", True, (0,0,0), (255,255,255))
                    text2 = font.render(f"Porcentaje de aciertos: {porcentaje_clicks_acertados}", True, (0,0,0), (255,255,255))

                    #Black filling
                    display.fill((0,0,0))


                    #Size, radius and drawing of a new circle
                    cx=random.randint(20,width-20)
                    cy=random.randint(68,height-20)
                    r=18
                    pygame.draw.circle(display,colour,(cx,cy),r)
                elif sqx+sqy>r**2:
                    clicks_por_fuera+=1

            break

    #Update of display and fps
    pygame.display.update()
    clock.tick(60)
