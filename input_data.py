from contacts import write_contact


def add_contact():
    print('Заполните данные нового контакта: ')
    flag = True
    while flag:
        surname = input('Фамилия: ')
        name = input('Имя: ')
        midname = input('Отчество: ')
        phone_num = input('Номер телефона: ')
        eml = input('E-Mail: ')
        description = input('Описание: ')
        confirm = input('\nНаберите 1 для сохранения контакта или нажмите любую клавишу для возврата в меню: ')
        if confirm == '1':
            write_contact(surname, name, midname, phone_num, eml, description)
        else:
            flag = False
