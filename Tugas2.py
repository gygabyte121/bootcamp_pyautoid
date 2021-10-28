from selenium import webdriver

#open chrome
driver = webdriver.Chrome(executable_path='C:\chromedriver\chromedriver.exe')

#open URL
driver.get('https://demoqa.com/webtables')


#Data
datas = [
    {'firstName':'Dandi','lastName':'Setiawan','userEmail':'dandi@gmail.com','age':'20','salary':'1000','department':'IT'},
    {'firstName':'Zulfa','lastName':'Dinda','userEmail':'dinda@gmail.com','age':'21','salary':'2000','department':'Finance'},
    {'firstName':'Andi','lastName':'Nugroho','userEmail':'andi@gmail.com','age':'22','salary':'3000','department':'Marketing'}
    ]

#Iterate data
for data in datas:

    driver.find_element_by_id('addNewRecordButton').click()

    driver.find_element_by_id('firstName').send_keys(data['firstName'])
    driver.find_element_by_id('lastName').send_keys(data['lastName'])
    driver.find_element_by_id('userEmail').send_keys(data['userEmail'])
    driver.find_element_by_id('age').send_keys(data['age'])
    driver.find_element_by_id('salary').send_keys(data['salary'])
    driver.find_element_by_id('department').send_keys(data['department'])

    submit = driver.find_element_by_id('submit')
    submit.click()

driver.close()
