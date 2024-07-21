from config import VACANCIES_PATH_JSON, VACANCIES_PATH_TXT
from classes.hh_api import HeadHunterAPI
from classes.json_saver import JSONSaver
from classes.txt_saver import TXTSaver
from classes.vacancy import Vacancy


def user_choice_json():
    """
    Запись в json-файл
    """
    keyword = input("Какую профессию ищите?\n").lower()
    per_page = int(input("Сколько профессии вывести?\n"))

    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies(keyword, per_page)
    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]
    vacancies = sorted(vacancies, reverse=True)

    print("Топ выбранных вакансии с 'HeadHunter' по зарплате: \n")
    for i in sorted(vacancies, reverse=True):
        print(i)

    vacancies = [vacancy.to_dict() for vacancy in vacancies]
    saver = JSONSaver(VACANCIES_PATH_JSON)

    saver.write_data(vacancies)
    saver.get_data()
    print("Данные записаны в json-файл")


def user_choice_txt():
    """
    Запись в txt-файл
    """
    keyword = input("Какую профессию ищите?\n").lower()
    per_page = int(input("Сколько профессии вывести?\n"))
    hh_api = HeadHunterAPI()
    vacancies = hh_api.get_vacancies(keyword, per_page)
    vacancies = [Vacancy.from_hh_dict(vacancy) for vacancy in vacancies]
    vacancies = sorted(vacancies, reverse=True)

    print("Топ выбранных вакансии с 'HeadHunter' по зарплате: \n")
    for i in sorted(vacancies, reverse=True):
        print(i)

    vacancies = "\n".join(str(vacancy) for vacancy in vacancies)
    saver = TXTSaver(VACANCIES_PATH_TXT)
    saver.write_data(vacancies)
    saver.get_data()
    print("Данные записаны в txt-файл")
