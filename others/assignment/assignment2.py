# -*- coding: utf-8 -*-
__author__ = 'florije'

import os


def get_content(file_path):
    '''
    This method will get the content from the file and return a list with lines data
    :param file_path: the path of the file you will to deal with
    :return: res_list like a data as [['State', 'Total #', '% passed', '%female'], ['Alabama', '126', '79', '17']]
    '''
    # method will raise error if file not exist
    if not (os.path.exists(file_path) and os.path.isfile(file_path)):
        raise Exception('file: %s not exist' % file_path)
    res_list = []  # res_list init
    # with open method to get the content from a file
    with open(name=file_path, mode='r') as ap_file:
        for line in ap_file.readlines():
            # because a line will have a '\n' or some item will has blanks so will strip it and items
            res_list.append([content_item.strip() for content_item in line.strip('\n').split(',')])
    return res_list


def list_bubble_sort(list_arg, index):
    '''
    This method is the ordered bubble_sort(from little to big)
    :param list_arg: the origin list like [2, 4, 1, 3]
    :param index: the index of the list item
    :return:list_arg like a data as [1, 2, 3, 4]
    '''
    for j in range(len(list_arg) - 1, -1, -1):
        for i in range(j):
            if int(list_arg[i][index]) > int(list_arg[i + 1][index]):
                list_arg[i], list_arg[i + 1] = list_arg[i + 1], list_arg[i]
    return list_arg


def resolve_assignment_1st(file_path):
    '''
    this is the solution for the first problem
    :param file_path: the path of the target file
    :return: min_five items and max_five items
    '''
    # get the origin list from the file
    org_list = get_content(file_path)
    # get the sorted list by the index
    sorted_list = list_bubble_sort(org_list[1:], 1)
    # return min_five items and max_five items
    return [sorted_item for sorted_item in sorted_list[0:5]], [sorted_item for sorted_item in sorted_list[-1:-6:-1]]


def resolve_assignment_2nd(file_path):
    '''
    this is the solution for the second problem
    :param file_path:the path of the target file
    :return:max_three items and zero_members
    '''
    # get the origin list from the file
    org_list = get_content(file_path)
    # get the sorted list by the index
    sorted_list = list_bubble_sort(org_list[1:], 3)
    # return max_three items and zero_members
    return [sorted_item for sorted_item in sorted_list[-1:-4:-1]], \
           [sorted_item for sorted_item in sorted_list if int(sorted_item[3]) == 0]


def resolve_assignment_3rd(file_path, percentage_arg):
    '''
    this is the solution for the third problem
    :param file_path:the path of the target file
    :param percentage_arg:the item user will input into
    :return:sorted_list the items more than percentage_arg
    '''
    # get the origin list from the file
    org_list = get_content(file_path)
    # get the sorted list by the index
    sorted_list = list_bubble_sort(org_list[1:], 3)
    item_index = 0
    for sorted_item in sorted_list:
        if int(sorted_item[3]) > percentage_arg:
            item_index = sorted_list.index(sorted_item)
            break
        elif int(sorted_item[3]) == percentage_arg:
            item_index = sorted_list.index(sorted_item) + 1
            break
    return sorted_list[item_index:]

if __name__ == '__main__':
    file_name = 'APExam.txt'

    # assignment_1st
    min_five, max_five = resolve_assignment_1st(file_name)
    for min_item in min_five:
        print 'State Name: %s, Total Num: %s' % (min_item[0], min_item[1])
    for max_item in max_five:
        print 'State Name: %s, Total Num: %s' % (max_item[0], max_item[1])

    # assignment_2nd
    max_three, zero_members = resolve_assignment_2nd(file_name)
    for max_item in max_three:
        print 'State Name: %s, The percentage of female: %s' % (max_item[0], max_item[3])

    print 'The number of states that  had no females taking the test is: %s' % len(zero_members)

    # assignment_3rd
    print 'Hello, you will get the states which have more than a given percentage of women writing the exam.'
    print 'Msg: you can enter Ctrl+C to stop.'
    while True:
        percentage = raw_input('Please input the percentage(integer between 0-100, please!):')
        items_3rd = resolve_assignment_3rd(file_name, int(percentage))
        for item in items_3rd:
            print 'State Name: %s, The percentage of female: %s' % (item[0], item[3])