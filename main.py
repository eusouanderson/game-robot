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
        self.image = self.spritesL[self.current_sprite_idle]
        self.rect1 = self.image.get_rect()
        self.rect1.topleft = [pos_x, pos_y]

        # --------------------------------------------------------------
        self.dead_animation = False
        self.spritesD = []
        self.spritesD.append(pygame.image.load('png/Dead (1).png'))
        self.spritesD.append(pygame.image.load('png/Dead (2).png'))
        self.spritesD.append(pygame.image.load('png/Dead (3).png'))
        self.spritesD.append(pygame.image.load('png/Dead (4).png'))
        self.spritesD.append(pygame.image.load('png/Dead (5).png'))
        self.spritesD.append(pygame.image.load('png/Dead (6).png'))
        self.spritesD.append(pygame.image.load('png/Dead (7).png'))
        self.spritesD.append(pygame.image.load('png/Dead (8).png'))
        self.spritesD.append(pygame.image.load('png/Dead (9).png'))
        self.spritesD.append(pygame.image.load('png/Dead (10).png'))

        self.current_sprite_dead = 0
        self.image = self.spritesD[self.current_sprite_dead]
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = [pos_x, pos_y]

        # ---------------------------------------------------------------
        self.jump_animation = False
        self.spritesJ = []
        self.spritesJ.append(pygame.image.load('png/Jump (1).png'))
        self.spritesJ.append(pygame.image.load('png/Jump (2).png'))
        self.spritesJ.append(pygame.image.load('png/Jump (3).png'))
        self.spritesJ.append(pygame.image.load('png/Jump (4).png'))
        self.spritesJ.append(pygame.image.load('png/Jump (5).png'))
        self.spritesJ.append(pygame.image.load('png/Jump (6).png'))
        self.spritesJ.append(pygame.image.load('png/Jump (7).png'))
        self.spritesJ.append(pygame.image.load('png/Jump (8).png'))
        self.spritesJ.append(pygame.image.load('png/Jump (9).png'))
        self.spritesJ.append(pygame.image.load('png/Jump (10).png'))


        self.current_sprite_jump = 0
        self.image = self.spritesJ[self.current_sprite_jump]
        self.rect3 = self.image.get_rect()
        self.rect3.topleft = [pos_x, pos_y]
        # --------------------------------------------------------------
        self.slide_animation = False
        self.spritesS = []
        self.spritesS.append(pygame.image.load('png/Slide (1).png'))
        self.spritesS.append(pygame.image.load('png/Slide (2).png'))
        self.spritesS.append(pygame.image.load('png/Slide (3).png'))
        self.spritesS.append(pygame.image.load('png/Slide (4).png'))
        self.spritesS.append(pygame.image.load('png/Slide (5).png'))
        self.spritesS.append(pygame.image.load('png/Slide (6).png'))
        self.spritesS.append(pygame.image.load('png/Slide (7).png'))
        self.spritesS.append(pygame.image.load('png/Slide (8).png'))
        self.spritesS.append(pygame.image.load('png/Slide (9).png'))
        self.spritesS.append(pygame.image.load('png/Slide (10).png'))

        self.current_sprite_slide = 0
        self.image = self.spritesS[self.current_sprite_slide]
        self.rect4 = self.image.get_rect()
        self.rect4.topleft = [pos_x, pos_y]

        # ---------------------------------------------------------------
        self.shoot_animation = False
        self.spritesShoot = []
        self.spritesShoot.append(pygame.image.load('png/Shoot (1).png'))
        self.spritesShoot.append(pygame.image.load('png/Shoot (2).png'))
        self.spritesShoot.append(pygame.image.load('png/Shoot (3).png'))
        self.spritesShoot.append(pygame.image.load('png/Shoot (4).png'))

        self.current_sprite_shoot = 0
        self.image = self.spritesShoot[self.current_sprite_shoot]
        self.rect5 = self.image.get_rect()
        self.rect5.topleft = [pos_x, pos_y]
        # -------------------------------------------------------------------
        self.melee_animation = False
        self.spritesMelee = []
        self.spritesMelee.append(pygame.image.load('png/Melee (1).png'))
        self.spritesMelee.append(pygame.image.load('png/Melee (2).png'))
        self.spritesMelee.append(pygame.image.load('png/Melee (3).png'))
        self.spritesMelee.append(pygame.image.load('png/Melee (4).png'))
        self.spritesMelee.append(pygame.image.load('png/Melee (5).png'))
        self.spritesMelee.append(pygame.image.load('png/Melee (6).png'))
        self.spritesMelee.append(pygame.image.load('png/Melee (7).png'))
        self.spritesMelee.append(pygame.image.load('png/Melee (8).png'))

        self.current_sprite_melee = 0
        self.image = self.spritesMelee[self.current_sprite_melee]
        self.rect6 = self.image.get_rect()
        self.rect6.topleft = [pos_x, pos_y]

    def melee(self):
        self.melee_animation = True

    def shoot(self):
        self.shoot_animation = True

    def slide(self):
        self.slide_animation = True

    def jump(self):
        self.jump_animation = True

    def dead(self):
        self.dead_animation = True

    def runL(self):
        self.runl_animation = True

    def run(self):
        self.run_animation = True

    def idle(self):
        self.idle_animation = True

    def update(self, speed):

        if self.idle_animation:
            self.current_sprite_idle += speed
            if int(self.current_sprite_idle) >= len(self.spritesL):
                self.current_sprite_idle = 0
                return
            self.image = self.spritesL[int(self.current_sprite_idle)]

        if self.run_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.run_animation = False

            self.image = self.sprites[int(self.current_sprite)]

        if self.dead_animation:
            self.current_sprite_dead += speed
            if int(self.current_sprite_dead) >= len(self.spritesD):
                self.current_sprite_dead = 0
                self.dead_animation = False

            self.image = self.spritesD[int(self.current_sprite_dead)]

        if self.jump_animation:
            self.current_sprite_jump += speed
            if int(self.current_sprite_jump) >= len(self.spritesJ):
                self.current_sprite_jump = 0
                self.jump_animation = False

            self.image = self.spritesJ[int(self.current_sprite_jump)]

        if self.slide_animation:
            self.current_sprite_slide += speed
            if int(self.current_sprite_slide) >= len(self.spritesS):
                self.current_sprite_slide = 0
                self.slide_animation = False
            self.image = self.spritesS[int(self.current_sprite_slide)]

        if self.shoot_animation:
            self.current_sprite_shoot += speed
            if int(self.current_sprite_shoot) >= len(self.spritesShoot):
                self.current_sprite_shoot = 0
                self.shoot_animation = False
            self.image = self.spritesShoot[int(self.current_sprite_shoot)]
            print(self.image.get_size())

        if self.melee_animation:
            self.current_sprite_melee += speed
            if int(self.current_sprite_melee) >= len(self.spritesMelee):
                self.current_sprite_melee = 0
                self.melee_animation = False
            self.image = self.spritesMelee[int(self.current_sprite_melee)]


