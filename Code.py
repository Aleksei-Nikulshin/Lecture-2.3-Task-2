

def check_exceptions():
  print('Вы можете использовать следующие операции для двух положительных чисел: \nСложение\nВычитание\nУмножение\nДеление')
  print()

  inp = input('Введите знак операции и положительные значения для двух чисел\n согласно правилам Польской нотации, разделяя каждый элемент ввода пробелом ')
  inp = inp.split(' ')

  result_input_list = list(filter(None, inp))
  # print(result_input_list)

  try:
    assert result_input_list[0] in ['+', '-', '*', '/'], 'первая операция не находится в списке доступных операций'
  except AssertionError:
    print('\nПервая операция не находится в списке доступных операций')

  try:
    if not isinstance(result_input_list[1:2], int):
      a = int(result_input_list[1])
      b = int(result_input_list[2])
    c = a / b
  except ZeroDivisionError:
    print('\nДеление на ноль недопустимо')
  except ValueError:
    print('\nВведенные Вами значения не являются числами')
  except IndexError:
    print('\nКоличество аргументов, введенных Вами  недостаточно')
  if len(result_input_list) > 3:
    print('\nКоличество аргументов, введенных Вами  избыточно')

check_exceptions()
