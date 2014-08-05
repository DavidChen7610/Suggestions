

'''
    Name:       Xiaoqi (cecilia) Zhong
Student Number: 10113208
    Date:       August 4th, 2014
    Assignment: 4
'''

'''
Questions
1. Using the code provided in linkedList.py, complete the insertNode(list, index, value) function. Unlike the
insertValueHead() function, this function will be a general insert function that will insert a node into an empty
list, at the head of a list, at the tail of a list or in the middle. Although nodes are not "numbered" like a list,
we can think of each node as having a position (index) with the head node being 0, the next node being 1 and so on.
The insertNode() function will use the "index" parameter to indicate where in the list to insert the new node. The
function returns the head of the modified list.The function inserts a node with "data" = value at position "index" in
the list. As an example, calling "insertNode(list, 2, 7) where list is a list containing the values (1, 4, 13, 17)
will resulting in a list containing (1, 4, 7, 13, 17). You may use the nthNode(linkedList, index) function that is
provided to assist you with this function. nthNode() returns the node at the "index" position in the list. Note that
if the index is 0, this indicates that you are inserting at the head of the list. The function should return the head
of the list. Use the testInsert() code to ensure that your function works.
'''

"""
Creates and returns a linked list containing all of the elements
of the Python-style list parameter.  A useful shortcut for testing.
"""
def createList(plist):
    linkedList = None
    # goes backwards, adding each element to the beginning of the list.
    for index in range(len(plist)-1, -1, -1):
        linkedList = insertValueHead(linkedList, plist[index])
    return linkedList

'''
Create an empty linked list
'''
def emptyList():
  return None   #absence of a value -- nothing

'''
Creates a string representation of the values in the linked list such as:
5->6->9->14.
'''

def listString(linkedList):
    ptr = linkedList  # create another linked list(ptr) from linkedList for editing
    str1 = ''  # create the empty string
    while  ptr != None  :  # naje sure that the linked list is not the empty list
        str1 += str(ptr['data'])  # add the first node into ptr
        ptr = ptr['next']    # delet the first one in the pt    ----
        if ptr!= None  :  # if there is another node after ptr['data']
            str1 += "-> "  # adding the sign to connect the node together


    str1 = str1 # finish editing the str1
    return str1




'''
Inserts a new node containing the value "value" to the head of the list.
LinkedList is the head of the list to be added to ; Value is the data to be stored in the node
'''
def insertValueHead(linkedList, value):
    newnode = {} # creating a new linked list named newnode
    newnode["data"] = value  # adding the new node['data'] with the ptr(value) into the newnode
    newnode["next"] = linkedList # the next node of the newnode is the linkedlist

    linkedList = newnode
    return newnode


'''
    The following code is here for demonstration purposes, to help
    you to understand how to create a list.  First we create an empty list
    and add 2 values using teh insertValueHead() function.  The resulting list
    will be a list with values 20 and then 9.
    You should replace the following code with the code to start the execution
    of your program (that is, call each of the test functions).
'''


def main():
    linkedList = emptyList()   # linkedList is the linked list without any node in it
    print "Inserting a new node with value 9"
    linkedList = insertValueHead(linkedList, 9)  # the value = 9 is the value which going to inser into linked list
    print "The list contains the following values", listString(linkedList)
    print "Inserting a new node with value 20"
    linkedList = insertValueHead(linkedList, 20)
    print "The list contains the following values", listString(linkedList)
    #The list contains the following values 20->9 (Complete)
main()
'''
The insertNode() function will use the "index" parameter to indicate where in the list to insert the new node. The
function returns the head of the modified list.The function inserts a node with "data" = value at position "index" in
the list. As an example, calling "insertNode(list, 2, 7) where list is a list containing the values (1, 4, 13, 17)
will resulting in a list containing (1, 4, 7, 13, 17).
'''
'''
This function is a general function for inserting values in a linked list.  I have provided a skeleton.
'''
def insertNode(list, index, value):
     #case 1:  Adding to the head of the list -- index == 0
         #which is the new head of the list.
    newnode = {}  # Create a new node and pass back the new node,
    newnode['data'] = value  # value == 0
    newnode_sec =  list
    if index == 0:  # against the invalid index here  # adding the node at teh beginning of the list
        newnode['next']= list
        list = newnode  # adding the newnode at the beginning  and change to list
    elif  index != 0:   # adding the number at the middle of the linked list or the end of the linked list
        index = index -1  # make the searching stop at before index for value inserting
        count = 0
        while count < index:
            if list['next'] == None:
                print 'The result is en error'
                return False
            list = list['next']
            count += 1

        if count == index :
            newnode['next'] = None
            list['next'] =  newnode
        list = newnode_sec
    else:
        return None

    return list
#case 2:  Adding elsewhere in the list use nthNode() to find the node before the position to insert
    #  (this will be at index - 1)if this function returns None, then the index is invalid --
# print an error message otherwise, add the node

