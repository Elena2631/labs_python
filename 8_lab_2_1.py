import os 
import math

def read_file(filename):
    f=open(filename, "r")
    str_array = f.readline()
    return [float(i) for i in str_array.split(' ')]


if __name__ == "__main__":
    filename = 'task1.txt'
    array = read_file(filename)
    size = len(array)
    batch_size = math.ceil(math.sqrt(size))
    sqrt_array = [sum(array[i*batch_size:(i+1)*batch_size]) for i in range(size// batch_size)]
    cycle_flag = True
    while cycle_flag:
        print("Enter your value l and r. Press 'exit' for exit from the program ")
        str_input = input() 
        if str_input == 'exit':
            cycle_flag = False
            continue
        l, r = [int(i) for i in str_input.split(' ')]
        from_ind = math.ceil(l / batch_size)
        to_ind = math.floor(r / batch_size)
        if from_ind > to_ind:
            lr_sum = sum(array[l:r])
        else:
            lr_sum = sum(array[l:batch_size*from_ind])
            lr_sum += sum(sqrt_array[from_ind:to_ind])
            lr_sum += sum(array[batch_size*to_ind:r])
        print("In interval (%s, %s) is %s" % (l, r, lr_sum) )

