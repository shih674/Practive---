#!/usr/bin/env python
# coding: utf-8

# In[7]:


from pygame import font as pyfont
from pygame import transform as pytransform
from pygame import image as pyimage
from pygame import display as pydisplay
from pygame import time as pytime
from pygame import mixer as pymixer
from pygame import quit as pyquit
from pygame import mouse as pymouse
from pygame import event as pyevent
from pygame import QUIT
from pygame import MOUSEBUTTONDOWN
from random import randint
import os
'''
終極密碼
'''

class answer_sheet():
    def __init__(self):
        self.bulleye = -1
        self.lowerbd = -1
        self.upperbd = -1
        self.gameset = False
    def reset(self):
        '''
        初始化class中三大參數
        '''
        self.bulleye = randint(0,100)
        self.lowerbd = 0
        self.upperbd = 100
    def check_answer(self,user_input):
        '''
        更新最大/最小範圍
        input : user_input-int
        '''
        if user_input == self.bulleye: # 命中答案
            self.gameset = True
        if user_input < self.bulleye:
            self.lowerbd = user_input
        if user_input > self.bulleye:
            self.upperbd = user_input

class welcome_window():
    def __init__(self,win,width,height):
        self.mother_win = win
        self.x = 0
        self.y = 0
        self.width = width
        self.height= height
        self.color = (255,255,127)
        self.band = 0
        self.bg_img = None
    def init(self,path0):
        print(" <歡迎頁面>初始化\n")
        path = path0 + '\\img\\welcomeBG.jpg'
        try:
            temp = pyimage.load(path)
            self.bg_img = pytransform.scale(temp,(800,600))
        except:
            print("ERROR: 歡迎頁面背景載入錯誤\n")
        else:
            print(" <歡迎畫面>初始化完成\n")
    def change_color(self,red,green,blue):
        self.color = (red,green,blue)
    def change_band(self,new_band):
        self.band = new_band
    def redraw(self):
        self.mother_win.blit(self.bg_img,(0,0))
    def press_start(self,position):
        '''
        判斷是否有按下開始
        :input : position - list 點擊時的滑鼠位置
        :output: result - boolean 
        '''
        if 490<= position[0] and position[0] <= (490+240):
            if 180 <= position[1] and position[1] <= (180+120):
                return True
            else:
                return False
        else:
            return False
        
    def press_exit(self,position):
        '''
        判斷是否有按下離開
        :input : position - list 點擊時的滑鼠位置
        :output: result - boolean 
        '''
        if 490<= position[0] and position[0] <= (490+240):
            if 360 <= position[1] and position[1] <= (360+120):
                return True
            else:
                return False
        else:
            return False