"""
Helper method: returns a reference to node n in a list counting from zero).
Parameters: the list and an index n . If there is no node n, returns None.
You may use the nthNode(linkedList, index) function that is
provided to assist you with this function. nthNode() returns the node at the "index" position in the list. Note that
if the index is 0, this indicates that you are inserting at the head of the list. The function should return the head
of the list.
"""
def nthNode(linkedList, n):
    ptr = linkedList   # create the ptr whcih is the same as linkedList
    count = 0  # start from the location of 0 in the linked list
    if n < 0:
        return None  # against the unvalid index
    while ptr != None and count < n:
        ptr = ptr['next']  # deleting the dead of the linked list 'ptr'
        count += 1   # count increase by one to make sure it search by each node
    return ptr    # this is the linlked list with the head of the list whihch is the value at the index

'''
Use the testInsert() code to ensure that your function works.
'''
def testInsert():
#{'data':0,'next':{'data': 1,'next':{'data': 2,'next':{'data':3,'next':{'data':4,'next':{'data':5,'next':{'data':6,'next':None}}}}}}}
  #test code to ensure that insertNode is working correctly.
  myList = createList([1, 2, 3, 4, 5, 6])
  print "The initial list", listString(myList)  # The initial list 1->2->3->4->5->6
  #insert 0 at the head
  myList = insertNode(myList,0, 0)
  print "Inserted 0 at the start of list: ", listString(myList)  #Inserted 0 at the start of list:  0->1->2->3->4->5->6
  #insert 7 at the end
  myList = insertNode(myList, 7, 7)   #  Inserted 7 at the end of list:  0->1->2->3->4->5->6->7
  print "Inserted 7 at the end of list: ", listString(myList)
  myList= insertNode(myList, 3, 2.2)
  print "Inserted 2.2 in the 3rd position ", listString(myList)
  myList = insertNode(myList, 26, 12)   #should generate an error

testInsert()
'''


2. Complete the function switch(list, index) that will switch the nodes at index with the head of the list. So, for
example if your list (list) has the values [1, 7, 9, 12] and you call switch(list, 2), your resulting list will be
[9, 7, 1, 12]. You may NOT assume that index is a valid index. Your function must test for these cases. Begin, however,
with code that makes this assumption & modify your code afterwards to take into account these special cases. Print
an error if index is invalid and return the head of the list with the list unchanged. Use the testSwitch() function
provided in the code to ensure that your function works.


'''
# your_list = [1, 7, 9, 12]   # called: switch(list, 2)  --->  [9, 7, 1, 12]

def switch(list, index):
    re_list = list
    switch_list = []
    while re_list != None:
        switch_list.append(re_list['data'])
        re_list = re_list['next']
    list = switch_list[:(index+1)][::-1] + switch_list[(index +1):]  # list = [30, 20, 10, 40, 50, 60]
      # switch the aprt of list and
    for l in range(len(list)):   # len(list) =  6
        if l == 0:
            linkedlist_list = {}  # making the list for the linkedList
            linkedlist_list['data'] = list[(len(list))-l-1]
            linkedlist_list['next'] = None  # add linkedList['next'] = None into linkedList
              #
        while l > 0:
            linkedlist_list['next']= linkedlist_list
            linkedlist_list['data'] = list[(len(list))-l]
    linkedlist_list = linkedlist_list
    return linkedlist_list


def testSwitch():
    #test code to ensure that switch() is working correctly.
    myList = createList([10, 20, 30, 40, 50, 60])
    print "The initial list", listString(myList)  # The initial list 10->20->30->40->50->60
    myList = switch(myList, 2)
    print myList
    print "Switching the 1 and the 2.  Resulting list is ", listString(myList)
    myList = switch(myList, 3)
    print "Switching the 4 and the 5.  Resuling list is ", listString(myList)
    myList = switch(myList, 5)
    myList = switch(myList, 29)  #should result in an error





'''
3. Complete the function sumEvens(list) that computes the sum of all the even values contained in the list. For
instance, if your list contains [1, 7, 4, 15, 16, 22] the sum that is returned is 44, the result of 4 + 16 + 22. Use
the testSumEvens() function provided in the code to ensure that your function works. You may assume that your list only
contains integers as its "data" values. The "main" function should be used to call the test functions. The code that is
currently in the main() function is to help

'''



def sumEvens(linkedList):
    linked_list = linkedList
    add_sum = 0    # adding the sum satrt with 0
    while linked_list['next'] != None:
        if (linked_list['data']) %2 == 1:  # pass the odd number and continue searching
            linked_list = linked_list['next']   # delet the first number
            if linked_list['next'] == None:
                return add_sum
        if (linked_list['data']) %2 == 0:  # find the even number
            add_sum +=  linked_list['data']  # add the even number in the add_sum
            linked_list = linked_list['next']  # delet the first number
            if linked_list['next'] == None:
                return add_sum
    add_sum
    return add_sum


def testSumEvens():
    myList = createList([14, 21, 29, 2, 16,49, -26])   # teh sum should == 6
    print "The sum of the even numbers in the first list is ", sumEvens(myList)
    myList = createList([])
    print "The sum of the even numbers in an empty list is ", sumEvens(myList)
    myList = createList([5, 15, 25])
    print "The sume of the even numbers in the final list is ", sumEvens(myList)

testSumEvens()


#



















