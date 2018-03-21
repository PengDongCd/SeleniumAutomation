from core.element_base import ElementBase

class LoginLink(ElementBase):
    def __init__(self,driver):
        ElementBase('xpath', "//a[.='登录']",driver)