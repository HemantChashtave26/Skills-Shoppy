from selenium.webdriver.common.by import By
from testdata.sklogindata import Sklogindata

class Skloginpg:

    title_xpath= "//*[@class='ui inverted centered header']"
    def verify_subtitle(self,driver):
        sub_element = driver.find_element(By.XPATH,Skloginpg.title_xpath)

        if sub_element.is_displayed():
            txt=sub_element.text
            print("txt =",txt)
            assert txt == Sklogindata.sk_foot_title
        else:
            print("Element not displayed")
            assert False

