from helper.CommonMethod import Helper
from projectpage import sklogigpg
from projectpage.sklogigpg import Skloginpg

helper=Helper()
skloginpg= Skloginpg()

class TestSklogin:

    def test_verify_subtitle(self):
        driver= helper.create_driver()
        helper.open_url()
        skloginpg.verify_subtitle(driver)






