from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys 
import winsound
from selenium.common.exceptions import NoSuchElementException

select=input('Group or Contact: ')
Contact=input("Enter Name: ")
Word= input("Enter Phrase: ")
Num=int(input("Enter Number of Messages: "))


driver=webdriver.Chrome(executable_path=#######Enter your chromdriver path)

driver.get('https://web.whatsapp.com/')

def beep():
    for i in range(3):
        winsound.Beep(440,1000)


sleep(10)

beep()

for i in range(100):
    try:
        if select=='Group':
            x=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div['+str(i)+']/div/div/div[2]/div[1]/div[1]/span')
            if x.text==Contact:
                x.click()
                for i in range(Num):
                    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]').send_keys(Word+Keys.ENTER)
        else:
            y=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div['+str(i)+']/div/div/div[2]/div[1]/div[1]/span/span')
            if y.text==Contact:
                y.click()
                for i in range(Num):
                    driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]').send_keys(Word+Keys.ENTER)




    except NoSuchElementException:
        pass


