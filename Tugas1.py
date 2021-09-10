from selenium import webdriver
import time



url_list = ['https://noobtest.id/','https://erzaf.com/','https://www.orangsiber.com/','https://demoqa.com/','https://automatetheboringstuff.com/']
for url in url_list:
    driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')
    driver.get(url)
    print(driver.title) 
driver.close()
