
from ui_tests_example.pages.base import WebPage
from ui_tests_example.pages.elements import WebElement


class AuthPage(WebPage):

    def __init__(self, web_driver, url=''):
        url = 'http://petfriends1.herokuapp.com/login'
        super().__init__(web_driver, url)

    email = WebElement(id='email')

    password = WebElement(id='pass')

    btn = WebElement(class_name='btn.btn-success')
