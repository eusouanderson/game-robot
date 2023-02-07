import sys, pygame
import pygame_menu
from random import randint


class Menu(pygame.sprite.Sprite):
    def __init__(self, pos_x=0, pos_y=0, tamL=100, tamA=550):
        super().__init__()

        difficult = pygame.image.load('png/Menu/difficult.png')
        level = pygame.image.load('png/Menu/level.png')
        level2 = pygame.image.load('png/Menu/level2.png')
        life = pygame.image.load('png/Menu/life.png')
        options = pygame.image.load('png/Menu/Options.png')
        paused = pygame.image.load('png/Menu/Paused.png')
        power = pygame.image.load('png/Menu/power.png')


        difficultLayout = []
        levelLayout = []
        level2Layout = []
        lifeLayout = []
        optionsLayout = []
        pausedLayout = []
        powerLayout = []

        levelLayout.append(level)
        level2Layout.append(level2)
        difficultLayout.append(difficult)
        lifeLayout.append(life)
        optionsLayout.append(options)
        pausedLayout.append(paused)
        powerLayout.append(power)

        menu_current = 0


        self.image = lifeLayout[menu_current]
        self.image = pygame.transform.scale(self.image, (tamA, tamL))
        self.rect = self.image.get_rect()

        self.rect.x = pos_x
        self.rect.y = pos_y


