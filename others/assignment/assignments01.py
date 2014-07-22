__author__ = 'kiwi'

'''
This method takes out the file 'APExam' with editing the type sorting. It prevents some special characters and
unecessary letters in the content
'''


def read_file(file_path):
    ape_list = []  # ape_list making as a list
    with open(file_path, 'r') as file:
        for line in file.readlines():
            # make sure that the lien is pure with split for making the list
            ape_list.append(line.strip('\n').split(','))
            # print line.strip('\n\r').split(',')  # making the list from the string of the file and the code includes'\n'
            # and '\r',which need to get rid of
    return ape_list  # the return make sure modify the code to handle the new data structure


''' This method depend on the bubble sort to sort the list that is going to input by replacing the numbers from lowest
 to highest.
'''


def sort_num(orig_list, index):
    for i in range(len(orig_list) - 1, -1, -1):
        for j in range(i):
            if int(orig_list[j][index]) > int(orig_list[j + 1][index]):
                orig_list[j], orig_list[j + 1] = orig_list[j + 1], orig_list[j]
    return orig_list


'''
    This method,resolved_assignment_1st, used for sort the data based on the total number of students taking the test.
    It also display the min-five and max-five data from the list.

'''


def resolved_assignment_1st(file_path):
    ori_list = read_file(file_path)  # input the original list of APExam for editing
    total_num_list = sort_num(ori_list[1:], 1)  # choosing the first and second column from the list of APExam
    # print total_num_list  # the state name and the total number of students taking the test in that state
    return [sort_item for sort_item in total_num_list[0:5]], \
           [sort_item for sort_item in total_num_list[-1:-6:-1]]
    # print out the names of the five states with the highest number and the five states with the lowest number.


'''
    This method, resolved_assignment_2nd select the first column and the forth column from the list to resort the data
     based on the percentage of female students taking the test
'''


def resolved_assignment_2nd(file_path):
    import re  # using import the research for searching the non-female exam in the states

    ori_list = read_file(file_path)
    sorted_list = sort_num(ori_list[1:], 3)
    return [sorted_item for sorted_item in sorted_list[-1:-4:-1]], \
           [sorted_item for sorted_item in sorted_list if int(sorted_item[3]) == 0]


'''
    Allow your user to search for states which have more than a given percentage of women writing the exam. Prompt the
    user for the percentage, and return all the states with a percentage more than the
percentage indicated.  you should issue an error if the user enters a number less than 0 or greater
than 100. Try to make your search as efficient as possible (although you will not be marked on efficiency).
'''


def resolved_assignment_3rd(file_path, percentage_arg):
    # get the origin list from the file
    org_list = read_file(file_path)
    # get the sorted list by the index
    sorted_list = sort_num(org_list[1:], 3)
    item_index = len(sorted_list)
    for sorted_item in sorted_list:
        if int(sorted_item[3]) > percentage_arg:
            item_index = sorted_list.index(sorted_item)
            break
        elif int(sorted_item[3]) == percentage_arg:
            item_index = sorted_list.index(sorted_item) + 1
            break
    return sorted_list[item_index:]


file_path = 'APExam.txt'

# assignment 1
min_five, max_five = resolved_assignment_1st(file_path)
print 'The min five state is:'
print '-' * 60
for min_item in min_five:
    print 'State Name: ' + min_item[0] + ', Total Num: ' + min_item[1]
print 'The max five state is:'
print '-' * 60
for max_item in max_five:
    print 'State Name: ' + max_item[0] + ', Total Num: ' + max_item[1]

# assignment_2nd
print '-' * 60
max_three, zero_members = resolved_assignment_2nd(file_path)
for max_item in max_three:
    print 'State Name: %s, The percentage of female: %s' % (max_item[0], max_item[3])
print 'The number of states that  had no females taking the test is: %s' % len(zero_members)

# assignment_3rd
print '-' * 60
print 'Hello, you will get the states which have more than a given percentage of women writing the exam.'
print 'Msg: you can enter Ctrl+C to stop.'
while True:
    print '-' * 60
    rate_input = raw_input('Please input the percentage(integer between 0-100, please!):')
    percent_arg = -1
    try:
        percent_arg = int(rate_input)
    except Exception as e:
        print e.message
        continue
    if percent_arg < 0 or percent_arg > 100:
        print 'You should input right num!'
        continue
    items_3rd = resolved_assignment_3rd(file_path, percent_arg)
    for item in items_3rd:
        print 'State Name: ', item[0], 'The percentage of female: ', item[3]