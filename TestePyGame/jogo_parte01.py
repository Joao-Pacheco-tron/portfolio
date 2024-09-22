import pygame 
import random 
pygame.init()
x = 400
y = 300
pos_x = 200
pos_y = 300
velocidade = 1000
velocidade_outros = 5
fundo = pygame.image.load('Jogo/Rua.png ')
carro = pygame.image.load('Jogo/download-removebg-preview.png')
cinza = pygame.image.load('Jogo/carro2.png')
dourado = pygame.image.load('Jogo/carro3.png')
preto = pygame.image.load('Jogo/carro4.png')

janela = pygame.display.set_mode((800,600))
pygame.display.set_caption("Criando um jogo com Python")

janela_aberta = True
while janela_aberta :
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False
            
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_UP]:
        y-= velocidade
    if comandos[pygame.K_DOWN]:
        y+= velocidade
    if comandos[pygame.K_RIGHT]:
        x+= velocidade
    if comandos[pygame.K_LEFT]:
        x-= velocidade
        
    if((x + 80 > pos_x and y + 180 > pos_y)):
        y = 1200
 
    if (pos_y <= -225):
        pos_y = 700
        
    pos_y -= velocidade_outros
            
    janela.blit(fundo,(0,0))
    janela.blit(carro,(x,y))
    janela.blit(cinza, (pos_x-150,pos_y))
    janela.blit(dourado, (pos_x+230,pos_y))
    janela.blit(preto, (pos_x+350,pos_y))
    pygame.display.update()
            
pygame.quit()