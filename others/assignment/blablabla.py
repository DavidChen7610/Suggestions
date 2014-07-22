__author__ = 'kiwi'
'''
This method takes out the file 'APExam.txt' with editing the type sorting. It prevents some special characters and
unecessary letters in the content
'''


def read_file(file_path):
    ape_list = []   # ape_list making as a list
    with open(file_path, 'rb+') as in_file:
        for line in in_file.readlines():
            # make sure that the lien is pure with split for making the list
            ape_list.append(line.strip().split(','))
            print line.strip('\n\r').split(',')  # making the list from the string of the file and the code includes'\n'
            #and '\r',which need to get rid of
    return ape_list  # the return make sure modify the code to handle the new data structure
''' This method depend on the bubble sort to sort the list that is going to input by replacing the numbers from lowest
 to highest.
'''


def sort_num(second_item, index):
    for one_item in range(1, len(num)):   # b sorting the number of the list
        #use second_item to "walk" the list from position one_item towards position 0
        second_item = one_item
        while (second_item > 0) and (num[second_item-1] > num[j]):
            #if the element on the left is larger, swap the items
            num[second_item-1], num[second_item] = num[second_item], num[second_item-1]
    return sort_num(second_item, index)

'''
    This method,resolved_assignment_1st, used for sort the data based on the total number of students taking the test.
    It also display the min-five and max-five data from the list.

'''


def resolved_assignment_1st(file_path):
    ori_list = read_file(file_path)   # input the original list of APExam for editing
    total_num_list = sort_num(ori_list[:1], [1])   # choosing the first and second column from the list of APExam
    print total_num_list  # the state name and the total number of students taking the test in that state
    return [sort_item for sort_item in total_num_list[0:5], index], \
           [sort_item for sort_item in total_num_list[-5:-1], index]
    #print out the names of the five states with the highest number and the five states with the lowest number.


'''
    This method, resolved_assignment_2nd select the first column and the forth column from the list to resort the data
     based on the percentage of female students taking the test
'''


def resolved_assignment_2nd(file_path):
    import re  # using import the research for searching the non-female exam in the states
    ori_list = read_file(file_path)
    passed_rate = sort_num(ori_list[:1], [3])
    print passed_rate  # Print the state name and the percentage of females taking the test.
    return re.findall(r'0', passed_rate, index)   # display the number of states that had no females taking the test.

'''
    Allow your user to search for states which have more than a given percentage of women writing the exam. Prompt the user for the
percentage, and return all the states with a percentage more than the
percentage indicated.  you should issue an error if the user enters a number less than 0 or greater
than 100. Try to make your search as efficient as possible (although you will not be marked on efficiency).
'''


def resolved_assignment_3rd(file_path, index):
    rate_input = raw_input(int('Please enter the number for the percentage here: '))  # assume integer input
    ori_list = read_file(file_path)  # get the original list from the file
    female_rate = sort_num(ori_list[3], index)  # sorting the list for searching
    female_rate.append(rate_input)  # add the number that the user input into the list
    if int(rate_input < 0) and int(rate_input > 100):  # avoid the situation that the number out of range
        print 'Please try again with the range of 0 to 100'
    elif 0 < rate_input < 100:
            for sort_item1 in range(1, len(num)):
                #use sort_item2 to "walk" the list from position sort_item1 towards position 0
                sort_item2 = sort_item1
                while (sort_item2 > 0) and (num[sort_item2-1] > num[sort_item2]):
                    #if the element on the left is larger, swap the items
                    num[sort_item2-1], num[sort_item2] = num[sort_item2], num[sort_item2-1]

            return resolved_assignment_3rd ([sort_item for sort_item in ori_list[rate_input:]],index)


if __name__ == '__main__':
    resolved_assignment_1st('APExam.txt')