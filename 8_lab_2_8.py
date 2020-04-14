def is_a_power_of_two():
    def power(my_number: int):
        while my_number > 1:
            my_number /= 2
        if my_number == 1:
            print('the number is a power of two')
        else:
            print('the number is not a power of two')

    number = True
    while number:
        print("Enter the number. If you want to end the program, enter 0")
        number = int(input())
        if number == 0:
            break
        else:
            print(power(number))


is_a_power_of_two()
