__author__ = 'psbsanno@gmail.com'

import os
import pygame

from env import *

#배경화면 그리기
def drawMenuBg():
    global gamepad, menuBg
    gamepad.blit(menuBg,(0,0))

#타이틀 그리기
def drawMenuTitle(x:float,y:float):
    global gamepad, menuTitle
    gamepad.blit(menuTitle,(x,y))
 
#타이틀 크기 설정 후, 위치 반납
def initMenuTitle():
    global menuTitle

    mTW = pad_width*0.9
    mTH = menuTitle.get_height()/menuTitle.get_width() * mTW
    menuTitle = pygame.transform.scale(menuTitle, (mTW,mTH))
    menuTitle_W = menuTitle.get_width()
    titleY = pad_hegith*0.25
    titleX = pad_width*0.5 - menuTitle_W*0.5
    
    return (titleX,titleY)

#메뉴 초기 설정
def initMenuList():
    global menuList, menuListFont, menuKey

    menuKey = 0
    menuListFont = pygame.font.SysFont("arial",40, True)
    menuList = [
        "SELECT GAME",
        "EXIT"
    ]

#메뉴 그리기
def drawMenuList(curIndex:int):
    global gamepad, menuListFont, menuList

    initX = pad_width*0.5
    initY = pad_hegith*0.5
    margin = 50
    index = 0

    for text in menuList:
        backgroundColor = WHITE if curIndex == index else None
        textButton = menuListFont.render(text, True, BLACK, backgroundColor) 
        gamepad.blit(textButton, (initX - textButton.get_width()*0.5, initY + index*margin))
        index += 1

#메뉴키 이동 시 유효 키 반납
def getMenuKey(delta):
    global menuList, menuKey
    length = len(menuList)
    key = (menuKey + delta) % length

    return key

#키로 메뉴 반납
def getMenuList(index):
    global menuList
    return menuList[index]

#게임 모드
def runGame():
    global gamepad, clock, menuTitle, menuKey

    (titleX, titleY) = initMenuTitle()
    
    crashed =False
    while not crashed:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                crashed = True

            #s: 키 조작

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    menuKey = getMenuKey(-1)
                elif event.key == pygame.K_DOWN:
                    menuKey = getMenuKey(1)
                elif event.key == pygame.K_x:
                    crashed = True
                elif event.key == pygame.K_SPACE:
                    if getMenuList(menuKey) == "SELECT GAME":
                        import select_menu
                        select_menu.initGame()
                        return
                    elif getMenuList(menuKey) == "EXIT":
                        crashed = True

            #e: 키 조작

        #s: 화면 표시
        gamepad.fill(WHITE)
        drawMenuBg()
        drawMenuTitle(titleX, titleY)
        drawMenuList(menuKey)
        pygame.display.update()
        #e: 화면 표시

        clock.tick(60)

    pygame.quit()

def initGame():
    global gamepad, clock, menuBg, menuTitle

    #s: 초기 설정
    pygame.init()
    gamepad = pygame.display.set_mode((pad_width, pad_hegith))
    pygame.display.set_caption(gameTitle)
    menuBg = pygame.image.load(os.path.join(rpImages, rsMainBgSrc))#pygame.image.load(mainBgSrc).convert_alpha()
    menuTitle = pygame.image.load(os.path.join(rpImages, rpmainTitleSrc)) #pygame.image.load(mainTitleSrc).convert_alpha()
    initMenuList()
    #e: 초기 설정

    clock = pygame.time.Clock()
    runGame()

#jaejun

if __name__ == '__main__':
    initGame()
