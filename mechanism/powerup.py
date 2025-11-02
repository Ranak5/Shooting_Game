import pygame 
import random as r 

pygame.init()

#Powerup Path
Path1 = "assets\PNG\Power-ups\bolt_bronze.png"
Path2 = "assets\PNG\Power-ups\bold_silver.png"
Path3 = "assets\PNG\Power-ups\bolt_gold.png"

class Powerup(pygame.sprite.Sprite):
    def __init__(self,path,x,y,speed):
        self.path = path
        self.img = pygame.transform.scale(pygame.image.load(self.path).convert_alpha(),(25,25))
        self.rect = self.img.get_rect(center = (x,y))
        self.speed = speed 

    def update(self):
        self.rect.y += self.speed 
        
    def draw(self,surf):
        surf.blit(self.img,(self.rect))

class Bronze_Powerup(Powerup):
    def __init__(self,x,y):
        super().__init__("assets\\PNG\Power-ups\\bolt_bronze.png",x,y,speed = 5)

class Silver_Powerup(Powerup):
    def __init__(self,x,y):
        super().__init__("assets\\PNG\\Power-ups\\bold_silver.png",x,y,speed = 5)

class Gold_Powerup(Powerup):
    def __init__(self,x,y):
        super().__init__("assets\\PNG\\Power-ups\\bolt_gold.png",x,y,speed = 7)
