from src.db_manager import DBManager


def handle_user_request(user_input, db_manager):
    if user_input == "1":
        handle_companies_and_vacancies_count(db_manager)
    elif user_input == "2":
        handle_all_vacancies(db_manager)
    elif user_input == '3':
        handle_avg_salary(db_manager)
    elif user_input == "4":
        handle_vacancies_with_higher_salary(db_manager)
    elif user_input == "5":
        handle_vacancies_with_keyword(db_manager)
    else:
        print("Неверный номер запроса. Пожалуйста, выберите снова.")

def handle_companies_and_vacancies_count(db_manager):
    companies_and_vacancies_count = db_manager.get_companies_and_vacancies_count()
    print(f"Список всех компаний и количество вакансий у каждой компании: {companies_and_vacancies_count}\n")

def handle_all_vacancies(db_manager):
    all_vacancies = db_manager.get_all_vacancies()
    print(f"Cписок всех вакансий с указанием названия компании, названия вакансии и зарплаты и ссылки на вакансию: {all_vacancies}\n")

def handle_avg_salary(db_manager):
    avg_salary = db_manager.get_avg_salary()
    print(f"Средняя зарплата по вакансиям: {avg_salary}\n")

def handle_vacancies_with_higher_salary(db_manager):
    vacancies_with_higher_salary = db_manager.get_vacancies_with_higher_salary()
    print(f"Список всех вакансий, у которых зарплата выше средней по всем вакансиям: {vacancies_with_higher_salary}\n")

def handle_vacancies_with_keyword(db_manager):
    keyword = input('Введите ключевое слово ')
    vacancies_with_keyword = db_manager.get_vacancies_with_keyword(keyword)
    print(f"Список всех вакансий, в названии которых содержатся запрашиваемое слово: {vacancies_with_keyword}")