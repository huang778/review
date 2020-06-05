from appium import webdriver


class Driver:
    app=None
    @classmethod
    def app_driver(cls):
         if not cls.app:
            kk = {
                'platformName': "Android",
                'platformVersion': '5.1',
                'deviceName': 'sanxing',
                'appPackage': 'com.android.settings',
                'appActivity': '.Settings'
            }
            cls.app = webdriver.Remote('http://127.0.0.1:4723/wd/hub', kk)
            return cls.app
         else:
             return  cls.app
    @classmethod
    def app_teardown(cls):
         if cls.app:
            cls.app.quit()
            cls.app=None


