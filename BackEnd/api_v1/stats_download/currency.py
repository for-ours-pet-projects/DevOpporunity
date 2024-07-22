from bs4 import BeautifulSoup
import requests




def convert(num, cur_from):
    if cur_from != "RUR":
        url = f"https://finance.rambler.ru/calculators/converter/{num}-{cur_from}-RUB/"

        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        inputs = soup.findAll("span", class_="_1wjU3")
        return inputs[1]
    else:
        return num


def rates():
    currencies = {"UZS": None,
                 "RUR": 1,
                 "KGS": None,
                 "KZT": None,
                 "BYN": None,
                 "USD": None}
    output = {}
    url = f'https://cbr.ru/currency_base/daily/'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")

    inputs = soup.find_all('tr')
    for cur in inputs:
        cur_line = cur.find_all('td')
        if cur_line:
            if cur_line[1].text in currencies:
                currencies[cur_line[1].text] = float(cur_line[4].text.replace(',', '.')) / float(cur_line[2].text.replace(',', '.'))
    currencies['BYR'] = currencies['BYN']
    return currencies
