from selenium import webdriver
from selenium.webdriver import ActionChains
from CONSTANT_VAR import *
import random
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException


def right_click(driver, y, x, c):
    c.plus_flag_count()
    ActionChains(driver).context_click(driver.find_element_by_id('cell_' + repr(x) + '_' + repr(y))).perform()


def left_click(driver, y, x):
    driver.find_element_by_id('cell_' + repr(x) + '_' + repr(y)).click()


def first_set_field():
    res = []
    for i in range(MINE_SIZE):
        tmp = []
        for j in range(MINE_SIZE):
            tmp.append([0, 0])
        res.append(tmp)
    return res


def set_field(driver, mine):
    for j in range(MINE_SIZE):
        for i in range(MINE_SIZE):
            if mine[j][i][1] == 0:
                string = driver.find_element_by_id(
                    'cell_' + repr(i) + '_' + repr(j)).get_attribute("class")
                if string == 'cell size24 hd_closed':
                    mine[j][i] = [0, 0]
                elif string == 'cell size24 hd_opened hd_type0':
                    mine[j][i] = [0, 1]
                elif string == 'cell size24 hd_opened hd_type1':
                    mine[j][i] = [1, 1]
                elif string == 'cell size24 hd_opened hd_type2':
                    mine[j][i] = [2, 1]
                elif string == 'cell size24 hd_opened hd_type3':
                    mine[j][i] = [3, 1]
                elif string == 'cell size24 hd_opened hd_type4':
                    mine[j][i] = [4, 1]
                elif string == 'cell size24 hd_opened hd_type5':
                    mine[j][i] = [5, 1]
                elif string == 'cell size24 hd_opened hd_type6':
                    mine[j][i] = [6, 1]
                elif string == 'cell size24 hd_opened hd_type7':
                    mine[j][i] = [7, 1]
                elif string == 'cell size24 hd_opened hd_type8':
                    mine[j][i] = [8, 1]
                elif string == 'cell size24 hd_opened hd_type10':
                    mine[j][i] = [9, 1]
                elif string == 'cell size24 hd_opened hd_type11':
                    mine[j][i] = [9, 1]
                elif string == 'cell size24 hd_opened hd_type12':
                    mine[j][i] = [9, 1]
                elif string == 'cell size24 hd_closed hd_flag':
                    mine[j][i] = [0, 2]
    return mine


def one_mine_check(driver, mine, j, i):  # 한개의 위치를 확인합니다.
    string = driver.find_element_by_id(
        'cell_' + repr(i) + '_' + repr(j)).get_attribute("class")
    if string == 'cell size24 hd_closed':
        mine[j][i] = [0, 0]
    elif string == 'cell size24 hd_opened hd_type0':
        mine[j][i] = [0, 1]
    elif string == 'cell size24 hd_opened hd_type1':
        mine[j][i] = [1, 1]
    elif string == 'cell size24 hd_opened hd_type2':
        mine[j][i] = [2, 1]
    elif string == 'cell size24 hd_opened hd_type3':
        mine[j][i] = [3, 1]
    elif string == 'cell size24 hd_opened hd_type4':
        mine[j][i] = [4, 1]
    elif string == 'cell size24 hd_opened hd_type5':
        mine[j][i] = [5, 1]
    elif string == 'cell size24 hd_opened hd_type6':
        mine[j][i] = [6, 1]
    elif string == 'cell size24 hd_opened hd_type7':
        mine[j][i] = [7, 1]
    elif string == 'cell size24 hd_opened hd_type8':
        mine[j][i] = [8, 1]
    elif string == 'cell size24 hd_opened hd_type10':
        mine[j][i] = [9, 1]
    elif string == 'cell size24 hd_opened hd_type11':
        mine[j][i] = [9, 1]
    elif string == 'cell size24 hd_opened hd_type12':
        mine[j][i] = [9, 1]
    elif string == 'cell size24 hd_closed hd_flag':
        mine[j][i] = [0, 2]
    return mine


