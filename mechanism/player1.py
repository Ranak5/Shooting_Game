import pygame
pygame.init()

Path = "assets\PNG\playerShip1_blue.png"
class Player(pygame.sprite.Sprite):
    
    def __init__(self,x,y,speed = 5):
        super().__init__()
    
        self.img = pygame.transform.scale(pygame.image.load(Path).convert_alpha(),(50,50))
        self.rect = self.img.get_rect(center = (x,y))
        
        self.speed = speed 

    def _input(self):
        key = pygame.key.get_pressed()
        
        if key[pygame.K_RIGHT]:
            self.rect.x  += self.speed
        if key[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if key[pygame.K_UP]:
            self.rect.y  -= self.speed
        if key[pygame.K_DOWN]:
            self.rect.y  += self.speed
    
    def update(self):
        self._input()

        #Position Management 

        if self.rect.x < 0:
            self.rect.x = 0
        elif self.rect.x > 750:
            self.rect.x = 750

        if self.rect.y > 620:
            self.rect.y = 620
        elif self.rect.y < 500:
            self.rect.y = 500 

    def surface(self,surf):
        surf.blit(self.img,self.rect)