class Inimig(pygame.sprite.Sprite):
    def __init__(self, pos_x=1500, pos_y=550):
        super().__init__()

        self.run_animation = False
        self.runl_animation = False
        self.left_animation = False
        self.jumpl_animation = False
        self.idle_animation = False
        self.dead_animation = False
        self.jump_animation = False
        self.jump_melee_animation = False
        self.slide_animation = False
        self.NinjaThrow_animation = False
        self.shoot_animation = False
        self.melee_animation = False
        self.left_animation = False

        self.NinjaAttack = []
        self.NinjaClimb = []
        self.NinjaDead = []
        self.NinjaGlide = []
        self.NinjaIdle = []
        self.NinjaJump = []
        self.NinjaJumpAttack = []
        self.NinjaJumpThrow = []
        self.NinjaRun = []
        self.NinjaSlide = []
        self.NinjaThrow = []
        b = -1

        for r in range(0, 10):
            b += 1

            NinjaAttack = f'png/Inimig/Attack__00{b}.png'
            NinjaClimb = f'png/Inimig/Climb_00{b}.png'
            NinjaDead = f'png/Inimig/Dead__00{b}.png'
            NinjaGlide = f'png/Inimig/Glide_00{b}.png'
            NinjaIdle = f'png/Inimig/Idle__00{b}.png'
            NinjaJump = f'png/Inimig/Jump__00{b}.png'
            NinjaJumpAttack = f'png/Inimig/Jump_Attack__00{b}.png'
            NinjaJumpThrow = f'png/Inimig/Jump_Throw__00{b}.png'
            NinjaRun = f'png/Inimig/Run__00{b}.png'
            NinjaSlide = f'png/Inimig/Slide__00{b}.png'
            NinjaThrow = f'png/Inimig/Throw__00{b}.png'

            self.ninjaList = [
                NinjaAttack,
                NinjaClimb,
                NinjaDead,
                NinjaGlide,
                NinjaIdle,
                NinjaJump,
                NinjaJumpAttack,
                NinjaJumpThrow,
                NinjaRun,
                NinjaSlide,
                NinjaThrow,
            ]

            insert = self.ninjaList[0]
            self.NinjaAttack.append(pygame.image.load(insert))

            insert = self.ninjaList[1]
            self.NinjaClimb.append(pygame.image.load(insert))

            insert = self.ninjaList[2]
            self.NinjaDead.append(pygame.image.load(insert))

            insert = self.ninjaList[3]
            self.NinjaGlide.append(pygame.image.load(insert))

            insert = self.ninjaList[4]
            self.NinjaIdle.append(pygame.image.load(insert))

            insert = self.ninjaList[5]
            self.NinjaJump.append(pygame.image.load(insert))

            insert = self.ninjaList[6]
            self.NinjaJumpAttack.append(pygame.image.load(insert))

            insert = self.ninjaList[7]
            self.NinjaJumpThrow.append(pygame.image.load(insert))

            insert = self.ninjaList[8]
            self.NinjaRun.append(pygame.image.load(insert))

            insert = self.ninjaList[9]
            self.NinjaSlide.append(pygame.image.load(insert))

            insert = self.ninjaList[10]
            self.NinjaThrow.append(pygame.image.load(insert))

        self.current_sprite = 0
        self.current_sprite_idle = 0
        self.current_sprite_dead = 0
        self.current_sprite_jump = 0
        self.current_sprite_jumpMelee = 0
        self.current_sprite_slide = 0
        self.current_sprite_shoot = 0
        self.current_sprite_melee = 0
        self.image = self.NinjaAttack[self.current_sprite]
        self.image = pygame.transform.scale(self.image, (150, 150))
        self.rect = self.image.get_rect()

        self.rect.x = pos_x
        self.rect.y = pos_y

    def melee(self):
        self.melee_animation = True

    def runshoot(self):
        self.left_animation = False
        self.runshoot_animation = True
        self.rect.right += 10

    def runshootL(self):
        self.left_animation = False
        self.runshoot_animation = True
        self.rect.right -= 10

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
        self.rect.right -= 5

    def run(self):
        self.run_animation = True
        self.left_animation = False
        self.rect.right += 5

    def idle(self):
        self.idle_animation = True

    # Robot Functions ---------------------------------

    def rundead(self):

        global lifepoint

        if player.rect.right <= rival.rect.right:
            rival.runL()

        if player.rect.right >= rival.rect.right:
            rival.run()

        if self.rect.colliderect(player.rect):
            rival.shoot()
            lifepoint -= 1

    def update(self, speed):

        global lifepoint1
        pygame.draw.rect(screen, color, pygame.Rect(player.rect), 2, 3)

        left = False

        if self.left_animation:
            left = True

        if self.idle_animation:
            self.current_sprite_idle += speed
            if int(self.current_sprite_idle) >= len(self.NinjaIdle):
                self.current_sprite_idle = 0
            self.image = self.NinjaIdle[int(self.current_sprite_idle)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.run_animation:
            self.current_sprite += speed

            if int(self.current_sprite) >= len(self.NinjaRun):
                self.current_sprite = 0
                self.run_animation = False
            self.image = self.NinjaRun[int(self.current_sprite)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.jump_animation:
            self.current_sprite_jump += speed

            if int(self.current_sprite_jump) >= len(self.NinjaJump):
                self.current_sprite_jump = 0
                self.jump_animation = False
            self.image = self.NinjaJump[int(self.current_sprite_jump)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.NinjaThrow_animation:
            self.current_sprite += speed
            if int(self.current_sprite) >= len(self.NinjaThrow):
                self.current_sprite = 0
                self.runshoot_animation = False
            self.image = self.NinjaThrow[int(self.current_sprite)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.dead_animation:
            self.current_sprite_dead += speed
            if int(self.current_sprite_dead) >= len(self.NinjaDead):
                self.current_sprite_dead = 0
                self.dead_animation = False
            self.image = self.NinjaDead[int(self.current_sprite_dead)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.jumpl_animation:
            self.current_sprite_jump += speed
            if int(self.current_sprite_jump) >= len(self.NinjaJump):
                self.current_sprite_jump = 0
                self.jump_animation = False
            self.image = self.NinjaJump[int(self.current_sprite_jump)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.slide_animation:
            self.current_sprite_slide += speed
            if int(self.current_sprite_slide) >= len(self.NinjaSlide):
                self.current_sprite_slide = 0
                self.slide_animation = False
            self.image = self.NinjaSlide[int(self.current_sprite_slide)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.shoot_animation:
            self.current_sprite_shoot += speed
            if int(self.current_sprite_shoot) >= len(self.NinjaAttack):
                self.current_sprite_shoot = 0
                self.shoot_animation = False
            self.image = self.NinjaAttack[int(self.current_sprite_shoot)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.melee_animation:
            self.current_sprite_melee += speed
            if int(self.current_sprite_melee) >= len(self.NinjaJumpAttack):
                self.current_sprite_melee = 0
                self.melee_animation = False
            self.image = self.NinjaJumpAttack[int(self.current_sprite_melee)]
            self.image = pygame.transform.flip(self.image, left, False)
            self.meleeRect = player.rect

        if self.jump_melee_animation:
            self.current_sprite_jumpMelee += speed
            if int(self.current_sprite_jumpMelee) >= len(self.NinjaJumpThrow):
                self.current_sprite_jumpMelee = 0
                self.jump_melee_animation = False
            self.image = self.NinjaJumpThrow[
                int(self.current_sprite_jumpMelee)
            ]
            self.image = pygame.transform.flip(self.image, left, False)
        self.image = pygame.transform.scale(self.image, (150, 150))


class Objects(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()

        global bullet_rect

        self.bullet_animation = False
        self.spritesBullet = []
        b = 0
        for c in range(b, 3):
            b += 1
            bulletPath = f'Bullet_00{b}.png'
            self.spritesBullet.append(
                pygame.image.load(f'png/Objects/{bulletPath}')
            )

        self.current_sprite_bullet = 0
        self.left_animation = False
        self.image = self.spritesBullet[self.current_sprite_bullet]
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()

        self.rect.x = pos_x + 100
        self.rect.y = pos_y + 50
        if pos_player:
            self.rect.x = pos_x - 10



    def bullet(self):
        moving_sprites.add(objects)

    def update(self, speed):

        global largura, bullet_rect, lifepoint1

        bullet_rect = self.rect
        pygame.draw.rect(screen, color, pygame.Rect(bullet_rect), 2, 3)

        # Objetcs colliderects

        if bullet_rect.colliderect(rival.rect):


            lifepoint1 -= 1
            if pos_player:
                rival.rect.right -= 5
            else:
                rival.rect.right += 5

            if lifepoint1 <= 0:
                sound.load(dano)
                sound.play()
                rival.dead()
                rival.rect.right = randint(0, largura)
                lifepoint1 = 500

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
    def __init__(self, pos_x=0, pos_y=550):
        super().__init__()

        global pos_player, left

        self.run_animation = False
        self.runl_animation = False
        self.left_animation = False
        self.jumpl_animation = False
        self.idle_animation = False
        self.dead_animation = False
        self.jump_animation = False
        self.jump_melee_animation = False
        self.slide_animation = False
        self.runshoot_animation = False
        self.shoot_animation = False
        self.melee_animation = False
        self.left_animation = False

        self.sprites = []
        self.spritesD = []
        self.spritesL = []
        self.spritesJ = []
        self.spritesJM = []
        self.spritesJS = []
        self.spritesMelee = []
        self.spritesRS = []
        self.spritesShoot = []
        self.spritesSlide = []
        self.spritesS = []
        b = 1

        for r in range(0, 10):

            self.white = 'WhiteRobot'
            self.black = 'BlackRobot'
            self.pink = 'PinkRobot'
            self.robot_select = self.pink
            robot_Run = f'png/Players/{self.robot_select}/Run ({b}).png'
            robot_Dead = f'png/Players/{self.robot_select}/Dead ({b}).png'
            robot_Idle = f'png/Players/{self.robot_select}/Idle ({b}).png'
            robot_Jump = f'png/Players/{self.robot_select}/Jump ({b}).png'
            robot_Jump_Melee = (
                f'png/Players/{self.robot_select}/JumpMelee ({b}).png'
            )
            robot_Jump_Shoot = (
                f'png/Players/{self.robot_select}/JumpShoot ({b}).png'
            )
            robot_Melee = f'png/Players/{self.robot_select}/Melee ({b}).png'
            robot_Run_Shoot = (
                f'png/Players/{self.robot_select}/RunShoot ({b}).png'
            )
            robot_Shoot = f'png/Players/{self.robot_select}/Shoot ({b}).png'
            robot_Slide = f'png/Players/{self.robot_select}/Slide ({b}).png'

            self.robotList = [
                robot_Run,  # 0
                robot_Dead,  # 1
                robot_Idle,  # 2
                robot_Jump,  # 3
                robot_Jump_Melee,  # 4
                robot_Jump_Shoot,  # 5
                robot_Melee,  # 6
                robot_Run_Shoot,  # 7
                robot_Shoot,  # 8
                robot_Slide,  # 9
            ]

            b += 1

            # Run
            insert = self.robotList[0]
            self.sprites.append(pygame.image.load(insert))
            # Dead
            insert = self.robotList[1]
            self.spritesD.append(pygame.image.load(insert))
            # Idle
            insert = self.robotList[2]
            self.spritesL.append(pygame.image.load(insert))
            # Jump
            insert = self.robotList[3]
            self.spritesJ.append(pygame.image.load(insert))
            # JumpMelee
            insert = self.robotList[4]
            self.spritesJM.append(pygame.image.load(insert))
            # JumpShoot
            insert = self.robotList[5]
            self.spritesJS.append(pygame.image.load(insert))
            # Melee
            insert = self.robotList[6]
            self.spritesMelee.append(pygame.image.load(insert))
            # Run_Shoot
            insert = self.robotList[7]
            self.spritesRS.append(pygame.image.load(insert))
            # Shoot
            insert = self.robotList[8]
            self.spritesShoot.append(pygame.image.load(insert))
            # Slide
            insert = self.robotList[9]
            self.spritesSlide.append(pygame.image.load(insert))

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

    def melee(self):
        self.melee_animation = True

    def runshoot(self):
        self.left_animation = False
        self.runshoot_animation = True
        self.rect.right += 10

    def runshootL(self):
        self.left_animation = False
        self.runshoot_animation = True
        self.rect.right -= 10

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
        for c in self.sprites:
            self.rect.right -= 5

    def vt(self, vt):
        self.rect.left = vt

    def run(self):
        self.run_animation = True
        self.left_animation = False
        for c in self.sprites:
            self.rect.right += 5

    def idle(self):
        self.idle_animation = True

    def update(self, speed):

        global pos_player, lifepoint1
        pygame.draw.rect(screen, color, pygame.Rect(player.rect), 2, 3)

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
            pos_player = left
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.run_animation = False
            self.image = self.sprites[int(self.current_sprite)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.jump_animation:
            self.current_sprite_jump += speed
            pos_player = left
            if int(self.current_sprite_jump) >= len(self.spritesJ):
                self.current_sprite_jump = 0
                self.jump_animation = False
            self.image = self.spritesJ[int(self.current_sprite_jump)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.runshoot_animation:
            self.current_sprite += speed
            pos_player = left
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.runshoot_animation = False
            self.image = self.spritesRS[int(self.current_sprite)]
            self.image = pygame.transform.flip(self.image, left, False)

        if self.dead_animation:
            self.current_sprite_dead += speed
            if int(self.current_sprite_dead) >= len(self.spritesD):
                self.current_sprite_dead = 0
                self.dead_animation = False
            self.image = self.spritesD[int(self.current_sprite_dead)]
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
            if int(self.current_sprite_slide) >= len(self.spritesSlide):
                self.current_sprite_slide = 0
                self.slide_animation = False
            self.image = self.spritesSlide[int(self.current_sprite_slide)]
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
            self.meleeRect = self.image.get_rect()
            if self.meleeRect.colliderect(rival.rect):
                sound.load(meleesound)
                sound.play()
                lifepoint1 -= 1

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
def set_difficulty(value, difficulty):
    # Do the job here !
    pass

def start_the_game():
    # Do the job here !
    pass

menu = pygame_menu.Menu('Welcome', 400, 300,
                       theme=pygame_menu.themes.THEME_BLUE)

menu.add.text_input('Name :', default='John Doe')
menu.add.selector('Difficulty :', [('Hard', 1), ('Easy', 2)], onchange=set_difficulty)
menu.add.button('Play', start_the_game)
menu.add.button('Quit', pygame_menu.events.EXIT)

while True:
    txttela = fontesys.render(f'{lifepoint}', 100, (color))
    txttela1 = fontesys.render(f'{lifepoint1}', 100, (color))
    objects = Objects(player.rect[0], player.rect[1])

    player.idle()
    rival.idle()
    rival.rundead()

    if lifepoint1 == 0:
        player.dead()
        sound.load(gameover)
        sound.play()

    if lifepoint == 0:
        player.dead()
        sound.load(gameover)
        sound.play()
        rival.idle()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        # ------------------------ CONTROL -------------------
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

            if control[pygame.K_h]:
                player.runshoot()
                objects.bullet()

            if control[pygame.K_a]:
                player.runL()
                objects.bullet()

            if control[pygame.K_d]:
                player.run()
                if control[pygame.K_h]:
                    player.runshoot()
                    objects.bullet()

            if control[pygame.K_SPACE]:
                player.jump()

            if control[pygame.K_f]:
                player.melee()

    if player.rect.right >= largura:
        player.rect.right = largura
        back_pos = 1, 0

    if player.rect.right <= largura - largura:
        player.rect.right = 90
        back_pos = -1, 0

    moving_sprites.update(0.25)
    screen.blit(back, (back_pos))

    pygame.draw.rect(screen, colorRed, [50, 17, lifepoint - 100, 40])
    bar = pygame.draw.rect(screen, colorRed, [550, 17, lifepoint1 - 100, 40])
    moving_sprites.draw(screen)

    screen.blit(txttela, [0, 0])
    screen.blit(txttela1, [largura - 40, 0])

    clock.tick(60)
    pygame.display.update()
