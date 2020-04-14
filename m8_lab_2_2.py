def file_generation(name: str, mb: float, a: int, b: int, c: int, d: int):
    from random import choice, randint
    from string import ascii_letters

    if a > b:
        a, b = eval(input("Error, a must be less than b! Enter a and b: "))
        print("K = (", a, ",", b, ")")
    else:
        print("K = (", a, ",", b, ")")

    if c > d:
        c, d = eval(input("Error, c should be less than d! Enter c and d: "))
        print("L = (", c, ",", d, ")")
    else:
        print("L = (", c, ",", d, ")")

    file = open(name, 'w', encoding='utf-8')
    mb_in_b = mb * 1024 * 1024
    line_length = 0
    while line_length < mb_in_b:
        i = 0
        ran_num_of_words = randint(a, b)
        while i < ran_num_of_words - 1:
            word_length = randint(c, d)
            word = ''.join(choice(ascii_letters) for j in range(word_length))
            file.write(word)
            file.write(" ")
            line_length = line_length + (len(word) + 1)
            i += 1
        word_length = randint(c, d)
        word = ''.join(choice(ascii_letters) for j in range(word_length))
        file.write(word)
        file.write("\n")
        line_length = line_length + (len(word) + 1)
        percent = line_length / mb_in_b * 100
        print(percent, "%")
    file.close

file_generation("mi.txt", 3, 4, 5, 6, 3)