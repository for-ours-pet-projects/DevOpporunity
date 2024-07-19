import datetime
import requests

from . import currency as c


async def download():
    url = "https://api.hh.ru/vacancies"
    session = requests.Session()
    first_page = session.get(url).json()
    output = []
    currency_rates = c.rates()
    for i in range(first_page["pages"] - 99):
        next_page = session.get(url, params={"page": i}).json()
        for vacancys in next_page["items"]:
            vacancy = session.get(vacancys["url"]).json()
            vacancy_id = vacancy["id"] + "_hhru"
            name = vacancy["name"]
            currency = (
                vacancy["salary"]["currency"] if vacancy["salary"] is not None else None
            )
            salary_range_min = (
                vacancy["salary"]["from"] * currency_rates[currency]
                if vacancy["salary"] and vacancy["salary"]["from"] is not None
                else None
            )
            salary_range_max = (
                vacancy["salary"]["to"] * currency_rates[currency]
                if vacancy["salary"] and vacancy["salary"]["to"] is not None
                else None
            )
            city = (
                vacancy["address"]["city"] if vacancy["address"] is not None else None
            )
            work_location = (
                "Удаленная работа"
                if vacancy["schedule"]["name"] == "Удаленная работа"
                else "Очно"
            )
            employment_type = vacancy["employment"]["name"]
            specialization = vacancy["professional_roles"][0]["name"]
            work_experience = vacancy["experience"]["name"]
            work_schedule = vacancy["schedule"]["name"]
            programming_language = vacancy["key_skills"]
            date_uploaded = datetime.datetime.now()

            output.append(
                (
                    name,
                    salary_range_min,
                    salary_range_max,
                    city,
                    work_location,
                    employment_type,
                    specialization,
                    work_experience,
                    work_schedule,
                    programming_language,
                    date_uploaded,
                )
            )

    return output

