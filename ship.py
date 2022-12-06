import pygame
import laser
from pygame import mixer

class Ship:
    COOLDOWN = 30
    WIDTH, HEIGHT = 650, 550 # kích cỡ của sổ
    # LINK_MUSIC_SHOOT = "./data/bullet.wav" 
    '''
    Lớp Ship chính là lớp cơ sở
    - Player và Enemy đều kế thừa từ lớp này
    - Các atribute của Ship
    + x, y: Toạ độ của Ship
    + health: Sức khoẻ(Máu)
    + ship_img: Ảnh hiển thị Ship
    + laser[]: Là một mảng, dùng để lưu trữ các đối tượng Laser
    '''

    # Construtor
    def __init__(self, x, y, health = 100):
        self.x = x
        self.y = y
        self.health = health
        self.ship_img = None
        self.laser_img = None
        self.lasers = []
        self.cool_down_counter = 0
        # self.music_shoot = pygame.mixer.music.load(self.LINK_MUSIC_SHOOT)


    # Function
    # Vẽ Ship ra màn hình
    def draw(self, window):
        window.blit(self.ship_img, (self.x, self.y))
        for laser in self.lasers:
            laser.draw(window)

    # # Âm thanh bắn
    # def music_shoot(self, url):
    #     bulletSound = mixer.Sound(url)
    #     bulletSound.play()

    # Di chuyển các viên đạn
    def move_lasers(self, vel, obj):
        self.cooldown()
        for laser1 in self.lasers:
            laser1.move(vel)
            if laser1.off_screen(self.HEIGHT):
                self.lasers.remove(laser1)
            elif laser1.collide(obj):
                obj.health -= 10
                self.lasers.remove(laser1)

    # get width của con tàu
    def get_width(self):
        return self.ship_img.get_width()

    # get height của con tàu
    def get_height(self):
        return self.ship_img.get_height()

    # HỆ so hồi chiêu
    def cooldown(self):
        if self.cool_down_counter >= self.COOLDOWN:
            self.cool_down_counter = 0
        elif self.cool_down_counter > 0:
            self.cool_down_counter += 1

    def shoot(self):
        if self.cool_down_counter == 0:
            laser1 = laser.Laser(self.x,self.y,self.laser_img)
            # self.music_shoot(self.LINK_MUSIC_SHOOT)
            self.lasers.append(laser1)
            self.cool_down_counter = 1

    # check_va cham
    def collide(self,obj):
        offset_x = self.x - obj.x
        offset_y = self.y - obj.y
        return self.mask.overlap(obj.mask, (offset_x,offset_y)) != None