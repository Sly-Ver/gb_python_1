# 3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов (не менее 10 строк).
# Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
# Пример файла:
#
# Иванов 23543.12
# Петров 13749.32

my_list = {'Ivanov': 23543.12, 'Petrov': 13749.32, 'Sidorov': 25698.85, 'Smirnov': 18965.50, 'Kuznecsov': 35550.10, 'Popov': 12250.48, 'Vasiljev': 20020.10, 'Petrakov': 18990.60, 'Sokolov': 29990.89, 'Mihailov': 19089.5}
try:
    file_obj = open("text-3.txt", 'w')
    for last_name, salary in my_list.items():
        file_obj.write(last_name + ': ' + str(salary) + "\n")
except IOError:
    print("Произошла ошибка ввода-вывода!")
finally:
    file_obj.close()
summa = 0
count = 0
persons = []
with open("text-3.txt", "r") as file_obj:
    for line in file_obj:
        print(line, end="")
        tokens = line.split(':')
        if float(tokens[1]) <= 20000:
            persons.append(tokens[0])
        summa += float(tokens[1])
        count += 1
result = summa / count
print(f"Оклад меньше 20 тыс: {persons}")
print(f"Средний оклад: {result}")