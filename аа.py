import csv
import re

def csv_reader(name) -> tuple[list, list]:
    with open(name, 'r', encoding='utf-8-sig') as csv_file:
        csvreader = csv.reader(csv_file)
        headers = next(csvreader)
        correct_rows = [row for row in csvreader if all(row) and len(row) == len(headers)]
    return headers, correct_rows

def csv_filer(title_row, reader) -> list[dict]:
    vacancy_list = []
    for row in reader:
        vacancy_dict = {}
        for j, value in enumerate(row):
            if title_row[j] == "key_skills":
                value = ', '.join(map(clean_text, value.split("\n")))
            elif title_row[j] in ("premium", 'salary_gross'):
                value = "Да" if value.lower() == 'true' else 'Нет'
            else:
                value = clean_text(value)
            vacancy_dict[title_row[j]] = value
        vacancy_list.append(vacancy_dict)
    return vacancy_list

def print_vacancies(data_vacancies, dic_naming):
    for vacancy in data_vacancies:
        for key in dic_naming:
            value = vacancy.get(key, '')
            print(f'{dic_naming[key]}: {value}')
        print()

def clean_text(text) :
    text = re.sub(r'<[^>]+>', '', text)
    return re.sub(r'\s+', ' ', text).strip()



translate_dict = {
    'name': 'Название',
    'description': 'Описание',
    'key_skills': 'Навыки',
    'experience_id': 'Опыт работы',
    'premium': 'Премиум-вакансия',
    'employer_name': 'Компания',
    'salary_from': 'Нижняя граница вилки оклада',
    'salary_to': 'Верхняя граница вилки оклада',
    'salary_gross': 'Оклад указан до вычета налогов',
    'salary_currency': 'Идентификатор валюты оклада',
    'area_name': 'Название региона',
    'published_at': 'Дата и время публикации вакансии'
}

file_name = input()
headers, data = csv_reader(file_name)
vacancies = csv_filer(headers, data)
print_vacancies(vacancies, translate_dict)