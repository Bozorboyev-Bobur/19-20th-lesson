# file = open('data.txt', 'w')

# file.write('Elbek')
# file.write('\n')
# file.write('Khakimbekov')
# file.writelines(['1', '2', '3'])
# file.read()
# file.close()

# file = open('data.txt', 'r')
# Читаем файл с помощью метода read
# print(file.read())
# print(file.read(43))
# Считать 1, 2, 5 и 8 строки
# lines = [1, 2, 5, 8]

# lineCounter = 1
# while True:
#     line = file.readline()
#     if line == '': break
#     else:
#         if lineCounter in lines: print(line, end='')
#         else: pass
#         lineCounter += 1

# file.close()

# print(file.readlines())


# file = open('number.txt', 'w')

# a = 10
# for i in range(1, a + 1):
#     if i == a: file.write(f'{i}')
#     else:file.write(f'{i}\n')

# file.close()

# file = open('number.txt', 'r+')

# nums = file.readlines()

# file.seek(0)

# for num in nums:
#     file.write(f'{str(int(num) * 2)}\n')
#     print(file.tell())
# file.close()

# print(file.closed)



file = open('names.txt', 'r+')
years = [1999, 2000, 2004, 2003, 2002, 2005, 2001]
names = file.readlines()
file.seek(0)

new_names = []
for i in range(0, len(years)):
    new_names.append(f'{names[i].strip()} {years[i]}\n')

file.writelines(new_names)

file.close()

