# -*- coding: utf-8 -*-
__author__ = 'florije'
import random


def dice():
    '''
    This is the first solution of the problem one, input is empty, and the return is null
    it will print the result of the problem show.
    :return:null
    '''
    dice_num = raw_input('Enter the number of pairs of rolls:')  # enter the times of rolling dice here
    res = {}
    print 'The result of the dice is:'
    for i in range(int(dice_num)):  # the number of the program goes to run here
        num = random.randint(1, 6) + random.randint(1, 6)  # the regular dice is 6 sided dice
        if num in res:
            res[num] += 1  # count times
        else:
            res[num] = 1  # start from 1
        print '%s--------%s' % (i + 1, num)  # frequency distribution table
    print 'The result of the calculated dice is:'
    for k, v in res.items():
        print '%s--------%s' % (k, v * '*')  # value of frequency histogram


def get_size():
    '''
    This function will get the pyramid size from the console, and will return the int(pyramid_size)
    :return:int(pyramid_size)
    '''
    pyramid_size = raw_input('Please input the size of the pyramid(number must!!!):')
    return int(pyramid_size)


def pyramid(size_arg):
    '''
    enter the value for the size of pyramid, and print the picture
    :param size_arg:
    :return:null
    '''
    for item in range(size_arg):  # range(size_arg): from 0 to size
        print (' ' * (size_arg - item - 1) + '*' * (item * 2 + 1))


def rot13(string):
    '''
    the function of the Caesar cipher
    :param string:the string you will to encrypted or decrypted
    :return:the string decrypted or encrypted
    '''
    str_res = ""
    for s in string:
        if s.islower():
            str_res += chr((ord(s) - ord('a') + 13) % 26 + ord('a'))
        elif s.isupper():
            str_res += chr((ord(s) - ord('A') + 13) % 26 + ord('A'))
        else:
            str_res += s
    return str_res


def testRot13():
    '''
    the test function you include in the file
    :return:
    '''
    encrypted = rot13("I have encrypted this message")
    print encrypted
    decrypted = rot13(encrypted)
    print decrypted
    encrypted = rot13("Computing is the profession for me")
    print encrypted
    decrypted = rot13(encrypted)
    print decrypted

if __name__ == '__main__':
    while True:
        print '-'*40
        print 'Now there are three problems to show!'
        print '1.Rolling 6 sided dice can teach us about probability.'
        print '2.Draw a pyramid of a specific size.'
        print '3.Use Caesar cipher to encrypt and decrypted military messages.'
        print 'Please choose the problem you want to play:'
        item_num = raw_input('Please input 1 or 2 or 3 to select the problem(or you can exit with ctrl+c):')
        try:
            selected_num = int(item_num)
        except Exception as e:
            print e.message
            continue

        if selected_num not in [1, 2, 3]:
            # raise Exception('Wrong num input, Please enter a num again')
            print 'Wrong num input, Please enter a num again'
            continue

        if selected_num == 1:
            print '-'*40
            print '1.Rolling 6 sided dice can teach us about probability.'
            dice()
        elif selected_num == 2:
            print '-'*40
            print '2.Draw a pyramid of a specific size.'
            size = get_size()
            pyramid(size)
        elif selected_num == 3:
            print '-'*40
            print '3.Use Caesar cipher to encrypt and decrypted military messages.'
            testRot13()
        else:
            raise Exception('Something is wrong!')