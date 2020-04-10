documents = [
    {"type": "Passport", "number": "2207 876234", "name": "Alexey"},
    {"type": "Invoice", "number": "11-2", "name": "Alexander"},
    {"type": "Insurance", "number": "10006", "name": "Petr"},
    {"type": "Passport", "number": "5455 028765", "name": "Dmitry"},
    {"type": "Passport", "number": "5400 028765", "name": "Alena"},
    {"type": "Passport", "number": "5455 002299", "name": "Vasilisa"},
    {"type": "Invoice", "number": "14-4"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006', '5400 028765', '5455 002299'],
    '3': ['14-4', '14-5']
}

def print_all_names_by_documents():
    print('Имена всех владельцев документов, хранящихся в архиве:')
    for directory in directories.values():
        for each_document in directory:
            found = False # Переменная нужна для случая, если номер документа присутвует в directories, но отсутствует в documents.
            for document in documents:
                try:
                    if document["number"] == each_document:
                        found = True
                        print(f'{document["name"]} - владелец документа {each_document}')
                except KeyError:
                    print(f'У документа {each_document} не указан владелец')
            if not found:
                print(f'Для документа {each_document} отсутствует запись')

while True:
    input_command = input("Введите команду: ")

    if input_command == "sc":
        print_all_names_by_documents()
    elif input_command == "q":
        break

    else:
        print("Неверный ввод. Доступные команды: sc и q.")