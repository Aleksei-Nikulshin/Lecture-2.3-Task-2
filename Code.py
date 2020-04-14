# задания 1 и 2 объединены



def main():

    print \
      ('Вы можете использовать следующие операции для двух положительных чисел: \nСложение\nВычитание\nУмножение\nДеление')
    print()

    inp = input \
      ('Введите знак операции и положительные значения для двух чисел\n согласно правилам Польской нотации, разделяя каждый элемент пробелом\n\n ')
    inp = inp.split(' ')

    inp_str = list(filter(None, inp))

    if len(inp_str) != 3:
        print("\nВы ввели не три элемента\n")
        main()





    try:
        assert inp_str[0] in ['+', '-', '*', '/'], 'первая операция не находится в списке доступных операций'
        if int(inp_str[1]) < 0 or int(inp_str[2]) < 0:
            print('Введенные Вами данные содержат отрицательные значения, что противоречит начальным условиям\n')
            main()
    except ValueError:
        print('\nВведенные Вами значения не являются числами\n')
        main()
    except AssertionError:
        print('\nОперация не находится в списке доступных операций\n')
        main()

    stack = 0

    try:
          if inp_str[0] == '-':
              stack = int(inp_str[1]) - int(inp_str[2])
              print(f'\nРезультат равен {stack}')
          elif inp_str[0] == '*':
              stack = int(inp_str[1]) * int(inp_str[2])
              print(f'\nРезультат равен {stack}')
          elif inp_str[0] == '/':
              stack = int(inp_str[1]) / int(inp_str[2])
              print(f'\nРезультат равен {stack}')
          elif inp_str[0] == '+':
              stack = int(inp_str[1]) + int(inp_str[2])
              print(f'\nРезультат равен {stack}')
    except ZeroDivisionError:
        print('\nДеление на ноль недопустимо')



main()



