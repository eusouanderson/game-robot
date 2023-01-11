import sys, pygame


class Objects(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        global objects_rect

        self.bullet_animation = False
        self.spritesBullet = []
        self.spritesBullet.append(
            pygame.image.load('png/Objects/Bullet_000.png')
        )
        self.spritesBullet.append(
            pygame.image.load('png/Objects/Bullet_001.png')
        )
        self.spritesBullet.append(
            pygame.image.load('png/Objects/Bullet_002.png')
        )
        self.spritesBullet.append(
            pygame.image.load('png/Objects/Bullet_003.png')
        )
        self.spritesBullet.append(
            pygame.image.load('png/Objects/Bullet_004.png')
        )

        self.current_sprite_bullet = 0
        self.left_animation = False
        self.image = self.spritesBullet[self.current_sprite_bullet]
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    def bullet(self):
        self.bullet_animation = True
        moving_sprites.add(objects)

    def update(self, speed):

        global largura

        self.objectsrect = self.rect.right

        if pos_player:
            self.rect.right -= 10

        if pos_player == False:
            self.rect.right += 10

        if self.rect.x <= 0:
            Objects.kill(self)
        if self.rect.x >= largura:
            Objects.kill(self)

            self.current_sprite_bullet += speed
            if int(self.current_sprite_bullet) >= len(self.spritesBullet):
                self.current_sprite_bullet = 1

        self.image = self.spritesBullet[int(self.current_sprite_bullet)]
        self.image = pygame.transform.flip(self.image, pos_player, False)
        self.image = pygame.transform.scale(self.image, (50, 50))


class Player(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        global pos_player

        self.run_animation = False
        self.runl_animation = False
        self.left_animation = False
        self.jumpl_animation = False
        self.idle_animation = False
        self.dead_animation = False
        self.jump_animation = False
        self.jump_melee_animation = False
        self.slide_animation = False
        self.shoot_animation = False
        self.melee_animation = False
        self.left_animation = False

        self.sprites = []
        self.spritesL = []
        self.spritesD = []
        self.spritesJ = []
        self.spritesJM = []
        self.spritesS = []
        self.spritesShoot = []
        self.spritesMelee = []
        b = 1

        for r in range(0, 9):

            # --------------Ninja-------------------------

            ninja_Attack = f'png/Attack__00{b}.png'
            ninja_Climb = f'png/Climb_00{b}.png'
            ninja_Glide = f'png/Glide_00{b}.png'
            ninja_Idle = f'png/Idle__00{b}.png'
            ninja_Dead = f'png/Dead__00{b}.png'
            ninja_Jump = f'png/Jump__00{b}.png'
            ninja_Jump_Attack = f'png/Jump_Attack__00{b}.png'
            ninja_Jump_Throw = f'png/Jump_Throw__00{b}.png'
            ninja_Run = f'png/Run__00{b}.png'
            ninja_Slide = f'png/Slide__00{b}.png'
            ninja_Throw = f'png/Throw__00{b}.png'

            self.ninjaList = [
                ninja_Run,
                ninja_Dead,
                ninja_Idle,
                ninja_Jump,
                ninja_Jump_Attack,
                ninja_Jump_Throw,
                ninja_Attack,
                ninja_Climb,
                ninja_Glide,
                ninja_Throw,
                ninja_Slide,

            ]

            robot_Run = f'png/Run ({b}).png'
            robot_Dead = f'png/Dead ({b}).png'
            robot_Idle = f'png/Idle ({b}).png'
            robot_Jump = f'png/Jump ({b}).png'
            robot_Jump_Melee = f'png/JumpMelee ({b}).png'
            robot_Jump_Shoot = f'png/JumpShoot ({b}).png'
            robot_Melee = f'png/Melee ({b}).png'
            robot_Run_Shoot = f'png/RunShoot ({b}).png'
            robot_Shoot = f'png/Shoot ({b}).png'
            robot_Slide = f'png/Slide ({b}).png'

            self.robotList = [
                robot_Run,#0
                robot_Dead,#1
                robot_Idle,#2
                robot_Jump,#3
                robot_Jump_Melee,#4
                robot_Jump_Shoot,#5
                robot_Melee,#6
                robot_Run_Shoot,#7
                robot_Shoot,#8
                robot_Slide,#9
            ]
            playerSelect = False
            b += 1
            # Run
            insert = self.alternat(r=playerSelect, value=0)
            self.sprites.append(pygame.image.load(insert))
            # Idle
            insert = self.alternat(r=playerSelect, value=2)
            self.spritesL.append(pygame.image.load(insert))
            # Dead
            insert = self.alternat(r=playerSelect, value=1)
            self.spritesD.append(pygame.image.load(insert))
            # Jump
            insert = self.alternat(r=playerSelect, value=3)
            self.spritesJ.append(pygame.image.load(insert))
            #JumpMelee
            insert = self.alternat(r=playerSelect, value=4)
            self.spritesJM.append(pygame.image.load(insert))
            #Slide
            insert = self.alternat(r=playerSelect, value=9)
            self.spritesS.append(pygame.image.load(insert))
            #Shoot
            insert = self.alternat(r=playerSelect, value=7)
            self.spritesShoot.append(pygame.image.load(insert))
            # Melee
            insert = self.alternat(r=playerSelect, value=6)
            self.spritesMelee.append(pygame.image.load(insert))

        self.current_sprite = 0
        self.current_sprite_idle = 0
        self.current_sprite_dead = 0
        self.current_sprite_jump = 0
        self.current_sprite_jumpMelee = 0
        self.current_sprite_slide = 0
        self.current_sprite_shoot = 0
        self.current_sprite_melee = 0
        self.image = self.sprites[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

        pos_player = False
        self.rect.x = pos_x
        self.rect.y = pos_y
    def alternat(self,r=False, value=0):

        if r:
            r = self.robotList[value]
            return r
        else:
            r = self.ninjaList[value]
            return r


    def melee(self):
        self.melee_animation = True

    def shoot(self):
        self.shoot_animation = True

    def slide(self):
        self.left_animation = False
        self.slide_animation = True
        self.rect.right += 9

    def jumpL(self):
        self.jump_animation = True
        self.left_animation = True

    def jump(self):
        self.jump_animation = True
        self.left_animation = False

    def jumpMelee(self):
        self.current_sprite_jumpMelee = True
        self.rect.right += 50
        self.left_animation = False

    def dead(self):
        self.left_animation = False
        self.dead_animation = True

    def runL(self):
        self.run_animation = True
        self.left_animation = True
        self.rect.right -= 50

    def vt(self, vt):
        self.rect.left = vt

    def run(self):
        self.run_animation = True
        self.left_animation = False
        passos = 0
        if self.run_animation is True:
            for p in self.sprites:
                passos += 5
            self.rect.right += passos

    def idle(self):
        self.idle_animation = True

    def update(self, speed):

        global pos_player

        left = False

        if self.left_animation:
            left = True

        if self.idle_animation:
            self.current_sprite_idle += speed
            if int(self.current_sprite_idle) >= len(self.spritesL):
                self.current_sprite_idle = 0
            self.image = self.spritesL[int(self.current_sprite_idle)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.run_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.run_animation = False
                pos_player = left
            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.dead_animation:
            self.current_sprite_dead += speed
            if int(self.current_sprite_dead) >= len(self.spritesD):
                self.current_sprite_dead = 0
                self.dead_animation = False
            self.image = self.spritesD[int(self.current_sprite_dead)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.jump_animation:
            self.current_sprite_jump += speed
            if int(self.current_sprite_jump) >= len(self.spritesJ):
                self.current_sprite_jump = 0
                self.jump_animation = False
            self.image = self.spritesJ[int(self.current_sprite_jump)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.jumpl_animation:
            self.current_sprite_jump += speed
            if int(self.current_sprite_jump) >= len(self.spritesJ):
                self.current_sprite_jump = 0
                self.jump_animation = False
            self.image = self.spritesJ[int(self.current_sprite_jump)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.slide_animation:
            self.current_sprite_slide += speed
            if int(self.current_sprite_slide) >= len(self.spritesS):
                self.current_sprite_slide = 0
                self.slide_animation = False
            self.image = self.spritesS[int(self.current_sprite_slide)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.shoot_animation:
            self.current_sprite_shoot += speed
            if int(self.current_sprite_shoot) >= len(self.spritesShoot):
                self.current_sprite_shoot = 0
                self.shoot_animation = False
            self.image = self.spritesShoot[int(self.current_sprite_shoot)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.melee_animation:
            self.current_sprite_melee += speed
            if int(self.current_sprite_melee) >= len(self.spritesMelee):
                self.current_sprite_melee = 0
                self.melee_animation = False
            self.image = self.spritesMelee[int(self.current_sprite_melee)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.jump_melee_animation:
            self.current_sprite_jumpMelee += speed
            if int(self.current_sprite_jumpMelee) >= len(
                self.current_sprite_jumpMelee
            ):
                self.current_sprite_jumpMelee = 0
                self.jump_melee_animation = False
            self.image = self.spritesJM[int(self.current_sprite_jumpMelee)]
            self.image = pygame.transform.flip(self.image, left, False)
        self.image = pygame.transform.scale(self.image, (150, 150))


pygame.init()

clock = pygame.time.Clock()
largura, altura = 1000, 768
tamanho_da_tela = largura, altura
screen = pygame.display.set_mode(tamanho_da_tela)
back = pygame.image.load('png/back.jpg')
life = pygame.Rect(0, 0, 10, 10)
back = pygame.transform.scale(back, (1360, 768))
pygame.display.set_caption('Game Robot')

color = 255, 255, 255
colorRed = 255, 0, 0
moving_sprites = pygame.sprite.Group()
player = Player(0, 550)

moving_sprites.add(player)
lifepoint = 450


while True:

    posy = player.rect[1]
    posx = player.rect[0]

    objects = Objects(posx, posy)
    if not objects.rect.colliderect(player.rect):
        lifepoint -= 1
        if lifepoint == 0:
            player.dead()

    for event in pygame.event.get():
        player.idle()
        player.idle()

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            control = pygame.key.get_pressed()
            if (
                control[pygame.K_LSHIFT]
                and control[pygame.K_d]
                or control[pygame.K_a]
                and control[pygame.K_LSHIFT]
            ):
                player.slide()

            if control[pygame.K_s]:
                player.dead()

            if control[pygame.K_a] and control[pygame.K_SPACE]:
                player.jumpL()

            if control[pygame.K_d] and control[pygame.K_SPACE]:
                player.jump()

            if control[pygame.K_g]:
                player.alternat(r=True, value=2)
                print('Eaeae')

            if control[pygame.K_a]:
                player.runL()

            if control[pygame.K_d]:
                player.run()

            if control[pygame.K_SPACE]:
                ...

            if control[pygame.K_h]:
                player.shoot()
                objects.bullet()

            if control[pygame.K_f]:
                player.melee()

        if player.rect.right >= largura:
            player.rect.right = largura

        if player.rect.right <= largura - largura:
            player.rect.right = 90
        if back.get_rect() == 0:
            ...

    screen.blit(back, (0, 0))
    moving_sprites.draw(screen)
    pygame.draw.rect(screen, colorRed, [0, 0, lifepoint, 50])
    moving_sprites.update(0.25)
    clock.tick(60)
    pygame.display.update()
