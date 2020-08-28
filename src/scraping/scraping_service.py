from .selenium_service import SeleniumService
from .beautiful_soup_service import BeautifulSoupService
from bs4 import BeautifulSoup
import requests
import json
class ScrapingService:
    def __init__(self,url,info_to_get_data_test_subj):
        self.beautiful_soup_service = BeautifulSoupService()
        self.url = url
        self.info_to_get_data_test_subj = info_to_get_data_test_subj
    
    def scrape_content(self):
        try:
            dashboard_url = self.scrape_plataforma_saude()
        except TypeError:
            if 'kibana' in self.url:
                dashboard_url = self.url
            else:
                raise Exception("Couldn't find valid information from provided URL")
    
        self.scrape_kibana_dashboard(dashboard_url)
    
    def scrape_plataforma_saude(self):
        web_page = requests.get(self.url)
        dashboard_url = self.beautiful_soup_service.get_kibana_dashboard_url(web_page.content)
        return dashboard_url
    
    def scrape_kibana_dashboard(self, dashboard_url):
        selenium_service = SeleniumService(dashboard_url,self.info_to_get_data_test_subj)
        page_content = selenium_service.crawl_kibana_dashboard()
        selenium_service.quit()
        response_data = self.beautiful_soup_service.get_text_from_response(page_content)
        response_dict = json.loads(response_data)
        return response_dict