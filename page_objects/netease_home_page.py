from core.element_base import ElementBase

class LoginLink(ElementBase):
    def __init__(self,test_driver):
        ElementBase.__init__(self, 'xpath', "//a[.='登录']",test_driver)

class SportNewsLink(ElementBase):
    def __init__(self, test_driver):
        ElementBase.__init__(self, 'xpath', '//a[@href="http://sports.163.com/"]', test_driver)