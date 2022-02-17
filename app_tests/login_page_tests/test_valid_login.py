from app_pages.primer_login import LoginPage
from app_base.base_page import BasePage as basepage
from pytest import mark
import allure

@mark.login
@allure.description("A user with valid credentials can login to Primer page")
@allure.severity(severity_level="CRITICAL")
@mark.parametrize('my_browser', [('chrome'), ('firefox')])
def test_login_page(my_browser):
    login_page = LoginPage(basepage)
    login_page.initial_setup()
    login_page.go()
    login_page.assert_login_page_url()
    login_page.assert_login_page_title()
    try:
        login_page.assert_login_btn_text()
    finally:
        if AssertionError:
            allure.attach(login_page.driver.get_screenshot_as_png(),
                          name="Login Page",
                          attachment_type=allure.attachment_type.PNG)
    login_page.login_to_primer("good@email.com", "goodpass1")
    login_page.quit()