def clickscan(driver, mine, y, x, c):  # 현재 y,x 의 셀 위치의 수와 주변의 안눌린 셀 갯수 비교
    unclicknum = 0
    if y == 0 and x == 0:  # 왼쪽 위 구석일때
        if mine[y][x + 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x + 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x][1] != 1:
            unclicknum += 1

    elif y == 0 and x == MINE_SIZE - 1:  # 오른쪽 위 구석일때
        if mine[y][x - 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x - 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x][1] != 1:
            unclicknum += 1

    elif y == MINE_SIZE - 1 and x == 0:  # 왼쪽 아래 구석일때
        if mine[y][x + 1][1] != 1:
            unclicknum += 1
        if mine[y - 1][x][1] != 1:
            unclicknum += 1
        if mine[y - 1][x + 1][1] != 1:
            unclicknum += 1

    elif y == MINE_SIZE - 1 and x == MINE_SIZE - 1:  # 오른쪽 아래 구석일때
        if mine[y][x - 1][1] != 1:
            mine[y][x][1] = 2
        if mine[y - 1][x - 1][1] != 1:
            mine[y][x][1] = 2
        if mine[y - 1][x][1] != 1:
            mine[y][x][1] = 2

    elif y == 0:  # 구석을 제외한 윗쪽일때
        if mine[y][x - 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x - 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x][1] != 1:
            unclicknum += 1
        if mine[y + 1][x + 1][1] != 1:
            unclicknum += 1
        if mine[y][x + 1][1] != 1:
            unclicknum += 1

    elif x == 0:  # 구석을 제외한 왼쪽일때
        if mine[y - 1][x][1] != 1:
            unclicknum += 1
        if mine[y - 1][x + 1][1] != 1:
            unclicknum += 1
        if mine[y][x + 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x + 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x][1] != 1:
            unclicknum += 1

    elif y == MINE_SIZE - 1:  # 구석을 제외한 아랫쪽일때
        if mine[y][x - 1][1] != 1:
            unclicknum += 1
        if mine[y - 1][x - 1][1] != 1:
            unclicknum += 1
        if mine[y - 1][x][1] != 1:
            unclicknum += 1
        if mine[y - 1][x + 1][1] != 1:
            unclicknum += 1
        if mine[y][x + 1][1] != 1:
            unclicknum += 1

    elif x == MINE_SIZE - 1:  # 구석을 제외한 오른쪽일때
        if mine[y - 1][x][1] != 1:
            unclicknum += 1
        if mine[y - 1][x - 1][1] != 1:
            unclicknum += 1
        if mine[y][x - 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x - 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x][1] != 1:
            unclicknum += 1

    else:  # 나머지 가운데 부분일때
        if mine[y - 1][x][1] != 1:
            unclicknum += 1
        if mine[y - 1][x - 1][1] != 1:
            unclicknum += 1
        if mine[y][x - 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x - 1][1] != 1:
            unclicknum += 1
        if mine[y + 1][x][1] != 1:
            unclicknum += 1
        if mine[y + 1][x + 1][1] != 1:
            unclicknum += 1
        if mine[y][x + 1][1] != 1:
            unclicknum += 1
        if mine[y - 1][x + 1][1] != 1:
            unclicknum += 1

    if mine[y][x][0] == unclicknum:  # 누른 자리의 숫자와 주변의 안눌린 자리의 수가 같으면 호출
        mine = checkmine(driver, mine, y, x, c)
        return mine
    return mine


