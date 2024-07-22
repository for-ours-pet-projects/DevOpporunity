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
            output = {
                "name": name,
                "description": vacancy['description'],
                "link": vacancys["url"],
                "city": city,
                "salary_range_min": salary_range_min,
                "salary_range_max": salary_range_max,
                #'work_location': work_location,
                #'employment_type': employment_type,
                #'specialization': specialization,
                #'work_experience': work_experience,
                #'work_schedule': work_schedule,
                #'programming_language': programming_language,
                #'date_uploaded': date_uploaded
            }
            yield output
