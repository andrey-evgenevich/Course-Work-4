class Vacancy:
    """
    Класс для работы с вакансиями
    """
    __slots__ = ("name", "alternate_url", "salary_from", "salary_to", "area_name", "requirement", "responsibility")

    def __init__(self, name, alternate_url, salary_from, salary_to, area_name, requirement, responsibility):
        self.name = name
        self.alternate_url = alternate_url
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.area_name = area_name
        self.requirement = requirement
        self.responsibility = responsibility

    def __str__(self):
        return (f"Наименование вакансии: {self.name}\n"
                f"Ссылка на вакансию: {self.alternate_url}\n"
                f"Зарплата: от {self.salary_from} до {self.salary_to}\n"
                f"Место работы: {self.area_name}\n"
                f"Краткое описание: {self.requirement}\n"
                f"{self.responsibility}\n")

    def __lt__(self, other):
        if isinstance(other, Vacancy):
            return self.salary_from < other.salary_from
        else:
            TypeError("Ошибка типа данных")

    @classmethod
    def from_hh_dict(cls, vacancy_data):
        """
        Возвращает экземпляр класса в виде списка
        """
        salary = vacancy_data.get("salary")

        return cls(
            vacancy_data["name"],
            vacancy_data["alternate_url"],
            salary.get("from") if salary.get("from") else 0,
            salary.get("to") if salary.get("to") else 0,
            vacancy_data["area"]["name"],
            vacancy_data["snippet"]["requirement"],
            vacancy_data["snippet"]["responsibility"],
        )

    def to_dict(self):
        """
        Возвращает вакансию в виде словаря
        """
        return {
            "name": self.name,
            "alternate_url": self.alternate_url,
            "salary_from": self.salary_from,
            "salary_to": self.salary_to,
            "area_name": self.area_name,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
        }
