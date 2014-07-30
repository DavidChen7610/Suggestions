__author__ = 'kiwi'
#___Assignment 3 by c .py____

'''
    Name:       Xiaoqi (cecilia) Zhong
Student Number: 10113208
    Date:       July 22, 2014
    Assignment: 3
'''


'''
Questions 1. a recursive function that accepts two arguments, x and y. The
function should return the value of x times y. Remember that multiplication can be performed as repeated addition
'''


def ques_1(x, y):
    if x == 0:  # make the base case that the multiplication does not run or stop at 0 in x
        return 0
    else:
        return y + ques_1(x-1, y)  # if x is larger then 0, the multiplication by continue adding repeat number


# make the list into string without any [] and ''

'''
Question 2
This method a recursive function that accepts an integer argument, n. The function display n lines of asterisks (*) on
the screen, with the first line showing 1 asterisk, the second line showing 2 asterisks, up to the nth line which
shows n asterisks.
'''


def ques_2(n):
    if n == 1:  # This is the base case to stop the program and print out the first line
        return n * '*'  # display the first line of asterisks when n is equal one
    else:
        return ques_2(n-1) + '\n'+n * '*'  # the n continue running when it is not equal one. Also, it print out the
    # asterisks on the line of n


'''
Question 3
Binary search represents a "divide and conquer" approach to searching. Implement a recursive binary search program.
'''


def search_item(search_value, search_list, low=0, high=None):
    midpoint = (low + high) / 2   # the mid is the location of mid number to divide the list into two part for searching
    if high is None:  # recall how we determined this in the iterative version
        high = len(search_list) - 1
    elif low > high:  # This situation is not logical
        return search_value, ' is not found at position'
    if search_value == search_list[midpoint]:  # value exactly at the midpoint
        return search_value, ' is found at position', midpoint
    elif search_value > search_list[midpoint]:  # when the searching value lager then the mid, low part increase one
        return search_item(search_value, search_list, midpoint + 1, high)
    elif search_value < search_list[midpoint]:  # when the searching value smaller then the mid, high part increase one
        return search_item(search_value, search_list, low, midpoint - 1)


def test_searching_item():
    print '7 is found at position', search_item(7, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0, 10)
    print '6 is found at position', search_item(6, [6, 7, 8, 9], 0, 3)
    print '0 is found at position', search_item(0, [6, 7, 8, 9], 0, 3)
    print '100 is found at position', search_item(100, [0, 50, 100, 150, 200], 0, 4)
    print '1 is found at position', search_item(1, [1], 0, 1)


'''
Question 4
This a recursive function called findMin to find the minimum value in a list of integers. The min is the smaller of the
first item and the min of all the other items.

'''


def find_min(mylist):
    min_value = mylist[0]
    if len(mylist) == 0:
        return -1
    elif len(mylist) == 1:
        return min_value
    elif len(mylist) > 1:
        if min_value < find_min(mylist[1:]):
            return min_value
        elif min_value > find_min(mylist[1:]):
            return find_min(mylist=mylist[1:])


def test_find_min():
    mylist = [17, 49, 32, 6, -1]
    print 'The min of ', mylist, 'is ', find_min(mylist)
    mylist = [0]
    print 'The min of ', mylist, 'is ', find_min(mylist)



'''
This method with the function called return_menu to make a menu for player choose to back to main menu or end of
playing game.
'''


def return_menu():
    print '                 Do you want to return to the menu? '
    print '                     If yes, please enter 1. '
    print '                     If no, please enter 0 '
    print ''
    choice = raw_input("        Please enter 1 or 0 here for your choice: ")
    choice = int(choice)
    if choice == 1:
        print '----'*15
        menu()
    elif choice == 0:
        print '     Thank you for running the program!'
        print '----'*15
    else:
        print 'Please enter the number again ! '
        return_menu()

'''
This is a menu for us to be able to run the different parts.Also, it is the opening instruction for this program
before the player running this program.  After reading the menu and enter the program that they are going to player
the player can start the program. For questions 3 and 4, selecting to run these questions should simply call the given
test function.
'''


def menu():
    print '                                    Assignment 3                                                        '
    print '                 '
    print '                             Hi! Welcome to the program. ^-^                 '
    print '                 '
    print ' No.1: This is a recursive function that accepts two arguments, x and y. The function can return the '
    print '       value of x times y. Remember that multiplication can be performed as repeated addition'
    print '                 '
    print ' No.2: A recursive function that accepts an integer argument, n. The function display n lines of '
    print '       asterisks (*) on the screen, with the first line showing 1 asterisk, the second line '
    print '       showing 2 asterisks, up to the nth line which shows n asterisks.'
    print '                 '
    print ' No.3: Implement a recursive binary search program.'
    print '                 '
    print ' No.4: This a recursive function called findMin to find the minimum value in a list of integers. '
    print '       The min is the smaller of the first item and the min of all the other items.'
    print '                 '
    print '                                 ~~~~~~~ 5: Exit   ~~~~~~~~              '
    print '----'*15
    print ''
    option = raw_input('      Please enter the number of the menu that you wanna play: ')
    option = int(option)
    if option == 1:
        print " Welcome to the No. 1 !"
        print '                 '
        print ' This is a recursive function that accepts two arguments, x and y. The function can return the '
        print '         value of x times y. Remember that multiplication can be performed as repeated addition'
        print '                 '
        print " Please enter the x value and y value each time for the multiplications. "
        print '--' * 20
        x = raw_input(' Please enter the times( x ) that you want to add: ')
        x = int(x)
        y = raw_input(' Please enter num( y ) that you want to add: ')
        y = int(y)
        print ques_1(x, y)
        print '--' * 20
        return_menu()
    elif option == 2:
        print ' No.2: A recursive function that accepts an integer argument, n. The function display n lines of '
        print '                 asterisks (*) on the screen, with the first line showing 1 asterisk, the second line '
        print '                 showing 2 asterisks, up to the nth line which shows n asterisks.'
        print '--' * 20
        n = raw_input(' Please inter the integer for making a graph of asterisks(*)')
        n = int(n)
        ques_2(n)
        print ques_2(n)
        print '--' * 20
        return_menu()

    elif option == 3:
        print ' No.3: Implement a recursive binary search program.'
        print '                '
        test_searching_item()
        print '                '
        return_menu()
    elif option == 4:
        print ' No.4: This a recursive function called findMin to find the minimum value in a list of integers. '
        print '              The min is the smaller of the first item and the min of all the other items.'
        print '                '
        test_find_min()
        print '                '
        return_menu()
    elif option == 5:
        print '                 '
        print " You have already exited the program. Thank you for running the program! "
    else:
        print '                 '
        print " Please enter the number again! "

menu()