class game_window():
    def __init__(self,win,width,height):
        self.mother_win = win
        self.x = 0
        self.y = 0
        self.width = width
        self.height= height
        self.color = (255,127,255)
        self.band = 0
        self.bg = None
        self.userinput = None
        self.font = pyfont.SysFont(None, 150) # 宣告 font 文字物件
        self.gameset_bg = None
    def init(self,path0):
        print(" <遊戲畫面> 初始化\n")
        path1 = path0 + '\\img\\gameBG.jpg'
        path2 = path0 + '\\img\\bg.png'
        try:
            temp = pyimage.load(path1)
            self.bg = pytransform.scale(temp,(800,600))
            temp = pyimage.load(path2)
            self.gameset_bg = pytransform.scale(temp,(600,450))
        except:
            print("ERROR: <遊戲畫面> 載入失敗\n")
        else:
            print(" <遊戲畫面> 初始化完成\n")
    def redraw(self,minmun,maxmum,userinput):
        self.mother_win.blit(self.bg,(0,0))
        pygameObj_minmun = self.font.render(minmun, True, (0, 0, 0)) # 渲染方法會回傳 surface 物件
        pygameObj_minmun_r = pygameObj_minmun.get_rect()
        pygameObj_minmun_r.center = (125+75,130+80)
        self.mother_win.blit(pygameObj_minmun,pygameObj_minmun_r)
        pygameObj_maxmun = self.font.render(maxmum, True, (0, 0, 0)) # 渲染方法會回傳 surface 物件
        pygameObj_maxmun_r = pygameObj_maxmun.get_rect()
        pygameObj_maxmun_r.center = (525+75,130+80)
        self.mother_win.blit(pygameObj_maxmun,pygameObj_maxmun_r)
        pygameObj_userinput = self.font.render(userinput, True, (0, 0, 0)) # 渲染方法會回傳 surface 物件
        pygameObj_userinput_r = pygameObj_userinput.get_rect()
        pygameObj_userinput_r.center = (325+75,130+80)
        self.mother_win.blit(pygameObj_userinput,pygameObj_userinput_r)
    def gameset_redraw(self,userinput):
        self.mother_win.blit(self.gameset_bg,(100,75))
        pygameObj_userinput = self.font.render(userinput, True, (200, 0, 0)) # 渲染方法會回傳 surface 物件
        pygameObj_userinput_r = pygameObj_userinput.get_rect()
        pygameObj_userinput_r.center = (400,300)
        self.mother_win.blit(pygameObj_userinput,pygameObj_userinput_r)
    def press_comfirm(self,position):
        if 540 < position[0] and position[0] < (540 + 120):
            if 430 < position[1] and position[1] < (430 + 60):
                return True
            else:
                return False
        else:
            return False
        
    def press_restart(self,position):
        '''
        判斷是否有按下<重新開始>
        :input : position - list 點擊時的滑鼠位置
        :output: result - boolean 
        '''
        x ,y ,width ,height = 525 ,20 ,120 ,60
        if x <= position[0] and position[0] <= (x + width):
            if y <= position[1] and position[1] <= (y + height):
                return True
            else:
                return False
        else:
            return False
    def press_exit(self,position):
        '''
        判斷是否有按下離開
        :input : position - list 點擊時的滑鼠位置
        :output: result - boolean 
        '''
        if 660<= position[0] and position[0] <= (660+120):
            if 20 <= position[1] and position[1] <= (20+60):
                return True
            else:
                return False
        else:
            return False
    def press_number(self,position):
        '''
        判斷是否有按下數字，包含0~9
        :input : position - list 點擊時的滑鼠位置
        :output: True,0/1/2/3/4/5/6/7/8/9 - boolean,str 
               : False,- - boolean,str
        '''
        if 460 < position[1] and position[1] < (460+100):
            if 55< position[0] and position[0] < (55+100):
                return True,'6'
            elif 175< position[0] and position[0] < (175+100):
                return True,'7'
            elif 295< position[0] and position[0] < (295+100):
                return True,'8'
            elif 415< position[0] and position[0] < (415+100):
                return True,'9'
            elif 535< position[0] and position[0] < (535+100):
                return True,'0'
            else:
                return False,'-'
        elif 340 < position[1] and position[1] < (340+100):
            if 55< position[0] and position[0] < (55+100):
                return True,'1'
            elif 175< position[0] and position[0] < (175+100):
                return True,'2'
            elif 295< position[0] and position[0] < (295+100):
                return True,'3'
            elif 415< position[0] and position[0] < (415+100):
                return True,'4'
            elif 535< position[0] and position[0] < (535+100):
                return True,'5'
            else:
                return False,'-'
        else:
            return False,'-'
    def press_backspace(self,position):
        '''
        判斷是否有按下[退格]
        :input : position - list 點擊時的滑鼠位置
        :output: True/False - boolean 
        '''
        if 655<= position[0] and position[0] <= (655+100):
            if 340 <= position[1] and position[1] <= (340+100):
                return True
            else:
                return False
        else:
            return False
    def press_send(self,position):
        '''
        判斷是否有按下[送出]
        :input : position - list 點擊時的滑鼠位置
        :output: True/False - boolean 
        '''
        if 655<= position[0] and position[0] <= (655+100):
            if 460 <= position[1] and position[1] <= (460+100):
                return True
            else:
                return False
        else:
            return False        
    
