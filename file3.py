"""Задача №3. В папке лежит некоторое количество файлов. Считайте, что их количество и имена вам заранее известны.

Необходимо объединить их в один по следующим правилам:

Содержимое исходных файлов в результирующем файле должно быть отсортировано по количеству строк в них (то есть первым
нужно записать файл с наименьшим количеством строк, а последним - с наибольшим)
Содержимое файла должно предваряться служебной информацией на 2-х строках: имя файла и количество строк в нем.
Эта информация выводится только один раз перед блоком текста из файла.

Пример. Даны файлы:

1.txt
"Строка номер 1 файла 1.txt
Строка номер 2 файла 1.txt"

2.txt
"Строка номер 1 файла 2.txt"

Итоговый файл:
"2.txt
1
Строка номер 1 файла 2.txt
1.txt
2
Строка номер 1 файла 1.txt
Строка номер 2 файла 1.txt"
"""

# Создаем список с названиями файлов
files = ['1.txt', '2.txt', '3.txt']

# Создаем словарь, где ключом будет количество строк в файле, а значением - список строк из файла.
# Внутри словаря еще один словарь, где ключами будут названия файлов, а значениями - количество строк в файле.
content = {}
for file_name in files:
  with open(file_name, 'r', encoding='utf-8') as f:
    lines = f.readlines()
  content[len(lines)] = {file_name: len(lines)}

# Список строк для записи в результирующий файл
result = []

# Сортируем словарь по ключам (количеству строк в файле) в порядке возрастания
for num_lines in sorted(content.keys()):
  # Для каждого файла записываем в список служебную информацию и сам текст файла
  for file_name, num_lines_file in content[num_lines].items():
    result.append('\n' + file_name + '\n')
    result.append(str(num_lines_file) + '\n')
    with open(file_name, 'r', encoding='utf-8') as f:
      file_content = f.readlines()
    result.extend(file_content)

# Записываем список строк в результирующий файл
with open('result.txt', 'w', encoding='utf-8') as f:
  f.writelines(result)

# Пример выполняет сортировку файлов по количеству строк в порядке возрастания, хранение содержимого файлов в словаре content, запись результатов в списке result и вывод списка result в файл result.txt. 

# Необходимо поместить файлы, которые нужно объединить, в одну папку со скриптом и запустить его. Результирующий файл будет создан также в этой же папке.