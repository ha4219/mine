from selenium import webdriver
from selenium.webdriver import ActionChains
from CONSTANT_VAR import *
import datetime, time

from mine_functions import *
from db import *


def start():
    try:
        driver = chrome_window_open()
        mine = first_set_field()
        driver_wait_by_id(driver, 'cell_0_0', WAIT_SEC)
        regame(driver=driver)
        start_time = datetime.datetime.now()
        driver_wait_by_id(driver, 'cell_0_0', WAIT_SEC)
        bk = False
        mine, rand_res = random_choose(driver=driver, mine=mine)

    except Exception as e:
        print(e)
        time.sleep(3)
        mine, rand_res = random_choose(driver=driver, mine=mine)
    finally:
        total_mine_count = total_mine(driver=driver)
        count = Constant()
        distinction = 1
        flag_tmp_count = 0
        if rand_res:
            mine = set_field(driver=driver, mine=mine)
            while True:
                flag_count = count.get_flag_count()
                for j in range(MINE_SIZE):
                    for i in range(MINE_SIZE):
                        if mine[j][i][0] != 0 and mine[j][i][1] == 1 and ch_step(mine=mine, y=j, x=i):
                            mine = clickscan(driver=driver, mine=mine, y=j, x=i, c=count)
                            mine = checkminenum(driver=driver, mine=mine, y=j, x=i)
                            if not one_block_mine_check(driver, y=j, x=i):
                                bk = True
                                break
                            mine = set_field(driver=driver, mine=mine)

                        if count.get_flag_count() == total_mine_count or not find_unclick_cell(mine):
                            bk = True
                    if bk:
                        break

                if distinction % DISTINCTION_POINT == 0:
                    if flag_count == flag_tmp_count:
                        if flag_count == total_mine_count or not find_unclick_cell(mine):
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
            score = MAX_SCORE - get_score(driver=driver)
            wrtime = start_time.strftime(
                "%H시 %M분 %S초 %A %d. %B %Y")
            print("시작 시각: {}".format(wrtime))
            print("점수(시간): {}".format(score))
            insert_data(start_time, score)
        else:
            score = 0
            wrtime = start_time.strftime(
                "%H시 %M분 %S초 %A %d. %B %Y")
            print("시작 시각: {}".format(wrtime))
            print('점수(시간) 실패: {}'.format(score))
            insert_data(start_time, score)
        return driver



def restart(driver):
    mine = first_set_field()
    driver_wait_by_id(driver, 'cell_0_0', WAIT_SEC)
    regame(driver=driver)
    start_time = datetime.datetime.now()
    driver_wait_by_id(driver, 'cell_0_0', WAIT_SEC)
    bk = False
    mine, rand_res = random_choose(driver=driver, mine=mine)
    total_mine_count = total_mine(driver=driver)
    count = Constant()
    distinction = 1
    flag_tmp_count = 0
    if rand_res:
        mine = set_field(driver=driver, mine=mine)
        while True:
            flag_count = count.get_flag_count()
            for j in range(MINE_SIZE):
                for i in range(MINE_SIZE):
                    if mine[j][i][0] != 0 and mine[j][i][1] == 1 and ch_step(mine=mine, y=j, x=i):
                        mine = clickscan(driver=driver, mine=mine, y=j, x=i, c=count)
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
                    if flag_count == total_mine_count or not find_unclick_cell(mine):
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
        score = MAX_SCORE - get_score(driver=driver)
        wrtime = start_time.strftime(
            "%H시 %M분 %S초 %A %d. %B %Y")
        print("시작 시각: {}".format(wrtime))
        print("점수(시간): {}".format(score))
        insert_data(start_time, score)
    else:
        score = 0
        wrtime = start_time.strftime(
            "%H시 %M분 %S초 %A %d. %B %Y")
        print("시작 시각: {}".format(wrtime))
        print('점수(시간) 실패: {}'.format(score))
        insert_data(start_time, score)


if __name__ == "__main__":
    first = True
    driver = None
    while True:
        if first:
            first = False
            driver = start()
        else:
            restart(driver=driver)
