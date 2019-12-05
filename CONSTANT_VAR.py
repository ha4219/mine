WINDOW_SIZE_WIDTH = 500
WINDOW_SIZE_HEIGHT = 600
WINDOW_POSITION_X = 100
WINDOW_POSITION_Y = 100
URL = 'https://minesweeper.online/ko/game/128909350'
CHROME_DRIVER_PATH = 'chromedriver'
MINE_SIZE = 9
DISTINCTION_POINT = 3
WAIT_SEC = 10
MAX_SCORE = 999


class Constant:
    def __init__(self):
        self.flag_count = 0

    def init_flag_count(self):
        self.flag_count = 0

    def plus_flag_count(self):
        self.flag_count += 1

    def get_flag_count(self):
        return self.flag_count
