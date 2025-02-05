from util import *
from selenium.webdriver.common.by import By

username = sys.argv[1] # username
password = sys.argv[2] # password
https_proxy = sys.argv[3] if len(sys.argv) > 3 else ""
img_path = os.getcwd() + "/1.png"

def save_img(src):
    img = requests.get(src)
    with open(img_path, "wb") as f:
        f.write(img.content)

def guyunsq():
    try:
        driver = get_web_driver(proxy = {'https': https_proxy} if https_proxy else {})

        # login
        driver.get("https://www.guyunsq.com/member.php?mod=logging&action=login")

        driver.find_element(By.XPATH, "//*[starts-with(@id, 'username_')]").send_keys(username)
        driver.find_element(By.XPATH, "//*[starts-with(@id, 'password3_')]").send_keys(password)

        driver.find_element(By.XPATH, "//*[@name='loginsubmit']").click()
        time.sleep(10)


        if driver.find_elements(By.XPATH, "//*[@id='todaysay']") != []:
            print('guyunsq: start checking in')

            driver.find_element(By.XPATH, "//*[@id='kx']").click()
            driver.find_element(By.XPATH, "//*[@id='todaysay']").send_keys('I am happy')
            driver.find_element(By.XPATH, "//*[@class='pn pnc']").click()
            time.sleep(10)

            print('guyunsq: checked in successfully')
        else:
            print('guyunsq: already checked in')
    except:
        return
    finally:
        driver.quit()

if __name__ == '__main__':
    guyunsq()