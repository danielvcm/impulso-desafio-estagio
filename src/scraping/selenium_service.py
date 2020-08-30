from .browser import Browser
import time
class SeleniumService:
    def __init__(self,url,info_to_get_data_test_subj):
        self.url = url
        self.browser = Browser()
        self.browser.get(url)
        self.css_selector_dashboard = f' [data-test-subj="{info_to_get_data_test_subj}"]'
        self.three_dots_xpath = f'//div[@data-test-subj="{info_to_get_data_test_subj}"]/div/div/div/button'
        self.inspector_xpath = '//button[@data-test-subj="dashboardPanelAction-openInspector"]'
        self.view_chooser_id = 'inspectorViewChooser'
        self.requests_view_xpath = '//button[@data-test-subj="inspectorViewChooserRequests"]'
        self.response_detail_xpath = '//button[@data-test-subj="inspectorRequestDetailResponse"]'

    def crawl_kibana_dashboard(self):
        self.wait_dashboard_to_load()
        self.find_element_by_xpath_and_click(self.three_dots_xpath)
        self.find_element_by_xpath_and_click(self.inspector_xpath)
        self.find_element_by_id_and_click(self.view_chooser_id)
        self.find_element_by_xpath_and_click(self.requests_view_xpath)
        self.find_element_by_xpath_and_click(self.response_detail_xpath)
        return self.browser.page_source


    def wait_dashboard_to_load(self):
        self.browser.wait_element_by_css_selector(self.css_selector_dashboard)
    
    def find_element_by_xpath_and_click(self,xpath):
        element = self.browser.find_element_by_xpath(xpath)
        element.click()
    
    def find_element_by_id_and_click(self,id):
        element = self.browser.find_element_by_id(id)
        time.sleep(3)
        element.click()
    
    def quit(self):
        self.browser.quit()