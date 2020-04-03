import pygame
from tkinter import *

SZ = 15
INF = 9999999999999999999999999999999999999999999999999999
MAX_STEP = 2


EMPTY = 0
BLACK = 1
WHITE = 2

black_color = [0, 0, 0]
# 定义黑色（黑棋用，画棋盘）
white_color = [255, 255, 255]
# 定义白色（白棋用）
background = [255,244,241]

red = [255,0,0]

class goLong:
    def __init__(self):
        self.g_map = [[0 for y in range(0,SZ)] for x in range(0,SZ)]
        self.cur_step = 0

    def reset(self,screen,start_screen2):
        for row in range(0,SZ):
            for j in range(0,SZ):
                self.g_map[row][j] = 0
        screen.blit(start_screen2, (0, 0))
        self.draw(screen)
        pygame.display.flip()

    def draw(self, screen):
        for h in range(1, SZ+1):
            pygame.draw.line(screen, black_color,
                             [40, h * 40], [600, h * 40], 1)
            pygame.draw.line(screen, black_color, [40 * h, 40], [40 * h, 600], 1)
        # 给棋盘加一个外框，使美观
        pygame.draw.rect(screen, black_color, [36, 36, 568, 568], 3)
        # 在棋盘上标出，天元以及另外4个特殊点位
        pygame.draw.circle(screen, black_color, [320, 320], 5, 0)
        pygame.draw.circle(screen, black_color, [160, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [160, 480], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 160], 3, 0)
        pygame.draw.circle(screen, black_color, [480, 480], 3, 0)
        # 做2次for循环取得棋盘上所有交叉点的坐标
        for row in range(0,SZ):
            for col in range(0,SZ):
                # 将下在棋盘上的棋子画出来
                if self.g_map[row][col] != EMPTY:
                    ccolor = black_color \
                        if self.g_map[row][col] == BLACK else white_color
                    # 取得这个交叉点下的棋子的颜色，并将棋子画出来
                    pos = [40 * (col + 1), 40 * (row + 1)]
                    # 画出棋子
                    pygame.draw.circle(screen, ccolor, pos, 18, 0)
                    if (row == self.AI_x and col == self.AI_y):
                        pygame.draw.circle(screen, red, pos, 4, 0)

    def move(self,row,col):
        if self.g_map[row][col] == EMPTY:
            self.g_map[row][col] = BLACK
            return True
        return False
        '''
        while(True):
            try :
                pos_x = int(input(" x : "))
                pos_y = int(input(" y : "))
                if (0<=(pos_x)<SZ and 0<=(pos_y)<SZ):
                    if(self.g_map[pos_x][pos_y] == 0):
                        self.g_map[pos_x][pos_y] = 1
                        self.cur_step += 1
                        return
            except ValueError :
                continue;
        '''
    def game_resualt(self):

        # 横向
        for i in range(0,SZ):
            for j in range(0,SZ-4):
                if (self.g_map[i][j] == 0):
                    continue
                now_color = self.g_map[i][j]
                f = 0;
                for k in range(0,5):
                    if(self.g_map[i][j+k] == now_color):
                        f+=1
                if(f >= 5):
                    return now_color
         #纵向
        for i in range(0,SZ-4):
            for j in range(0,SZ):
                if (self.g_map[i][j] == 0):
                    continue
                now_color = self.g_map[i][j]
                f = 0
                for k in range(0,5):
                    if(self.g_map[i+k][j] == now_color):
                        f += 1
                if(f >= 5):
                    return now_color
        #斜向
        for i in range(0,SZ-4):
            for j in range(0,SZ-4):
                if(self.g_map[i][j] ==0):
                    continue
                now_color = self.g_map[i][j]
                f = 0
                for k in range(0,5):
                    if(self.g_map[i+k][j+k] == now_color):
                        f += 1
                if(f >= 5):
                    return now_color
        #反斜线
        for i in range(0, SZ-4):
            for j in range(4, SZ ):
                if (self.g_map[i][j] == 0):
                    continue
                now_color = self.g_map[i][j]
                f = 0
                for k in range(0, 5):
                    if (self.g_map[i + k][j - k] == now_color):
                        f += 1
                if (f >= 5):
                    return now_color
               # print(i," + ",j," + ",f)
        return 0

    def judge(self,i,j):
        for k in range(i-1,i+2):
            for l in range(j-1,j+2):
                if(0<=k<=SZ-1 and 0<=l<=SZ-1 and self.g_map[k][l] !=0):
                    return 1
        return 0

    def getScore(self,jue): # 1    2      3         4        5              1    2      3        4         5
        #scoreList1 = [[],[0 ,100 ,10000 ,1000000 ,100000000 ,100000000],[0 ,10 ,1000 ,100000  ,10000000 ,1000000000 ]]# 活
        #scoreList2 = [[],[0 ,10  ,100,   10000 , 50000000,   100000000],[0, 1 , 10  , 1000    ,10000000 ,1000000000 ]]  # 死
                    #人：     1    2     3        4          5                           1   2     3         4            5
        scoreList1 = [[], [0 ,10 ,100000 , 1000000000   ,10000000000000 ,10000000000000000000 ,1000000000000000000000000],[0 ,1000 ,10000000  ,100000000000 ,1000000000000000  ,1000000000000000000000000,1000000000000000000000000]]  # 活
        scoreList2 = [[], [0, 1 , 10000  , 100000000    ,1000000000000  ,1000000000000000000  ,1000000000000000000000000],[0  ,100  ,1000000,   10000000000 , 100000000000000,   1000000000000000000000000   ,1000000000000000000000000]]  # 死
        sum = 0

        #横向得分

        for i in range(0, SZ):
            j = 0
            while j < SZ:
                if (self.g_map[i][j] == jue):
                    now_j = j
                    f = 0
                    while 0<=j<=SZ-1 and self.g_map[i][j] == jue:
                        f += 1
                        j += 1
                    if j == SZ or self.g_map[i][j] == 3-jue:
                        if now_j == 0 or self.g_map[i][now_j-1] == 3-jue:
                            if f == 5:
                                sum += scoreList2[jue][5]
                            else:
                                sum += 0
                        else :
                            sum +=  scoreList2[jue][f]
                    else:
                        if now_j == 0 or self.g_map[i][now_j-1] == 3-jue:
                            try:
                                sum += scoreList2[jue][f]
                            except Exception:
                                print(i,j,f," !!!!!!!!!!!!!!!!!!!!!!!!!!! ")
                        else :
                            sum +=  scoreList1[jue][f]
                else:
                    j += 1


        # 纵向得分
        for j in range(0, SZ):
            i = 0
            while i<SZ:
                if (self.g_map[i][j] == jue):
                    now_i = i
                    f = 0
                    while 0 <= i <= SZ - 1 and self.g_map[i][j] == jue:
                        f += 1
                        i += 1
                    if i == SZ or self.g_map[i][j] == 3 - jue:
                        if now_i == 0 or self.g_map[now_i-1][j] == 3 - jue:
                            if f == 5:
                                sum += scoreList2[jue][5]
                            else:
                                sum += 0
                        else:
                            sum +=  scoreList2[jue][f]
                    else:
                        if now_i == 0 or self.g_map[now_i-1][j] == 3 - jue:
                            sum += scoreList2[jue][f]
                        else:
                            sum += scoreList1[jue][f]
                else:
                    i += 1
             
        
        # 斜向得分
        for i in range(0,SZ):
            now_j = 0
            now_i = i
            while now_j < SZ and now_i < SZ:
                if (self.g_map[now_i][now_j] == jue):
                    cur_i = now_i
                    cur_j = now_j
                    f = 0
                    while 0 <= now_i <= SZ - 1 and 0<=now_j<SZ and self.g_map[now_i][now_j] == jue:
                        f += 1
                        now_i += 1
                        now_j += 1
                    #print(now_i, " !!! ", now_j,f)
                    if now_i == SZ or  now_j == SZ or self.g_map[now_i][now_j] == 3 - jue:
                        if cur_i == 0 or cur_j == 0 or self.g_map[cur_i - 1][cur_j-1] == 3 - jue:
                            if f == 5:
                                sum += scoreList2[jue][5]
                            else:
                                sum += 0
                        else:
                            sum += scoreList2[jue][f]
                    else:
                        if cur_i == 0 or cur_j == 0 or self.g_map[cur_i - 1][cur_j-1] == 3 - jue:
                            sum += scoreList2[jue][f]
                        else:
                            sum += scoreList1[jue][f]
                else:
                    now_i += 1
                    now_j += 1
        for j in range(1,SZ):
            now_j = j
            now_i = 0
            while now_i<SZ and now_j<SZ:
                if(self.g_map[now_i][now_j] == jue):
                    cur_i = now_i
                    cur_j = now_j
                    f = 0
                    while 0 <= now_i <= SZ - 1 and 0 <= now_j < SZ and self.g_map[now_i][now_j] == jue:
                        f += 1
                        now_i += 1
                        now_j += 1
                    if now_i == SZ or now_j == SZ or self.g_map[now_i][now_j] == 3 - jue:
                        if cur_i == 0 or cur_j == 0 or self.g_map[cur_i - 1][cur_j - 1] == 3 - jue:
                            if f == 5:
                                sum += scoreList2[jue][5]
                            else:
                                sum += 0
                        else:
                            sum += scoreList2[jue][f]
                    else:
                        if cur_i == 0 or cur_j == 0 or self.g_map[cur_i - 1][cur_j - 1] == 3 - jue:
                            sum += scoreList2[jue][f]
                        else:
                            sum += scoreList1[jue][f]
                else:
                    now_i += 1
                    now_j += 1


        # 反斜向得分
        for i in range(0, SZ):
            now_j = SZ-1
            now_i = i
            while now_j >= 0  and now_i < SZ:
                if (self.g_map[now_i][now_j] == jue):
                    cur_i = now_i
                    cur_j = now_j
                    f = 0
                    while 0 <= now_i <= SZ - 1 and 0 <= now_j < SZ and self.g_map[now_i][now_j] == jue:
                        f += 1
                        now_i += 1
                        now_j -= 1
                    #print(now_i, " !!! ", now_j,f)
                    if now_i == SZ or now_j == -1 or self.g_map[now_i][now_j] == 3 - jue:
                        if cur_i == 0 or cur_j == SZ-1 or self.g_map[cur_i - 1][cur_j + 1] == 3 - jue:
                            if f == 5:
                                sum += scoreList2[jue][5]
                            else:
                                sum += 0
                        else:
                            sum += scoreList2[jue][f]
                    else:
                        if cur_i == 0 or cur_j == SZ-1 or self.g_map[cur_i - 1][cur_j + 1] == 3 - jue:
                            sum += scoreList2[jue][f]
                        else:
                            sum += scoreList1[jue][f]
                else:
                    now_i += 1
                    now_j -= 1
        for j in range(0, SZ-1):
            now_j = j
            now_i = 0
            while now_j >= 0 and now_i < SZ:
                if (self.g_map[now_i][now_j] == jue):
                    cur_i = now_i
                    cur_j = now_j
                    f = 0
                    while 0 <= now_i <= SZ - 1 and 0 <= now_j < SZ and self.g_map[now_i][now_j] == jue:
                        f += 1
                        now_i += 1
                        now_j -= 1
                    #print(now_i, " !!! ", now_j,f)
                    if now_i == SZ or now_j == -1 or self.g_map[now_i][now_j] == 3 - jue:
                        if cur_i == 0 or cur_j == SZ-1 or self.g_map[cur_i - 1][cur_j + 1] == 3 - jue:
                            if f==5:
                                sum += scoreList2[jue][5]
                            else:
                                sum += 0
                        else:
                            sum += scoreList2[jue][f]
                    else:
                        if cur_i == 0 or cur_j == SZ-1 or self.g_map[cur_i - 1][cur_j + 1] == 3 - jue:
                            sum += scoreList2[jue][f]
                        else:
                            sum += scoreList1[jue][f]
                else:
                    now_i += 1
                    now_j -= 1

        return sum


    def dfs(self,step,alpha, beta):
        if(step == MAX_STEP):
            return self.getScore(2)-self.getScore(1)
        list = []
        for i in range(0,SZ):
            for j in range(0,SZ):
                 if(self.g_map[i][j] == 0 and self.judge(i,j) ):
                     list.append((i,j))
        #print(list)
        if(step %2 == 1):
            for son in list:
                self.g_map[son[0]][son[1]] = 1;
                s = self.dfs(step+1,alpha,beta)
                self.g_map[son[0]][son[1]] = 0;
                if(s < beta):
                    beta = s
                    if(alpha >= beta):
                        return alpha
                    if(step == 0):
                        (self.AI_x ,self.AI_y)= son
            return beta
        else:
            for son in list:
                self.g_map[son[0]][son[1]] = 2;
                s = self.dfs(step+1,alpha,beta)
                self.g_map[son[0]][son[1]] = 0;
                if(s > alpha):
                    alpha = s
                    if(alpha >= beta):
                        return beta
                    if(step == 0):
                        (self.AI_x ,self.AI_y)= son
            return  alpha

    def dfs2(self,step,sson):
        if (step == MAX_STEP):
            #self.show()
            #print(self.getScore(2)," --------》 " ,self.getScore(1),sson)
            return self.getScore(2) - self.getScore(1)
        list = []
        for i in range(0, SZ):
            for j in range(0, SZ):
                if (self.g_map[i][j] == 0 and self.judge(i, j)):
                    list.append((i, j))
        #print(step," : ++++++")
        #print(list)
        if (step % 2 == 0):
            Max = -INF
            for son in list:
                #print("put:  --------------->  ",son)
                self.g_map[son[0]][son[1]] = 2;
                s = self.dfs2(step + 1,son)
                self.g_map[son[0]][son[1]] = 0;
                #print("unput : ----------------->",son)
                #print()
                if(s >= Max):
                    Max = s
                    if (step == 0):
                        (self.AI_x, self.AI_y) = son
            return Max
        else:
            Min = INF
            for son in list:
                #print("put:  --------------->  ", son)
                self.g_map[son[0]][son[1]] = 1;
                s = self.dfs2(step + 1,son)
                self.g_map[son[0]][son[1]] = 0;
                #print("unput : ----------------->", son)
                #print()
                if (s <= Min):
                    Min = s
                    if (step == 0):
                        (self.AI_x, self.AI_y) = son
           # print(Min," MinMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMINMIN")
            return Min
    def ai_move(self):
        #self.dfs2(0,(0,0))
        self.dfs(0,-INF,INF)
        (x,y) = (self.AI_x,self.AI_y)
        self.g_map[x][y] = 2;
        self.cur_step += 1
        print("My AI occupied : ",x,y)

        return

    def prt(self,x,i,j):
        if(x == 2):
            print("○".center(3),end = "");
        elif(x == 1):
            print("●".center(3),end= "")
        elif i == 0 and j == 0:
            print("┌".center(3), end="")
        elif (i == 0 and j == SZ - 1):
            print("┐".center(3), end="")

        elif i == SZ - 1 and j == 0:
            print("└".center(3), end="")

        elif i == SZ - 1 and j == SZ - 1:
            print("┘".center(3), end="")
        elif i == 0:
            print("┬".center(3),end = "")
        elif j == 0:
            print("├".center(3),end = "")
        elif i == SZ-1:
            print("┴".center(3),end = "")
        elif j == SZ-1:
            print("┤".center(3),end = "")
        else:
            print("┼".center(3),end = "")


    def play(self):
        self.AI_x = 7
        self.AI_y = 7
        pygame.init()
        kc = pygame.image.load("./image/tim.png")
        pygame.display.set_icon(kc)
        pygame.display.set_caption('zxf 的 人工智障')  # 改标题
        screen = pygame.display.set_mode((1050, 640))
        i0 = pygame.image.load("./image/bgg.jpg")
        i0.convert()
        screen.blit(i0,(0,0))
        clock = pygame.time.Clock()
        start_screen = pygame.Surface(screen.get_size())  
        start_screen2 = pygame.Surface(screen.get_size())
        start_screen = start_screen.convert()
        start_screen2 = start_screen2.convert()
        start_screen_lose = pygame.Surface(screen.get_size())  
        start_screen_win = pygame.Surface(screen.get_size()) 
        start_screen_lose = start_screen_lose.convert()
        start_screen_win = start_screen_win.convert()

        start_screen.blit(i0,(0,0)) 
        start_screen2.fill([255,192,205])
        start_screen_lose.fill([255,192,205])
        start_screen_win.fill([255,192,205])

        i2 = pygame.image.load("./image/reset.png")
        i2.convert()
        start_screen2.blit(i2,(640,40))
        i1 = pygame.image.load("./image/start.png")
        i1.convert()
        i3 = pygame.image.load("./image/lose.png")
        i3.convert()
        i4 = pygame.image.load("./image/win.png")
        i4.convert()
        i5 = pygame.image.load("./image/draw.png")
        i5.convert()
        start_screen2.blit(i5,(640,240))
        start_screen_lose.blit(i3,(640,240))
        start_screen_lose.blit(i2, (640, 40))
        start_screen_win.blit(i2, (640, 40))
        start_screen_win.blit(i4,(640,240))
        #self.draw(screen)  # 给棋盘类发命令，调用draw()函数将棋盘画出来
        pygame.display.flip()  # 刷新窗口显
       #print(" ************ ")
        ff = 0
        n1 = True
        while n1:
            clock.tick(10)
            buttons = pygame.mouse.get_pressed()
            x1, y1 = pygame.mouse.get_pos()
            if x1 >= 400 and x1 <= 728 and y1 >= 300 and y1 <= 366:
                start_screen.blit(i1, (400, 300))
                if buttons[0]:
                    n1 = False
            else:
                start_screen.blit(i1, (400, 300))
            screen.blit(start_screen, (0, 0))
            pygame.display.update()
            # 监听退出动作
            for event in pygame.event.get():
                # 判断事件类型是否是退出事件
                if event.type == pygame.QUIT:
                    print("游戏退出...")
                    pygame.quit()
                    exit()

        screen.blit(start_screen2,(0,0))
        self.draw(screen)
        pygame.display.update()

        running = True
        while running:
            ff  = 0
            # 遍历建立窗口后发生的所有事件
            for event in pygame.event.get():
                # 根据事件的类型
                ff = 0
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYUP:
                    pass
                # pygame.MOUSEBUTTONDOWN表示鼠标的键被按下
                elif event.type == pygame.MOUSEBUTTONDOWN and \
                        event.button == 1:  # button表示鼠标左键
                    x, y = event.pos  # 拿到鼠标当前在窗口上的位置坐标
                    # 将鼠标的(x, y)窗口坐标，转化换为棋盘上的坐标
                    if 640<=x<=720 and 45<=y<=115:
                        self.reset(screen,start_screen2)
                    elif 0<=x<=600 and 0<=y<=600:
                        row = round((y - 40) / 40)
                        col = round((x - 40) / 40)
                        if(self.g_map[row][col] != 0):
                            continue;
                        self.move(row, col)
                        screen.blit(start_screen2,(0,0))
                        self.draw(screen)
                        pygame.display.flip()
                        # 调用判断胜负函数
                        #screen.blit(i2, (700, 40))
                        res = self.game_resualt()
                        #self.ck(res,screen,start_screen2)
                        if res == 1 or res == 2:
                            if res == 1:
                                screen.blit(start_screen_win, (0, 0))
                                self.draw(screen)
                                pygame.display.flip()
                            if (res == 2):
                                screen.blit(start_screen_lose, (0, 0))
                                self.draw(screen)
                                pygame.display.flip()
                            Rr = True
                            while Rr:
                                # 遍历建立窗口后发生的所有事件
                                for event in pygame.event.get():
                                    # 根据事件的类型
                                    if event.type == pygame.MOUSEBUTTONDOWN and \
                                            event.button == 1:  
                                        x, y = event.pos  # 拿到鼠标当前在窗口上的位置坐标
                                        # 将鼠标的(x, y)窗口坐标，转化换为棋盘上的坐标
                                        if 640 <= x <= 720 and 45 <= y <= 115:
                                            self.reset(screen, start_screen2)
                                            Rr = False
                                            ff = 1
                                        # 判断事件类型是否是退出事件
                                    if event.type == pygame.QUIT:
                                        print("游戏退出...")
                                        pygame.quit()
                                        exit()

                        if(ff != 1):
                            self.ai_move()
                            screen.blit(start_screen2,(0,0))
                            #screen.blit(i2, (700, 40))
                            self.draw(screen)
                            pygame.display.flip()
                            # 调用判断胜负函数
                            res = self.game_resualt()
                            #self.ck(res,screen,start_screen2)
                            if res == 1 or res == 2:
                                if res == 1:
                                    screen.blit(start_screen_win, (0, 0))
                                    self.draw(screen)
                                    pygame.display.flip()
                                if (res == 2):
                                    screen.blit(start_screen_lose, (0, 0))
                                    self.draw(screen)
                                    pygame.display.flip()
                                Rr = True
                                while Rr:
                                    # 遍历建立窗口后发生的所有事件
                                    for event in pygame.event.get():
                                        # 根据事件的类型
                                        if event.type == pygame.MOUSEBUTTONDOWN and \
                                                event.button == 1:  # button表示鼠标左键
                                            x, y = event.pos  # 拿到鼠标当前在窗口上的位置坐标
                                            # 将鼠标的(x, y)窗口坐标，转化换为棋盘上的坐标
                                            if 640 <= x <= 720 and 45 <= y <= 115:
                                                self.reset(screen, start_screen2)
                                                Rr = False
                                        if event.type == pygame.QUIT:
                                            print("游戏退出...")
                                            pygame.quit()
                                            exit()
                        else:
                            ff = 0

                    else:
                        continue
        pygame.quit()

        '''
        self.show()
        while (True):
            try:
                self.move()
                self.show()
                res = self.game_resualt()
                if (res != 0):
                    screen(res)
                    break
                self.ai_move()
                self.show()
                res = self.game_resualt()
                if (res != 0):
                    screen(res)
                    break
                a = self.getScore(2)
                b = self.getScore(1)
                print("人机胜算 : ",(a*100/(a+b)),"%")
                print("你的胜算 : ",(b*100/(a+b)),"%")
            except ValueError:
                continue
        '''
    def show(self):
        print("   ",end = "")
        for i in range(0,SZ):
            if i!=0 :
                print("   ",end = "")
            print(str(i).rjust(2),end = "")
        print()
        for i in range(0,SZ):
            print(str(i).ljust(2), end="")
            for j in range(0,SZ):
                if j!=0:
                    print("-",end = "")
                self.prt(self.g_map[i][j],i,j)
            print()
            if(i != SZ-1):
                print("  ", end="")
                for j in range(0,SZ):
                    print("┃".center(3)+" ",end = "")
            print()
    def ck(self,x,screen,start_screen2):
        i1 = pygame.image.load("./image/lose.png")
        i1.convert()
        if(x == 2):
            screen.blit(start_screen2, (0, 0))
            screen.blit(i1,(820,40))
            self.draw(screen)
            pygame.display.flip()

            print("！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
            print("！！！！！！！！！！！！！！ You have been beaten by my AI！！！！！！！！！！！！！！！")
            print("！！！！！！！！！！！！！！！！！！ What is a pity ！！！！！！！！！！！！！！！！！！")
            print("！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")

        elif(x == 1):
            print("！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")
            print("！！！！！！！！！！！！！！ You have beaten my stdupid AI！！！！！！！！！！！！！！！")
            print("！！！！！！！！！！！！！！！！！！Congratulation  ！！！！！！！！！！！！！！！！！！")
            print("！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！！")

