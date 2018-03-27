from core.element_base import ElementBase

class LoginLink(ElementBase):
    def __init__(self):
        ElementBase.__init__(self, 'xpath', '//a/span[.="登录"]')

class SearchSubmit(ElementBase):
    def __init__(self):
        ElementBase.__init__(self, 'id', 'sb_form_go')

class SearchTextInput(ElementBase):
    def __init__(self):
        ElementBase.__init__(self, 'id', 'sb_form_q')

class SearchResultsList(ElementBase):
    def __init__(self):
        ElementBase.__init__(self, 'xpath', '//h2/a')

class SearchResultsCount(ElementBase):
    def __init__(self):
        ElementBase.__init__(self, 'class_name', 'sb_count')

class WebpageTabLink(ElementBase):
    def __init__(self):
        ElementBase.__init__(self, 'xpath', "//a[text()='网页']")

class PicTabLink(ElementBase):
    def __init__(self):
        ElementBase.__init__(self, 'xpath', "//a[text()='图片']")

class FilterLink(ElementBase):
    def __init__(self):
        ElementBase.__init__(self,'xpath', "//a[@title='显示或隐藏筛选器']")
