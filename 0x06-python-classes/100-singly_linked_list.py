#!/usr/bin/python3
class Node:
    """Node class for singularly linked list"""
    def __init__(self, data, next_node=None):
        """init method to instantiate object"""
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """getter for data"""
        return self.__data

    @property
    def next_node(self):
        """getter for next_node"""
        return self.__next_node

    @data.setter
    def data(self, value):
        """setter for data"""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @next_node.setter
    def next_node(self, value):
        """setter for next_node"""
        if value is not None and type(value) is not Node:
            raise TypeError("next node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """singly linked list in Python"""
    def __init__(self):
        """init method to instantiate the singly linked list"""
        self.__head = None

    def sorted_insert(self, value):
        """inserts into linked list in sorted order"""
        newnode = Node(value)
        if self.__head is None:
            self.__head = newnode
        else:
            cur = None
            nextnode = self.__head
            nextval = nextnode.data
            while value > nextval and nextnode is not None:
                cur = nextnode
                nextnode = nextnode.next_node
                if nextnode is not None:
                    nextval = nextnode.data
            newnode.next_node = nextnode
            if cur is None:
                self.__head = newnode
            else:
                cur.next_node = newnode

    def __str__(self):
        """builds a string to return to print"""
        tmpnode = self.__head
        tmplist = []
        while tmpnode is not None:
            tmplist.append(str(tmpnode.data))
            tmpnode = tmpnode.next_node
        return "\n".join(tmplist)