def checkmine(driver, mine, y, x, c):  # 주변자리에 깃발을 놓는 함수
    if y == 0 and x == 0:
        if mine[y][x + 1][1] == 0:
            right_click(driver=driver, y=y, x=x + 1, c=c)
        if mine[y + 1][x + 1][1] == 0:
            right_click(driver=driver, y=y + 1, x=x + 1, c=c)
        if mine[y + 1][x][1] == 0:
            right_click(driver=driver, y=y + 1, x=x, c=c)
    elif y == 0 and x == MINE_SIZE - 1:
        if mine[y][x - 1][1] == 0:
            right_click(driver=driver, y=y, x=x - 1, c=c)
        if mine[y + 1][x - 1][1] == 0:
            right_click(driver=driver, y=y + 1, x=x - 1, c=c)
        if mine[y + 1][x][1] == 0:
            right_click(driver=driver, y=y + 1, x=x, c=c)

    elif y == MINE_SIZE - 1 and x == 0:
        if mine[y][x + 1][1] == 0:
            right_click(driver=driver, y=y, x=x + 1, c=c)
        if mine[y - 1][x][1] == 0:
            right_click(driver=driver, y=y - 1, x=x, c=c)
        if mine[y - 1][x + 1][1] == 0:
            right_click(driver=driver, y=y - 1, x=x + 1, c=c)

    elif y == MINE_SIZE - 1 and x == MINE_SIZE - 1:
        if mine[y][x - 1][1] == 0:
            right_click(driver=driver, y=y, x=x - 1, c=c)
        if mine[y - 1][x - 1][1] == 0:
            right_click(driver=driver, y=y - 1, x=x - 1, c=c)
        if mine[y - 1][x][1] == 0:
            right_click(driver=driver, y=y - 1, x=x, c=c)

    elif x == 0:
        if mine[y - 1][x][1] == 0:
            right_click(driver=driver, y=y - 1, x=x, c=c)
        if mine[y - 1][x + 1][1] == 0:
            right_click(driver=driver, y=y - 1, x=x + 1, c=c)
        if mine[y][x + 1][1] == 0:
            right_click(driver=driver, y=y, x=x + 1, c=c)
        if mine[y + 1][x + 1][1] == 0:
            right_click(driver=driver, y=y + 1, x=x + 1, c=c)
        if mine[y + 1][x][1] == 0:
            right_click(driver=driver, y=y + 1, x=x, c=c)

    elif y == 0:
        if mine[y][x - 1][1] == 0:
            right_click(driver=driver, y=y, x=x - 1, c=c)
        if mine[y + 1][x - 1][1] == 0:
            right_click(driver=driver, y=y + 1, x=x - 1, c=c)
        if mine[y + 1][x][1] == 0:
            right_click(driver=driver, y=y + 1, x=x, c=c)
        if mine[y + 1][x + 1][1] == 0:
            right_click(driver=driver, y=y + 1, x=x + 1, c=c)
        if mine[y][x + 1][1] == 0:
            right_click(driver=driver, y=y, x=x + 1, c=c)

    elif y == MINE_SIZE - 1:
        if mine[y][x - 1][1] == 0:
            right_click(driver=driver, y=y, x=x - 1, c=c)
        if mine[y - 1][x - 1][1] == 0:
            right_click(driver=driver, y=y - 1, x=x - 1, c=c)
        if mine[y - 1][x][1] == 0:
            right_click(driver=driver, y=y - 1, x=x, c=c)
        if mine[y - 1][x + 1][1] == 0:
            right_click(driver=driver, y=y - 1, x=x + 1, c=c)
        if mine[y][x + 1][1] == 0:
            right_click(driver=driver, y=y, x=x + 1, c=c)

    elif x == MINE_SIZE - 1:
        if mine[y - 1][x][1] == 0:
            right_click(driver=driver, y=y - 1, x=x, c=c)
        if mine[y - 1][x - 1][1] == 0:
            right_click(driver=driver, y=y - 1, x=x - 1, c=c)
        if mine[y][x - 1][1] == 0:
            right_click(driver=driver, y=y, x=x - 1, c=c)
        if mine[y + 1][x - 1][1] == 0:
            right_click(driver=driver, y=y + 1, x=x - 1, c=c)
        if mine[y + 1][x][1] == 0:
            right_click(driver=driver, y=y + 1, x=x, c=c)

    else:
        if mine[y - 1][x][1] == 0:
            right_click(driver=driver, y=y - 1, x=x, c=c)
        if mine[y - 1][x - 1][1] == 0:
            right_click(driver=driver, y=y - 1, x=x - 1, c=c)
        if mine[y][x - 1][1] == 0:
            right_click(driver=driver, y=y, x=x - 1, c=c)
        if mine[y + 1][x - 1][1] == 0:
            right_click(driver=driver, y=y + 1, x=x - 1, c=c)
        if mine[y + 1][x][1] == 0:
            right_click(driver=driver, y=y + 1, x=x, c=c)
        if mine[y + 1][x + 1][1] == 0:
            right_click(driver=driver, y=y + 1, x=x + 1, c=c)
        if mine[y][x + 1][1] == 0:
            right_click(driver=driver, y=y, x=x + 1, c=c)
        if mine[y - 1][x + 1][1] == 0:
            right_click(driver=driver, y=y - 1, x=x + 1, c=c)
    mine = set_field(driver=driver, mine=mine)
    return mine


