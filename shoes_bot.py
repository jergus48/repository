from selenium import webdriver
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
PATH="C:\Program Files (x86)\chromedriver.exe"
driver= webdriver.Chrome(PATH)
driver.get("https://www.supremenewyork.com/shop/all/shoes")

cas=True
while cas==True:
    if datetime.now().strftime("%H:%M")== "18:58":
        cas=False
        print("start:", datetime.now().strftime("%H:%M:%S"))
        run=True

def order():

    y=1

    while True:
        z=y
        try:
            size3 = WebDriverWait(driver, 2).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="size"]/option['+str(z)+']')))
            size3 = size3.get_attribute('innerHTML')

            print(y)
        except:
            driver.refresh()
            size4 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="size"]/option[1]')))
            size4.click()
            print("2e")
            break

        try:
            if "US 9 / UK 8" in size3:
                size5 = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, '//*[@id="size"]/option[' + str(z) + ']')))
                size5.click()
                print("1e")
                break
        except:
            size5 = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="size"]/option[' + str(z) + ']')))
            size5.click()
            print("1e2")
            break

        if "US 9 / UK 8" not in size3:
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
    print("end:", datetime.now().strftime("%H:%M:%S"))


if run==True:
    driver.refresh()
    while True:
        try:
            driver.find_element_by_xpath('//*[@id="container"]/article[1]/div/p/a').click()
            farba=WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH, '//*[@id="details"]/p[1]')))
            farba=farba.get_attribute('innerHTML')
            print(farba)
            if "Blue" in farba:
                order()
                break
            if "Blue" not in farba:
                break

        except:
            driver.refresh()

    x = 1
    while "Blue" not in farba:
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
        if "Blue" in farba:
            order()












