from selenium.webdriver.common.by import By



def test_guest_should_see_login_link(browser):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, "#login_link")