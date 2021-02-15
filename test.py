import pygame
from level import *

pygame.display.set_caption("Load Runner")
box = pygame.image.load('wood_box.png')
ladder = pygame.image.load('ladder.png')
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'),
             pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'),
             pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'),
            pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'),
            pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
walkRight_enemy = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'),
                   pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load('R6E.png'),
                   pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R1E.png')]
walkLeft_enemy = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'),
                  pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load('L6E.png'),
                  pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L1E.png')]
char = pygame.image.load('standing.png')
clock = pygame.time.Clock()
width, height = 960, 608

pygame.init()
pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play(-1)


def draw():
    pygame.init()
    size = width, height = 960, 608
    win = pygame.display.set_mode(size)
    pygame.display.set_caption("Load Runner")
    win.fill((0, 0, 0))
    font = pygame.font.Font(None, 50)
    text = font.render("Hello, Wanderer!", True, 'red')
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 - 25
    text_w = text.get_width()
    text_h = text.get_height()
    win.blit(text, (text_x, text_y))
    text2 = font.render("level 1  or  level 2", True, 'red')
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2 + 25
    win.blit(text2, (text_x, text_y))
    pygame.draw.line(win, color='red', start_pos=(text_x + 85, text_y + 35), end_pos=(text_x + 105, text_y + 35),
                     width=5)
    pygame.draw.line(win, color='red', start_pos=(text_x + 265, text_y + 35), end_pos=(text_x + 285, text_y + 35),
                     width=5)
    pygame.display.update()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_1]:
            print('1')
            draw_level1()
        if keys[pygame.K_2]:
            print('2')
            draw_level2()
        pygame.display.update()
    pygame.quit()


def ReDrawGameWindow(win, left, right, x, y):
    global walkCount, box, x_up_TF, floor
    pygame.init()
    size = width, height = 960, 608
    screen = pygame.display.set_mode(size)
    win = pygame.display.set_mode(size)
    win.fill('black')
    w1 = -32
    h1 = -32

    for i in level:
        h1 += 32
        w1 = -32
        for j in i:
            w1 += 32
            if j == 1:
                win.blit(box, (w1, h1))
            elif j == 2:
                win.blit(ladder, (w1, h1))

    if walkCount + 1 >= 27:
        walkCount = 0
    if x_up_TF:
        if floor == 1:
            floor += 1
            x_up_TF = False
        elif floor == 2:
            floor += 1
            x_up_TF = False
        elif floor == 3:
            floor += 1
            x_up_TF = False
        elif floor == 4:
            floor += 1
            x_up_TF = False
        elif floor == 5:
            floor = 0
            x_up_TF = False

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    if x == 875 and y == 32:
        YouAreWin()

    pygame.display.update()


