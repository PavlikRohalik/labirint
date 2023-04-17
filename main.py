from pygame import *
import random as rnd
import datetime as dt
import time as tm
font.init()
mixer.init()

class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y):
        sprite.Sprite.__init__(self)
    
        self.image = transform.scale(image.load(player_image), (size_x, size_y))

        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
 
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):  
        if packman.rect.x <= win_width-80 and packman.x_speed > 0 or packman.rect.x >= 0 and packman.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        platforms_touched2 = sprite.spritecollide(self, barriersbreak, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) 
        elif self.x_speed < 0: 
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) 
        if self.x_speed > 0: 
            for p in platforms_touched2:
                self.rect.right = min(self.rect.right, p.rect.left) 
        elif self.x_speed < 0: 
            for p in platforms_touched2:
                self.rect.left = max(self.rect.left, p.rect.right) 
        if packman.rect.y <= win_height-80 and packman.y_speed > 0 or packman.rect.y >= 0 and packman.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers, False)
        platforms_touched2 = sprite.spritecollide(self, barriersbreak, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
            for p in platforms_touched2:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        if self.y_speed > 0: 
            for p in platforms_touched2:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched2:
                self.rect.top = max(self.rect.top, p.rect.bottom)
            for p in platforms_touched2:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        speed_bullet = rnd.randint(30, 90)
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top+5, 50, 30, speed_bullet)
        bullets.add(bullet)
    def fire2(self):
        speed_bullet2 = rnd.randint(30, 90)
        bullet2 = Bullet2('bullet2.png', self.rect.centerx-50, self.rect.top+50, 50, 30, -speed_bullet2)
        bullets2.add(bullet2)

class Player2(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_x_speed,player_y_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)

        self.x_speed = player_x_speed
        self.y_speed = player_y_speed
    def update(self):  
        if packman2.rect.x <= win_width-80 and packman2.x_speed > 0 or packman2.rect.x >= 0 and packman2.x_speed < 0:
            self.rect.x += self.x_speed
        platforms_touched = sprite.spritecollide(self, barriers2, False)
        platforms_touched2 = sprite.spritecollide(self, barriersbreak2, False)
        if self.x_speed > 0: 
            for p in platforms_touched:
                self.rect.right = min(self.rect.right, p.rect.left) 
        elif self.x_speed < 0: 
            for p in platforms_touched:
                self.rect.left = max(self.rect.left, p.rect.right) 
        if self.x_speed > 0: 
            for p in platforms_touched2:
                self.rect.right = min(self.rect.right, p.rect.left) 
        elif self.x_speed < 0: 
            for p in platforms_touched2:
                self.rect.left = max(self.rect.left, p.rect.right) 
        if packman2.rect.y <= win_height-80 and packman2.y_speed > 0 or packman2.rect.y >= 0 and packman2.y_speed < 0:
            self.rect.y += self.y_speed
        platforms_touched = sprite.spritecollide(self, barriers2, False)
        platforms_touched2 = sprite.spritecollide(self, barriersbreak2, False)
        if self.y_speed > 0: 
            for p in platforms_touched:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched:
                self.rect.top = max(self.rect.top, p.rect.bottom)
            for p in platforms_touched2:
                self.rect.top = max(self.rect.top, p.rect.bottom)
        if self.y_speed > 0: 
            for p in platforms_touched2:
                if p.rect.top < self.rect.bottom:
                    self.rect.bottom = p.rect.top
        elif self.y_speed < 0: 
            for p in platforms_touched2:
                self.rect.top = max(self.rect.top, p.rect.bottom)
            for p in platforms_touched2:
                self.rect.top = max(self.rect.top, p.rect.bottom)
    def fire(self):
        speed_bullet = rnd.randint(30, 90)
        bullet = Bullet('bullet.png', self.rect.centerx, self.rect.top+5, 50, 30, speed_bullet)
        bullets.add(bullet)
    def fire2(self):
        speed_bullet2 = rnd.randint(30, 90)
        bullet2 = Bullet2('bullet2.png', self.rect.centerx-50, self.rect.top+50, 50, 30, -speed_bullet2)
        bullets2.add(bullet2)

class Enemy(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, start_x1, start_x2):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
        self.start_x1=start_x1
        self.start_x2=start_x2

    def update(self):
        if self.rect.x <= self.start_x1:
            self.side = "right"
        if self.rect.x >= self.start_x2:
            self.side = "left"
        if self.side == "left":
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed

class Enemy2(GameSprite):
    side = "left"
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed, start_y1, start_y2):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
        self.start_y1=start_y1
        self.start_y2=start_y2

    def update(self):
        if self.rect.y <= self.start_y1:
            self.side = "right"
        if self.rect.y >= self.start_y2:
            self.side = "left"
        if self.side == "left":
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed

