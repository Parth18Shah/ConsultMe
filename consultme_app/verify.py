from selenium import webdriver

def verify_doctor(regdno,name):
    option = webdriver.ChromeOptions()
    option.add_argument('headless')

    # chrome_path = r"C:\MY STUFF\SEM 6\MIP\chromedriver.exe"
    chrome_path = r"C:\Users\Kirti1\Desktop\TY\sem 6\MIP\ConsultMe\chromedriver.exe"
    driver = webdriver.Chrome(chrome_path,options=option)
    driver.get("https://www.nmc.org.in/information-desk/indian-medical-register") 

    driver.find_element_by_xpath("""//*[@id="main-content"]/div[2]/div/div/div/ul/li[3]/a""").click()

    driver.implicitly_wait(10)
    inputElement = driver.find_element_by_id("doct_regdNo")

    # value = '123456'
    inputElement.send_keys(regdno)

    inputElement.submit()

    try:
        info = driver.find_elements_by_xpath("""//*[@id="doct_info3"]/tbody/tr""")
        print(info)
        # print("hi")
        for i in info:
            # print(i.text, end ="\n")
            s = i.text
            s = list(s.split(" "))
            index1 = s.index('Council')
            index2 = s.index('') 
            username = s[index1+1:index2]
            # print(s,index1,index2,username)
            val = (" ").join(username)
            print(val,name)
            print(len(val))
            print(len(name))
            if(val == name):
                return 1
        return 0
        # print("hey")

    finally:
        driver.quit()


# reg no. 98989