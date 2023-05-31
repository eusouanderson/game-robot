import pygame
from main import Player, Inimig, Menu


pygame.init()

pygame.mixer.init()
dano = 'sounds/mixkit-boxer-getting-hit-2055.wav'
gameover = 'sounds/mixkit-player-losing-or-failing-2042.wav'
meleesound = 'sounds/mixkit-martial-arts-fast-punch-2047.wav'
sound = pygame.mixer.music


clock = pygame.time.Clock()
largura, altura = 1000, 768
tamanho_da_tela = largura, altura
screen = pygame.display.set_mode(tamanho_da_tela)
back = pygame.image.load('png/back.jpg')

back = pygame.transform.scale(back, (1360, 768))
back_rect = back.get_rect()
back_pos = 0, 0

pygame.display.set_caption('Game Robot')
color = 255, 255, 255
colorRed = 255, 0, 0

pygame.font.init()

lifepoint = 500
lifepoint1 = 500

fonte = pygame.font.get_default_font()
fontesys = pygame.font.SysFont(fonte, 35)


moving_sprites = pygame.sprite.Group()

player = Player(0, 550)

rival = Inimig(500, 550)

lifebar = Menu(0, 0, 80, lifepoint)
lifebar2 = Menu(500, 0, 80, lifepoint1)
moving_sprites.add(player, rival, lifebar, lifebar2)