def checkminenum(driver, mine, y, x):  # 그 자리의 숫자랑 주변의 깃발의 숫자가 같으면 그 숫자를 다시 누르는 함수
    minenum = 0
    if y == 0 and x == 0:
        if mine[y][x + 1][1] == 2:
            minenum += 1
        if mine[y + 1][x + 1][1] == 2:
            minenum += 1
        if mine[y + 1][x][1] == 2:
            minenum += 1

    elif y == 0 and x == MINE_SIZE - 1:
        if mine[y][x - 1][1] == 2:
            minenum += 1
        if mine[y + 1][x - 1][1] == 2:
            minenum += 1
        if mine[y + 1][x][1] == 2:
            minenum += 1

    elif y == MINE_SIZE - 1 and x == 0:
        if mine[y][x + 1][1] == 2:
            minenum += 1
        if mine[y - 1][x][1] == 2:
            minenum += 1
        if mine[y - 1][x + 1][1] == 2:
            minenum += 1

    elif y == MINE_SIZE - 1 and x == MINE_SIZE - 1:
        if mine[y - 1][x][1] == 2:
            minenum += 1
        if mine[y - 1][x - 1][1] == 2:
            minenum += 1
        if mine[y - 1][x][1] == 2:
            minenum += 1

    elif x == 0:
        if mine[y - 1][x][1] == 2:
            minenum += 1
        if mine[y - 1][x + 1][1] == 2:
            minenum += 1
        if mine[y][x + 1][1] == 2:
            minenum += 1
        if mine[y + 1][x + 1][1] == 2:
            minenum += 1
        if mine[y + 1][x][1] == 2:
            minenum += 1

    elif y == 0 and x != 0 and x != MINE_SIZE - 1:
        if mine[y][x - 1][1] == 2:
            minenum += 1
        if mine[y + 1][x - 1][1] == 2:
            minenum += 1
        if mine[y + 1][x][1] == 2:
            minenum += 1
        if mine[y + 1][x + 1][1] == 2:
            minenum += 1
        if mine[y][x + 1][1] == 2:
            minenum += 1

    elif y == MINE_SIZE - 1:
        if mine[y][x - 1][1] == 2:
            minenum += 1
        if mine[y - 1][x - 1][1] == 2:
            minenum += 1
        if mine[y - 1][x][1] == 2:
            minenum += 1
        if mine[y - 1][x + 1][1] == 2:
            minenum += 1
        if mine[y][x + 1][1] == 2:
            minenum += 1

    elif x == MINE_SIZE - 1:
        if mine[y - 1][x][1] == 2:
            minenum += 1
        if mine[y - 1][x - 1][1] == 2:
            minenum += 1
        if mine[y][x - 1][1] == 2:
            minenum += 1
        if mine[y + 1][x - 1][1] == 2:
            minenum += 1
        if mine[y + 1][x][1] == 2:
            minenum += 1

    else:
        if mine[y - 1][x][1] == 2:
            minenum += 1
        if mine[y - 1][x - 1][1] == 2:
            minenum += 1
        if mine[y][x - 1][1] == 2:
            minenum += 1
        if mine[y + 1][x - 1][1] == 2:
            minenum += 1
        if mine[y + 1][x][1] == 2:
            minenum += 1
        if mine[y + 1][x + 1][1] == 2:
            minenum += 1
        if mine[y][x + 1][1] == 2:
            minenum += 1
        if mine[y - 1][x + 1][1] == 2:
            minenum += 1
    if mine[y][x][0] == minenum:
        left_click(driver=driver, y=y, x=x)
        mine = set_field(driver=driver, mine=mine)
        return mine
    return mine


def ch_step(mine, y, x):  # 확인 필요하면 True 아니면 False
    if y == 0 and x == 0:
        if mine[y][x + 1][1] != 1 and mine[y + 1][x + 1][1] != 1 and mine[y + 1][x][1] != 1:
            return False
        return True
    elif y == MINE_SIZE - 1 and x == MINE_SIZE - 1:
        if mine[y][x - 1][1] != 1 and mine[y - 1][x - 1][1] != 1 and mine[y - 1][x][1] != 1:
            return False
        return True
    elif y == 0 and x == MINE_SIZE - 1:
        if mine[y][x - 1][1] != 1 and mine[y + 1][x - 1][1] != 1 and mine[y + 1][x][1] != 1:
            return False
        return True
    elif y == MINE_SIZE - 1 and x == 0:
        if mine[y][x + 1][1] != 1 and mine[y - 1][x + 1][1] != 1 and mine[y - 1][x][1] != 1:
            return False
        return True
    elif y == 0:
        if (mine[y][x + 1][1] != 1 and mine[y + 1][x + 1][1] != 1 and mine[y + 1][x][1] != 1 and mine[y + 1][x - 1][
            1] != 1 and mine[y][x - 1][1] != 1):
            return False
        return True
    elif y == MINE_SIZE - 1:
        if (mine[y][x + 1][1] != 1 and mine[y - 1][x + 1][1] != 1 and mine[y - 1][x][1] != 1 and mine[y - 1][x - 1][
            1] != 1 and mine[y][x - 1][1] != 1):
            return False
        return True
    elif x == 0:
        if (mine[y - 1][x][1] != 1 and mine[y - 1][x + 1][1] != 1 and mine[y][x + 1][1] != 1 and mine[y + 1][x + 1][
            1] != 1 and mine[y + 1][x][1] != 1):
            return False
        return True
    elif x == MINE_SIZE - 1:
        if (mine[y - 1][x][1] != 1 and mine[y - 1][x - 1][1] != 1 and mine[y][x - 1][1] != 1 and mine[y + 1][x - 1][
            1] != 1 and mine[y + 1][x][1] != 1):
            return False
        return True
    else:
        if (mine[y - 1][x - 1][1] != 1 and mine[y - 1][x][1] != 1 and mine[y - 1][x + 1][1] != 1 and mine[y][x - 1][
            1] != 1 and mine[y][x + 1][1] != 1 and mine[y + 1][x - 1][1] != 1 and mine[y + 1][x][1] != 1 and
                mine[y + 1][x + 1][1] != 1):
            return False
        return True


