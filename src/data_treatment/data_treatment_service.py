from .data_extraction import DataExtraction
from .analysis_service import AnalysisService
class DataTreatmentService:
    def __init__(self):
        self.data_extraction = DataExtraction()
        self.analysis_service = AnalysisService()
    
    def get_positive_percentage_per_state_dataframe(self,exams_data):
        exams_per_state_dataframe = self.data_extraction.extract_exams_per_state(exams_data)
        self.analysis_service.get_positive_percentage_column(exams_per_state_dataframe)
        positive_percentage_per_state_dataframe = exams_per_state_dataframe[['UF','% Positivo/Detectável']]
        return positive_percentage_per_state_dataframe