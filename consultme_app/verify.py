from selenium import webdriver

def verify_doctor(regdno,input_name):
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
            # # print(i.text, end ="\n")
            # s = i.text
            # s = list(s.split(" "))
            # index1 = s.index('Council')
            # index2 = s.index('') 
            # username = s[index1+1:index2]
            # print(s,index1,index2,username)
            s = i.text
            s = list(s.split(" "))
            s1 =[]
            flag = 0
            for i in range(len(s)):
                a = list(s[i])
                if(s[i]=='Council,'):
                    flag = 1
                res = [i for i in a if i != ',' and i !='.']
                a = ("").join(res)
                # print(a)
                s1.append(a)
            print(s1)
            index1 = s1.index('Council')
            index2 = s1.index('') 
            if(flag):
                name = s1[index1+2:index2]
            else:
                name = s1[index1+1:index2]
            # for i in range(len(name)):
            #     a = list(name[i])
            #     res = [i for i in a if i != ',' and i !='.']
            #     a = ("").join(res)
            #     # print(a)
            print(name)
            if('of' in name):
                name.pop(0)
                name.pop(0)
            val = (" ").join(name)
            actual_name = []
            input_list = []
            for i in range(len(val)):
                temp = val[i].lower()
                actual_name.append(list(temp))
            for i in range(len(input_name)):
                temp = input_name[i].lower()
                # if(temp == ' ')
                input_list.append(list(temp))
            print(actual_name,val,input_name,input_list)
            print(len(val))
            print(len(input_name))
            if(actual_name == input_list):
                return 1
        return 0
        # print("hey")

    finally:
        driver.quit()


# reg no. 98989