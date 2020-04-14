def leonardo():
    def leo(n):
        if n == 1:  # if you count the sequence from 1
            return 1
        elif n == 2:
            return 1
        else:
            return leo(n - 1) + leo(n - 2) + 1

    number = True
    while number:
        print("Enter the number. If you want to end the program, enter 0")
        number = int(input())
        if number == 0:
            break
        else:
            print(leo(number))


leonardo()
