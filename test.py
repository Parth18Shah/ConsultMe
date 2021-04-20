# # import 
from selenium import webdriver

option = webdriver.ChromeOptions()
option.add_argument('headless')

chrome_path = r"C:\MY STUFF\SEM 6\MIP\chromedriver.exe"
driver = webdriver.Chrome(chrome_path,options=option)
driver.get("https://www.nmc.org.in/information-desk/indian-medical-register") 
# from selenium.common.exceptions import TimeoutException

# from selenium.webdriver.support.ui import WebDriverWait # available since 2.4.0

# from selenium.webdriver.support import expected_conditions as EC # available since 2.26.0

# # Create a new instance of the Firefox driver
# driver = webdriver.Firefox()

# # go to the google home page
# driver.get("http://www.google.com")

# # the page is ajaxy so the title is originally this:
# print driver.title
driver.find_element_by_xpath("""//*[@id="main-content"]/div[2]/div/div/div/ul/li[3]/a""").click()
# find the element that's name attribute is q (the google search box)
driver.implicitly_wait(10)
inputElement = driver.find_element_by_id("doct_regdNo")

# type in the search
inputElement.send_keys('12345')

# submit the form (although google automatically searches now without submitting)
inputElement.submit()

try:
#     # we have to wait for the page to refresh, the last thing that seems to be updated is the title
#     WebDriverWait(driver, 10).until(EC.title_contains("cheese!"))
    info = driver.find_elements_by_xpath("""//*[@id="doct_info3"]/tbody/tr""")
    print(info)
    print("hi")
    for i in info:
        print(i.text, end ="\n")
        s = i.text
        s = list(s.split(" "))
        print(s)
    print("hey")
#     # You should see "cheese! - Google Search"
#     # print driver.title

finally:
    driver.quit()