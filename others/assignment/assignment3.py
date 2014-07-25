# -*- coding: utf-8 -*-
__author__ = 'florije'

'''
Write a recursive function that accepts two arguments, x and y. The
function should return the value of x times y.
'''


def func_time(x, y):
    if x == 0:
        return 0
    elif x == 1:
        return y
    else:
        return y + func_time(x - 1, y)


'''
Write a recursive function that accepts an integer argument, n. The
function should display n lines of asterisks (*) on the screen, with the first
line showing 1 asterisk, the second line showing 2 asterisks, up to the nth
line which shows n asterisks.
'''


def func_asterisk(n):
    if n == 0:
        pass
    elif n == 1:
        return '*'
    else:
        return func_asterisk(n - 1) + '\n' + n * '*'


'''
Binary search represents a "divide and conquer" approach to searching.
Implement a recursive binary search program.
'''


def func_binary(search_value, list_arg, low=0, high=None):
    if high is None:
        high = len(list_arg) - 1
    if low > high:
        return '%s is not in the search_list' % search_value

    middle = (low + high) / 2

    if list_arg[middle] == search_value:
        return '%s is found at position %s' % (search_value, middle)
    elif list_arg[middle] < search_value:
        return func_binary(search_value, list_arg, middle + 1, high)
    elif list_arg[middle] > search_value:
        return func_binary(search_value, list_arg, low, middle - 1)


'''
Write a recursive funct ion called findMin to find the minimum value in a
list of integers. The min is the smaller of the first item and the min of all
the other items.
'''


def func_find_min(list_arg):
    min_value = list_arg[0]
    if len(list_arg) == 1:
        return min_value
    else:
        tmp_value = func_find_min(list_arg[1:])
        if tmp_value < min_value:
            min_value = tmp_value
    return min_value


if __name__ == '__main__':
    print 'Now you will see the four problems and you will select one to see the test of the function:'
    print 60 * '-'
    print 'number 1 for :'
    print 'Write a recursive function that accepts two arguments, x and y. The ' \
          'function should return the value of x times y.'
    print 60 * '-'
    print 'number 2 for :'
    print 'Write a recursive function that accepts an integer argument, n. The' \
          'function should display n lines of asterisks (*) on the screen, with the first' \
          'line showing 1 asterisk, the second line showing 2 asterisks, up to the nth' \
          'line which shows n asterisks.'
    print 60 * '-'
    print 'number 3 for :'
    print 'Binary search represents a "divide and conquer" approach to searching.' \
          'Implement a recursive binary search program.'
    print 60 * '-'
    print 'number 4 for :'
    print 'Write a recursive funct ion called findMin to find the minimum value in a' \
          'list of integers. The min is the smaller of the first item and the min of all' \
          'the other items.'
    while True:
        selected_num = int(raw_input('Please input your choice:'))
        if not selected_num in [1, 2, 3, 4]:
            print 'You have input a wrong number! please try again!'
            continue

        if selected_num == 1:
            print 'function func_time() need two args, please input them!'
            x_arg = int(raw_input('x_arg is:'))
            y_arg = int(raw_input('y_arg is:'))
            print 'The result of the func_time(%s, %s) is %s' % (x_arg, y_arg, func_time(x_arg, y_arg))
        elif selected_num == 2:
            print 'function func_asterisk() need one args, please input it!'
            n_arg = int(raw_input('n_arg is:'))
            print 'The result of the func_asterisk(%s) is:' % n_arg
            print func_asterisk(n_arg)
        elif selected_num == 3:
            print '7 is found at position', func_binary(7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10)
            print '6 is found at position', func_binary(6, [6, 7, 8, 9], 0, 3)
            print '0 is found at position', func_binary(0, [6, 7, 8, 9], 0, 3)
            print '100 is found at position', func_binary(100, [0, 50, 100, 150, 200], 0, 4)
            print '1 is found at position', func_binary(1, [1], 0, 1)
        elif selected_num == 4:
            myList = [17, 49, 32, 6, -1]
            print 'The min of ', myList, 'is ', func_find_min(myList)
            myList = [0]
            print 'The min of ', myList, 'is ', func_find_min(myList)