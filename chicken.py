import time
import pygame as py
from sys import exit
import sys
import res.setting.setting as color
import random
from time import sleep
import os
#获取绝对路径
last_path=os.path.dirname(os.path.realpath(sys.argv[0]))
list=os.listdir(last_path)
abs_path=''
for i in list:
    full_path=os.path.join(last_path,i)
    if not os.path.isfile(full_path):
        abs_path = full_path
#创建Smallchicken精灵
class Smallchicken(py.sprite.Sprite):
    def __init__(self,image,speed):
        super().__init__()
        self.image=image
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0,screen_rect.width-self.rect.width)
        self.speed=speed
    def fall(self):
        self.rect.y +=self.speed
class Smallchicken2(py.sprite.Sprite):
    def __init__(self,speed):
        super().__init__()
        self.image = small_chicken2_left_image
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0,screen_rect.width-self.rect.width)
        self.speed=speed - 4
        self.speed_low = True
        self.turn_num = 0
        if self.rect.centerx <= screen_rect.centerx:
            self.image = small_chicken2_right_image
            self.forword = 1
        else:
            self.image = small_chicken2_left_image
            self.forword = 2
    def turning(self):
        if self.turn_num <= 3:
            if self.forword == 1:
                self.image = py.transform.rotate(self.image,10).convert_alpha()#rotate方法默认为逆时针旋转
            else:
                self.image = py.transform.rotate(self.image,-10).convert_alpha()#如需顺时针旋转可指定angle参数为负数
            self.turn_num += 1
    def fall(self):
        self.rect.y +=self.speed
        if self.rect.centery >= (screen_rect.centery/2):
            if self.speed_low:
                self.speed += 4
                self.speed_low = False
            if self.forword == 1:
                self.rect.x +=self.speed
                self.turning()
            else:
                self.rect.x -=self.speed
                self.turning()
        if self.rect.top > screen_rect.bottom:
            self.kill()

class Upper(py.sprite.Sprite):
    def __init__(self,image,speed):
        super().__init__()
        self.image = image
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.centerx = chicken_rect.centerx
        self.rect.bottom = chicken_rect.top
        upper_group.add(self)
    def go_up(self):
        self.rect.y -= self.speed
        if self.rect.bottom < 0:
            upper_group.remove(self)
        move_egg = 1
#创建函数
def born_fall_object1(image,speed,group):
    fall_object = Smallchicken(image,speed)
    group.add(fall_object)
def born_fall_object2(speed,group):
    fall_object = Smallchicken2(speed)
    group.add(fall_object)
#下落函数
def fall(group):
    for i in group:
        i.fall()
        if i.rect.top > screen_rect.bottom:
            group.remove(i)
#发射函数
def fire():
    egg_upper = Upper(up_egg_image, 5)
    egg_upper_list.append(egg_upper)

#显示指定文本函数
def present(content,size,color):
    content_font=py.font.SysFont(None,size)
    content_img = content_font.render(content,True,color)
    content_rect=content_img.get_rect()
    content_rect.center = screen_rect.center
    screen.blit(content_img,content_rect)
    py.display.update()
    return content_rect.midbottom
def present_gameover():
    midbottom = present('GAMEOVER!', 150, 'red')
    content_font = py.font.SysFont(None,80)
    content_img = content_font.render('Press r to replay or press q to exit',True,'blue')
    content_rect = content_img.get_rect()
    content_rect.midtop = midbottom
    screen.blit(content_img,content_rect)
    py.display.update()
#声明特定属性


#初始化
py.init()
py.mixer.init()
sound1=py.mixer.Sound(abs_path+'/sounds/kunkun1.mp3')
sound2=py.mixer.Sound(abs_path+'/sounds/jump.mp3')
sound2.set_volume(0.5)
sound3=py.mixer.Sound(abs_path+'/sounds/鸡.mp3')
sound4=py.mixer.Sound(abs_path+'/sounds/迎面走来的你.mp3')
sound4.set_volume(0.5)
sound5=py.mixer.Sound(abs_path+'/sounds/再近一点.mp3')
sound5.set_volume(0.5)
sound6=py.mixer.Sound(abs_path+'/sounds/鸡你太美.mp3')
sound7=py.mixer.Sound(abs_path+'/sounds/篮球.mp3')
sound8=py.mixer.Sound(abs_path+'/sounds/下蛋.mp3')
py.mixer.music.load(abs_path+'/sounds/游戏背景1.mp3')#加载背景音
py.mixer.music.set_volume(0.6)

#创建时钟指定帧数
clock=py.time.Clock()
#创建事件常量
SMALLCHICKEN_BORN=py.USEREVENT
BALL_BORN=py.USEREVENT+1
SPEED_UP_BORN = py.USEREVENT + 2
EGG_BORN = py.USEREVENT + 3
SMALLCHICKEN2_BORN = py.USEREVENT + 4

new_start = 1