def draw_level1():
    global walkCount, x_up_TF, x_up_down, floor
    pygame.init()
    size = width, height = 960, 608
    screen = pygame.display.set_mode(size)
    win = pygame.display.set_mode(size)
    run = True
    pygame.display.set_caption("Load Runner")
    x = 16
    x_up_down = x
    x_up_TF = False
    floor = 1
    y = 608 - 96
    width = 64
    height = 64
    vel = 5
    left = False
    right = False
    walkCount = 0
    while run:
        clock.tick(27)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    # print(floor)
                    if (l_1[0][0] <= x - 16 <= l_1[0][1] or l_1[0][0] <= x - 50 <= l_1[0][1]) and floor == 1:
                        x += 32
                        walkCount = 0
                        y -= 96
                        x_up_TF = True
                    if (l_1[1][0] <= x <= l_1[1][1] or l_1[1][0] <= x <= l_1[1][1]) and floor == 1:
                        x = l_1[1][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if l_2[0] <= x + 50 <= l_2[1] and floor == 2:
                        x = l_2[0] + 32
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if (l_3[1][0] <= x <= l_3[1][1] or l_3[1][0] <= x <= l_3[1][1]) and floor == 3:
                        x = l_3[1][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if (l_3[0][0] <= x <= l_3[0][1] or l_3[0][0] <= x <= l_3[0][1]) and floor == 3:
                        x = l_3[0][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if (l_4[0][0] <= x - 16 <= l_4[0][1] or l_4[0][0] <= x + 50 <= l_4[0][1]) and floor == 4:
                        x += 32
                        walkCount = 0
                        y -= 96
                        x_up_TF = True
                    if (l_4[1][0] <= x - 16 <= l_4[1][1] or l_4[1][0] <= x + 50 <= l_4[1][1]) and floor == 4:
                        x = l_4[1][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if (l_4[2][0] <= x <= l_4[2][1] or l_4[2][0] <= x <= l_4[2][1]) and floor == 4:
                        x = l_4[2][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if (l_5[0][0] <= x <= l_5[0][1] or l_5[0][0] <= x <= l_5[0][1]) and floor == 5:
                        x = l_5[0][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True

        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x - 16 > vel:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 960 - width - vel - 16:
            x += vel
            right = True
            left = False
        else:
            right = False
            left = False
            walkCount = 0

        ReDrawGameWindow(win, left, right, x, y)


def YouAreDead():
    pygame.init()
    size = width, height = 960, 608
    win = pygame.display.set_mode(size)
    win.fill('black')
    font = pygame.font.Font(None, 50)
    text = font.render("YOU ARE LOST...", True, 'red')
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    win.blit(text, (text_x, text_y))
    text2 = font.render("press any key to continue", True, 'red')
    text_x = width // 2 - text.get_width() // 2 - 45
    text_y = height // 2 - text.get_height() // 2 + 25
    win.blit(text2, (text_x, text_y))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                draw()
    pygame.quit()


def YouAreWin():
    pygame.init()
    size = width, height = 960, 608
    win = pygame.display.set_mode(size)
    win.fill('black')
    font = pygame.font.Font(None, 50)
    text = font.render("YOU ARE WIN...", True, (255, 200, 0))
    text_x = width // 2 - text.get_width() // 2
    text_y = height // 2 - text.get_height() // 2
    win.blit(text, (text_x, text_y))
    text2 = font.render("press any key to continue", True, 'red')
    text_x = width // 2 - text.get_width() // 2 - 45
    text_y = height // 2 - text.get_height() // 2 + 25
    win.blit(text2, (text_x, text_y))
    pygame.display.update()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                draw()
    pygame.quit()


def ReDrawGameWindow2(win, left, right, x, y, left_e, right_e, x_e, y_e):
    global walkCount, walkCount_enemy, x_up_TF, floor, width, height, run
    win.fill('black')
    w1 = -32
    h1 = -32
    for i in level:
        h1 += 32
        w1 = -32
        for j in i:
            w1 += 32
            if j == 1:
                win.blit(box, (w1, h1))
            elif j == 2:
                win.blit(ladder, (w1, h1))

    if walkCount + 1 >= 27:
        walkCount = 0
    if walkCount_enemy + 1 >= 27:
        walkCount_enemy = 0
    if x_up_TF:
        if floor == 1:
            floor += 1
            x_up_TF = False
        elif floor == 2:
            floor += 1
            x_up_TF = False
        elif floor == 3:
            floor += 1
            x_up_TF = False
        elif floor == 4:
            floor += 1
            x_up_TF = False
        elif floor == 5:
            floor = 0
            x_up_TF = False

    if left:
        win.blit(walkLeft[walkCount // 3], (x, y))
        walkCount += 1
    elif right:
        win.blit(walkRight[walkCount // 3], (x, y))
        walkCount += 1
    else:
        win.blit(char, (x, y))
    if left_e:
        win.blit(walkLeft_enemy[walkCount_enemy // 3], (x_e, y_e))
        walkCount_enemy += 1
    elif right_e:
        win.blit(walkRight_enemy[walkCount_enemy // 3], (x_e, y_e))
        walkCount_enemy += 1
    if -16 <= x_e - x <= 16 and floor == 0:
        YouAreDead()
    if x == 875 and y == 32:
        YouAreWin()

    pygame.display.update()


def draw_level2():
    global walkCount, walkCount_enemy, i, x_up_TF, floor
    pygame.init()
    size = width, height = 960, 608
    win = pygame.display.set_mode(size)
    run = True
    pygame.display.set_caption("Load Runner")
    x = 16
    x_e = 960 - 64
    y = 608 - 96
    y_e = 35
    width = 64
    height = 64
    vel = 5
    left = False
    right = False
    x_up_down = x
    x_up_TF = False
    left_e = True
    right_e = True
    walkCount_enemy = 0
    walkCount = 0
    floor = 1
    while run:
        clock.tick(27)

        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                run = False
            if i.type == pygame.KEYDOWN:
                if i.key == pygame.K_UP:
                    # print(floor)
                    if (l_1[0][0] <= x - 16 <= l_1[0][1] or l_1[0][0] <= x - 50 <= l_1[0][1]) and floor == 1:
                        x += 32
                        walkCount = 0
                        y -= 96
                        x_up_TF = True
                    if (l_1[1][0] <= x <= l_1[1][1] or l_1[1][0] <= x <= l_1[1][1]) and floor == 1:
                        x = l_1[1][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if l_2[0] <= x + 50 <= l_2[1] and floor == 2:
                        x = l_2[0] + 32
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if (l_3[1][0] <= x <= l_3[1][1] or l_3[1][0] <= x <= l_3[1][1]) and floor == 3:
                        x = l_3[1][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if (l_3[0][0] <= x <= l_3[0][1] or l_3[0][0] <= x <= l_3[0][1]) and floor == 3:
                        x = l_3[0][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if (l_4[0][0] <= x - 16 <= l_4[0][1] or l_4[0][0] <= x + 50 <= l_4[0][1]) and floor == 4:
                        x += 32
                        walkCount = 0
                        y -= 96
                        x_up_TF = True
                    if (l_4[1][0] <= x - 16 <= l_4[1][1] or l_4[1][0] <= x + 50 <= l_4[1][1]) and floor == 4:
                        x = l_4[1][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if (l_4[2][0] <= x <= l_4[2][1] or l_4[2][0] <= x <= l_4[2][1]) and floor == 4:
                        x = l_4[2][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
                    if (l_5[0][0] <= x <= l_5[0][1] or l_5[0][0] <= x <= l_5[0][1]) and floor == 5:
                        x = l_5[0][0]
                        y -= 96
                        walkCount = 0
                        x_up_TF = True
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] and x - 16 > vel:
            x -= vel
            left = True
            right = False
        elif keys[pygame.K_RIGHT] and x < 960 - width - vel - 16:
            x += vel
            right = True
            left = False
        else:
            x_up_down = x
            right = False
            left = False
            walkCount = 0
        if x_e < 50:
            left_e = False
            right_e = True
        elif x_e > 890:
            left_e = True
            right_e = False
        if left_e:
            x_e -= vel
            left_e = True
            right_e = False
        if right_e:
            x_e += vel
            right_e = True
            left_e = False
        ReDrawGameWindow2(win, left, right, x, y, left_e, right_e, x_e, y_e)


run = True
while run:
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_1]:
        draw_level1()
    if keys[pygame.K_2]:
        draw_level2()

pygame.quit()
