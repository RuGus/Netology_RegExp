from pprint import pprint

# читаем адресную книгу в формате CSV в список contacts_list
import csv
import re

with open("phonebook_raw.csv") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
# pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

# корректировка данных
fio_regex_pattern = re.compile(r"\s*(\w*)\s*(\w*)\s*(\w*)\s*")

phone_regex_pattern = re.compile(
    r"\+?(\d{1})\s?\(?(\d{3})\)?\-?\s?(\d{3})\-?\s?(\d{2})\-?\s?(\d{2}\s?)\(?(\w*\.?\s?\d*)\)?"
)
phone_regex_substitution = r"+7(\2)\3-\4-\5\6"

for line in contacts_list:
    # корректировка ФИО
    fio = line[0] + " " + line[1] + " " + line[2]
    line[0] = fio_regex_pattern.sub(r"\1", fio)
    line[1] = fio_regex_pattern.sub(r"\2", fio)
    line[2] = fio_regex_pattern.sub(r"\3", fio)
    # корретировка телефона
    line[5] = phone_regex_pattern.sub(phone_regex_substitution, line[5])
    print(line)

# объединение дублей
dublicate_line_indexes = []
for index, line in enumerate(contacts_list):
    for compare_index, compare_line in enumerate(contacts_list):
        if (
            line[0] == compare_line[0]
            and line[1] == compare_line[1]
            and index != compare_index
            and index not in dublicate_line_indexes
        ):
            for column_index, column_value in enumerate(line):
                if column_value == "":
                    line[column_index] = compare_line[column_index]
            dublicate_line_indexes.append(compare_index)

# удаление дублей
for index in reversed(dublicate_line_indexes):
    contacts_list.pop(index)

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("phonebook.csv", "w") as f:
    datawriter = csv.writer(f, delimiter=",")
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list)
