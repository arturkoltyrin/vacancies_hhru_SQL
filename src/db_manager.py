import psycopg2


class DBManager:
    """Класс для работы с БД PostgreSQL."""

    def __init__(self, params):
        self.conn = psycopg2.connect(dbname='hh', **params)
        self.cur = self.conn.cursor()

    def get_companies_and_vacancies_count(self):
        """ Выводит список всех компаний и количество вакансий."""
        self.cur.execute("""
        SELECT employers.employer_name, COUNT(vacancy.employer_id)
        FROM employers
        JOIN vacancy USING (employer_id)
        GROUP BY employers.employer_name
        ORDER BY COUNT DESC
        """)

        return self.cur.fetchall()

    def get_all_vacancies(self):
        """Выводит всех вакансий с указанием названия компании, вакансии, зарплаты и ссылки"""
        self.cur.execute("""
        SELECT employers.employer_name, vacancy_name, salary, vacancy_url
        FROM vacancy
        JOIN employers USING (employer_id)
        ORDER BY salary desc""")
        return self.cur.fetchall()

    def get_avg_salary(self):
        """ Рассчитывает среднюю зарплату по вакансиям"""
        self.cur.execute("""
        SELECT avg(salary) from vacancy""")
        return self.cur.fetchall()

    def get_vacancies_with_higher_salary(self):
        """Выводит список вакансий, где зарплата выше средней"""
        self.cur.execute("""
        SELECT vacancy_name, salary
        FROM vacancy
        GROUP BY vacancy_name, salary
        having salary > (SELECT AVG(salary) FROM vacancy)
        ORDER BY salary DESC
        """)
        return self.cur.fetchall()

    def get_vacancies_with_keyword(self, keyword):
        """Выводит вакансии по ключевому слову"""
        request_sql = """
        SELECT * FROM vacancy
        WHERE LOWER (vacancy_name) LIKE %s
        """
        self.cur.execute(request_sql, ('%' + keyword.lower() + '%',))
        return self.cur.fetchall()