from collections import defaultdict
from math import ceil, log2

# класс Node для представления узлов дерева Хаффмана
class Node:
    def __init__(self, label, weight=0):
        self.label = label
        self.weight = weight #частота
        self.left = None
        self.right = None
        self.code = ""

    def __repr__(self): # Для представления объекта в виде строки.
        return f"{self.label}: {self.weight}" #Возвращает строку, представляющую метку и вес объекта.

# создаем кодовые слова для узлов дерева Хаффмана
def codewords_making(node, code=""):
    if node.left is not None: #Проверка, что у узла есть левый потомок.
        node.left.code = code + "0" # Устанавливает код левого потомка узла с добавлением "0" к текущему коду.
        codewords_making(node.left, code + "0") # Рекурсивный вызов функции для левого потомка с обновленным кодом.
    if node.right is not None:
        node.right.code = code + "1"
        codewords_making(node.right, code + "1")

#используем для кодирования текста с помощью предоставленных кодовых слов
def encoding(text, codes):
    encoded_text = "" # Инициализация переменной для хранения закодированного текста.
    for ch in text: # проходим по символам в тексте.
        encoded_text += codes[ch] #Добавление кода символа к закодированному тексту.
    return encoded_text #Возвращает закодированный текст.

# формула Шенона
def Shannon_formula(frequencies, text_length): # frequencies (словарь с частотами символов) и text_length (длина текста).
    shannon = 0
    for char, prob in frequencies.items(): #Цикл по элементам словаря frequencies, где char - символ, а prob - вероятность его появления.
        shannon += (prob / text_length) * log2(prob / text_length) #вероятность символа делится на длину текста, затем умножается на логарифм по основанию 2 от этого значения.
    return round(-1 * shannon, 6) # 6  - точность знаков после запятой


# алгоритм Хаффмана
freqs1 = defaultdict(int) # Создание словаря freqs1 с значениями по умолчанию 0 (буква)
freqs2 = defaultdict(int) # Создание словаря freqs2 с значениями по умолчанию 0 (пары)
text = "" # для хранения текста из файла.
with open("input.txt", "r") as file:
    text = file.read() #Считывание содержимого файла в переменную text
for ch in text: # Цикл по каждому символу в тексте.
    freqs1[ch] += 1 #Увеличение частоты символа ch в словаре freqs1 на 1
for i in range(0, len(text) - 1): # Цикл по индексам от 0 до длины текста минус 1.
    freqs2[text[i] + text[i + 1]] += 1 #Увеличение частоты пары символов (символ на позиции i и следующий за ним) в словаре freqs2 на 1.
# построение кодов Хаффмана
nodes = [] # Инициализация списка nodes для хранения узлов дерева Хаффмана.
for k, v in freqs1.items(): # Цикл по элементам словаря freqs1.
    nodes.append(Node(k, v)) # Создание объектов типа Node (узлы дерева) для каждого символа из словаря freqs1 и добавление их в список nodes
nodes.sort(key=lambda x: x.weight) # Сортировка узлов по весу (частоте) в порядке возрастания.
end_nodes = nodes.copy() # Создание копии.
while len(nodes) != 1: #Цикл, который выполняется до тех пор, пока в списке nodes не останется один узел.
    left = nodes.pop(0) #Извлечение узла с наименьшим весом
    right = nodes.pop(0)
    node = Node(left.label + right.label, left.weight + right.weight)
    node.left = left
    node.right = right
    nodes.insert(0, node) #Вставка нового узла в начало списка nodes.
    nodes.sort(key=lambda x: x.weight) #Повторная сортировка узлов по весу.
codewords_making(nodes[0])
codes = dict() # Создание словаря codes, где ключами являются символы или пары символов, а значениями - соответствующие коды Хаффмана.
for node in end_nodes:
    codes[node.label] = node.code
encoded = encoding(text, codes)
freqs1_list = []
freqs2_list = []
for i in freqs1.keys():
    freqs1_list.append([i, freqs1[i]])
for i in freqs2.keys():
    freqs2_list.append([i, freqs2[i]])
