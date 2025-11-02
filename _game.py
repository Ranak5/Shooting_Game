import pygame
import random as r
import sys

from mechanism.player1 import Player
from mechanism.enemy import Enemy1, Enemy2, Enemy3, Enemy4
from mechanism.bullet import Bullet
from mechanism.powerup import Bronze_Powerup
from mechanism.powerup import Silver_Powerup
from mechanism.powerup import Gold_Powerup

pygame.init()
pygame.mixer.init()

# Background Music  
Back_Path = "assets\\Bonus\\background.mp3"
pygame.mixer.music.load(Back_Path)

#Background Music play 
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.5)

# Screen of the Display
screen = pygame.display.set_mode((800, 640))

# Set Caption
pygame.display.set_caption("Shooting Game")

# Set Icon
icon = pygame.image.load('assets\PNG\playerShip1_blue.png')
pygame.display.set_icon(icon)

# Set FPS
FPS = 45
f = pygame.time.Clock()

# Background Image
Background = "assets\Backgrounds\darkPurple.png"
Back_Img = pygame.transform.scale(pygame.image.load(Background), (800, 640))

# Player
player = Player(600, 610)

enemy_types = [Enemy1, Enemy2, Enemy3, Enemy4]

# Create initial enemy list
enemies = [
    Enemy1(r.randint(25, 184), -100),
    Enemy2(r.randint(205, 387), -100),
    Enemy3(r.randint(403, 583), -100),
    Enemy4(r.randint(600, 760), -100)
]

#Powerups
powerups = [
            Bronze_Powerup(r.randint(50,760),r.randint(50,400)),
            Silver_Powerup(r.randint(50,760),r.randint(50,400)),
            Gold_Powerup(r.randint(50,760),r.randint(50,400))
        ]

# Bullet
bullet_list = []

# Font render for Game Over
font = pygame.font.Font(None, 64)
display = font.render("GAME OVER", True, (255, 250, 0))

# Lives
life_score = 10
life_font = pygame.font.Font(None, 48)
display_life = life_font.render(f"Life : {life_score} ", True, (255, 255, 0))

# Score
point_score = 0
score_font = pygame.font.Font(None, 48)
display_score = score_font.render(f"Score : {point_score} ", True, (255, 255, 0))

# Sound effects
sound_Path = "assets\Bonus\sfx_laser2.ogg"
sound = pygame.mixer.Sound(sound_Path)
sound.set_volume(0.5) # Sound volume set from 0.0 to 1.0 

#Explosion sound 
explosion_path = "assets\Bonus\explosion.mp3"
explosion = pygame.mixer.Sound(explosion_path)

# Powerup Collecting sound 
powerup_collide_path = "assets\\Bonus\\powerup_sound.mp3"
power_up = pygame.mixer.Sound(powerup_collide_path)
power_up.set_volume(1.0)

while True:
    # Screen Color and Background
    screen.fill((135, 206, 235))
    screen.blit(Back_Img, (0, 0))

    player_hit_this_frame = False

    for power in powerups:
        power.update()
        power.draw(screen)

    if r.randint(0,2048) < 5:
        
        powerup_list = r.choice([Bronze_Powerup,Silver_Powerup,Gold_Powerup])
        powerup = powerup_list(r.randint(50,760),r.randint(50,400))
        powerups.append(powerup)

    # UI Display
    screen.blit(display_life, (0, 0))
    screen.blit(display_score, (605, 0))

    # Player
    player._input()
    player.surface(screen)
    player.update()

    # Enemies
    for enemy in enemies:
        enemy.update()
        enemy.surface(screen)

    # Enemy Bullet hitting player
    for enemy in enemies:
        for bullet in enemy.bullet_list:
            if bullet.rect.colliderect(player.rect):
                life_score -= 1
                if life_score == 0:
                    screen.blit(display, (262, 280))
                    pygame.display.update()
                    pygame.time.delay(2000)
                    pygame.quit()
                    sys.exit()
                else:
                    display_life = life_font.render(f"Life : {life_score} ", True, (255, 255, 0))
                    enemy.bullet_list.remove(bullet)

    # Powerups colliding player 
    for power in powerups[:]:
        if power.rect.colliderect(player.rect):
            power_up.play()
            if isinstance(power,Bronze_Powerup):
                life_score += 1
                display_life = life_font.render(f"Life : {life_score} ", True, (255, 255, 0))
                pygame.display.update()
                powerups.remove(power)

            if isinstance(power,Silver_Powerup):
                life_score += 2
                display_life = life_font.render(f"Life : {life_score} ", True, (255, 255, 0))
                pygame.display.update()
                powerups.remove(power)

            if isinstance(power,Gold_Powerup):
                life_score += 3
                display_life = life_font.render(f"Life : {life_score} ", True, (255, 255, 0))
                pygame.display.update()
                powerups.remove(power)

    # Player Bullet hitting enemy
    for bullet in bullet_list[:]:
        for enemy in enemies[:]:
            if bullet.rect.colliderect(enemy.rect):
                point_score += 10
                explosion.play() # Plays the sound 
                explosion.fadeout(1000) # Plays for only 1 second
                display_score = score_font.render(f"Score : {point_score} ", True, (255, 255, 0))
                bullet_list.remove(bullet)
                enemies.remove(enemy)
                enemy = type(enemy)
                position = [
                (r.randint(25, 184), -100),
                (r.randint(205, 387), -100),
                (r.randint(403, 583), -100),
                (r.randint(600, 760), -100) ]

                enemy_position = r.choice(position)
                enemies.append(enemy(*enemy_position))
                break

    # Enemy Collides with player 
    for enemy in enemies[:]:
        if enemy.rect.colliderect(player.rect) and not player_hit_this_frame:
            life_score -= 3
            explosion.play() # Plays the sound 
            explosion.fadeout(1000) # Plays for only 1 second

            if life_score  != 0:
                display_life = life_font.render(f"Life : {life_score} ", True, (255, 255, 0))
                player_hit_this_frame = True
                enemies.remove(enemy)
                enemy = type(enemy)
                position = [
                (r.randint(25, 184), -100),
                (r.randint(205, 387), -100),
                (r.randint(403, 583), -100),
                (r.randint(600, 760), -100) ]
                enemy_position = r.choice(position)
                enemies.append(enemy(*enemy_position))
                pygame.display.update()

            if life_score <= 0:
                display_life = life_font.render(f"Life : {life_score} ", True, (255, 255, 0))
                screen.blit(display,(258,280))
                pygame.display.update()
                pygame.time.delay(2000)
                pygame.quit()
                sys.exit()

    # Events
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(player.rect.centerx, player.rect.top)
                bullet_list.append(bullet)
                sound.play()
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Bullets
    for bullet in bullet_list:
        bullet.update()
        bullet.surface(screen)

    # FPS
    f.tick(FPS)

    # Update Screen
    pygame.display.update()