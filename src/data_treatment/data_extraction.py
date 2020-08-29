import pandas as pd
class DataExtraction:
    def __init__(self):
        pass

    def extract_exams_per_state(self,exams_data):
        exams_per_state_list = self.get_exams_per_state_list(exams_data)
        exams_per_state_dataframe = pd.DataFrame.from_dict(exams_per_state_list)
        return exams_per_state_dataframe

    def get_exams_per_state_list(self, exams_data):
        exams_per_state_list = []
        for state_data in exams_data['aggregations']['2']["buckets"]:
            state_dict = self.get_state_dict(state_data)
            exams_per_state_list.append(state_dict)
        return exams_per_state_list

    def get_state_dict(self, state_data):
        state_dict = {'UF': state_data['key'], 'total_de_exames':state_data['doc_count']}
        for exam in state_data['3']['buckets']:
            state_dict[exam['key']] = exam['doc_count']
        return state_dict
        
        