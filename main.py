import sys, pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()


        self.run_animation = False
        self.runl_animation = False
        self.sprites = []
        self.sprites.append(pygame.image.load('png/Run (1).png'))
        self.sprites.append(pygame.image.load('png/Run (2).png'))
        self.sprites.append(pygame.image.load('png/Run (3).png'))
        self.sprites.append(pygame.image.load('png/Run (4).png'))
        self.sprites.append(pygame.image.load('png/Run (5).png'))
        self.sprites.append(pygame.image.load('png/Run (6).png'))
        self.sprites.append(pygame.image.load('png/Run (7).png'))
        self.sprites.append(pygame.image.load('png/Run (8).png'))

        self.current_sprite = 0

        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_x, pos_y]

        # ------------------------------------------------------------
        self.idle_animation = False
        self.spritesL = []
        self.spritesL.append(pygame.image.load('png/Idle (1).png'))
        self.spritesL.append(pygame.image.load('png/Idle (2).png'))
        self.spritesL.append(pygame.image.load('png/Idle (3).png'))
        self.spritesL.append(pygame.image.load('png/Idle (4).png'))
        self.spritesL.append(pygame.image.load('png/Idle (5).png'))
        self.spritesL.append(pygame.image.load('png/Idle (6).png'))
        self.spritesL.append(pygame.image.load('png/Idle (7).png'))
        self.spritesL.append(pygame.image.load('png/Idle (8).png'))
        self.spritesL.append(pygame.image.load('png/Idle (9).png'))
        self.spritesL.append(pygame.image.load('png/Idle (10).png'))

        self.current_sprite_idle = 0

        self.imageL = self.spritesL[self.current_sprite_idle]
        self.rect1 = self.imageL.get_rect()
        self.rect1.topleft = [pos_x, pos_y]

    def runL(self):
        self.runl_animation = True

    def run(self):
        self.run_animation = True

    def idle(self):
        self.idle_animation = True

    def update(self, speed):

        if self.run_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                'self.andar_animation = False'

        self.image = self.sprites[int(self.current_sprite)]

        if self.runl_animation:
            'self.img_with_flip = pygame.transform.flip(self.image, True, False)'

        if self.idle_animation:

            self.current_sprite_idle += speed
            if int(self.current_sprite_idle) >= len(self.spritesL):
                self.current_sprite_idle = 0
                'self.idle_animation = False'

        self.image = self.spritesL[int(self.current_sprite_idle)]


pygame.init()
clock = pygame.time.Clock()
altura, largura = 600, 600
tamanho_da_tela = altura, largura
screen = pygame.display.set_mode(tamanho_da_tela)
pygame.display.set_caption('Game')
color = 255, 255, 255
moving_sprites = pygame.sprite.Group()
player = Player(50, 50)
moving_sprites.add(player)

while True:
    pygame.sprite.Group().update(player)
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_d:
                player.run()

            if event.key == pygame.K_s:
                player.idle()

            if event.key == pygame.K_a:
                ' player.runL()'

    screen.fill(color)
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    'screen.blit(screen, (50 + 1 * 120, 100))'
    pygame.display.flip()
    clock.tick(60)
