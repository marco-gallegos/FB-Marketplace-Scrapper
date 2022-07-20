# facebook marketplace
from time import sleep
import sys
from selenium import webdriver
from selenium.webdriver import FirefoxOptions
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pymysql
import config

account_id = 0

def dbConnect():
    try:
        conn = pymysql.connect(host=config.HOST, user=config.USER,
                               db=config.DB, passwd=config.PASS, connect_timeout=5)
        return conn
    except pymysql.MySQLError as e:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(e)
        sys.exit()


def getDriver():
    opts = FirefoxOptions()
    # opts.add_argument("--headless")
    driver = webdriver.Firefox(options=opts)
    return driver


def log_in():
    try:
        driver.get(config.MAIN_URL)
        sleep(2)
        email, password = config.ACCOUNTS[account_id]
        email_input = driver.find_element(By.ID,"email")
        email_input.send_keys(email)
        sleep(0.5)
        password_input = driver.find_element(By.ID,"pass")
        password_input.send_keys(password)
        sleep(0.5)
        login_button = driver.find_element(By.XPATH,"//*[@type='submit']")
        login_button.click()
        print("Successfully logged in! (sleep for 3 secs)")
        sleep(3)
    except Exception as e:
        print('Some exception occurred while trying to find username or password field')
        print(e)
    exit


def scrape_item_links(category):
    """
    """
    # marketplace_button = driver.find_element(By.ID,
        # '//span[contains(text(), "Marketplace")]')
    # marketplace_button.click()
    driver.get("https://www.facebook.com/marketplace/?ref=app_tab")
    # wait until new page loaded
    sleep(5)
    element = driver.find_element(By.XPATH,
        '/html/body/div[1]/div[1]/div[1]/div/div[3]/div/div/div/div[1]/div[1]/div[2]/div/div/div/div/div')
    # element.click()
    driver.implicitly_wait(5)
    print("scrolling")
    for _ in range(1):
        try:
            driver.execute_script(
                "window.scrollTo(0, document.body.scrollHeight);")
            sleep(0.5)
        except:
            print("exception while scroll")
    items_wrapper_list = driver.find_elements(By.XPATH,
        f'//div/div[contains(@class, "kbiprv82")]')
    
    for element in items_wrapper_list:
        element.click()

        titleElements = None
        try:
            titleElements = driver.find_elements(
                    By.XPATH,
                    "/html/body/div[1]/div/div[1]/div/div[4]/div/div/div/div/div/div/div/div/div/div/div/div/div/div//span[string-length(text()) > 0]"
            )
        except:
            print("no title")
        print("=="*100)
        title = titleElements[0].text
        price = titleElements[1].text


        data = {
            "title": title,
            "price": price,
        }
        print(data)
        # sleep(1)
        driver.execute_script("history.back();")
        sleep(2)
        #return
       


if __name__ == '__main__':
    categories = ["Vehicles"]

    dbclient = dbConnect()
    driver = getDriver()
    log_in()
    
    for category in categories:
        print("Processing {}".format(category))
        driver.get(config.MAIN_URL)
        scrape_item_links(category)
        print("Finish")
    sleep(1)
    driver.quit()
