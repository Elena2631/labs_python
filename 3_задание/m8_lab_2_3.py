def my_sort(name):
    from os import remove
    file = open(name, 'r')
    file2 = open("task3_2.txt", 'w', encoding='utf-8')
    number_of_lines = 0
    for line in file:
        m = line
        k = m.split()
        k.sort()
        b = ' '.join(k)
        file2.write(b)
        file2.write("\n")
        number_of_lines += 1
    file2.close()
    file.close()

    print(number_of_lines)

    sum2 = number_of_lines // 4
    file2 = open("task3_2.txt", 'r')
    file3 = open("task3_3.txt", 'w', encoding='utf-8')
    file4 = open("task3_4.txt", 'w', encoding='utf-8')
    file5 = open("task3_5.txt", 'w', encoding='utf-8')
    file6 = open("task3_6.txt", 'w', encoding='utf-8')
    i = 0
    while i < sum2:
        my_line = file2.readline()
        file3.write(my_line)
        i += 1
    i = 0
    while i < sum2:
        my_line = file2.readline()
        file4.write(my_line)
        i += 1
    i = 0
    while i < sum2:
        my_line = file2.readline()
        file5.write(my_line)
        i += 1
    i = 3 * sum2
    while i < number_of_lines:
        my_line = file2.readline()
        file6.write(my_line)
        i += 1
    file2.close()
    file3.close()
    file4.close()
    file5.close()
    file6.close()

    file3 = open("task3_3.txt", 'r')
    file3_1 = open("task3_3_1.txt", 'w')
    lines = []
    for line in file3:
        lines.append(line[1:])
    lines.sort()
    for line in lines:
        file3_1.write(line)
    file3.close()
    file3_1.write("|")
    file3_1.close()

    file4 = open("task3_4.txt", 'r')
    file4_1 = open("task3_4_1.txt", 'w')
    lines = []
    for line in file4:
        lines.append(line[1:])
    lines.sort()
    for line in lines:
        file4_1.write(line)
    file4.close()
    file4_1.write("|")
    file4_1.close()

    file5 = open("task3_5.txt", 'r')
    file5_1 = open("task3_5_1.txt", 'w')
    lines = []
    for line in file5:
        lines.append(line[1:])
    lines.sort()
    for line in lines:
        file5_1.write(line)
    file5.close()
    file5_1.write("|")
    file5_1.close()

    file6 = open("task3_6.txt", 'r')
    file6_1 = open("task3_6_1.txt", 'w')
    lines = []
    for line in file6:
        lines.append(line[1:])
    lines.sort()
    for line in lines:
        file6_1.write(line)
    file6.close()
    file6_1.write("|")
    file6_1.close()

    file3_main = open("task_main.txt", "w")
    file3_1 = open("task3_3_1.txt", "r")
    file4_1 = open("task3_4_1.txt", "r")
    file5_1 = open("task3_5_1.txt", "r")
    file6_1 = open("task3_6_1.txt", "r")
    line1 = file3_1.readline()
    line2 = file4_1.readline()
    line3 = file5_1.readline()
    line4 = file6_1.readline()
    while not ((line2 == "|") and (line3 == "|") and (line4 == "|") and (line1 == "|")):
        if line1 < line2:
            if line1 < line3:
                if line1 < line4:
                    file3_main.write(line1)
                    line1 = file3_1.readline()
                else:
                    file3_main.write(line4)
                    line4 = file6_1.readline()
            else:
                if line3 < line4:
                    file3_main.write(line3)
                    line3 = file5_1.readline()
                else:
                    file3_main.write(line4)
                    line4 = file6_1.readline()
        else:
            if line2 < line3:
                if line2 < line4:
                    file3_main.write(line2)
                    line2 = file4_1.readline()
                else:
                    file3_main.write(line4)
                    line4 = file6_1.readline()
            else:
                if line3 < line4:
                    file3_main.write(line3)
                    line3 = file5_1.readline()
                else:
                    file3_main.write(line4)
                    line4 = file6_1.readline()
    file3_main.close()
    file3_1.close()
    file4_1.close()
    file5_1.close()
    file6_1.close()
    remove("task3_3_1.txt")
    remove("task3_4_1.txt")
    remove("task3_5_1.txt")
    remove("task3_6_1.txt")
    remove("task3_3.txt")
    remove("task3_4.txt")
    remove("task3_5.txt")
    remove("task3_2.txt")
    remove("task3_6.txt")

my_sort("task3.txt")








