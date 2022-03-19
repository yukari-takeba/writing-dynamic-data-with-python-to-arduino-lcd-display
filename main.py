import serial
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC





driver = webdriver.Chrome("C:\Program Files (x86)/chromedriver.exe")

driver.get("https://populationmatters.org/population-numbers?gclid=CjwKCAjw_tWRBhAwEiwALxFPoVhr5NimVxTuFLhNZudGPhpwhWQb3KBtnW9sjmVxRlfmWBlYwTpslhoCUugQAvD_BwE")






#print(driver.find_element_by_class_name("value dw").aria_role)
driver.implicitly_wait(200)



element = driver.find_element(By.XPATH , "/html/body/section/div[2]/div/div/div[1]/div[2]/div")

print("\r" , element.text , end="")
sleep(2)










arduino = serial.Serial("COM6")

arduino.timeout = 1






print(type(element.text))

while True:

    sleep(3)
    arduino.write(str(element.text).encode())


    print(arduino.read_all().decode() , element.text ,  "hey")




driver.close()

