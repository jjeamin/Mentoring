from selenium import webdriver

path = "./chromedriver.exe"
driver = webdriver.Chrome(path)

# ============================== search

from selenium import webdriver

path = "./chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://google.com/")
search_box = driver.find_element_by_name("q")
search_box.send_keys("crawling")
search_box.submit()

# ============================== naver

from selenium import webdriver

driver = webdriver.Chrome("./chromedriver.exe")

delay_time = 3
driver.implicitly_wait(delay_time)

driver.get('https://nid.naver.com/nidlogin.login')

id = "ID"
pw = "PASSWORD"
driver.find_element_by_name('id').send_keys(id)
driver.find_element_by_name('pw').send_keys(pw)

driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

# ============================== facebook

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

id = "ID"
pw = "PASSWORD"

path = "./chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("http://www.facebook.com")
assert "Facebook" in driver.title
elem = driver.find_element_by_id("email")
elem.send_keys(id)
elem = driver.find_element_by_id("pass")
elem.send_keys(pw)
elem.send_keys(Keys.RETURN) # ENTER

