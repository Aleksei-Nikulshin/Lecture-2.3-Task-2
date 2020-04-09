# задания 1 и 2 объединены

def main():

  print \
    ('Вы можете использовать следующие операции для двух положительных чисел: \nСложение\nВычитание\nУмножение\nДеление')
  print()

  inp = input \
    ('Введите знак операции и положительные значения для двух чисел\n согласно правилам Польской нотации, разделяя каждый элемент пробелом\n\n ')
  inp = inp.split(' ')
  # print(inp)
  # print(type(inp))


  inp_str = list(filter(None, inp))
  # print(inp_str)
  # print(len(inp_str))


  stack = 0

  try:
    assert inp_str[0] in ['+', '-', '*', '/'], 'первая операция не находится в списке доступных операций'
    if int(inp_str[1]) < 0 or int(inp_str[2]) < 0:
      print('Введенные Вами данные содержат отрицательные значения, что противоречит начальным условиям\n')
      main()
    if not isinstance(inp_str[1:2], int):
      a = int(inp_str[1])
      b = int(inp_str[2])
    # c = a / b
  except ValueError:
    print('\nВведенные Вами значения не являются числами')
  except IndexError:
    print('\nКоличество аргументов, введенных Вами  недостаточно')
  except AssertionError:
    print('\nОперация не находится в списке доступных операций')
  if len(inp_str) > 3:
    print('\nКоличество аргументов, введенных Вами  избыточно')

  try:
    for i in inp_str:
      if i == '-':
        stack = int(inp_str[1]) - int(inp_str[2])
        print(f'\nРезультат равен {stack}')
        break
      elif i == '*':
        stack = int(inp_str[1]) * int(inp_str[2])
        print(f'\nРезультат равен {stack}')
        break
      elif i == '/':
        stack = int(inp_str[1]) / int(inp_str[2])
        print(f'\nРезультат равен {stack}')
        break
      elif i == '+':
        stack = int(inp_str[1]) + int(inp_str[2])
        print(f'\nРезультат равен {stack}')
        break
  except ZeroDivisionError:
    print('\nДеление на ноль недопустимо')



main()



