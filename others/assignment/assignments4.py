# -*- coding: utf-8 -*-
__author__ = 'florije'

"""
COMPLETED VERSION OF THE LINKED LIST MODULE
This module implements a simple singly-linked list.  Each node of a list
is a "dict" containing two entries:
    data: the value in the node
    next: a reference to the next node
If a node is the last one in the list, the value of next will be None.
An empty list is represented by the value None.

CISC 121, fall 2012
M. Lamb
"""

def insertValue(linkedList, index, value):
    """
    Adds a new element to a list.
    Parameters:
        value: the value for the new element
        index: the index for the new list element
    The new value does not replace the current element at
    position index; it is inserted before that element and
    the size of the list grows by 1.

    The return value is the head of the modified list.
    (That's usually the same as the lis parameter, unless
    we've added a new first element.)

    If the index is out of bounds, prints an error message and
    returns the list unchanged.
    """

    # create a new node to hold the value
    newNode = {'data': value}

    # special case: inserting at the beginning
    if index == 0:
        # This node is now the first node.  The first node of
        # the original list comes right after it.
        newNode['next'] = linkedList
        return newNode

    else:
        # find the node right before the insertion point
        before = nthNode(linkedList, index-1)
        if before == None:
            print "Error: illegal index to insertValue"
            return linkedList
        else:
            after = before['next'] # the node after the insertion point
            before['next'] = newNode
            newNode['next'] = after
            return linkedList # same first node


def listString(linkedList):
    """
    Returns a string describing the list, suitable for printing.
    """
    description = "["
    isFirst = True
    node = linkedList
    while node != None:
        if isFirst:
            isFirst = False
        else:
            description += ","
        description += str(node['data'])
        node = node['next']
    description += "]"
    return description


def printList(linkedList):
    """
    Prints a representation of a list
    """
    print listString(linkedList)


def createList(plist):
    """
    Creates and returns a linked list containing all of the elements
    of the Python-style list parameter.  A useful shortcut for testing.
    """
    linkedList = None
    for index in range(len(plist)-1, -1, -1):
        linkedList = insertValue(linkedList,0, plist[index])
    return linkedList


def nthNode(linkedList, n):
    """
    Helper method: returns a reference to node n in a list
    (counting from zero).
    Parameters: the list and an index n
    If there is no node n, returns None.
    """
    if n < 0 or linkedList == None:
        return None

    count = 0
    node = linkedList
    while count < n:
        node = node['next']
        if node == None:
            return None
        count += 1
    return node


def get(linkedList, index):
    """
    Returns the value of a list element
    Parameters: the list and the index of the element
    If the index is not the index of an existing list element,
        prints an error message and returns None
    """
    node = nthNode(linkedList, index)
    if node == None:
        print "Error: illegal index to get function"
        return None
    else:
        return node['data']


def set(linkedList, index, value):
    """
    Changes the value of a list element
    Parameters: the index of the element and the new value
    No return value (always None).
    If the index is not the index of an existing list element,
        writes an error and returns the list unchanged
    """
    node = nthNode(linkedList, index)
    if node == None:
        print "Error: illegal index to set function"
        return
    node['data'] = value



def delete(linkedList, index):
    """
    Deletes an element from a linked list.
    Parameter: list and index of the element to delete

    The return value is the head of the modified list.
    (That's usually the same as the linkedList parameter, unless
    we've deleted the first element.)

    If the index is out of bounds, writes an error message and
    returns the list unchanged.
    """

    # special case: deleting first element
    if index == 0 and linkedList != None:
        return linkedList['next']

    else:
        # the node before the one we're going to delete
        before = nthNode(linkedList, index-1)
        if before == None:
            print "Error: illegal index to delete function"
            return linkedList
        nodeToDelete = before['next']
        if nodeToDelete == None:
            print "Error: illegal index to delete function"
            return linkedList
        before['next'] = nodeToDelete['next']
        return linkedList


def getSize(linkedList):
    """
    Returns the size of a list
    """
    count = 0
    node = linkedList
    while node != None:
        count += 1
        node = node['next']
    return count
