# Дана строка (возможно,пустая),состоящая из букв A-Z. Нужно написать функцию RLE, которая на выходе даст строку вида :A4B3C2XYZD4E3F3A6B28. 
# И сгенерирует ошибку, если на вход пришла невалидная строка .
# Пояснения: Если символ встречается 1 раз, он остается без изменений;
# Если символ повторяется более 1 раза, к нему добавляется количество повторений.

def counting_letters(array: list):
    count = 1
    for i in range(len(array) - 1):
        count_let = array[i]
        if count_let == array[i + 1]:
            count = count + 1
        else:
            print(f'{count}{count_let}', end = '')
            count = 1

new_string = input('Введите набор букв английского алфавита: ').upper()
while new_string.isdigit():
    print('На вход пришла невалидная строка ')
    new_string = input('Введите набор букв английского алфавита: ').upper()
# print(new_string)

list_string = list(new_string)
# print(list_string)
list_string.append('')
# print(list_string)

counting_letters(list_string)






# count = 1
# for i in range(len(list_string) - 1):
#     need_letter = list_string[i]
#     if need_letter == list_string[i + 1]:
#         count = count + 1
#     else:
#         print(f'{count}{need_letter}', end = '')
#         count = 1