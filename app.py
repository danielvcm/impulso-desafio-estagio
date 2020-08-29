from src.controller.exams_controller import ExamsController

def main(url):
    exams_controller = ExamsController()
    positive_percentage_per_state_dataframe = exams_controller.get_positive_percentage_per_state(url)
    print(positive_percentage_per_state_dataframe)

if __name__ == "__main__":
    main('http://plataforma.saude.gov.br/coronavirus/virus-respiratorios/')