# GUI
def mainloop(width,height,title):
    '''
    主程式
    主視窗名稱 : main_window
    :input : width - int 主視窗寬度
           : height- int 主視窗高度
           : title - str 主視窗標題
    :output: none
    '''
    # 後端 ===================================
    game_on = False
    AnswerSheet = answer_sheet()
    userinput = ''
    progress_loc = os.getcwd()
    # GUI ====================================
    pyfont.init() # 初始化字型
    main_window = pydisplay.set_mode((width,height))
    pydisplay.set_caption(title)
    wel_win = welcome_window(main_window,width,height)
    wel_win.init(progress_loc)
    game_win = game_window(main_window,width,height)
    game_win.init(progress_loc)
    
    #關閉程式的程式碼
    running = True
    while running:
        
       
        pytime.delay(50) # 每27毫秒更新一次
        for event in pyevent.get():
            if event.type == QUIT:
                print(" 遊戲視窗關閉 \n")
                running = False
                        
            if event.type == MOUSEBUTTONDOWN:
                position = pymouse.get_pos()
                # <歡迎頁面>的按鍵反應
                if game_on == False:
                    if wel_win.press_start(position):
                        AnswerSheet.reset()
                        game_on = True
                    if wel_win.press_exit(position):
                        running = False
                else:
                    # <遊戲頁面>的按鍵反應
                    if AnswerSheet.gameset == False:
                        # 按下[離開]
                        if game_win.press_exit(position):
                            print(" 離開遊戲\n")
                            running = False
                        # 按下[數字紐]
                        elif game_win.press_number(position)[0]:
                            temp = game_win.press_number(position)[1]
                            if len(userinput) < 3:
                                userinput = userinput + temp
                            else:
                                print("已達長度上限\n")
                        # 按下[退格]
                        elif game_win.press_backspace(position):
                            if len(userinput) == 3:
                                temp = userinput[0]+userinput[1]
                                userinput = temp
                            elif len(userinput) == 2:
                                userinput = userinput[0]
                            elif len(userinput) == 1:
                                userinput = ''
                        # 按下[行為]
                        elif game_win.press_send(position):
                            userinput_int = int(userinput)
                            if userinput_int < AnswerSheet.lowerbd:
                                print("ERROR: smaller than lowerbound\n")
                                userinput = ''
                            elif userinput_int > AnswerSheet.upperbd:
                                print("ERROR: larger than lowerbound\n")
                                userinput = ''
                            else:
                                AnswerSheet.check_answer(userinput_int)
                                userinput = ''
                        # 按下[重新開始]
                        elif game_win.press_restart(position):
                            AnswerSheet.reset()
                            print(" Game restart\n")
                    # <遊戲結束>的按鍵反應
                    else:
                        if game_win.press_comfirm(position):
                            game_on = False
                            AnswerSheet.gameset = False
        
        # [畫面更新]
        if game_on == False:
            wel_win.redraw()
            if pymixer.music.get_busy()==False:
                pymixer.music.play()
        else:
            if AnswerSheet.gameset == True:
                pymixer.music.stop()
                game_win.gameset_redraw(str(AnswerSheet.bulleye))
            else:
                
                game_win.redraw(str(AnswerSheet.lowerbd),str(AnswerSheet.upperbd),userinput)
        pydisplay.update() # 重要! 畫面會更新的關鍵    

# 一些常數
window_width,window_height = 800,600
window_title = ' 終極密碼'

# 放音樂
pymixer.init()
try:
    tempPath = os.getcwd() + "\\bgm\\On_My_Way_Home.mp3"
    pymixer.music.load(tempPath)
except:
    print(" <背景音樂> 載入失敗\n")
else:
    print(" <背景音樂> 載入完成\n")
# mainloop        
mainloop(window_width,window_height,window_title)
pyquit()     


# In[ ]:




