import csv

def fio(stroka):
    '''
    выделяет имя и фамилию
    :param stroka: строка файла (str)
    :return: строку в формате "И. Фамилия" (str)
    '''
    surname, name, last_name = stroka[1].split()
    return name[0] + '. ' + surname
#открыли файл
with open ('students.csv', encoding='utf8') as file:
    reader = list(csv.reader(file, delimiter= ','))[1:]
#вводим id проекта
    id_project = input()
    #цикл будет работать до тех пор, пока пользователь не введет СТОП
    while id_project != 'СТОП':
        #идем по файлу, ищем нужный id проекта
        for stroka in reader:
            #если нашли - выводим сообщение в нужном формате
            if stroka[2] == id_project:
                print(f'Проект № {stroka[2]} делал: {fio(stroka)} он(а) получил(а) оценку - {stroka[4]}')
                break
        #если весь файл просмотрели, но не нашли нужный id проекта, выводим сообщение
        else:
            print('Ничего не найдено')
    # вводим следующий id проекта
        id_project = input()

        