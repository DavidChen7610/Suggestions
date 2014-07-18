# -*- coding: utf-8 -*-
__author__ = 'florije'

import os


def get_content(file_path):
    if not (os.path.exists(file_path) and os.path.isfile(file_path)):
        raise Exception('file: %s not exist' % file_path)
    res_list = []
    with open(name=file_path, mode='r') as ap_file:
        for line in ap_file.readlines():
            res_list.append([item.strip() for item in line.strip('\n').split(',')])
    return res_list


def list_bubble_sort(list_arg, index):
    for j in range(len(list_arg) - 1, -1, -1):
        for i in range(j):
            if int(list_arg[i][index]) > int(list_arg[i + 1][index]):
                list_arg[i], list_arg[i + 1] = list_arg[i + 1], list_arg[i]
    return list_arg


def resolve_assignment_1st(file_path):
    org_list = get_content(file_path)
    sorted_list = list_bubble_sort(org_list[1:], 1)
    return [item for item in sorted_list[0:5]], [item for item in sorted_list[-1:-6:-1]]


def resolve_assignment_2nd(file_path):
    org_list = get_content(file_path)
    sorted_list = list_bubble_sort(org_list[1:], 3)
    return [item for item in sorted_list[-1:-4:-1]], [item for item in sorted_list if int(item[3]) == 0]


def resolve_assignment_3rd(file_path, percentage):
    org_list = get_content(file_path)
    sorted_list = list_bubble_sort(org_list[1:], 3)
    item_index = 0
    for item in sorted_list:
        if int(item[3]) > percentage:
            item_index = sorted_list.index(item)
            break
        elif int(item[3]) == percentage:
            item_index = sorted_list.index(item) + 1
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