pygame.init()
clock = pygame.time.Clock()
altura, largura = 600, 600
tamanho_da_tela = altura, largura
screen = pygame.display.set_mode(tamanho_da_tela)
pygame.display.set_caption('Game')
color = 255, 255, 255
moving_sprites = pygame.sprite.Group()

player = Player(50, 50)
image = pygame.transform.flip(screen, True, True)
moving_sprites.add(player)

while True:


    for event in pygame.event.get():
        player.idle()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:

            if pygame.key.get_pressed()[pygame.K_LSHIFT] and pygame.key.get_pressed()[pygame.K_d]:
                player.slide()

            if pygame.key.get_pressed()[pygame.K_s]:
                player.dead()

            if pygame.key.get_pressed()[pygame.K_a]:
                ' player.runL()'

            if pygame.key.get_pressed()[pygame.K_d]:
                player.run()

            if pygame.key.get_pressed()[pygame.K_SPACE]:
                player.jump()

            if pygame.key.get_pressed()[pygame.KMOD_CTRL]:
                player.slide()

            if pygame.key.get_pressed()[pygame.K_h]:
                player.shoot()

            if pygame.key.get_pressed()[pygame.K_f]:
                player.melee()

    screen.fill(color)
    moving_sprites.draw(screen)
    moving_sprites.update(0.25)
    screen.blit(screen, (10 * 120, 100))
    pygame.display.flip()
    clock.tick(60)
