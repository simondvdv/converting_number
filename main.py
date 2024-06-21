from converting_defs import *

number = int_input_check()
convertors_start(number)


for i in range(32):  # цикл для теста при правильном вводе
    convertors_start(i)

for i in range(32):  # цикл для теста при правильном вводе в другую систему
    convertors_start(i, 3)


