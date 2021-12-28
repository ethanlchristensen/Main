import itertools
import threading
import time
import sys

class node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        self.previous = None


class double_linked_list():
    def __init__(self):
        self.head = node()

    def push(self, value):
        if self.head.value is None:
            self.head = node(value)
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = node(value)
            cur.next.previous = cur

    def pop(self, value):
        position = self.search(value)
        if position != -1:
            if position == 0 and self.length() == 1:
                self.head = node()
            elif position == 0:
                self.head = self.head.next
            else:
                cur = self.head
                for i in range(position):
                    cur = cur.next
                if cur.next is not None:
                    cur.previous.next = cur.next
                    cur.next.previous = cur.previous
                    cur = None
                else:
                    cur.previous.next = None
        else:
            print('Value is not in the list.')

    def display(self):
        cur = self.head
        while cur.next is not None:
            print('{} -> '.format(cur.value), end = '')
            cur = cur.next
        if cur.value is not None:
            print(cur.value)

    def length(self):
        cur = self.head
        total = 0
        while cur is not None:
            total += 1
            cur = cur.next
        return total

    def search(self, value):
        cur = self.head
        position = 0
        while cur is not None:
            if cur.value == value:
                return position
            else:
                cur = cur.next
                position += 1
        return -1

    def print_neighbors(self, value):
        cur = self.head
        position = self.search(value)
        if position == -1:
            print("Value is not in the list.")
        else:
            if position == 0:
                if cur.next is not None:
                    print('{} -> {}'.format(cur.value, cur.next.value))
                else:
                    print('{} has no neighbors.'.format(cur.value))
            elif position == self.length() - 1:
                for i in range(position):
                    cur = cur.next
                print('{} <- {}'.format(cur.previous.value, cur.value))
            else:
                for i in range(position):
                    cur = cur.next
                print('{} <- {} -> {}'.format(cur.previous.value, cur.value, cur.next.value))

    def print_relations(self):
        cur = self.head
        i = 1
        while cur is not None:
            print('{}: '.format(i), end='')
            self.print_neighbors(cur.value)
            cur = cur.next
            i += 1


def display():
    print('Choose and Option . . .')
    print('1: Add a Node')
    print('2: Delete a Node')
    print('3: Get Neighbors of a Node')
    print('4: Get all the Relationships in the List')
    print('5: Print the List')
    print('6: Quit')

def loading_animation():
    done = False
    def animate_start():
        for c in itertools.cycle(['...', '-..', '.-.', '..-']):
            if done:
                break
            sys.stdout.write('\rLoading ' + c)
            sys.stdout.flush()
            time.sleep(0.2)
    t = threading.Thread(target=animate_start)
    t.start()
    time.sleep(3)
    done = True
    print()

def quitting_animation():
    done = False
    def animate_start():
        for c in itertools.cycle(['...', '-..', '.-.', '..-']):
            if done:
                break
            sys.stdout.write('\rQuitting ' + c)
            sys.stdout.flush()
            time.sleep(0.2)
    t = threading.Thread(target=animate_start)
    t.start()
    time.sleep(3)
    done = True
    print()


def main():
    loading_animation()
    dll = double_linked_list()
    print('Double Linked List Program')
    ans = 0
    while ans != 6:
        display()
        ans = int(input('Enter a choice: '))
        if ans == 1:
            print()
            value = int(input('Enter a value to add: '))
            dll.push(value)
            print()
        elif ans == 2:
            print()
            value = int(input('Enter a value to remove: '))
            dll.pop(value)
            print()
        elif ans == 3:
            print()
            value = int(input('Enter a Node to get Neighbors: '))
            dll.print_neighbors(value)
            print()
        elif ans == 4:
            print()
            dll.print_relations()
            print()
        elif ans == 5:
            print()
            dll.display()
            print()
        else:
            if ans != 6:
                print('Input a number 1 - 5 . . .')
    print()
    quitting_animation()


main()