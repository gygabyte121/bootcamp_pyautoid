from selenium import webdriver
import time


#open chrome
driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

#open URL
driver.get('https://demoqa.com/webtables')

#Wait time
#time.sleep(2)

#Data
datas = [
    ['Dandi','Setiawan','dandi@gmail.com','20','10000','IT'],
    ['Zulfa','Dinda','dinda@gmail.com','21','20000','Finance'],
    ['Andi','Nugroho','andi@gmail.com','22','30000','Marketing']
    ]

#Iterate data
for data in datas:
    count = 0

    button = driver.find_element_by_id('addNewRecordButton')
    button.click()

    textfirst = driver.find_elements_by_id('firstName')
    textlast = driver.find_elements_by_id('lastName')
    textemail = driver.find_elements_by_id('userEmail')
    textage = driver.find_elements_by_id('age')
    textsalary = driver.find_elements_by_id('salary')
    textdepartment = driver.find_elements_by_id('department')

    # Iterate all input text
    for value in textfirst:
        value.send_keys(data[count])
        count += 1
        time.sleep(2)

    for value in textlast:
        value.send_keys(data[count])
        count += 1
        time.sleep(2)

    for value in textemail:
        value.send_keys(data[count])
        count += 1
        time.sleep(2)

    for value in textage:
        value.send_keys(data[count])
        count += 1
        time.sleep(2)

    for value in textsalary:
        value.send_keys(data[count])
        count += 1
        time.sleep(2)

    for value in textdepartment:
        value.send_keys(data[count])
        count += 1
        time.sleep(2)

    submit = driver.find_element_by_id('submit')
    submit.click()
    