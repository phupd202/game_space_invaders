import pygame
import ship
import os

class Player(ship.Ship):
    WIDTH, HEIGHT = 650, 550
    LINK_PLAYER_IMG = os.path.join("data","spaceship.png")
    LINK_LASER_IMG = os.path.join("data","laser.png")


    def __init__(self,x,y,health=100):
        super().__init__(x,y,health)
        self.ship_img = pygame.image.load(self.LINK_PLAYER_IMG)
        self.laser_img = pygame.image.load(self.LINK_LASER_IMG)
        self.mask = pygame.mask.from_surface(self.ship_img)
        self.max_health = health

    def move_lasers(self, vel, objs):
        self.cooldown()
        for laser1 in self.lasers:
            laser1.move(vel)
            if laser1.off_screen(self.HEIGHT):
                self.lasers.remove(laser1)
            else:
                for obj in objs:
                    if laser1.collide(obj):
                        objs.remove(obj)
                        if laser1 in self.lasers:
                            self.lasers.remove(laser1)

    def healthbar(self,window):
        pygame.draw.rect(window, (255,0,0), (self.x,self.y+self.ship_img.get_height() + 10, self.ship_img.get_width(), 10))
        pygame.draw.rect(window, (0,255,0), (self.x,self.y+self.ship_img.get_height() + 10, self.ship_img.get_width() * (self.health/self.max_health), 10))

    def draw(self, window):
        super().draw(window)
        self.healthbar(window)