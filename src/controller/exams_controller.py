from ..scraping.scraping_service import ScrapingService
from ..data_treatment.data_treatment_service import DataTreatmentService
class ExamsController:
    def __init__(self):
        self.result_per_state_data_test_subj = "dashboardPanelHeading-Examesrealizados,segundoresultadoporUFderesidência"
        self.data_treatment_service = DataTreatmentService()
        
    def get_positive_percentage_per_state(self,url):
        scraping_service = ScrapingService(url,self.result_per_state_data_test_subj)
        exams_data = scraping_service.scrape_content()
        positive_percentage_per_state_dataframe = self.data_treatment_service.get_positive_percentage_per_state_dataframe(exams_data)
        return positive_percentage_per_state_dataframe