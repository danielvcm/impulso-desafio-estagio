class AnalysisService:
    def __init__(self):
        pass
    
    def get_positive_percentage_column(self,exams_per_state_dataframe):
        exams_per_state_dataframe['% Positivo/Detectável'] = exams_per_state_dataframe.apply(lambda row: self.get_positive_percentage(row['Positivo / Detectável'],row['total_de_exames']),axis=1)
    
    def get_positive_percentage(self,positive_exams,total_exams):
        return (positive_exams/total_exams)*100
