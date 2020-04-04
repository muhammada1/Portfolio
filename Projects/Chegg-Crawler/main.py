from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

username = 'muhammadabedeljaber@hotmail.com'
password = 'Muhammad@12'

url = 'http://www.facebook.com/'

driver = webdriver.Chrome("/Users/muham/Downloads/chromedriver/chromedriver")

executable_path = "path_to_webdriver"
os.environ["webdriver.chrome.driver"] = executable_path

chrome_options = Options()
chrome_options.add_extension('path_to_extension')

driver = webdriver.Chrome(executable_path=executable_path, chrome_options=chrome_options)



#driver.SetProfile('C:/Users/muham/AppData/Local/Google/Chrome/User Data/')
'''
options = webdriver.ChromeOptions()
options.add_argument("user-data-dir=C:/Users/muham/AppData/Local/Google/Chrome/User Data/")
driver = webdriver.Chrome("C:/Users/muham/Downloads/chromedriver/chromedriver)

'''



#driver.implicitly_wait(10)

driver.get(url)

driver.find_element_by_id('email').send_keys(username)
driver.find_element_by_id('pass').send_keys(password)
driver.find_element_by_id('loginbutton').click()

#driver.save_screenshot("screenshot.png")

page = driver.page_source



