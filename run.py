from selenium import webdriver
from selenium.webdriver import ActionChains

from CONSTANT_VAR import *
import time

from mine_functions import *


def start():
    driver = chrome_window_open()
    mine = first_set_field()
    driver_wait_by_id(driver, 'cell_0_0', WAIT_SEC)
    regame(driver=driver)
    driver_wait_by_id(driver, 'cell_0_0', WAIT_SEC)
    time.sleep(1)
    bk = False
    mine, rand_res = random_choose(driver=driver, mine=mine)
    total_mine_count = total_mine(driver=driver)
    count = Constant()
    distinction = 1
    flag_tmp_count = 0
    if rand_res:
        print('game start')
        mine = set_field(driver=driver, mine=mine)
        while True:
            print(count.get_flag_count())
            flag_count = count.get_flag_count()
            for j in range(MINE_SIZE):
                for i in range(MINE_SIZE):
                    print(j, i)
                    if mine[j][i][0] != 0 and mine[j][i][1] == 1 and ch_step(mine=mine, y=j, x=i):
                        mine = clickscan(driver=driver, mine=mine, y=j, x=i, c=count)
                        # left_click(driver=driver, y=j, x=i)
                        mine = checkminenum(driver=driver, mine=mine, y=j, x=i)
                        if not one_block_mine_check(driver, y=j, x=i):
                            bk = True
                            break
                        mine = set_field(driver=driver, mine=mine)

                    if count.get_flag_count() == total_mine_count and not find_unclick_cell(mine):
                        bk = True
                if bk:
                    break

            if distinction % DISTINCTION_POINT == 0:
                if flag_count == flag_tmp_count:
                    print('flag count', flag_count)
                    if flag_count == total_mine_count and not find_unclick_cell(mine):
                        bk = True
                    if not bk:
                        mine, rand_res = random_choose_one(driver=driver, mine=mine)
                    if not rand_res:
                        bk = True
                flag_tmp_count = flag_count
            distinction += 1

            if bk:
                break

    if rand_res:
        print(get_score(driver=driver))
    else:
        print('failed')


def restart():
    driver = chrome_window_open()
    mine = first_set_field()
    time.sleep(10)
    regame(driver=driver)
    time.sleep(1)
    bk = False
    mine, rand_res = random_choose(driver=driver, mine=mine)
    total_mine_count = total_mine(driver=driver)
    count = Constant()
    distinction = 1
    flag_tmp_count = 0
    if rand_res:
        print('game start')
        mine = set_field(driver=driver, mine=mine)
        while True:
            print(count.get_flag_count())
            flag_count = count.get_flag_count()
            for j in range(MINE_SIZE):
                for i in range(MINE_SIZE):
                    print(j, i)
                    if mine[j][i][0] != 0 and mine[j][i][1] == 1 and ch_step(mine=mine, y=j, x=i):
                        mine = clickscan(driver=driver, mine=mine, y=j, x=i, c=count)
                        # left_click(driver=driver, y=j, x=i)
                        mine = checkminenum(driver=driver, mine=mine, y=j, x=i)
                        if not one_block_mine_check(driver, y=j, x=i):
                            bk = True
                            break
                        mine = set_field(driver=driver, mine=mine)

                    if count.get_flag_count() == total_mine_count and not find_unclick_cell(mine):
                        bk = True
                if bk:
                    break

            if distinction % DISTINCTION_POINT == 0:
                if flag_count == flag_tmp_count:
                    mine, rand_res = random_choose_one(driver=driver, mine=mine)
                    if not rand_res:
                        bk = True
                flag_tmp_count = flag_count
            distinction += 1

            if bk:
                break

    if rand_res:
        print(get_score(driver=driver))
    else:
        print('failed')


if __name__ == "__main__":
    start()
