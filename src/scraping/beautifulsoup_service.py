from bs4 import BeautifulSoup
class BeautifulSoupService:
    def __init__(self, html):
        self.html = BeautifulSoup(html,'html.parser')
    
    def get_text_from_response(self):
        soup = self.html.find('code', {'data-test-subj':"inspectorResponseBody"})
        text = soup.get_text()
        return text
