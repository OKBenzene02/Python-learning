# """
# Implementation of Linked Lists
# Date - 23 - 04 - 23
# """
#
# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None
#
# class LinkedList:
#     def __init__(self):
#         self.head = None
#
# # # Add element at the beginning
#     def pushleft(self, data):
#         new_node = Node(data)
#         new_node.next = self.head
#         self.head = new_node
#
# # # Add element after a specified element
#     def add(self, prev, new):
#         new_node = Node(new)
#         if not self.head:
#             return
#
#         if prev == self.head.data:
#             new_node.next = self.head.next
#             self.head.next = new_node
#             return
#
#         head = self.head
#         while head.data != prev:
#             head = head.next
#             if not head:
#                 return
#         new_node.next = head.next
#         head.next = new_node
#
# # # Add element at a specified index
#     def insert(self, index, data):
#         new_node = Node(data)
#         if not self.head:
#             return
#
#         if index == 0 and self.head:
#             new_node.next = self.head.next
#             self.head.next = new_node
#             return
#
#         head = self.head
#         while head and index > 1:
#             head = head.next
#             if not head:
#                 return
#             index -= 1
#         new_node.next = head.next
#         head.next = new_node
#
# # # Add element at the end
#     def append(self, data):
#         new_node = Node(data)
#
#         if not self.head:
#             self.head = new_node
#             return
#
#         temp = self.head
#         while temp.next:
#             temp = temp.next
#         temp.next = new_node
#
# # # To check whether the element is in the linked list
#     def isPresent(self, ele):
#         temp = self.head
#         while temp:
#             if temp.data == ele:
#                 return True
#             temp = temp.next
#         return False
#
# # # To get the element based on the index
#     def get(self, index):
#         temp = self.head
#         if index == 0 and temp:
#             return temp.data
#
#         while temp and index > 0:
#             temp = temp.next
#             index -= 1
#         return temp.data
#
# # # Calculate the length of the linked list
#     def length(self):
#         count = 0
#         curr = self.head
#         while curr:
#             count += 1
#             curr = curr.next
#
#         return count
#
# # # Reverse a linked list
#     def reverse(self):
#         prev = None
#         curr = self.head
#         while curr:
#             next = curr.next
#             curr.next = prev
#             prev = curr
#             curr = next
#         self.head = prev
#
# # # Deleting an element based on the position
#     def deleteIDX(self, pos):
#         if not self.head:
#             return
#         temp = self.head
#         prev = self.head
#         for i in range(pos):
#             if i == 0 and pos == 1:
#                 self.head = self.head.next
#             else:
#                 if i == pos - 1 and temp:
#                     prev.next = temp.next
#                 else:
#                     prev = temp
#                     if not prev:
#                         break
#                     temp = temp.next
#
# # # Sorting a linked list using merge sort o(nlogn)
#     def sort(self, l, r):
#         merged = Node(-1)
#         temp = merged
#
#         while l and r:
#             if l.data < r.data:
#                 temp.next = l
#                 l = l.next
#             else:
#                 temp.next = r
#                 r = r.next
#             temp = temp.next
#
#         while l:
#             temp.next = l
#             l = l.next
#             temp = temp.next
#
#         while r:
#             temp.next = r
#             r = r.next
#             temp = temp.next
#         return merged.next
#
#     def mergeSort(self, temp):
#         if temp is None or temp.next is None:
#             return temp
#
#         mid = self.middle(temp)
#         nxt = mid.next
#         mid.next = None
#         return self.sort(self.mergeSort(temp), self.mergeSort(nxt))
#
#     def middle(self, temp):
#         hare, tort = temp.next, temp
#         while hare and hare.next:
#             hare = hare.next.next
#             tort = tort.next
#         return tort
#
# # # Display the linked list
#     def show(self, head):
#         while head:
#             print(head.data, "-- ",end="")
#             head = head.next
#         print()
#
# ll = LinkedList()
# ll.append(4)
# ll.append(1)
# ll.append(3)
# ll.append(23)
# ll.append(6)
# ll.mergeSort(ll.head)
# # print(ll.middle(ll.head))
# ll.show(ll.head)
#
#
#

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    # # Adding data at the beginning
    def pushleft(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        self.size += 1

    def insertPos(self, prev, data):
        new_node = Node(data)
        if not self.head: return
        head = self.head
        if prev == head.data:
            new_node.next = head.next
            head.next = new_node
            self.size += 1
            return

        while head.data != prev:
            head = head.next
            if not head: return

        new_node.next = head.next
        head.next = new_node
        self.size += 1

    def insertIdx(self, idx, data):
        new_node = Node(data)
        if not self.head: return
        head = self.head
        if idx == 0 and self.head:
            new_node.next = head.next
            head.next = new_node
            self.size += 1
            return

        while head and idx > 1:
            head = head.next
            if not head: return
            idx -= 1
        new_node.next = head.next
        head.next = new_node
        self.size += 1

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.size += 1
            return

        head = self.head
        while head.next:
            head = head.next
        head.next = new_node
        self.size += 1

    def reverse(self):
        prev, curr = None, self.head
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        self.head = prev

    def deleteAt(self, pos):
        if not self.head: return
        idx = 0; curr = self.head; prev = None
        while curr.next and idx < pos:
            prev = curr
            curr = curr.next
            idx += 1
        if idx < pos: return
        elif idx == 0: self.head = self.head.next
        else: prev.next = curr.next
        self.size -= 1

    def isPresent(self, ele):
        temp = self.head
        while temp:
            if temp.data == ele: return True
            temp = temp.next
        return False

    # # Display the linked list
    def show(self, head):
        while head:
            print(head.data, "-- ",end="")
            head = head.next
        print()


ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(4)
ll.append(5)
# ll.insertPos(4, 5)
# ll.insertPos(5, 6)
# ll.insertPos(6, 7)
# ll.insertPos(7, 8)
# ll.insertIdx(2, 10)
# ll.pushleft(23)
# ll.insertPos(3,6)
# ll.mergeSort(ll.head)
# print(ll.middle(ll.head))
ll.show(ll.head)
print(ll.size)
# ll.deleteAt(ll.size - 1)
# ll.show(ll.head)
# print(ll.size)
# ll.deleteAt()
# ll.show(ll.head)
# print(ll.isPresent(4))

