from config import VACANCIES_PATH_TXT, VACANCIES_PATH_JSON
from classes.json_saver import JSONSaver
from classes.txt_saver import TXTSaver
from utils import user_choice_json, user_choice_txt


def main():
    user_input = input("Здравствуйте!\n"
                       "В каком формате записать данные?\n"
                       "json формат, введите 1\n"
                       "txt формат, введите 2\n"
                       "Для удаления данных из файла, введите 3\n")

    if user_input == "1":
        user_choice_json()
    elif user_input == "2":
        user_choice_txt()
    elif user_input == "3":
        user_input = input("Какой файл отчистить?\n"
                           "json-файл, введите 1\n"
                           "txt-файл, введите 2\n")
        if user_input == "1":
            deleter = JSONSaver(VACANCIES_PATH_JSON)
            deleter.del_data()
            print("Данные удалены!")
        elif user_input == "2":
            deleter = TXTSaver(VACANCIES_PATH_TXT)
            deleter.del_data()
            print("Данные удалены!")
    return


if __name__ == '__main__':
    main()
