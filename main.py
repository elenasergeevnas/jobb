import csv
import os
csv_file = "clients.csv"

def create_csv():
    '''
    создание нового csv-файла
    :return: новый файл
    '''
    header = ['Familia', 'Name', 'Second_name', 'Borned', 'Passport', 'Sale_cost']
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
