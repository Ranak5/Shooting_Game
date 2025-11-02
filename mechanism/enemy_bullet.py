import pygame


pygame.init()
pygame.mixer.init()

Enemy1_Path = "assets\PNG\Lasers\laserBlue04.png"
Enemy2_Path = "assets\PNG\Lasers\laserBlue04.png"
Enemy3_Path = "assets\PNG\Lasers\laserGreen04.png"
Enemy4_Path = "assets\PNG\Lasers\laserRed04.png"


class Enemy_1(pygame.sprite.Sprite):
    
    def __init__(self,x,y,speed = 10):
        super().__init__()
        self.img = pygame.transform.scale(pygame.image.load(Enemy1_Path).convert_alpha(),(10,30))
        self.rect = self.img.get_rect(center = (x,y))
        self.speed = speed 

    def update(self):
        self.rect.y += self.speed 

    def Surface(self,surf):
        surf.blit(self.img,(self.rect))

class Enemy_2(pygame.sprite.Sprite):
    
    def __init__(self,x,y,speed = 10):
        super().__init__()
        self.img = pygame.transform.scale(pygame.image.load(Enemy2_Path).convert_alpha(),(10,30))
        self.rect = self.img.get_rect(center = (x,y))
        self.speed = speed 

    def update(self):
        self.rect.y += self.speed 

    def Surface(self,surf):
        surf.blit(self.img,(self.rect))

class Enemy_3(pygame.sprite.Sprite):
    
    def __init__(self,x,y,speed = 10):
        super().__init__()
        self.img = pygame.transform.scale(pygame.image.load(Enemy3_Path).convert_alpha(),(10,30))
        self.rect = self.img.get_rect(center = (x,y))
        self.speed = speed 

    def update(self):
        self.rect.y += self.speed 

    def Surface(self,surf):
        surf.blit(self.img,(self.rect))

class Enemy_4(pygame.sprite.Sprite):
    
    def __init__(self,x,y,speed = 10):
        super().__init__()
        self.img = pygame.transform.scale(pygame.image.load(Enemy4_Path).convert_alpha(),(10,30))
        self.rect = self.img.get_rect(center = (x,y))
        self.speed = speed 

    def update(self):
        self.rect.y += self.speed 

    def Surface(self,surf):
        surf.blit(self.img,(self.rect))

        