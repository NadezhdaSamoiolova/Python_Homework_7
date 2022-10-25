from input_data import add_contact
from contacts import read_contacts, find_contact


def user_interface():
    flag = True
    while flag:
        print("\n***** Добро пожаловать в телефонный справочник! ***** \n\nВыберете пункт меню для продолжения")
        while True:
            print("1 - Найти контакт")
            print("2 - Добавить контакт")
            print("3 - Показать все контакты")
            print("4 - Выход")
            choise = input()
            if choise not in ['1', '2', '3', '4']:
                print("Выбран неверный пункт меню! \nПопробуйте еще раз")
                continue
            elif choise == '1':
                find_contact()
                break
            elif choise == '2':
                add_contact()
                break
            elif choise == '3':
                read_contacts()
            else:
                flag = False
                break