class Bullet(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()
class Bullet2(GameSprite):
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        GameSprite.__init__(self, player_image, player_x, player_y, size_x, size_y)
        self.speed = player_speed
    def update(self):
        self.rect.x += self.speed
        if self.rect.x > win_width+10:
            self.kill()


win_width = 1320
win_height = 720
display.set_caption("Labirint")
window = display.set_mode((win_width, win_height))
back = transform.scale(image.load('background.jpg'), (win_width, win_height))
backlevel2 = transform.scale(image.load('backlevel2.jpg'), (win_width, win_height))
backmenu = transform.scale(image.load('main.jpg'), (win_width, win_height))

imagebutton = image.load('buttonplay.png')
imagebutton = transform.scale(imagebutton, (250, 100))
imagebutton2 = image.load('goldbutton.png')
imagebutton2 = transform.scale(imagebutton2, (250, 50))
imagebutton3 = image.load('buttonclosed.png')
imagebutton3 = transform.scale(imagebutton3, (250, 100))
imagebutton4 = image.load('buttonrandom.png')
imagebutton4 = transform.scale(imagebutton4, (250, 80))
imagebutton5 = image.load('bluebutton.png')
imagebutton5 = transform.scale(imagebutton5, (300, 50))
imagebutton6 = image.load('redbutton.png')
imagebutton6 = transform.scale(imagebutton6, (200, 50))
imagebutton7 = image.load('buttonrandom.png')
imagebutton7 = transform.scale(imagebutton7, (200, 50))
imagebutton8 = image.load('music_button_on.png')
imagebutton8 = transform.scale(imagebutton8, (50, 50))
imagebutton9 = image.load('music_icon.png')
imagebutton9 = transform.scale(imagebutton9, (40, 35))
imagebutton10 = image.load('music_button_off.png')
imagebutton10 = transform.scale(imagebutton10, (50, 50))
imagebutton11 = image.load('music_icon.png')
imagebutton11 = transform.scale(imagebutton11, (40, 35))

button_width = 250
button_height = 100
button_x = (win_width - button_width) // 2
button_y = (win_height - button_height) // 2

button_rect = Rect(button_x, button_y, button_width, button_height)

button2_width = 250
button2_height = 100
button2_x = (win_width - button2_width) // 2
button2_y = (win_height - button2_height) // 4 - 68

button2_rect = Rect(button2_x, button2_y, button2_width, button2_height)

button3_width = 250
button3_height = 100
button3_x = (win_width - button3_width) // 7
button3_y = (win_height - button3_height) // 2 + 3

button3_rect = Rect(button3_x, button3_y, button3_width, button3_height)

button4_width = 250
button4_height = 80
button4_x = (win_width - button4_width) // 2
button4_y = (win_height- 250)

button4_rect = Rect(button4_x, button4_y, button4_width, button4_height)

button5_width = 300
button5_height = 50
button5_x = (win_width - button4_width) // 2 - 25
button5_y = (win_height - button4_height) // 4 - 25

button5_rect = Rect(button5_x, button5_y, button5_width, button5_height)

button6_width = 200
button6_height = 50
button6_x = win_width - 500
button6_y = (win_height - button6_height) // 2

button6_rect = Rect(button6_x, button6_y, button6_width, button6_height)

button7_width = 200
button7_height = 50
button7_x = win_width // 4
button7_y = (win_height - button7_height) // 2

button7_rect = Rect(button7_x, button7_y, button7_width, button7_height)

button8_width = 50
button8_height = 50
button8_x = win_width - 60
button8_y = 40

button8_rect = Rect(button8_x, button8_y, button8_width, button8_height)

button9_width = 40
button9_height = 35
button9_x = win_width - 56
button9_y = 48

button9_rect = Rect(button9_x, button9_y, button9_width, button9_height)

button10_width = 50
button10_height = 50
button10_x = win_width - 60
button10_y = 120

button10_rect = Rect(button10_x, button10_y, button10_width, button10_height)

button11_width = 40
button11_height = 35
button11_x = win_width - 56
button11_y = 128

button11_rect = Rect(button11_x, button11_y, button11_width, button11_height)

characterback1_image = image.load("backhero3.png").convert_alpha()
characterback1_image = transform.scale(characterback1_image, (200, 200))
characterback2_image = image.load("backhero2.png").convert_alpha()
characterback2_image = transform.scale(characterback2_image, (240, 200))
characterback3_image = image.load("backhero.png").convert_alpha()
characterback3_image = transform.scale(characterback3_image, (180, 200))

character1_image = image.load("hero.png").convert_alpha()
character2_image = image.load("hero2.png").convert_alpha()
character3_image = image.load("hero3.png").convert_alpha()
character1_image = transform.scale(character1_image, (135, 150))
character2_image = transform.scale(character2_image, (160, 150))
character3_image = transform.scale(character3_image, (120, 150))

characterback1_width = 200
characterback1_height = 150
characterback1_x = ((win_width / 2) - 20) + 430
characterback1_y = 80


characterback2_width = 200
characterback2_height = 150
characterback2_x = ((win_width / 2) - 20) - 100
characterback2_y = 80

characterback3_width = 200
characterback3_height = 150
characterback3_x = ((win_width / 2) - 20) - 530
characterback3_y = 80

character1_width = 200
character1_height = 150
character1_x = ((win_width / 2) - 60) + 502.5
character1_y = 100

character2_width = 200
character2_height = 150
character2_x = (win_width / 2) - 80
character2_y = 100

character3_width = 200
character3_height = 150
character3_x = ((win_width / 2) - 20) - 500
character3_y = 100

characterback1_rect = Rect(characterback1_x, characterback1_y, characterback1_width, characterback1_height)
characterback2_rect = Rect(characterback2_x, characterback2_y, characterback2_width, characterback2_height)
characterback3_rect = Rect(characterback3_x, characterback3_y, characterback3_width, characterback3_height)
character1_rect = Rect(character1_x, character1_y, character1_width, character1_height)
character2_rect = Rect(character2_x, character2_y, character2_width, character2_height)
character3_rect = Rect(character3_x, character3_y, character3_width, character3_height)

barriers = sprite.Group()

barriersbreak = sprite.Group()

bullets = sprite.Group()

bullets2 = sprite.Group()

monsters = sprite.Group()

barriers2 = sprite.Group()

barriersbreak2 = sprite.Group()

monsters2 = sprite.Group()

lootboxs = sprite.Group()

b1 = GameSprite('barrier.png', 0, -1, 10, 720)
b2 = GameSprite('barrier2.png', 0, 0, 1320, 10)
b3 = GameSprite('barrier.png', 1310, 0, 10, 720)
b4 = GameSprite('barrier2.png', 0, 710, 1320, 10)

barriers.add(b1)
barriers.add(b2)
barriers.add(b3)
barriers.add(b4)

wb1 = GameSprite('wall4_y_broken.png', 350, 400, 50, 200)
wb2 = GameSprite('wall4_y_broken.png', 500, 510, 50, 200)
wb3 = GameSprite('wall4_y_broken.png', 500, 90, 50, 200)
wb4 = GameSprite('wall4_y_broken.png', 330, 90, 50, 160)
wb5 = GameSprite('wall4_y_broken.png', 1120, 260, 50, 205)
wb6 = GameSprite('wall4_y_broken.png', 1120, 130, 50, 205)
wb7 = GameSprite('wall4_y_broken.png', 800, 260, 50, 205)
wb8 = GameSprite('wall4_y_broken.png', 500, 10, 50, 200)
barriersbreak.add(wb1)
barriersbreak.add(wb2)
barriersbreak.add(wb3)
barriersbreak.add(wb4)
barriersbreak.add(wb5)
barriersbreak.add(wb6)
barriersbreak.add(wb7)
barriersbreak.add(wb8)

scaled_image = transform.scale(image.load('platform2.png'), (800, 800))

w1 = GameSprite('wall4.png', 10, 550, 220, 40)
w2 = GameSprite('wall4_y.png', 350, 515, 50, 195)
w3 = GameSprite('wall4.png', 125, 360, 220, 40)
w4 = GameSprite('wall4.png', 180, 360, 220, 40)
w5 = GameSprite('wall4_y.png', 500, 415, 50, 195)
w6 = GameSprite('wall4_y.png', 650, 515, 50, 195)
w7 = GameSprite('wall4.png', 545, 380, 220, 40)
w8 = GameSprite('wall4_y.png', 800, 415, 50, 195)
w9 = GameSprite('wall4.png', 630, 380, 220, 40)
w10 = GameSprite('wall4.png', 800, 590, 220, 40)
w11 = GameSprite('wall4_y.png', 970, 590, 50, 120)
w12 = GameSprite('wall4_y.png', 120, 100, 50, 300)
w13 = GameSprite('wall4_y.png', 970, 590, 50, 120)
w14 = GameSprite('wall4_y.png', 500, 220, 50, 200)
w15 = GameSprite('wall4.png', 330, 210, 220, 40)
w16 = GameSprite('wall4_y.png', 120, 110, 50, 151)
w17 = GameSprite('wall4.png', 330, 90, 220, 40)
w18 = GameSprite('wall4_y.png', 650, 90, 50, 210)
w19 = GameSprite('wall4.png', 650, 260, 220, 40)
w20 = GameSprite('wall4.png', 750, 260, 220, 40)
w21 = GameSprite('wall4_y.png', 950, 260, 50, 210)
w22 = GameSprite('wall4.png', 950, 460, 190, 40)
w23 = GameSprite('wall4_y.png', 1120, 461, 50, 150)
w24 = GameSprite('wall4.png', 650, 90, 220, 40)
w25 = GameSprite('wall4.png', 1120, 260, 190, 40)
w26 = GameSprite('wall4.png', 860, 90, 220, 40)
w27 = GameSprite('wall4.png', 980, 90, 220, 40)
w28 = GameSprite('wall4_y_inv.png', 1120, 500, 50, 150)

barriers.add(w1)
barriers.add(w2)
barriers.add(w3)
barriers.add(w4)
barriers.add(w5)
barriers.add(w6)
barriers.add(w7)
barriers.add(w8)
barriers.add(w9)
barriers.add(w10)
barriers.add(w11)
barriers.add(w12)
barriers.add(w13)
barriers.add(w14)
barriers.add(w15)
barriers.add(w16)
barriers.add(w17)
barriers.add(w18)
barriers.add(w19)
barriers.add(w20)
barriers.add(w21)
barriers.add(w22)
barriers.add(w23)
barriers.add(w24)
barriers.add(w25)
barriers.add(w26)
barriers.add(w27)
barriers.add(w28)



wall1 = GameSprite('wall4_y.png', win_width-200, win_height-190, 50, 195)
wall2 = GameSprite('wall4_y.png', win_width-200, win_height-480, 50, 195)
wall3 = GameSprite('wall4_y.png', win_width-200, win_height-640, 50, 195)
wall4 = GameSprite('wall4.png', win_width-535, win_height-190, 220, 40)
wall5 = GameSprite('wall4.png', win_width-418, win_height-325, 220, 40)
wall6 = GameSprite('wall4.png', win_width-699, win_height-190, 220, 40)
wall7 = GameSprite('wall4.png', win_width-750, win_height-325, 220, 40)
wall8 = GameSprite('wall4_y.png', win_width-580, win_height-480, 50, 195)
wall7 = GameSprite('wall4.png', win_width-419, win_height-450, 220, 40)
wall9 = GameSprite('wall4_y.png', win_width-580, win_height-384, 50, 195)
wall10 = GameSprite('wall4.png', win_width-799, win_height-325, 220, 40)
wall11 = GameSprite('wall4.png', win_width-1030, win_height-190, 220, 40)
wall12 = GameSprite('wall4_y.png', win_width-1190, win_height-190, 50, 195)
wall13 = GameSprite('wall4_y.png', win_width-1030, win_height-384, 50, 195)
wall14 = GameSprite('wall4.png', -5, win_height-320, 220, 40)
wall15 = GameSprite('wall4.png', 72, win_height-320, 220, 40)
wall16 = GameSprite('wall4.png', win_width-880, win_height-325, 220, 40)
wall17 = GameSprite('wall4.png', win_width-580, win_height-325, 220, 40)
wall18 = GameSprite('wall4_y.png', win_width-1030, win_height-449, 50, 195)
wall19 = GameSprite('wall4.png', win_width-982, win_height-450, 220, 40)
wall20 = GameSprite('wall4.png', win_width-902, win_height-450, 220, 40)
wall21 = GameSprite('wall4_y.png', win_width-580, win_height-604, 50, 195)
wall22 = GameSprite('wall4.png', win_width-798, win_height-570, 220, 40)
wall23 = GameSprite('wall4.png', win_width-1030, win_height-570, 220, 40)
wall24 = GameSprite('wall4.png', win_width-1005, win_height-570, 220, 40)
wall25 = GameSprite('wall4.png', win_width-1155, win_height-570, 220, 40)
wall26 = GameSprite('wall4_y.png', win_width-1190, win_height-570, 50, 175)
wall27 = GameSprite('wall4.png', -5, win_height-570, 220, 40)
wall28 = GameSprite('wall4.png', win_width-535, win_height-450, 220, 40)
wall29 = GameSprite('wall4_y.png', win_width-350, 0, 50, 195)
wall30 = GameSprite('brick_block.png', win_width-580, 102, 50, 50)
wall31 = GameSprite('wall4_y.png', win_width-730, -120, 50, 195)
wall32 = GameSprite('brick_block.png', win_width-880, 102, 50, 50)
wall33 = GameSprite('brick_block.png', win_width-1030, 0, 50, 50)
wall34 = GameSprite('brick_block.png', win_width-1180, 102, 50, 50)
wall35 = GameSprite('brick_block.png', win_width-530, 102, 50, 50)

barriers2.add(wall1)
barriers2.add(wall2)
barriers2.add(wall3)
barriers2.add(wall4)
barriers2.add(wall5)
barriers2.add(wall6)
barriers2.add(wall7)
barriers2.add(wall8)
barriers2.add(wall9)
barriers2.add(wall10)
barriers2.add(wall11)
barriers2.add(wall12)
barriers2.add(wall13)
barriers2.add(wall14)
barriers2.add(wall15)
barriers2.add(wall16)
barriers2.add(wall17)
barriers2.add(wall18)
barriers2.add(wall19)
barriers2.add(wall20)
barriers2.add(wall21)
barriers2.add(wall22)
barriers2.add(wall23)
barriers2.add(wall24)
barriers2.add(wall25)
barriers2.add(wall26)
barriers2.add(wall27)
barriers2.add(wall28)
barriers2.add(wall29)
barriers2.add(wall30)
barriers2.add(wall31)
barriers2.add(wall32)
barriers2.add(wall33)
barriers2.add(wall34)
barriers2.add(wall35)

wallfake1 = GameSprite('wall4_y.png', win_width-200, win_height-290, 50, 105)
wallfake2 = GameSprite('wall4_y.png', win_width-200, 0, 50, 105)
wallfake3 = GameSprite('wall4_y.png', win_width-535, win_height-150, 50, 195)
wallfake4 = GameSprite('wall4_y.png', win_width-700, win_height-150, 50, 195)
wallfake5 = GameSprite('wall4_y.png', win_width-1190, win_height-320, 50, 195)
wallfake6 = GameSprite('wall4_y.png', win_width-1030, win_height-195, 50, 195)
wallfake7 = GameSprite('wall4_y.png', win_width-880, win_height-410, 50, 220)

barriersbreak2.add(wallfake1)
barriersbreak2.add(wallfake2)
barriersbreak2.add(wallfake3)
barriersbreak2.add(wallfake4)
barriersbreak2.add(wallfake5)
barriersbreak2.add(wallfake6)
barriersbreak2.add(wallfake7)

lootbox1 = GameSprite('lootbox.png', 10, 10, 50, 50)
lootbox2 = GameSprite('lootbox.png', 10, 300, 50, 50)
lootboxs.add(lootbox1)
lootboxs.add(lootbox2)


count_bullet = 20
monster_stuck = 6
skins_monsters = ['cyborg.png', 'cyborg2.png', 'cyborg3.png', 'cyborg4.png', 'cyborg5.png', 'cyborg6.png']
skins_monsters_hard = ['cyborg7.png', 'cyborg8.png']

skin_cyborg = rnd.choice(skins_monsters)
skins_monsters.remove(skin_cyborg)
monster1 = Enemy(skin_cyborg, 100, 420, 80, 80, 5, 10, 275)
skin_cyborg = rnd.choice(skins_monsters)
skins_monsters.remove(skin_cyborg)
monster2 = Enemy(skin_cyborg, 900, 640, 70, 70, 10, 780, 890)
skin_cyborg = rnd.choice(skins_monsters)
skins_monsters.remove(skin_cyborg)
monster3 = Enemy2(skin_cyborg, 420, 230, 65, 65, 15, 250, 630)
skin_cyborg = rnd.choice(skins_monsters)
skins_monsters.remove(skin_cyborg)
monster4 = Enemy(skin_cyborg, 450, 15, 70, 70, 30, 25, 405)
skin_cyborg = rnd.choice(skins_monsters)
skins_monsters_hard.append(skin_cyborg)
skins_monsters.remove(skin_cyborg)
monster5 = Enemy2(skin_cyborg, 565, 15, 70, 70, 10, 20, 310)
skin_cyborg = rnd.choice(skins_monsters)
skins_monsters_hard.append(skin_cyborg)
skins_monsters.remove(skin_cyborg)
monster6 = Enemy(skin_cyborg, 1000, 155, 70, 70, 10, 700, 1040)
final_sprite = GameSprite('pac-1.png', win_width - 85, win_height - 70, 60, 60)

monsters.add(monster1)
monsters.add(monster2)
monsters.add(monster3)
monsters.add(monster4)
monsters.add(monster5)
monsters.add(monster6)

monster_stuck2 = 6
skins_monsters2 = ['monster1.png', 'monster2.png', 'monster3.png', 'monster4.png', 'monster5.png', 'monster6.png']

skin_cyborg = rnd.choice(skins_monsters2)
skins_monsters2.remove(skin_cyborg)
monster11 = Enemy(skin_cyborg, win_width-200, win_height-280, 70, 70, 15, win_width-970, win_width-70)
skin_cyborg = rnd.choice(skins_monsters2)
skins_monsters2.remove(skin_cyborg)
monster22 = Enemy2(skin_cyborg, 200, 200, 70, 70, 20, 200, 630)
skin_cyborg = rnd.choice(skins_monsters2)
skins_monsters2.remove(skin_cyborg)
monster33 = Enemy(skin_cyborg, win_width//2, win_height//2-50, 70, 70, 15, 350, 1050)
skin_cyborg = rnd.choice(skins_monsters2)
skins_monsters2.remove(skin_cyborg)
monster44 = Enemy2(skin_cyborg, win_width-285, 200, 70, 70, 30, 25, 300)
skin_cyborg = rnd.choice(skins_monsters2)
skins_monsters2.remove(skin_cyborg)
monster55 = Enemy2(skin_cyborg, 30, 70, 70, 70, 15, 30, 320)
skin_cyborg = rnd.choice(skins_monsters2)
skins_monsters2.remove(skin_cyborg)
monster66 = Enemy(skin_cyborg, 30, 30, 70, 70, 15, 10, 900)
final_sprite2 = GameSprite('win_flags.png', 40, win_height-130, 60, 120)

monsters2.add(monster11)
monsters2.add(monster22)
monsters2.add(monster33)
monsters2.add(monster44)
monsters2.add(monster55)
monsters2.add(monster66)

menu = 1
difficulty_selection = 0
select_player = 0
music_menu = 1
music_game = 1
difficulty = None
loot_box = 0
level = 1
finish = True
run = True
test = 1

if music_menu == 1:
    mixer.music.load('menu_music.mp3')
    mixer.music.play(-1)

while run:
    if menu == 1:
        time.delay(1)
        for e in event.get():
            if e.type == QUIT:
                run = False
            elif e.type == MOUSEBUTTONDOWN:
                mouse_pos = e.pos
                if button8_rect.collidepoint(mouse_pos):
                    if music_menu == 1:
                        music_menu = 0
                        mixer.music.stop()
                    else:
                        music_menu = 1
                        mixer.music.load('menu_music.mp3')
                        mixer.music.play(-1)
                if button10_rect.collidepoint(mouse_pos):
                    if music_game == 1:
                        music_game = 0
                    else:
                        music_game = 1
                if select_player == 0 and  difficulty_selection == 0:
                    if button_rect.collidepoint(mouse_pos):
                        select_player = 1
                elif select_player == 1 and difficulty_selection == 0:
                    if characterback1_rect.collidepoint(mouse_pos):
                        hero = 'hero'
                        packman = Player(hero+'.png', 10, win_height - 100, 100, 80, 0, 0)
                        packman2 = Player2(hero+'.png', win_width-100, win_height-150, 100, 60, 0, 0)
                        select_player = 0
                        difficulty_selection = 1
                    if characterback2_rect.collidepoint(mouse_pos):
                        hero = 'hero2'
                        packman = Player(hero+'.png', 10, win_height - 100, 100, 80, 0, 0)
                        packman2 = Player2(hero+'.png', win_width-100, win_height-150, 100, 60, 0, 0)
                        select_player = 0
                        difficulty_selection = 1
                    if characterback3_rect.collidepoint(mouse_pos):
                        hero = 'hero3'
                        packman = Player(hero+'.png', 10, win_height - 100, 100, 80, 0, 0)
                        packman2 = Player2(hero+'.png', win_width-100, win_height-150, 100, 60, 0, 0)
                        select_player = 0
                        difficulty_selection = 1
                    if button4_rect.collidepoint(mouse_pos):
                        hero = rnd.choice(('hero', 'hero2', 'hero3'))
                        packman = Player(hero+'.png', 10, win_height - 100, 100, 80, 0, 0)
                        packman2 = Player2(hero+'.png', win_width-100, win_height-150, 100, 60, 0, 0)
                        select_player = 0
                        difficulty_selection = 1
                elif select_player == 0 and difficulty_selection == 1:
                    if button6_rect.collidepoint(mouse_pos):
                        difficulty = 'hard'
                        count_bullet = 12
                        menu = 0                 
                        monsters.remove(monster5)
                        monsters.remove(monster6)
                        skin_cyborg = rnd.choice(skins_monsters_hard)
                        skins_monsters_hard.remove(skin_cyborg)
                        monster5 = Enemy2(skin_cyborg, 565, 15, 70, 70, 30, 20, 310)
                        monsters.add(monster5)
                        skin_cyborg = rnd.choice(skins_monsters_hard)
                        skins_monsters_hard.remove(skin_cyborg)
                        monster6 = Enemy(skin_cyborg, 1000, 155, 70, 70, 30, 700, 1040)
                        monsters.add(monster6)
                        skin_cyborg = rnd.choice(skins_monsters_hard)
                        skins_monsters_hard.remove(skin_cyborg)
                        monster7 = Enemy2(skin_cyborg, 200, 155, 70, 70, 30, 30, 250)
                        monsters.add(monster7)
                        skin_cyborg = rnd.choice(skins_monsters_hard)
                        skins_monsters_hard.remove(skin_cyborg)
                        monster8 = Enemy2(skin_cyborg, win_width-100, 400, 70, 70, 30, 320, 570)
                        monsters.add(monster8)
                        mixer.music.stop()
                    if button7_rect.collidepoint(mouse_pos):
                        difficulty = 'easy'
                        count_bullet = 20
                        menu = 0
                        monsters.remove(monster5)
                        monsters.remove(monster6)
                        mixer.music.stop()

        if finish:
            window.blit(backmenu, (0, 0))
            if music_menu == 1:
                window.blit(imagebutton8, button8_rect)
            else:
                window.blit(imagebutton10, button8_rect)
            if music_game == 1:
                window.blit(imagebutton8, button10_rect)
            else:
                window.blit(imagebutton10, button10_rect)
            window.blit(imagebutton9, button9_rect)
            main_font = font.Font(None, 25)
            text = main_font.render("Меню", True, ((0, 0, 0)))
            window.blit(text, (button8_x+2, button8_y+50))
            window.blit(imagebutton11, button11_rect)
            main_font = font.Font(None, 25)
            text = main_font.render("Гра", True, ((0, 0, 0)))
            window.blit(text, (button10_x+10, button10_y+50))
            if select_player == 1 and difficulty_selection == 0:
                window.blit(characterback1_image, characterback1_rect)
                window.blit(characterback2_image, characterback2_rect)
                window.blit(characterback3_image, characterback3_rect)
                window.blit(character1_image, character1_rect)
                window.blit(character2_image, character2_rect)
                window.blit(character3_image, character3_rect)
                window.blit(imagebutton4, button4_rect)
                main_font = font.Font(None, 30)
                text = main_font.render("Луїджі", True, ((0, 0, 0)))
                window.blit(text, (characterback2_x+78, characterback2_y+200))
                main_font = font.Font(None, 30)
                text = main_font.render("Маріо", True, ((0, 0, 0)))
                window.blit(text, (characterback1_x+70, characterback1_y+200))
                main_font = font.Font(None, 30)
                text = main_font.render("Купа-трупа", True, ((0, 0, 0)))
                window.blit(text, (characterback3_x+32, characterback3_y+200))
                main_font = font.Font(None, 30)
                text = main_font.render("Щоб обрати персонажа, просто натисніть на його рамку або на нього самого!", True, ((0, 0, 0)))
                window.blit(text, ((win_width//4)-50, win_height/2))
                main_font = font.Font(None, 40)
                text = main_font.render("Рандомізація", True, ((0, 0, 0)))
                window.blit(text, (button4_x+32, button4_y+25))

            elif difficulty_selection == 1 and select_player == 0:
                backtext = image.load('backtext.png')
                backtext = transform.scale(backtext, (300, 50))
                main_font = font.Font(None, 40)
                text = main_font.render("Вибір складності гри", True, ((255, 255, 255)))
                window.blit(backtext, (win_width/2.5-2, button4_y/8-12))
                window.blit(text, (win_width/2.5, button4_y/8))
                window.blit(imagebutton6, button6_rect)
                window.blit(imagebutton7, button7_rect)
                main_font = font.Font(None, 40)
                text = main_font.render("Легко", True, ((255, 255, 255)))
                window.blit(text, (button7_x+60, button7_y+11))
                main_font = font.Font(None, 40)
                text = main_font.render("Складно", True, ((255, 255, 255)))
                window.blit(text, (button6_x+40, button6_y+11))
            else:
                window.blit(imagebutton, (button_x, button_y+3))
                window.blit(imagebutton2, button2_rect)
                window.blit(imagebutton3, button3_rect)
                window.blit(imagebutton5, button5_rect)
                main_font = font.Font(None, 40)
                text = main_font.render("Лабіринт Маріо", True, ((0, 0, 0)))
                window.blit(text, (button_x+18, 100))
                main_font = font.Font(None, 40)
                text = main_font.render("Початок пригодам", True, ((0, 0, 0)))
                window.blit(text, (button4_x-4, 150))
                main_font = font.Font(None, 36)
                text = main_font.render("Старт", True, ((6, 9, 55)))
                text_rect = text.get_rect(center=button_rect.center)
                window.blit(text, text_rect)
                main_font = font.Font(None, 36)
                text = main_font.render("В розробці", True, ((224, 224, 224)))
                text_rect = text.get_rect(center=button3_rect.center)
                window.blit(text, text_rect)

            main_font = font.Font(None, 25)
            text = main_font.render("Game version: 2.0", True, ((97, 53, 202)))
            window.blit(text, (0, 0))
            main_font = font.Font(None, 25)
            text = main_font.render("Author: Sbirioni", True, ((97, 53, 202)))
            window.blit(text, (win_width-131, 0))



    elif level == 2:
        time.delay(1)
        if music_game == 2:
            mixer.music.load('level2_music.mp3')
            mixer.music.play(-1)
            music_game = 1
        start_time = dt.datetime.now()
        for e in event.get():
            if e.type == QUIT:
                run = False
            if count_bullet >= 1:
                if e.type == KEYDOWN:
                    if e.key == K_w:
                        packman2.y_speed = -20
                    elif e.key == K_s:  
                        packman2.y_speed = 20
                    elif e.key == K_a:
                        packman2.x_speed = -20
                    elif e.key == K_d:
                        packman2.x_speed = 20
                    elif e.key == K_e:
                        packman2.fire()
                        count_bullet-=1
                        if finish: 
                            sound = mixer.Sound('piu.wav')
                            mixer.Sound.play(sound).set_volume(70)
                    elif e.key == K_q:
                        packman2.fire2()
                        count_bullet-=1
                        if finish: 
                            sound = mixer.Sound('piu.wav')
                            mixer.Sound.play(sound).set_volume(70)
                    if test == 1:
                        if e.key == K_u:
                            count_bullet = 999
                        if e.key == K_i:
                            sprite.Group.empty(barriers2)
                            sprite.Group.empty(barriersbreak2)
                        if e.key == K_o:
                            sprite.Group.empty(monsters2)
                        if e.key == K_1:
                            level = 1
                        if e.key == K_2:
                            level = 2   
                elif e.type == KEYUP:
                    if e.key == K_w:
                        packman2.y_speed = 0
                    elif e.key == K_s:
                        packman2.y_speed = 0
                    elif e.key == K_a:
                        packman2.x_speed = 0
                    elif e.key == K_d:
                            packman2.x_speed = 0
            else:
                if e.type == KEYDOWN:
                    if e.key == K_w:
                        packman2.y_speed = -20
                    elif e.key == K_s:  
                        packman2.y_speed = 20
                    elif e.key == K_a:
                        packman2.x_speed = -20
                    elif e.key == K_d:
                        packman2.x_speed = 20
                    if test == 1:
                        if e.key == K_u:
                            count_bullet = 999
                        if e.key == K_i:
                            sprite.Group.empty(barriers2)
                            sprite.Group.empty(barriersbreak2)
                        if e.key == K_o:
                            sprite.Group.empty(monsters2)
                        if e.key == K_1:
                            level = 1
                        if e.key == K_2:
                            level = 2   
                elif e.type == KEYUP:
                    if e.key == K_w:
                        packman2.y_speed = 0
                    elif e.key == K_s:
                        packman2.y_speed = 0
                    elif e.key == K_a:
                        packman2.x_speed = 0
                    elif e.key == K_d:
                            packman2.x_speed = 0

        if finish:
            window.blit(backlevel2, (0, 0))
            barriers2.draw(window)
            barriersbreak2.draw(window)
            packman2.update()
            bullets.update()
            bullets2.update()
            packman2.reset()
            bullets.draw(window)
            bullets2.draw(window)
            barriersbreak2.draw(window)
            barriers2.draw(window)
            final_sprite2.reset()    
            lootboxs.draw(window)

            if sprite.spritecollide(packman2, lootboxs, True):
                if loot_box == 0:
                    if difficulty == 'hard':
                        count_bullet+=6
                    else:
                        count_bullet+=rnd.randint(10, 15)
                else:
                    if difficulty == 'hard':
                        count_bullet+=3
                    else:
                        opens_box = rnd.randint(1, 2)
                        if opens_box == 1:
                            count_bullet+=rnd.randint(10, 15)
                loot_box+=1
            
            lootboxs.update()

            main_font = font.Font(None, 25)
            text = main_font.render('Кількість куль:', True, ((0, 0, 0)))
            window.blit(text, (10, 10))    
            main_font = font.Font(None, 25)
            text = main_font.render(str(count_bullet), True, ((0, 0, 0)))
            window.blit(text, (140, 11))     

            if sprite.groupcollide(monsters2, bullets, True, True):
                sound = mixer.Sound('death_cyborg.wav')
                mixer.Sound.play(sound).set_volume(70)
                sprite.groupcollide(monsters2, bullets, True, True)
            if sprite.groupcollide(monsters2, bullets2, True, True):
                sound = mixer.Sound('death_cyborg.wav')
                mixer.Sound.play(sound).set_volume(70)
                sprite.groupcollide(monsters2, bullets2, True, True)
            sprite.groupcollide(bullets, barriers2, True, False)
            if sprite.groupcollide(bullets, barriersbreak2, True, True):
                sprite.groupcollide(bullets, barriersbreak2, True, True)
                sound = mixer.Sound('broken_wall.wav')
                mixer.Sound.play(sound).set_volume(70)
            sprite.groupcollide(bullets2, barriers2, True, False)
            if sprite.groupcollide(bullets2, barriersbreak2, True, True):
                sprite.groupcollide(bullets2, barriersbreak2, True, True)
                sound = mixer.Sound('broken_wall.wav')
                mixer.Sound.play(sound).set_volume(70)
            barriersbreak2.update()
            barriersbreak2.draw(window)
            monsters2.update()
            monsters2.draw(window)   

            if sprite.spritecollide(packman2, monsters2, True):
                mixer.music.stop()
                finish = False
                img = image.load('game-over_1.png')
                img2 = image.load('mario_end.png')
                img2 = transform.scale(img2, (300, 450))
                imgback = transform.scale(image.load('backtext.png'), (win_width+200, win_height+200))
                d = img.get_width() // img.get_height()
                sound = mixer.Sound('death_music.wav')
                mixer.Sound.play(sound).set_volume(70)
                elapsed_time = dt.datetime.now() - start_time
                elapsed_time_str = str(elapsed_time).split('.')[0]
                text_font = font.Font(None, 30)
                text = text_font.render("Час проходження: {}".format(elapsed_time_str), True, ((255, 255, 255)))
                window.blit(imgback, (-50, 0))
                window.blit(transform.scale(img, (win_height*d, win_height)), (300, 0))
                window.blit(img2, (10, 100))

            if loot_box == 2:
                if sprite.collide_rect(packman2, final_sprite2):
                    mixer.music.stop()
                    finish = False
                    img = image.load('thumb.jpg')
                    img2 = image.load('mario_win.png')
                    imgback = transform.scale(image.load('backtext.png'), (win_width+200, win_height+200))
                    sound = mixer.Sound('win_sound.wav')
                    mixer.Sound.play(sound).set_volume(70)
                    window.blit(imgback, (-50, 0))
                    window.blit(transform.scale(img, (win_width-200, win_height-200)), (100, 0))
                    window.blit(transform.scale(img2, (win_width//3, win_height//3)), (win_width//3, win_height-300))



    else:
        time.delay(1)
        start_time = dt.datetime.now()
        if music_game == 1:
            mixer.music.load('music_game.mp3')
            mixer.music.play(-1)
            music_game = 2
        for e in event.get():
            if e.type == QUIT:
                run = False
            if count_bullet >= 1:
                if e.type == KEYDOWN:
                    if e.key == K_w:
                        packman.y_speed = -20
                    elif e.key == K_s:  
                        packman.y_speed = 20
                    elif e.key == K_a:
                        packman.x_speed = -20
                    elif e.key == K_d:
                        packman.x_speed = 20
                    elif e.key == K_e:
                        packman.fire()
                        count_bullet-=1
                        if finish:
                            sound = mixer.Sound('piu.wav')
                            mixer.Sound.play(sound).set_volume(70)
                    elif e.key == K_q:
                        packman.fire2()
                        count_bullet-=1
                        if finish:
                            sound = mixer.Sound('piu.wav')
                            mixer.Sound.play(sound).set_volume(70)
                    if test == 1:
                        if e.key == K_u:
                            count_bullet = 999
                        if e.key == K_i:
                            sprite.Group.empty(barriers)
                            sprite.Group.empty(barriersbreak)
                        if e.key == K_o:
                            sprite.Group.empty(monsters)
                        if e.key == K_1:
                            level = 1
                        if e.key == K_2:
                            level = 2                      
                elif e.type == KEYUP:
                    if e.key == K_w:
                        packman.y_speed = 0
                    elif e.key == K_s:
                        packman.y_speed = 0
                    elif e.key == K_a:
                        packman.x_speed = 0
                    elif e.key == K_d:
                            packman.x_speed = 0
            else:
                if e.type == KEYDOWN:
                    if e.key == K_w:
                        packman.y_speed = -20
                    elif e.key == K_s:  
                        packman.y_speed = 20
                    elif e.key == K_a:
                        packman.x_speed = -20
                    elif e.key == K_d:
                        packman.x_speed = 20
                    if test == 1:
                        if e.key == K_u:
                            count_bullet = 999
                        if e.key == K_i:
                            sprite.Group.empty(barriers)
                            sprite.Group.empty(barriersbreak)
                        if e.key == K_o:
                            sprite.Group.empty(monsters)
                        if e.key == K_1:
                            level = 1
                        if e.key == K_2:
                            level = 2   
                elif e.type == KEYUP:
                    if e.key == K_w:
                        packman.y_speed = 0
                    elif e.key == K_s:
                        packman.y_speed = 0
                    elif e.key == K_a:
                        packman.x_speed = 0
                    elif e.key == K_d:
                            packman.x_speed = 0

        if finish:
            window.blit(back, (0, 0))
            barriers.draw(window)
            barriersbreak.draw(window)
            packman.update()
            bullets.update()
            bullets2.update()
            packman.reset()
            bullets.draw(window)
            bullets2.draw(window)
            barriersbreak.draw(window)
            barriers.draw(window)
            final_sprite.reset()    

            main_font = font.Font(None, 25)
            text = main_font.render('Кількість куль:', True, ((0, 0, 0)))
            window.blit(text, (10, 10))    
            main_font = font.Font(None, 25)
            text = main_font.render(str(count_bullet), True, ((0, 0, 0)))
            window.blit(text, (140, 11))     

            if sprite.groupcollide(monsters, bullets, True, True):
                sound = mixer.Sound('death_cyborg.wav')
                mixer.Sound.play(sound).set_volume(70)
                sprite.groupcollide(monsters, bullets, True, True)
            if sprite.groupcollide(monsters, bullets2, True, True):
                sound = mixer.Sound('death_cyborg.wav')
                mixer.Sound.play(sound).set_volume(70)
                sprite.groupcollide(monsters, bullets2, True, True)
            monsters.update()
            monsters.draw(window)
            sprite.groupcollide(bullets, barriers, True, False)
            if sprite.groupcollide(bullets, barriersbreak, True, True):
                sprite.groupcollide(bullets, barriersbreak, True, True)
                sound = mixer.Sound('broken_wall.wav')
                mixer.Sound.play(sound).set_volume(70)
            sprite.groupcollide(bullets2, barriers, True, False)
            if sprite.groupcollide(bullets2, barriersbreak, True, True):
                sprite.groupcollide(bullets2, barriersbreak, True, True)
                sound = mixer.Sound('broken_wall.wav')
                mixer.Sound.play(sound).set_volume(70)
            barriersbreak.update()
            barriersbreak.draw(window)

            main_font = font.Font(None, 25)
            text = main_font.render('Кількість ворогів:', True, ((0, 0, 0)))
            window.blit(text, (win_width-180, 10))    
            main_font = font.Font(None, 25)
            text = main_font.render(str(len(monsters)), True, ((0, 0, 0)))
            window.blit(text, (win_width-25, 11))    

            if sprite.spritecollide(packman, monsters, True):
                mixer.music.stop()
                finish = False
                img = image.load('game-over_1.png')
                img2 = image.load('mario_end.png')
                img2 = transform.scale(img2, (300, 450))
                imgback = transform.scale(image.load('backtext.png'), (win_width+200, win_height+200))
                d = img.get_width() // img.get_height()
                sound = mixer.Sound('death_music.wav')
                mixer.Sound.play(sound).set_volume(70)
                elapsed_time = dt.datetime.now() - start_time
                elapsed_time_str = str(elapsed_time).split('.')[0]
                text_font = font.Font(None, 30)
                text = text_font.render("Час проходження: {}".format(elapsed_time_str), True, ((255, 255, 255)))
                window.blit(imgback, (-50, 0))
                window.blit(transform.scale(img, (win_height*d, win_height)), (300, 0))
                window.blit(img2, (10, 100))
            
            if len(monsters) == 0:
                if sprite.collide_rect(packman, final_sprite):
                    mixer.music.stop()
                    sound = mixer.Sound('win_sound.wav')
                    mixer.Sound.play(sound).set_volume(70)
                    img = image.load('thumb.jpg')
                    img2 = image.load('mario_win.png')
                    imgback = transform.scale(image.load('backtext.png'), (win_width+200, win_height+200))
                    sound = mixer.Sound('win_sound.wav')
                    mixer.Sound.play(sound).set_volume(70)
                    window.blit(imgback, (-50, 0))
                    window.blit(transform.scale(img, (win_width-200, win_height-200)), (100, 0))
                    window.blit(transform.scale(img2, (win_width//3, win_height//3)), (win_width//3, win_height-300))

                    tm.sleep(4)
                    count_bullet+=4
                    level = 2

    display.update()