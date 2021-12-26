from datetime import datetime

from datetime import timedelta

import random

end_date = datetime.now() + timedelta(days=random.randint(1, 5))
end_day_formatted = end_date.strftime('%d/%m/%Y')
current_date = datetime.today()

print()
print("Вас приветствует мастерская по ремонту техники!"
      " Для записи на ремонт заполните заявку ниже.\n")


def sur():
      global surname
      surname = input('Фамилия: ')
      if surname.isalpha() is False:
            print("Вводите фамилию корректно!")
            sur()

def nam():
      global name
      name = input("Имя: ")
      if name.isalpha() is False:
            print("Вводите имя корректно!")
            nam()


def patr():
      global patronymic
      patronymic = input("Отчество: ")
      if patronymic.isalpha() is False:
            print('Вводите отчество корректно!')
            patr()


sur()
nam()
patr()

print()
print(f'{name.capitalize()}, выберите тип техники для ремонта и введите соответствующее этому типу число.\n'
      '1 - Телефон\n'
      '2 - Ноутбук\n'
      '3 - Телевизор\n'
      )


def telephone():
      global stamp_tel
      stamp_tel = input('Марка телефона: ')
      global OS_tel
      OS_tel = input('Операционная система: ')
      global inf_tel
      inf_tel = input('Описание поломки: ')
      print()
      print('Квитанция № TEL' + str(random.randint(1000, 2000)))
      print(f'Заказ принят: {current_date}')
      print(f'ФИО: {surname.capitalize()} {name.capitalize()} {patronymic.capitalize()}')
      print(f'Марка телефона: {stamp_tel.capitalize()}\n'
            f'Операционная система: {OS_tel.capitalize()}\n'
            f'Описание поломки: {inf_tel.capitalize()}')
      print('Заказ будет готов ' + end_day_formatted + '!')
      print('Спасибо, что выбрали нас!')

def comp():
      global stamp_comp
      stamp_comp = input('Марка ноутбука: ')
      global OS_comp
      OS_comp = input('Операционная система: ')
      global year_comp
      year_comp = input('Год выпуска: ')
      while year_comp.isdecimal() is False:
           print('Вводите значение цифрами!')
           year_comp = input('Год выпуска: ')
      global inf_comp
      inf_comp = input('Описание поломки: ')
      print()
      print('Квитанция № COMP' + str(random.randint(2000, 3000)))
      print(f'Заказ принят: {current_date}')
      print(f'ФИО: {surname.capitalize()} {name.capitalize()} {patronymic.capitalize()}')
      print(f'Марка ноутбука: {stamp_comp.capitalize()}\n'
            f'Операционная система: {OS_comp.capitalize()}\n'
            f'Описание поломки: {inf_comp.capitalize()}')
      print('Заказ будет готов ' + end_day_formatted + '!')


def tv():
      global stamp_tv
      stamp_tv = input('Марка телевизора: ')
      global dia
      dia = input('Диагональ экрана (в дюймах): ')
      while dia.isdecimal() is False:
           print('Вводите значение цифрами!')
           dia = input('Диагональ экрана (в дюймах): ')
      global inf_tv
      inf_tv = input('Описание поломки: ')
      print()
      print('Квитанция № TV' + str(random.randint(3000, 4000)))
      print(f'Заказ принят: {current_date}')
      print(f'ФИО: {surname.capitalize()} {name.capitalize()} {patronymic.capitalize()}')
      print(f'Марка телевизора : {stamp_tv.capitalize()}\n'
            f'Диагональ экрана: {dia}\n'
            f'Описание поломки: {inf_tv.capitalize()}')
      print('Заказ будет готов ' + end_day_formatted + '!')


def tech_type():
      number = input('Тип техники: ')
      if number in ['1', '1.', '1)']:
            telephone()
      elif number in ['2', '2.', '2)']:
            comp()
      elif number in ['3', '3.', '3)']:
            tv()
      else:
            print('Введите число, соответствующее типу техники!')
            tech_type()


tech_type()