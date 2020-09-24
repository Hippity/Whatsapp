from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys 
import winsound
from selenium.common.exceptions import NoSuchElementException

select=input('Group or Contact: ')
Contact=input("Enter Name: ")


driver=webdriver.Chrome(executable_path=##### Chromedrive path)

driver.get('https://web.whatsapp.com/')

def beep():
    for i in range(3):
        winsound.Beep(440,1000)


sleep(20)

beep()

for i in range(100):
    try:
        if select=='Group':
            x=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div['+str(i)+']/div/div/div[2]/div[1]/div[1]/span')
            print(x.text)
            if x.text==Contact:
                x.click()
                msg=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
                file=open('Shrek.txt','r')
                for line in file:
                    for word in line.split():
                        msg.send_keys(word+Keys.ENTER)
                file.close()
        else:
            y=driver.find_element_by_xpath('//*[@id="pane-side"]/div[1]/div/div/div['+str(i)+']/div/div/div[2]/div[1]/div[1]/span/span')
            print(y.text)
            if y.text==Contact:
                y.click()
                msg=driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]')
                file=open('Shrek.txt','r')
                for line in file:
                    for word in line.split():
                        msg.send_keys(word+Keys.ENTER)
                file.close()



    except NoSuchElementException:
        pass


