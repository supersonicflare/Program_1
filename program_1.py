import math
#Словари с данными
d1 = dict(n="Игорь Акинфеев", d="08.04.1986", cl="ЦСКА", m=58, g=-44)
d2 = dict(n="Владимир Габулов", d="19.10.1983", cl="Анжи", m=9, g=-5)
d3 = dict(n="Сергей Рыжиков", d="19.09.1980", cl="Рубин", m=1, g=-1)
d4 = dict(n="Александр Анюков", d="28.09.1982", cl="Зенит", m=74, g=1)
d5 = dict(n="Алексей Березуцкий", d="20.06.1982", cl="ЦСКА", m=51, g=0)
d6 = dict(n="Василий Березуцкий", d="20.06.1982", cl="ЦСКА", m=68, g=2)
d7 = dict(n="Андрей Ещенко", d="09.02.1984", cl="Анжи", m=5, g=0)
d8 = dict(n="Сергей Игнашевич", d="14.07.1979", cl="ЦСКА", m=85, g=5)
d9 = dict(n="Кирилл Набабкин", d="08.09.1986", cl="ЦСКА", m=2, g=0)
d10 = dict(n="Владимир Быстров", d="31.01.1984", cl="Зенит", m=41, g=4)
d11 = dict(n="Денис Глушаков", d="27.01.1987", cl="Локомотив", m=17, g=1)
d12 = dict(n="Игорь Денисов", d="17.05.1984", cl="Зенит", m=36, g=0)
d13 = dict(n="Алан Дзагоев", d="17.06.1990", cl="ЦСКА", m=27, g=8)
d14 = dict(n="Юрий Жирков", d="20.08.1983", cl="Анжи", m=56, g=0)
d15 = dict(n="Олег Иванов", d="04.08.1986", cl="Терек", m=0, g=0)
d16 = dict(n="Дмитрий Комбаров", d="22.01.1987", cl="Спартак", m=10, g=0)
d17 = dict(n="Игорь Лебеденко", d="27.05.1983", cl="Терек", m=0, g=0)
d18 = dict(n="Александр Рязанцев", d="05.09.1986", cl="Рубин", m=1, g=0)
d19 = dict(n="Александр Самедов", d="19.06.1984", cl="Локомотив", m=6, g=0)
d20 = dict(n="Виктор Файзулин", d="22.04.1986", cl="Зенит", m=6, g=2)
d21 = dict(n="Олег Шатов", d="29.07.1990", cl="Анжи", m=1, g=1)
d22 = dict(n="Роман Широков", d="06.07.1981", cl="Зенит", m=31, g=11)
d23 = dict(n="Максим Григорьев", d="06.07.1990", cl="Локомотив", m=1, g=0)
d24 = dict(n="Александр Кержаков", d="27.11.1982", cl="Зенит", m=70, g=22)
d25 = dict(n="Федор Смолов", d="09.02.1990", cl="Анжи", m=2, g=1)
#Кортеж словарей для возможности их прохождения циклом
dt = (d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11, d12, d13, d14, d15,
      d16, d17, d18, d19, d20, d21, d22, d23, d24, d25)
#Циклы для ручной обработки исключений
f = 1
while f == 1:
    c = 1
    while c == 1:
        print('Введите Имя и Фамилию игрока текущего состава '
              'сборной России по футболу: ')
        a = input()
#Цикл для прохода ключей словарей с целью установления соответствия
#значения, введенного с клавиатуры и ключа с именем игрока
        for i in range(0, 25):
            if dt[i].get('n') == a:
                c = 0
                if dt[i].get('m') == 0:
                    k = 1
                else:
                    k = dt[i].get('m')
#Функция для вычисления результативности игрока
                ch = lambda x, y: math.trunc((x / y) * 100)/100
                b = [["Имя игрока:       ", dt[i].get('n')],
                     ["Дата рождения:    ", dt[i].get('d')],
                     ["Клуб:             ", dt[i].get('cl')],
                     ["Количество матчей:", dt[i].get('m')],
                     ["Голы:             ", dt[i].get('g')],
                     ["Результативность: ", ch(dt[i].get('g'), k),
                      "голов за матч"]]
                print()
#Цикл вывода таблицы
                for i in range(len(b)):
                    for j in range(len(b[i])):
                        print(b[i][j], end = ' ')
                    print()
#Все нижеследующее - обработка исключений, связанных с неправильным вводом
        if c == 1:
            print("Либо Вы ввели имя неправильно, либо в настоящее время "
                  "этого игрока нет в списке сборной. Попробуйте еще раз.")
    
        
    print()
    print("Вы хотите еще раз запустить программу? (y/n)")
    h = input()
    if (h != 'y') and (h != 'n'):
        while (h != 'y') and (h != 'n'):
            print("Можно вводить только 'y' или 'n'! Введите еще раз: ")
            h = input()
    if h == 'y':
        pass
    elif h == 'n':
        f = 0