def check_mine_open(mine):  # [0,1] 발견시 탈출을 목적
    for j in range(MINE_SIZE - 1):
        for i in range(MINE_SIZE - 1):
            if mine[j][i][0] == 0 and mine[j][i][1] == 1:
                return True
    return False


def random_choose(driver, mine):
    while True:
        x = random.choice(range(0, 9))
        y = random.choice(range(0, 9))
        if mine[y][x][1] != 0:
            continue
        left_click(driver, y=y, x=x)
        mine = set_field(driver=driver, mine=mine)
        if not one_block_mine_check(driver=driver, y=y, x=x):  # 지뢰 발견
            return mine, False
        if check_mine_open(mine):  # 충분히 열려서 게임 시작
            return mine, True


def random_choose_one(driver, mine):
    while True:
        x = random.choice(range(0, 9))
        y = random.choice(range(0, 9))
        if mine[y][x][1] != 0:
            continue
        left_click(driver, y=y, x=x)
        mine = set_field(driver=driver, mine=mine)
        if not one_block_mine_check(driver=driver, y=y, x=x):  # 지뢰 발견
            return mine, False
        return mine, True


def check_game_clear(driver):
    state = driver.find_element_by_id('top_area_face'). \
        get_attribute('class')
    if state == 'top-area-face zoomable hd_top-area-face-unpressed':
        return False
    else:
        return True


def chrome_window_open():
    driver = webdriver.Chrome(CHROME_DRIVER_PATH)
    driver.set_window_size(WINDOW_SIZE_WIDTH, WINDOW_SIZE_HEIGHT)
    driver.set_window_position(WINDOW_POSITION_X, WINDOW_POSITION_Y)
    driver.get(URL)
    return driver


def regame(driver):  # 게임초기화
    driver.find_element_by_xpath('//*[@id="top_area_face"]').click()


def one_block_mine_check(driver, y, x):
    string = driver.find_element_by_id('cell_' + repr(x) + '_' + repr(y)).get_attribute("class")
    if string == 'cell size24 hd_opened hd_type11' or string == 'cell size24 hd_opened hd_type12':
        return False
    return True


def class2num(string):
    tmp = 'hd_top-area-num'
    idx = string.find(tmp)
    return int(string[idx + len(tmp)])


def total_mine(driver):
    a = driver.find_element_by_id('top_area_mines_100').get_attribute('class')
    b = driver.find_element_by_id('top_area_mines_10').get_attribute('class')
    c = driver.find_element_by_id('top_area_mines_1').get_attribute('class')
    return class2num(a) * 100 + class2num(b) * 10 + class2num(c)


def get_score(driver):
    a = driver.find_element_by_id('top_area_time_100').get_attribute('class')
    b = driver.find_element_by_id('top_area_time_10').get_attribute('class')
    c = driver.find_element_by_id('top_area_time_1').get_attribute('class')
    return class2num(a) * 100 + class2num(b) * 10 + class2num(c)


def find_unclick_cell(mine):
    for col in mine:
        if [0, 0] in col:
            return True
    return False


def driver_wait_by_id(driver, id, delay):
    try:
        element = WebDriverWait(driver, delay).until(EC.presence_of_element_located((By.ID, id)))
    except TimeoutException as e:
        print(e)
