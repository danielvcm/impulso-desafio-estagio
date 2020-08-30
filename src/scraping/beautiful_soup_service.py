from bs4 import BeautifulSoup
class BeautifulSoupService:
    def __init__(self):
        pass

    def get_html(self,page_content):
        return BeautifulSoup(page_content,'html.parser')
    
    def get_text_from_response(self,page_content):
        html = self.get_html(page_content)
        soup = html.find('code', {'data-test-subj':"inspectorResponseBody"})
        text = soup.get_text()
        return text

    def get_kibana_dashboard_url(self,page_content):
        html = self.get_html(page_content)
        soup = html.find('iframe')
        return soup['src']