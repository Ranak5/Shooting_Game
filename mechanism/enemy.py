import random as r 
import pygame 

from mechanism.enemy_bullet import Enemy_1
from mechanism.enemy_bullet import Enemy_2
from mechanism.enemy_bullet import Enemy_3
from mechanism.enemy_bullet import Enemy_4

pygame.init()
pygame.mixer.init()

class Sound():
    # Sound effects
    def __init__(self,path):
        self.sound = pygame.mixer.Sound(path)
        self.sound.set_volume(0.5)

    def play(self):
        self.sound.play()

fire_sound = Sound("assets\Bonus\sfx_laser2.ogg")

class BaseClass(pygame.sprite.Sprite):

    def __init__(self,x,y,path,speed,fire_sound = Sound("assets\Bonus\sfx_laser2.ogg")):
        super().__init__()
        self.path = path 
        self.enemies = pygame.transform.scale(pygame.image.load(self.path).convert_alpha(),(50,50))
        self.rect = self.enemies.get_rect(center = (x,y))
        self.speed = speed
        self.bullet_list = []
        self.sound = fire_sound

class Enemy1(BaseClass):

    def __init__(self,x,y):
        super().__init__(x,y,"assets\PNG\Enemies\enemyBlack1.png",speed = 4.7)
    
    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 640:  # Use .top for better accuracy
            self.rect.y = -100  # Reset above screen
            self.rect.x = r.randint(25,190)  # Random horizontal position

        if r.randint(0,150) < 2:
            enemy_bullet = Enemy_1(self.rect.centerx,self.rect.bottom)
            self.bullet_list.append(enemy_bullet)
            self.sound.play()

        #Update Bullet 
        for bullet in self.bullet_list:
            bullet.update()

        #Remove Off Screen Bullets
        self.bullet_list = [b for b in self.bullet_list if b.rect.top < 640]

    def surface(self,surf):

        surf.blit(self.enemies,(self.rect))

        for bullet in self.bullet_list:
            bullet.Surface(surf)


class Enemy2(BaseClass):

    def __init__(self,x,y):
        super().__init__(x,y,"assets\PNG\Enemies\enemyBlue5.png",speed = 4.3)

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 640:  # Use .top for better accuracy
            self.rect.y = -100  # Reset above screen
            self.rect.x = r.randint(205,376)  # Random horizontal position

        if r.randint(0,150) < 2:
            enemy_bullet = Enemy_2(self.rect.centerx,self.rect.bottom)
            self.bullet_list.append(enemy_bullet)
            self.sound.play()

        #Update Bullet 
        for bullet in self.bullet_list:
            bullet.update()

        #Remove Off Screen Bullets
        self.bullet_list = [b for b in self.bullet_list if b.rect.top < 640]

    def surface(self,surf):

        surf.blit(self.enemies,(self.rect))

        for bullet in self.bullet_list:
            bullet.Surface(surf)


class Enemy3(BaseClass):

    def __init__(self,x,y):
        super().__init__(x,y,"assets\PNG\Enemies\enemyGreen2.png",speed = 5)
    
    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 640:  # Use .top for better accuracy
            self.rect.y = -100  # Reset above screen
            self.rect.x = r.randint(405,570)  # Random horizontal position

        if r.randint(0,150) < 2:
            enemy_bullet = Enemy_3(self.rect.centerx,self.rect.bottom)
            self.bullet_list.append(enemy_bullet)
            self.sound.play()

        #Update Bullet 
        for bullet in self.bullet_list:
            bullet.update()

        #Remove Off Screen Bullets
        self.bullet_list = [b for b in self.bullet_list if b.rect.top < 640]

    def surface(self,surf):

        surf.blit(self.enemies,(self.rect))

        for bullet in self.bullet_list:
            bullet.Surface(surf)


class Enemy4(BaseClass):

    def __init__(self,x,y):
        super().__init__(x,y,"assets\PNG\Enemies\enemyRed5.png",speed = 5.6)

    def update(self):
        self.rect.y += self.speed

        if self.rect.top > 640:  # Use .top for better accuracy
            self.rect.y = -100  # Reset above screen
            self.rect.x = r.randint(583,760)  # Random horizontal position

        if r.randint(0,150) < 2:
            enemy_bullet = Enemy_4(self.rect.centerx,self.rect.bottom)
            self.bullet_list.append(enemy_bullet)
            self.sound.play()

        #Update Bullet 
        for bullet in self.bullet_list:
            bullet.update()

        #Remove Off Screen Bullets
        self.bullet_list = [b for b in self.bullet_list if b.rect.top < 640]

    def surface(self,surf):

        surf.blit(self.enemies,(self.rect))

        for bullet in self.bullet_list:
            bullet.Surface(surf)
