import csv
import os
csv_file = "clients.csv"

def create_csv():
    '''
    создание нового csv-файла
    :return: новый файл
    '''
    header = ['surname', 'name', 'second_name', 'borned', 'passport', 'sale_cost']
    with open (csv_file, "w", newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
    file.close()


def view_clients():
    if os.path.isfile(csv_file):
        with open(csv_file, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                print(reader)
    else:
        print('File not found')


def add_clients():
    if os.path.isfile(csv_file):
        with open(csv_file, "w", newline='', encoding="utf-8") as file:
            wrier = csv.writer(file)
            surname = input('Введите фамилию ')
            name = input('Введите имя ')
            second_name = input('Введите отчество ')
            borned = input('Введите дату рождения ')
            passport = input('Введите паспортные данные ')
            sale_cost = input('Введите есть ли скидка ')
            writer. writerow([surname, name, second_name, borned, passport, sale_cost])
    else:
        print('File not found')

def delete_elem():
    if os.path.isfile(csv_file):
        with open(csv_file, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[4] = passport_to_delete:
                    rows.append(row)

    else:
        print('File not found')


def edit_client():
    '''
    управляет значением скидки
    :return:
    '''
    if os.path.isfile(csv_file):
        with open(csv_file, "r", newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row[4] == passport_to_edit
                    row[5] = ('Есть ли скидка [да\нет] )
                rows.append(row)
        file.close()

    else:
        print('File not found')


while True:
    print('1 - добавить клиента, 2 - просмотр клиента, 3 - удаление клиента, 4 - изменение скидки', 5 - выход)
    menu = int(input('Выберете пункт меню '))

    if menu == 1:
        add.cliens