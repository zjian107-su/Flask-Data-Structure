# This file of "[LinkedList.py](http://linkedlist.py/)" shows the implementation of LinkedList with Node. It has APIs such as: init(), to_list(), print_ll(), insert_beginning(), insert_at_end(), get_user_by_id()
# In LinkedList, if the head is not None, you can append all next nodes' data into the LinkedList by moving the pointer of the node and store its corresponding data.
# When inserting into an empty LinkedList(beginning), you need to address the head nad last_node first, then add nodes. If not empty, insert in the front by connecting the new node to the self.head()
# When inserting into the end of a LinkedList, if empty, use insertBeginning API. If not, append.

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        l = []
        if self.head is None:
            return l

        node = self.head
        while node:
            l.append(node.data)
            node = node.next_node
        return l

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f" {str(node.data)} ->"
            node = node.next_node
        ll_string += " None"
        print(ll_string)

    def insert_beginning(self, data):
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head

        new_node = Node(data, self.head)
        self.head = new_node

    def insert_at_end(self, data):
        # to check empty ll
        if self.head is None:
            self.insert_beginning(data)
        else:
            self.last_node.next_node = Node(data, None)
            self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None
