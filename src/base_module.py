from src.vacancy_hh import get_employee_data, create_database, save_data_to_database_emp, save_data_to_database_vac, get_vacancies_data
from config_module import config
from src.db_manager import DBManager



def initialize_database():
    params = config()
    data_emp = get_employee_data()
    data_vac = get_vacancies_data()
    create_database('hh', params)
    save_data_to_database_emp(data_emp, 'hh', params)
    save_data_to_database_vac(data_vac, 'hh', params)
    return DBManager(params)

def display_menu():
    print(f"Выберите запрос: \n"
          f"1 - Список всех компаний и количество вакансий у каждой компании\n"
          f"2 - Список всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию\n"
          f"3 - Средняя зарплата по вакансиям\n"
          f"4 - Список всех вакансий, у которых зарплата выше средней по всем вакансиям\n"
          f"5 - Список всех вакансий, в названии которых содержатся запрашиваемое слово\n"
          f"0 - Выход из программы")


def main():
    from src.user_interaction import handle_user_request
    db_manager = initialize_database()
    display_menu()

    while True:
        user_input = input('Введите номер запроса\n')
        if user_input == '0':
            break
        handle_user_request(user_input, db_manager)

if __name__ == "__main__":
    main()