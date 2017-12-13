#!usr/bin/env python
#queue实现队列
queue = []


def insert():
    queue_buff = input('Enter new string:')
    queue.append(queue_buff)


def delete():
    if len(queue) == 0:
        print("Cannot pop from empty queue")
    else:
        queue_buff = queue.pop(0)
        print(queue_buff)


def view():
    print(queue)


def showmenu():
    print("""
        insert:
        delete:
        view:
        quit:
    
    Enter you choice:
    """)

    while True:
        try:
            choice = input().strip().lower()
        except(EOFError, KeyboardInterrupt, IndexError):
            choice = "quit"

        if choice == "insert":
            insert()
        elif choice == "delete":
            delete()
        elif choice == "view":
            view()
        elif choice == "quit":
            break


if __name__ == '__main__':
    showmenu()
