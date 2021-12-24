from datetime import datetime

from datetime import timedelta

import random

end_date = datetime.now() + timedelta(days=random.randint(1, 5))
end_day_formatted = end_date.strftime('%d/%m/%Y')

print("Вас приветствует мастерская по ремонту техники!"
      " Для записи на ремонт заполните заявку ниже.")


def sur():
      surname = input('Фамилия: ')
      if surname.isalpha() is False:
            print("Вводите фамилию корректно!")
            sur()


def nam():
      name = input("Имя: ")
      if name.isalpha() is False:
            print("Вводите имя корректно!")
            nam()


def patr():
      patronymic = input("Отчество: ")
      if patronymic.isalpha() is False:
            print('Вводите отчество корректно!')
            patr()


sur()
nam()
patr()

print('Выберите тип техники для ремонта и введите соответствующее этому типу число.\n'
      '1 - Телефон\n'
      '2 - Ноутбук\n'
      '3 - Телевизор')


def telephone():
      global stamp_tel
      stamp_tel = input('Марка телефона: ')
      global OS_tel
      OS_tel = input('Операционная система: ')
      global inf_tel
      inf_tel = input('Описание поломки: ')
      print('Спасибо, что выбрали нас!')
      print()
      print('Квитанция № TEL' + str(random.randint(1000, 2000)))
      print(f'Марка телефона: {stamp_tel}\n'
            f'Операционная система: {OS_tel}\n'
            f'Описание поломки: {inf_tel}')
      print('Заказ будет готов ' + end_day_formatted + '!')


def comp():
      global stamp_comp
      stamp_comp = input('Марка ноутбука: ')
      global OS_comp
      OS_comp = input('Операционная система: ')
      global year_comp
      year_comp = input('Год выпуска: ')
      global inf_comp
      inf_comp = input('Описание поломки: ')
      print()
      print('Квитанция № COM' + str(random.randint(2000, 3000)))
      print(f'Марка ноутбука: {stamp_comp}\n'
            f'Операционная система: {OS_comp}\n'
            f'Описание поломки: {inf_comp}')
      print('Заказ будет готов ' + end_day_formatted + '!')


def tv():
      global stamp_tv
      stamp_tv = input('Марка телевизора: ')
      global dia
      dia = input('Диагональ экрана: ')
      global inf_tv
      inf_tv = input('Описание поломки: ')
      print()
      print('Квитанция № TV' + str(random.randint(3000, 4000)))
      print(f'Марка телевизора : {stamp_tv}\n'
            f'Диагональ экрана: {dia}\n'
            f'Описание поломки: {inf_tv}')
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