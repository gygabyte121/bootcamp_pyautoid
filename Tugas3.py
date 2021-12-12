from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException

driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
driver.implicitly_wait(10)
driver.maximize_window()
driver.get('https://demoqa.com/alerts')

driver.find_element_by_id('timerAlertButton').click()

try:
    WebDriverWait(driver,10).until(EC.alert_is_present())
    driver.switch_to.alert.accept()
    print('Berhasil')

except TimeoutException:
    print('Gagal')
    pass

driver.close()

"""
Testing nambah commit

Buat Automation Testing Fitur2

try:
    WebDriverWait(driver,10).until(EC.title_contains('Google'))
    Tittle = driver.title
    print(Tittle)

except TimeoutException:
    print('Tidak Muncul')
    pass
"""
