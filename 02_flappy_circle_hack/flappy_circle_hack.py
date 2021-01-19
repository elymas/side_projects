'''
Hack html canvas using Selenium with python by kairess
source: youtu.be/rswFAwVIO40
'''

import os
from selenium import webdriver
import time

dir_path = os.path.dirname(p=os.path.realpath(__file__))
driver_path = os.path.join(dir_path, 'chromedriver')

# print(dir_path)
# print(driver_path)

driver = webdriver.Chrome(executable_path=driver_path)
driver.get('http://tanksw.com/flappy-circle/')

play_button = driver.find_element_by_css_selector('div#menu')
replay_button = driver.find_element_by_css_selector('div#replay')

play_button.click()

while True:
    is_playing = driver.execute_script('return window.isPlaying')

    if is_playing == False:
        time.sleep(3)
        replay_button.click()
        time.sleep(2)
        play_button.click()

    pos_now = driver.execute_script('return window.PosNow')
    lines = driver.execute_script('return window.line')
    cp = int(driver.execute_script('return window.CP'))

    now_line_height = -(lines[cp + 1][0] - pos_now[0]) * ((lines[cp + 1][1] - lines[cp][1]) / (lines[cp + 1][0] - lines[cp][0])) + lines[cp + 1][1]
    gap = (now_line_height - 8) - (pos_now[1] - 65)
    print(gap)

    if gap < 15:
        driver.execute_script('mouseListener(new Event("none"))')
        time.sleep(0.1)

    time.sleep(0.001)
    