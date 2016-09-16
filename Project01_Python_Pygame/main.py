#-*- coding: utf-8 -*-

import pygame, os, random

pygame.init()
clock = pygame.time.Clock()
BRANCO = (255,255,255)
PRETO = (0,0,0)

# resolucao do nosso display: largura e altura
RESOLUCAO = (800, 600)
# criando janela e superficie
tela = pygame.display.set_mode(RESOLUCAO)

########fundo############
caminho = os.path.join('images', 'fundo.png')
fundo = pygame.image.load(caminho)

running = True
############quadrado################
quadrado = pygame.Surface((100,100))
quadrado.fill(BRANCO) # branco

caminho = os.path.join('fonts', 'gta.ttf')
fonte	= pygame.font.Font(caminho, 32)
primeiro_numero = random.randint(1,100)
segundo_numero = random.randint(1,100)
lista_sinais = ['+','-','x',':']
escolha = random.choice(lista_sinais)
conta = str(primeiro_numero)+str(escolha)+str(segundo_numero)
surface = fonte.render(conta, True, PRETO)
x = random.randint(0,700) # x do quadrado # 700 eh o tamanhp maximo, para nao ficar fora da tela.
y = 0 # y do quadrado
def cair(): # quadrado caindo e letra caindo.
    global x,y,primeiro_numero, segundo_numero, surface, conta, escolha
    tela.blit(quadrado, (x,y))
    tela.blit(surface, (x+18,y+35))
    y += 1
    if y >= 600:
        primeiro_numero = random.randint(1,100)
        segundo_numero = random.randint(1,100)
        escolha = random.choice(lista_sinais)
        conta = str(primeiro_numero)+str(escolha)+str(segundo_numero)
        surface = fonte.render(conta, True, PRETO)
        y = 0
        x = random.randint(0,700)



        
while running:
    clock.tick(60)
    pygame.display.set_caption('FPS %.2f' %(clock.get_fps()) )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    tela.blit(fundo, (0,0))
    cair()
    #atualiza a tela
    pygame.display.update()
pygame.display.quit()
#sys.exit()
