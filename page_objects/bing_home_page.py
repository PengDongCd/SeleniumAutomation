from core.element_base import ElementBase

class LoginLink(ElementBase):
    def __init__(self,test_driver):
        ElementBase.__init__(self, 'xpath', '//a/span[.="登录"]',test_driver)

class SearchSubmit(ElementBase):
    def __init__(self, test_driver):
        ElementBase.__init__(self, 'id', 'sb_form_go', test_driver)

class SearchTextInput(ElementBase):
    def __init__(self, test_driver):
        ElementBase.__init__(self, 'id', 'sb_form_q', test_driver)

class SearchResultsList(ElementBase):
    def __init__(self, test_driver):
        ElementBase.__init__(self, 'xpath', '//h2/a', test_driver)

class SearchResultsCount(ElementBase):
    def __init__(self, test_driver):
        ElementBase.__init__(self, 'class_name', 'sb_count', test_driver)

class WebpageTabLink(ElementBase):
    def __init__(self, test_driver):
        ElementBase.__init__(self, 'xpath', "//a[text()='网页']", test_driver)