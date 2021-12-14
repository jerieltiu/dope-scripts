# HeTheLegend bro

import os
import time
import random
import string

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

os.environ[
    "PATH"] += r":/Users/jefftheeagle/Code/Personal/dope-scripts/gformSpam" # folder of web driver
driver = webdriver.Chrome()

link = "https://docs.google.com/forms/d/e/1FAIpQLSec7AxgHDDQCN4wWQr5-2yg7kL_G-zCZEK8BLdqphuBsVoaSw/viewform" # inset gform here

driver.get(link)
driver.implicitly_wait(8)

count = 0
while (count < 69):
    formName = random.choices(string.ascii_uppercase + string.digits, k=19)
    d = driver.find_elements_by_css_selector(
        '.quantumWizTextinputPaperinputInput.exportInput')
    d[0].send_keys('test@gmail.com')
    d[1].send_keys(formName)
    d[2].send_keys(formName)
    d[3].send_keys(formName)
    d = driver.find_element_by_css_selector(
        '.quantumWizTextinputPapertextareaInput.exportTextarea')
    d.send_keys(formName)
    d = driver.find_element_by_css_selector(
        '.appsMaterialWizToggleRadiogroupOffRadio.exportOuterCircle')
    d.click()
    submit = driver.find_element_by_css_selector(
        '.appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel'
    )
    submit.click(link)
    count = count + 1
    driver.get(

if __name__ == '__main__':
    pass