def start_game():
    global screen, screen_rect, chicken_rect, upper_group, fall_egg_image,up_egg_image,small_chicken2_left_image,small_chicken2_right_image,new_start,egg_upper_list,move_egg
    # 设置定时器
    interval = 500
    ball_interval = random.randint(8000, 20000)
    speed_up_interval = random.randint(28000, 35000)
    interval2 = random.randint(10000,15000)
    py.time.set_timer(SMALLCHICKEN_BORN, 500)
    py.time.set_timer(BALL_BORN, ball_interval)
    py.time.set_timer(SPEED_UP_BORN, speed_up_interval)
    py.time.set_timer(EGG_BORN, 25000)
    py.time.set_timer(SMALLCHICKEN2_BORN,interval2)

    #显示窗口
    screen=py.display.set_mode((800,1000),py.FULLSCREEN)#(x,y) 第二个参数FULLSCREEN表示全屏
    # 加载图像
    #.convert_alpha()方法能够保留png的透明度信息,使用前要先使用set_mode()加载窗口
    chicken1_image = py.image.load(abs_path + '/images/chicken.png').convert_alpha()
    chicken2_image = py.image.load(abs_path + '/images/chicken2.png').convert_alpha()
    small_chicken_image = py.image.load(abs_path + '/images/small_chicken.png').convert_alpha()
    ball_image = py.image.load(abs_path + '/images/ball.png').convert_alpha()
    speed_up_image = py.image.load(abs_path + '/images/speed_up.png').convert_alpha()
    fall_egg_image = py.image.load(abs_path + '/images/egg.png').convert_alpha()
    up_egg_image = py.transform.scale(fall_egg_image,(100,150))
    bg1_image = py.image.load(abs_path + '/images/bg2.png').convert_alpha()
    small_chicken2_left_image = py.image.load(abs_path + '/images/small_chicken2_left.png').convert_alpha()
    small_chicken2_right_image = py.image.load(abs_path + '/images/small_chicken2_right.png').convert_alpha()

    score = 0
    small_chicken2_speed = 6
    ball_speed = 4
    minspeed = 3
    maxspeed = 6
    yourspeed = 5
    egg_num = 1
    global egg_upper
    egg_upper = 0
    egg_upper_list =[]
    move_egg = 0
    speed_up1 = 1
    speed_up2 = 1
    speed_up3 = 1
    speed_up4 = 1
    speed_up5 = 1

    #初始化精灵组
    small_chicken_group=py.sprite.Group()
    ball_group=py.sprite.Group()
    speed_up_group = py.sprite.Group()
    egg_group = py.sprite.Group()
    upper_group = py.sprite.Group()

    #文本设置
    txt_font=py.font.SysFont(None,40)#字体设置,(name,size)

    #使bg_image适配全屏显示
    screen_width,screen_height = screen.get_size()
    bg1_image = py.transform.scale(bg1_image,(screen_width,screen_height))#使用transform.scale方法转换image尺寸

    #get_rect()获取位置信息
    screen_rect=screen.get_rect()
    chicken_rect=chicken1_image.get_rect()
    egg_rect = fall_egg_image.get_rect()
    egg_rect.bottomleft=screen_rect.bottomleft
    #使chicken显示于屏幕底部中心
    chicken_rect.center=screen_rect.center
    chicken_rect.bottom=screen_rect.bottom
    #创建you精灵
    you1=py.sprite.Sprite()
    you2=py.sprite.Sprite()
    you_group = py.sprite.Group()
    you1.image=chicken1_image
    you2.image=chicken2_image
    you_group.add(you1)
    #设置标题
    py.display.set_caption('chicken')
    #背景颜色填充

    '''
    buttle_rect=py.Rect(0,0,50,60) #(x,y,weidh,heigh)
    py.draw.rect(screen,'red',buttle_rect) #draw.rect(幕布,颜色,画的物体)
    '''

    #设置音量播放背景音乐
    py.mixer.music.set_volume(1)
    py.mixer.music.play(-1)#参数-1表示无限循环
    going = 1#控制游戏暂停
    #游戏循环

    while 1:
        while going:
            clock.tick(color.ZHENSHU)#设置帧数
            small_chicken_speed=random.randint(minspeed,maxspeed)
            txt = txt_font.render(f'Score:{score}', True, 'red', 'yellow')  # 渲染成图像 ('文本',True,字体色，背景色)
            txt_rect = txt.get_rect()

            py.display.update()
            for event in py.event.get():#事件监视
                if event.type== py.QUIT:#点击关闭
                    exit()
                elif event.type==SMALLCHICKEN_BORN:
                    born_fall_object1(small_chicken_image, small_chicken_speed, small_chicken_group)
                elif event.type==BALL_BORN:
                    born_fall_object1(ball_image, ball_speed, ball_group)
                elif event.type == SPEED_UP_BORN:
                    born_fall_object1(speed_up_image, 5, speed_up_group)
                elif event.type == EGG_BORN:
                    born_fall_object1(fall_egg_image, 5, egg_group)
                elif event.type == SMALLCHICKEN2_BORN:
                    born_fall_object2( small_chicken2_speed, small_chicken_group)
                elif event.type == py.KEYDOWN:
                    if event.key == py.K_p:
                        present('press p to continue or press q to exit',95,'white')
                        going = 0
            keys_pressed=py.key.get_pressed()#key.get_pressed返回键盘按下情况的元组
            if keys_pressed[py.K_LEFT] and chicken_rect.x>0:
                chicken_rect.x -= yourspeed
                if you2 in you_group:
                    you_group.remove(you2)
                    you_group.add((you1))
            elif keys_pressed[py.K_RIGHT] and chicken_rect.right<screen_rect.width:
                chicken_rect.x += yourspeed
                if you1 in you_group:
                    you_group.remove(you1)
                    you_group.add(you2)
            elif keys_pressed[py.K_SPACE]:
                if egg_num == 1:
                    sound2.play()
                    egg_num = 0
                    fire()


            elif keys_pressed[py.K_q]:#q键退出
                exit()
            you1.rect = chicken_rect
            you2.rect = chicken_rect

            # 绘值背景,txt
            #screen.fill(color.bgcolor)
            screen.blit(bg1_image,(0,0))
            screen.blit(txt, txt_rect)
            if egg_num == 1:
                screen.blit(fall_egg_image, egg_rect)
            you_group.draw(screen)
            chicken_rect.bottom=screen_rect.bottom
            small_chicken_group.draw(screen)#将精灵组中精灵绘制在screen上
            ball_group.draw(screen)
            speed_up_group.draw(screen)
            egg_group.draw(screen)
            upper_group.draw(screen)

            while new_start:
                present('click anywhere to start',120,(173,216,230))
                for event in py.event.get():
                    if event.type == py.MOUSEBUTTONDOWN:#捕获鼠标点击
                        new_start = 0
                    elif event.type == py.KEYDOWN:
                        if event.key == py.K_q:
                            exit()

            # 在分数达到特定值后加速
            if (score >= 80 and score < 150) and speed_up1:
                speed_up1=0
                sound4.play()
                interval -= 50
                minspeed += 1
                maxspeed += 1
                py.time.set_timer(SMALLCHICKEN_BORN, interval)
            if (score >= 150 and score < 250) and speed_up2:
                speed_up2=0
                sound4.play()
                interval -= 50
                minspeed += 1
                maxspeed += 1
                py.time.set_timer(SMALLCHICKEN_BORN, interval)
            if (score >= 250 and score <350) and speed_up3:
                speed_up3=0
                sound5.play()
                minspeed += 1
                maxspeed += 1
                small_chicken2_speed += 1
                interval -= 70
                py.time.set_timer(SMALLCHICKEN_BORN, interval)
            if (score >= 350 and score <500) and speed_up4:
                speed_up3=0
                sound5.play()
                minspeed += 1
                maxspeed += 1
                small_chicken2_speed += 1
                interval -= 70
                py.time.set_timer(SMALLCHICKEN_BORN, interval)
            if score >= 500 and speed_up5:
                speed_up5 = 0
                sound6.play()
                minspeed += 5
                maxspeed += 5
                small_chicken2_speed += 5
                interval -= 120
                py.time.set_timer(SMALLCHICKEN_BORN, interval)
            #让精灵移动
            for smck in small_chicken_group:
                smck.fall()
                if smck.rect.top > screen_rect.bottom:
                    small_chicken_group.remove(smck)
                    score += 1

            #凋落物下降
            fall(ball_group)
            fall(speed_up_group)
            fall(egg_group)
            #发射物上升
            if len(egg_upper_list) > 0:
                for egg_uppers in egg_upper_list:
                    egg_uppers.go_up()
                    if move_egg == 1:
                        egg_upper_list.pop(0)
                        move_egg = 0

            #碰撞检测
            if py.sprite.spritecollide(you1, ball_group, True):
                sound7.play()
                score += 15
            if py.sprite.spritecollide(you1,speed_up_group,True):
                sound2.play()
                yourspeed += 2
            if py.sprite.spritecollide(you1,egg_group,True):
                if egg_num == 0:
                    egg_num = 1
                    sound8.play()
            if py.sprite.groupcollide(upper_group,small_chicken_group,False,True):
                sound3.play()
                score += 2.5
            if py.sprite.spritecollide(you1, small_chicken_group, False):#精灵和精灵组碰撞检测
                py.mixer.music.pause()#背景音暂停
                sound1.play()#播放音效
                #present('GAMEOVER!',150,'red')
                present_gameover()
                while 1:
                    for event in py.event.get():
                        if event.type == py.KEYDOWN:
                            if event.key == py.K_r:
                                sound1.stop()
                                time.sleep(0.5)
                                start_game()
                            if event.key == py.K_q:
                                exit()
        while not going:
            for event in py.event.get():
                if  event.type == py.KEYDOWN:
                    if event.key == py.K_p:
                        going = 1
                    if event.key == py.K_q:
                        exit()

#运行游戏
start_game()