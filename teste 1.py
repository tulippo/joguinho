import pygame
from random import randint
pygame.init()

#proporções da tela:
x = 1920 #int(input('Qual o tamanho do seu X? '))
y = 1080 #int(input('Qual o tamanho do seu Y? '))


#posiçoes dos objetos:
a = x/2
b = y/2


raiox = 0
raioy = randint(180, 980)

raio1 = 0
raio2 = randint(180, 980)

raio3 = 0
raio4 = randint(180, 980)

raio5 = 0
raio6 = randint(180, 980)


#velocidades:
velocidade = 15
vraio = 15
vraio1 = 13.5
vraio2 = 14
vraio3 = 13
timer = 0
tempo_segundo = 0

#images:
bola = pygame.image.load('bola.png')
raio = pygame.image.load('raio1.png')
raioZ = pygame.image.load('raio1.png')
raioW = pygame.image.load('raio1.png')
raioF = pygame.image.load('raio1.png')


#timer
font = pygame.font.SysFont('arial black', 30)
texto = font.render('Tempo: ', True, (0, 0, 0), (255, 170, 160))
postext = texto.get_rect()
postext.center = (920, 150)

#display:
janela = pygame.display.set_mode((x, y))
pygame.display.set_caption('britinho games')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(24)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False


#comandos do player:
    comandos = pygame.key.get_pressed()
    if comandos[pygame.K_w]:
        b -= velocidade
    if comandos[pygame.K_s]:
        b += velocidade
    if comandos[pygame.K_d]:
        a += velocidade
    if comandos[pygame.K_a]:
        a -= velocidade


#propriedades dos objetos
    if a >= x:
        a = int(x)*0.02
    if a <= -int(x)*0.02:
        a = x

    raiox += vraio
    if raiox >= x:
        raiox = int(x)*0.025
        raioy = randint(180, 980)

    raio1 += vraio1
    if raio1 >= x:
        raio1 = int(x)*0.025
        raio2 = randint(180, 980)

    raio3 += vraio2
    if raio3 >= x:
        raio3 = int(x)*0.025
        raio4 = randint(180, 980)

    raio5 += vraio3
    if raio5 >= x:
        raio5 = int(x)*0.025
        raio6 = randint(180, 980)

    if (timer < 41.7):
        timer += 1
    else:
        tempo_segundo += 1
        texto = font.render("Tempo: {}".format(tempo_segundo), True, (0, 0, 0), (255, 170, 160))
        timer = 0
#inserindo a imagem:
    janela.fill((255, 170, 160))
    janela.blit(bola, (a, b))
    janela.blit(raio, (raiox, raioy))
    janela.blit(raioZ, (raio1, raio2))
    janela.blit(raioW, (raio3, raio4))
    janela.blit(raioF, (raio5, raio6))
    janela.blit(texto, postext)
    pygame.display.update()

pygame.quit()
