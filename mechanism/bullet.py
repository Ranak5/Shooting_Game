import pygame 

pygame.init()

#Bullet Path
Laser_Path = "assets\PNG\Lasers\laserBlue16.png"

class Bullet(pygame.sprite.Sprite):
  
    def __init__(self,x,y,speed = 8.2):
        super().__init__()
        self.bullet = pygame.transform.scale(pygame.image.load(Laser_Path).convert_alpha() , (10,30))
        self.rect = self.bullet.get_rect(center = (x,y))
        self.speed = speed 

    def update(self):
        self.rect.y -= self.speed 

    def surface(self,surf):
        surf.blit(self.bullet,self.rect)
