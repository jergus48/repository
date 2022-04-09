from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
PATH="C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.get("https://www.supremenewyork.com/shop/all/sweatshirts")

cas=True
while cas==True:
    if datetime.now().strftime("%H:%M")== "08:29":
        cas=False
        print(datetime.now().strftime("%H:%M"))
        run=True



def order():

    size1=WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="size"]/option[1]')))
    size1 = size1.get_attribute('innerHTML')
    if "Large" in size1:
        run2=False
        print("1")
    if "Large" not in size1:
        y=2
        run2 = True

    while run2==True:
        try:
            size3 = WebDriverWait(driver, 15).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="size"]/option['+str(y)+']')))
            size3 = size3.get_attribute('innerHTML')
            print(y)
        except:
            size4 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="size"]/option[1]')))
            size4.click()
            print("2e")
            break
        if "Large" in size3:
            size5 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="size"]/option[' + str(y) + ']')))
            size5.click()
            print("1e")
            break
        if "Large" not in size3:
            y+=1


    main1 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="add-remove-buttons"]/input')))
    main1.click()
    main2 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "checkout now")))
    main2.click()
    main3 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '// *[ @ id = "order_billing_name"]')))
    main3.send_keys("Jergus Snahnican")
    main4 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="order_email"]')))
    main4.send_keys("jergussnahnican@gmail.com")
    main5 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="order_tel"]')))
    main5.send_keys("+421904435240")
    main6 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="order_billing_address"]')))
    main6.send_keys("Dražkovce 220")
    main7 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="order_billing_city"]')))
    main7.send_keys("Dražkovce")
    main8 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="order_billing_zip"]')))
    main8.send_keys("03802")

    main10 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="order_billing_country"]/option[30]')))
    main10.click()
    main9 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="store-address"]')))
    main9.click()

    main11 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="credit_card_number"]')))
    main11.send_keys("4263982640269299")

    main13 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="credit_card_month"]/option[2]')))
    main13.click()

    main15 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="credit_card_year"]/option[2]'))) #option1=2022
    main15.click()
    main16 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="credit_card_verification_value"]')))
    main16.send_keys("837")
    main17 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="cart-cc"]/fieldset/p/label/div/ins')))
    main17.click()
    main18 = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="pay"]/input')))
    main18.click()






if run==True:
    driver.refresh()
    driver.find_element_by_xpath('//*[@id="container"]/article[1]/div/p/a').click()
    farba=WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH, '//*[@id="details"]/p[1]')))
    farba=farba.get_attribute('innerHTML')
    print(farba)
    if "Black" in farba:
        order()
    x=1

    while "Black" not in farba:
        x+=1
        try:
            colour2 = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="details"]/ul/li['+str(x)+']/button')))
            colour2.click()

            farba = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="details"]/p[1]')))
            farba = farba.get_attribute('innerHTML')
            print(farba)
        except:
            order()
            break
        if "Black" in farba:
            order()



#//*[@id="details"]/ul/li[2]/button
#//*[@id="details"]/p[1]


#main=WebDriverWait(driver,10).until(
#        EC.presence_of_element_located((By.LINK_TEXT, "next t-shirt >")))
#    main.click()












