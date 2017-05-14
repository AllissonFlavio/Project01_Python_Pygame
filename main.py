#-*- coding: utf-8 -*-
# Python 2.7
import pygame, os, random, time, sys

pygame.init()
clock = pygame.time.Clock()
AMARELO = (230,255,0)
VERDE = (0,255,0)
VERMELHO = (255,0,0)
BRANCO = (255,255,255)
PRETO = (0,0,0)

# resolucao do nosso display: largura e altura
RESOLUCAO = (800, 600)
# criando janela e superficie
tela = pygame.display.set_mode(RESOLUCAO)

########fundo############
fundo = pygame.image.load('images\\quadro.jpg')

#barra de informações
surface_informacaoes = pygame.Surface((800, 30))
surface_informacaoes.fill(BRANCO)

running = True
#importando fonte
fonte = pygame.font.SysFont(None, 60)

#numeros aleatrios
escolha = None
lista_sinais = ['+','-','x',':']
primeiro_numero = None
segundo_numero = None
def escolher_conta(): #está função escolhe a conta. Se for divisão, o segundo numero aleatório sempre será multiplo
    global escolha, primeiro_numero, segundo_numero
    escolha = random.choice(lista_sinais)
    if escolha == ':':
        lista_multiplos = []
        primeiro_numero = random.randint(1, 100)
        for i in range(1,primeiro_numero+1):
            if primeiro_numero%i == 0:
                lista_multiplos.append(i)
        segundo_numero = random.choice(lista_multiplos)
    elif escolha == 'x':
        primeiro_numero = random.randint(1,100)
        segundo_numero = random.randint(0,10)
    elif escolha == '-':
        primeiro_numero = random.randint(0,100)
        segundo_numero = random.randint(0,primeiro_numero)
    else:
        primeiro_numero = random.randint(1, 100)
        segundo_numero = random.randint(1, 100)
    definir_resultado(primeiro_numero,segundo_numero) # sempre quando definir dois numeros alétorios, é chamada essa funcao que defini o resultado.

resultado = None
def definir_resultado(numero1,numero2):
    global resultado, escolha
    if escolha == '+':
        resultado = numero1+numero2
    elif escolha == '-':
        resultado = numero1-numero2
    elif escolha == 'x':
        resultado = numero1*numero2
    elif escolha == ':':
        resultado = numero1/numero2

escolher_conta()#chamada para função escolher as operações e numeros pela primeira vez
conta = str(primeiro_numero)+str(escolha)+str(segundo_numero) # construção da 'string' da conta
surface = fonte.render(conta, True, BRANCO) #criação da string da conta
x = random.randint(0,700) # x do quadrado # 700 eh o tamanhp maximo, para nao ficar fora da tela.
y = 0 # y do quadrado
velocidade = 0.5 #velocidade inicial
def cair(): # quadrado caindo e letra caindo.
    global x,y,primeiro_numero, segundo_numero, surface, conta, escolha, acerto, chances, mensagem
    tela.blit(surface, (x,y))
    y += velocidade
    if y >= 600 or acerto == True:# quando a conta sair da tela, é criada uma nova conta
        escolher_conta()
        conta = str(primeiro_numero)+str(escolha)+str(segundo_numero)
        surface = fonte.render(conta, True, BRANCO)
        y = 0
        x = random.randint(0,680)
        mensagem = []
        if acerto == True:
            acerto = False
        else:
            chances -= 1

fonte_resultado = pygame.font.SysFont(None, 30)
mensagem = []
def desenha_caixa():
    global mensagem
    caixa = fonte_resultado.render('Resultado: '+''.join(mensagem), True, PRETO, BRANCO)
    tela.blit(caixa, (600,580))
pontos = 0
chances = 3
def desenhar_pontos():
    global pontos, chances
    string_pontos = fonte_resultado.render('Pontos: '+str(pontos), True, PRETO)
    string_chances = fonte_resultado.render('Vida: '+str(chances), True, PRETO)
    string_velocidade = fonte_resultado.render('Nivel: '+str(int(velocidade/0.5)), True, PRETO)
    tela.blit(string_pontos, (0,580))
    tela.blit(string_chances, (150,580))
    tela.blit(string_velocidade, (300,580))

fonte_corrigir = pygame.font.SysFont(None, 40)
acerto = False
def corrigir():
    global mensagem, y, pontos, acerto, velocidade
    if str(resultado) == ''.join(mensagem):
        mensagem = []
        balao_resultado = fonte.render('Acertou!!!!', True, VERDE)
        tela.blit(balao_resultado, (330,300))
        pontos += 1
        pygame.display.update()
        time.sleep(1)
        acerto = True
        if pontos%5 == 0:
            velocidade += 0.5
    else:
        mensagem = []
        balao_resultado = fonte.render('Errou', True, VERMELHO)
        tela.blit(balao_resultado, (330, 300))
        pygame.display.update()
        time.sleep(1)
        y = 600 # quando é atribuido 600 a y, automaticamente é criado um novo retangulo com um problema


while running:
    clock.tick(60)
    pygame.display.set_caption('Mathematics FPS %.2f Versão: 0.1' %(clock.get_fps()) )
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                mensagem = mensagem[0:-1]
            elif event.key == pygame.K_RETURN:
                corrigir()
            elif event.key >= 48 and event.key <= 57:
                if len(mensagem) < 7:
                    mensagem.append(pygame.key.name(event.key))
            elif event.key >= 256 and event.key <= 265:
                if len(mensagem) < 7:
                    mensagem.append(pygame.key.name(event.key)[1])
    tela.blit(fundo, (0, -12))
    cair()
    tela.blit(surface_informacaoes, (0, 570))
    desenha_caixa()
    desenhar_pontos()
    if chances < 1:
        balao_pontos = fonte.render('Pontos: '+str(pontos), True, VERMELHO)
        tela.blit(balao_pontos, (300, 300))
        pygame.display.update()
        time.sleep(4)
        running = False
    pygame.display.update() #atualiza a tela
pygame.display.quit()
sys.exit()