print("Количество символов в исходном тексте: ", len(text))
print("Количество уникальных символов: ", len(freqs1_list))
with open('output1.txt', 'w') as file:
    file.write("Символы и их частоты: " + str(sorted(freqs1_list, key=lambda frequency: frequency[1])))
    file.write("\n\n")
    file.write("Пары символов и их частоты: " + str(sorted(freqs2_list, key=lambda frequency: frequency[1])))
    file.close()
with open('output2.txt', 'w') as file:
    file.write("Символы и их коды Хаффмана: " + str(codes))
    file.write("\n\n")
    file.write("Закодированная строка: " + encoded)
    file.close()
print("Длина закодированного текста (метод Хаффмана):", len(encoded))
print("Длина при равномерном (пятибитовом) кодировании:", 5 * len(text))
print("Степень сжатия по сравнению с равномерным (пятибитовым) кодированием:",
      round(100 - (len(encoded) / (5 * len(text))) * 100, 6), "%")
print("Формула Шеннона (метод Хаффмана):", Shannon_formula(freqs1, len(text)), "бит")

# алгоритм LZW
LZW_dict = dict() #Создается пустой словарь LZW_dict, который будет использоваться для хранения кодов символов.
i = 0 # Инициализируется переменная i для присвоения уникальных кодов символам.
for char in codes: #Для каждого символа из словаря codes выполняется следующее:
    LZW_dict[char] = i  #Символу присваивается уникальный код i в словаре LZW_dict.
    i += 1 #Увеличивается значение переменной i для следующего уникального кода.
dictionary_size = len(LZW_dict) #Вычисляется размер словаря LZW_dict, который будет использоваться для инициализации битового размера.
init_bits = ceil(log2(dictionary_size)) #Вычисляется размер словаря LZW_dict, который будет использоваться для инициализации битового размера.
string = ""
LZW_encoded = [] #Создается пустой список LZW_encoded, в который будут добавляться закодированные значения.
for char in text: # Для каждого символа в тексте выполняется следующее:
    new_string = string + char #Создается новая строка, объединяя текущую строку и текущий символ.
    if new_string in LZW_dict: # Проверяется, если новая строка уже есть в словаре LZW_dict.
        string = new_string #Обновляется текущая строка.
    else:
        LZW_encoded.append(LZW_dict[string]) #Добавляется код текущей строки в список закодированных значений.
        LZW_dict[new_string] = dictionary_size #Добавляется новая строка в словарь с уникальным кодом.
        dictionary_size += 1
        string = char #Обновляется текущая строка на текущий символ.
if string in LZW_dict:
    LZW_encoded.append(LZW_dict[string]) #После обработки всех символов текста, закодированные значения хранятся в списке LZW_encoded.
LZW_encoded_res = "" #Инициализируется пустая строка для хранения закодированных результатов.
for seq in LZW_encoded: #Для каждого закодированного значения выполняется следующее:
    bits = 0 #для хранения количества бит для кодирования значения.
    if seq == 0: #Если значение равно 0, то количество бит устанавливается равным исходному количеству бит
        bits = init_bits
    elif ceil(log2(seq)) < init_bits: #Если количество бит для кодирования значения меньше исходного количества бит, устанавливается исходное количество бит.
        bits = init_bits
    else:
        bits = ceil(log2(seq)) #минимальное количество бит, необходимых для кодирования значений
    LZW_encoded_res += format(seq, f'0{bits}b') #Закодированное значение добавляется к строке с использованием форматирования бинарного представления с заданным количеством бит.
with open('output3.txt', 'w') as file:
    file.write("Словарь: " + str(LZW_dict))
    file.write("\n\n")
    file.write("Закодированная строка (битовая): " + LZW_encoded_res)
    file.write("\n\n")
    file.write("Закодированная строка (кодовая): " + str(LZW_encoded))
    file.close()
print()
print("Длина закодированного текста (метод LZW): ", len(LZW_encoded_res))
print("Степень сжатия по сравнению с равномерным (пятибитовым) кодированием:",
      round(100 - (len(LZW_encoded_res) / (5 * len(text))) * 100, 6), "%")
print("Степень сжатия по сравнению с кодами Хаффмана:",
      round(100 - (len(LZW_encoded_res) / len(encoded)) * 100, 6), "%")
