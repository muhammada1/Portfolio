from selenium import webdriver
import time




#from selenium.webdriver.common.keys import Keys

#Intended chegg url for questions
intended_url = input("Paste Chegg link here: ")

#Enter account credentials
username = 'premium@gmail.com'
password = 'PASSWORD'

#Url of intended website
url = intended_url

#open Chrome Browser (change chromedriver to location to your local host chrome driver)
driver = webdriver.Chrome("/Users/muham/Downloads/chromedriver/chromedriver")

#wait 10 seconds for browser to load before executing next commands
#driver.implicitly_wait(10)



#open website Url
driver.get(url)

driver.find_element_by_link_text('See the answer').click()

#driver.implicitly_wait(10)

time.sleep(10)

#Switch from “Create Account” to “Sign in”
driver.find_elements_by_xpath("//span[@class='sign-in active-link']")[0].click()
#Taken out to speed up process and switched with above code
'''
url = driver.current_url
url = url.replace("signup&data","signin&data")
driver.get(url)
'''

time.sleep(10)

#commands to login (change id fields to match your website)
driver.find_element_by_id('emailForSignIn').send_keys(username)
driver.find_element_by_id('passwordForSignIn').send_keys(password)
driver.find_elements_by_xpath("//button[@name='login']")[0].click()

#Grab Url to covert to pdf
#url = driver.current_url

#pdfkit.from_file('test.html', 'out.pdf')


#element.send_keys(Keys.CONTROL, 'p')

'''
time.sleep(4)

driver.save_screenshot("screenshot.png")

driver.close()
'''
