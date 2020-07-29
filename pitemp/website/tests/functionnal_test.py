from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver
from website.models import CustomUser, Temperature


class MySeleniumTests(StaticLiveServerTestCase):

    def setUp(self):
        super(MySeleniumTests, self).setUp()
        self.selenium = WebDriver()
        self.user = CustomUser.objects.create_user(id=1, username='usertest', password='test123', email='test@test.com',
                                                   adress='50 rue du test', city='Test', postal_code='00000')
        self.temp = Temperature.objects.create(id=1, temperature=22.01, date='29.85 2020-07-23 09:24:36.534325+00:00',
                                               idUser=self.user)
        self.user.save(), self.temp.save()

    def tearDown(self):
        self.selenium.quit()
        super(MySeleniumTests, self).tearDown()

    def test_login(self, username="usertest", password="test123"):
        self.selenium.get('%s%s' % (self.live_server_url, "/authenticate/login/"))
        self.selenium.implicitly_wait(1)
        self.selenium.find_element_by_id('authenticate').is_displayed()
        self.selenium.find_element_by_name("username").send_keys(username)
        self.selenium.find_element_by_name("password").send_keys(password)
        self.selenium.find_element_by_id("button_login").click()
        self.selenium.implicitly_wait(1)
        self.selenium.find_element_by_id("logout").is_displayed()  # check if logout img is displayed

    def test_dashboard_view(self, username="usertest", password="test123"):
        self.selenium.get('%s%s' % (self.live_server_url, "/authenticate/login/"))
        self.selenium.implicitly_wait(1)
        self.selenium.find_element_by_id('authenticate').is_displayed()
        self.selenium.find_element_by_name("username").send_keys(username)
        self.selenium.find_element_by_name("password").send_keys(password)
        self.selenium.find_element_by_id("button_login").click()
        self.selenium.implicitly_wait(1)
        self.selenium.find_element_by_id("my_temperatures").click()
        self.selenium.implicitly_wait(1)
        self.selenium.find_element_by_id("myChart")
