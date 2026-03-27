'''
Из предложенного текстового файла (text18-22.txt) вывести на экран его содержимое, 
количество букв в верхнем регистре. Сформировать новый файл, в который поместить текст 
в стихотворной форме предварительно заменив символы третей строки их числовыми 
кодами

И молвил он, сверкнув очами:
«Ребята! не Москва ль за нами?
Умремте же под Москвой,
Как наши братья умирали!»
И умереть мы обещали,
И клятву верности сдержали
Мы в Бородинский бой.
'''
input_file = "text18-22.txt"
output_file = "output_stanza.txt"

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

original_text = "".join(lines)
print("Содержимое исходного файла: ")
print(original_text)

uppercase_count = 0
for char in original_text:
    if char.isupper():  
        uppercase_count += 1

print("\nКоличество букв в верхнем регистре: ", uppercase_count)

processed_lines = []
for i, line in enumerate(lines):
    line = line.rstrip('\n')
    if i == 2:
        coded_line = ' '.join(str(ord(char)) for char in line)
        processed_lines.append(coded_line)
    else:
        processed_lines.append(line)

new_text = "\n".join(processed_lines)

with open(output_file, "w", encoding="utf-8") as f:
    f.write(new_text)

print("\nСодержимое нового файла: \n", new_text)