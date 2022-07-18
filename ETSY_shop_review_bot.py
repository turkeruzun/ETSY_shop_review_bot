

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
import time

driver_path = "chromedriver"
driver = webdriver.Chrome(executable_path=driver_path)

shopname="LingoBottles"
url = f'https://www.etsy.com/shop/{shopname}'

driver.get(url)
driver.maximize_window()
time.sleep(1)

element = driver.find_element_by_class_name("col-md-4.text-right-md-up.p-xs-0")
actions = ActionChains(driver)
actions.move_to_element(element).perform()

driver.find_element_by_class_name("col-md-4.text-right-md-up.p-xs-0").click()
time.sleep(1)
driver.find_element_by_xpath('//*[@id="sort-reviews-menu"]/div/button[2]').click()
time.sleep(3)
Yorumlar = driver.find_element_by_class_name('reviews-list')
Yorum = Yorumlar.find_elements_by_tag_name("li")
Yorum2 = Yorumlar.find_elements_by_tag_name("li")
print(len(Yorumlar.find_elements_by_tag_name("li")))


print("""
-------------------------------------------------------------
Reviews
-------------------------------------------------------------
""")
for item in Yorum:
    print(item.text+"\n\n")
    
print("""
-------------------------------------------------------------
User and product links who submitted reviews
-------------------------------------------------------------
""")

for item2 in Yorum2:
    linkler=item2.find_elements_by_tag_name("a")
    for link in linkler:
        if "people" in link.get_attribute('href'):
            print("User Link: ",link.get_attribute('href'))
        if "listing" in link.get_attribute('href'):
            print("Product Link: ",link.get_attribute('href'))
    print('-----------------')
    
time.sleep(3)
driver.quit()