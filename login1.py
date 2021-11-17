import time

from selenium import webdriver

driver= webdriver.Chrome(executable_path="C:/chromedriver.exe")

driver.get("https://www.stitchfix.com/")
driver.maximize_window()

#will go to signin page ,from there user can signup

log1=driver.find_element_by_xpath('/html/body/div[1]/header/div/nav/a[2]')
log1.click()
time.sleep(1)

#signup form button

signupbutton= driver.find_element_by_xpath('/html/body/div[1]/main/div/div/div[2]/p/button')
signupbutton.click()
time.sleep(1)

# sign up form filling

driver.find_element_by_id('It’s okay').click()

but1=driver.find_element_by_xpath('/html/body/div[1]/main/section/section/form/div[1]/button')
but1.click()
time.sleep(2)

driver.find_element_by_id('Tons').click()
but2=driver.find_element_by_xpath('/html/body/div[1]/main/section/section/form/div[2]/button')
but2.click()
time.sleep(1)

driver.find_element_by_id('Occasionally').click()
but3=driver.find_element_by_xpath('/html/body/div[1]/main/section/section/form/div[3]/button')
but3.click()
time.sleep(1)

#email registration

email=driver.find_element_by_id('email')
email.send_keys("youremail@gmail.com")
time.sleep(3)

but4=driver.find_element_by_xpath('/html/body/div[1]/main/section/section/form/div[4]/div/div[1]/fieldset/button')
but4.click()


# name form

name=driver.find_element_by_id('first')
name.send_keys("mohit")

lname=driver.find_element_by_id('last')
lname.send_keys("kandpal")


but5=driver.find_element_by_xpath('/html/body/div[1]/main/section/section/form/div[5]/button')
but5.click()
time.sleep(2)

#zip code

zcode=driver.find_element_by_id('zip-code')
zcode.send_keys("85001")
time.sleep(2)

but6=driver.find_element_by_xpath('/html/body/div[1]/main/section/section/form/div[6]/button')
but6.click()

#selection of preference

butpref= driver.find_element_by_xpath('/html/body/div[1]/main/section/section/form/div[7]/button[2]')
butpref.click()


#logout form
logout1=driver.find_element_by_xpath('/html/body/main/div[1]/header/div/nav/div[3]/div/div/div/button/svg')
logout1.click()
time.sleep(2)

logout=driver.find_element_by_xpath('/html/body/main/div[1]/header/div/div/div/div/div/div[5]/div/a')
logout.click()
time.sleep(2)




