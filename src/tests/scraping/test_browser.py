from ...scraping.browser import Browser
from selenium.webdriver.remote.webelement import WebElement

def test_wait_element_by_css_selector():
    test_browser = Browser()
    test_browser.get('https://www.google.com/')
    element = test_browser.wait_element_by_css_selector('[itemtype="http://schema.org/WebPage"]')
    assert isinstance(element, WebElement)
    test_browser.quit()

def test_wait_element_by_css_selector_with_time_out():
    test_browser = Browser()
    test_browser.get('https://www.google.com/')
    try:
        test_browser.wait_element_by_css_selector('[data-test-subj="dashboardPanelHeading-Examesrealizados,segundoresultadoporUFderesidência"]',delay=1)
    
    except Exception as err:
        assert err.args[0] == "Page did not found your element in 1 seconds"
    test_browser.quit()
    

